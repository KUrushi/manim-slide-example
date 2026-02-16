---
name: slide-reviewer
description: |
  Trigger when: (1) User asks to "review", "check", or "critique" their slides/presentation,
  (2) User wants feedback on rendered slides from the audience perspective,
  (3) An output.html exists and user asks "how does this look" about their presentation,
  (4) User mentions wanting a "second opinion" or audience feedback on slides,
  (5) User wants to iterate and improve an existing presentation.

  Reviews rendered manim-slides presentations from the AUDIENCE perspective using
  Playwright MCP to view the actual HTML export. Captures screenshots of each slide,
  evaluates message clarity, cognitive load, narrative flow, and engagement,
  then produces an actionable review report.

  NOT for source code review (use manim-slides-best-practices checklist).
  NOT for planning new presentations (use slides-composer).
  This skill evaluates the RENDERED output as an audience member would experience it.
---

## Workflow

### Phase 0: 前提確認

1. **HTMLファイルの確認**
   - `output.html` のパスを確認する
   - 存在しない場合、以下のコマンドを案内:
     ```bash
     .venv/bin/manim-slides convert --one-file --offline <ClassName> output.html
     ```

2. **Playwright MCP ツールの確認**
   - 以下のツールが利用可能か確認:
     - `mcp__playwright__browser_navigate`
     - `mcp__playwright__browser_take_screenshot`
     - `mcp__playwright__browser_evaluate`
     - `mcp__playwright__browser_resize`

3. **コンテキスト収集**
   - `slides.md` があれば読み込み、意図した構成と比較する材料にする
   - 聴衆の情報を確認（`slides.md` になければ `AskUserQuestion` で確認）:
     - 対象者（エンジニア、経営層、学生、一般）
     - 発表の場（カンファレンス、チームミーティング、講義）
     - 持ち時間

### Phase 1: スライドキャプチャ

1. **ビューポート設定**
   ```
   mcp__playwright__browser_resize → 1920x1080
   ```

2. **HTML を開く**
   ```
   mcp__playwright__browser_navigate → file://<absolute-path>/output.html
   ```

3. **総スライド数を取得**
   ```javascript
   // browser_evaluate で実行
   Reveal.getTotalSlides()
   ```

4. **各スライドをキャプチャ**
   各スライド (i = 0 ~ N-1) について:
   ```javascript
   // 1. スライドへ移動
   Reveal.slide(i)

   // 2. 動画読み込み待機（1秒以上）
   const video = Reveal.getCurrentSlide().slideBackgroundContentElement?.querySelector('video');
   video && video.readyState >= 2  // HAVE_CURRENT_DATA 以上

   // 3. スクリーンショット取得
   // mcp__playwright__browser_take_screenshot を使用

   // 4. スピーカーノート抽出
   const notes = Reveal.getCurrentSlide().querySelector('aside.notes');
   notes ? notes.textContent.trim() : null
   ```

5. **記録**: 全スライドのスクリーンショットとノートを保持

### Phase 2: 個別スライドレビュー

各スライドのスクリーンショットを [rules/audience-criteria.md](rules/audience-criteria.md) の8観点で評価:

1. 第一印象（タイトルスライドのみ）
2. メッセージ明確性
3. 認知負荷
4. ナラティブ一貫性
5. エンゲージメント
6. 可読性・アクセシビリティ
7. 聴衆の疑問
8. 感情的アーク

- 具体的な観察に基づくフィードバック（「スライド5のテキストは...」）
- 各観点ごとに Strong / Adequate / Needs Improvement でスコアリング

### Phase 3: ナラティブフローレビュー

スライド全体を**シーケンス**として評価:

1. **ストーリーアーク**: 全体の構成は論理的で説得力があるか
2. **ペーシング**: 情報の密度変化は適切か、緩急があるか
3. **セクション間の接続**: スライド間のつながりは明確か
4. **混乱ポイント**: 聴衆が混乱・退屈・迷子になる箇所はないか
5. **ピラミッド原則**: 結論が先に提示され、理由→詳細の流れが聴衆体験として機能しているか
6. **ステアケース法**: 合意→ステップアップの流れが体験として機能しているか

### Phase 4: レポート生成

1. [templates/review-report.md](templates/review-report.md) に基づいてレポートを作成
2. インパクト順に改善提案を優先度付け
3. 各改善提案に対応する既存スキルを明記（[references/iteration-guide.md](references/iteration-guide.md) 参照）
4. レポートは日本語で出力

## RevealJS API クイックリファレンス

```javascript
// ナビゲーション
Reveal.getTotalSlides()       // 総スライド数
Reveal.slide(indexH, indexV)  // 特定スライドへ移動（0-based）
Reveal.next()                 // 次のスライドへ
Reveal.getCurrentSlide()      // 現在のスライド要素

// スライド情報
Reveal.getIndices()           // { h: number, v: number, f: number }
Reveal.getSlidePastCount()    // 現在までに通過したスライド数

// 動画チェック
const bg = Reveal.getCurrentSlide().slideBackgroundContentElement;
const video = bg?.querySelector('video');
video?.readyState >= 2        // HAVE_CURRENT_DATA 以上で読み込み完了

// スピーカーノート
Reveal.getCurrentSlide().querySelector('aside.notes')?.textContent
```

## Playwright MCP コマンド例

```
# ページを開く
mcp__playwright__browser_navigate(url="file:///absolute/path/output.html")

# ビューポートサイズ変更
mcp__playwright__browser_resize(width=1920, height=1080)

# JavaScript実行
mcp__playwright__browser_evaluate(expression="Reveal.getTotalSlides()")

# スクリーンショット取得
mcp__playwright__browser_take_screenshot()
```

## Rules

- [rules/playwright-navigation.md](rules/playwright-navigation.md) - HTML閲覧・スクリーンショット取得手順
- [rules/audience-criteria.md](rules/audience-criteria.md) - 聴衆視点の評価基準（8観点）
- [rules/review-report-format.md](rules/review-report-format.md) - レポート出力形式・スコアリング定義

## References

- [references/audience-perspective.md](references/audience-perspective.md) - 聴衆心理の理論的背景
- [references/iteration-guide.md](references/iteration-guide.md) - 改善フィードバック→他スキルへの振り分け

## Templates

- [templates/review-report.md](templates/review-report.md) - レビューレポートのテンプレート
