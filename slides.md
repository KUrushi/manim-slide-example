# Claude Code + manim-slides で発表資料を自動生成する

## Overview
- **Topic**: manim-slides と Claude Code を組み合わせたスライド作成ワークフロー
- **Key Message**: Claude Code に指示するだけで、アニメーション付きスライドが手に入る
- **Target Audience**: エンジニアチーム（manim を知らない前提）
- **Setting**: 社内勉強会 / ミートアップ
- **Duration**: 10分、17スライド
- **Audience Action**: manim-slides + Claude Code のワークフローに興味を持ち、自分の発表で試してみたいと思う

## Presentation Structure
結論を冒頭で提示し（Pyramid Principle）、聴衆の共感から段階的に新しい提案へ導く（Staircase Method）。「発表資料作りは面倒」という共通認識から出発し、manim-slides の紹介を経て、Claude Code との組み合わせワークフローを**具体的な7ステップ**で詳細に解説する。最後にこのスライド自体がその成果物であるというメタ演出で説得力を高める。

### Pyramid Overview
```
              [ Claude Code に指示するだけで               ]
              [ アニメーション付きスライドが手に入る       ]    <-- Slide 2
             /                                              \
    [課題: 資料作りは面倒]          [解決策: Claude Code + manim-slides]
    /                    \          /                                   \
[共感]             [既存ツール]  [ワークフロー詳細 7ステップ]       [実証]
Slides 3-4                      Slides 7-15                    Slide 16
```

---

## Slide 1: タイトル
**Type**: Title slide
**Purpose**: トピックと発表者の提示

### Content
- "Claude Code + manim-slides で発表資料を自動生成する" (Primary)
- 発表者名 / 所属 (Tertiary)

### Speaker Notes
「今日は、エンジニアの発表資料作りを劇的に楽にする方法についてお話しします。」

---

## Slide 2: 結論
**Type**: Conclusion slide
**Purpose**: Key Message を冒頭で伝える（Pyramid Principle）

### Content
- "Claude Code に指示するだけで、アニメーション付きスライドが手に入る" (Primary, Accent)

### Speaker Notes
「結論から言います。Claude Code に自然言語で指示するだけで、こういったアニメーション付きのスライドが完成します。どういうことか、順を追って説明します。」

---

## Slide 3: 共感 — 発表資料作りは面倒
**Type**: Shared ground (Staircase)
**Purpose**: 聴衆の共感を得る

### Content
- "エンジニアにとって発表資料作りは面倒" (Primary)

### Speaker Notes
「皆さん、発表って大事ですよね。自分のやったこと、チームの成果、技術の知見。でも正直、スライド作りは面倒じゃないですか？」

---

## Slide 4: 課題の深堀り — 既存ツールの限界
**Type**: Shared ground (Staircase)
**Purpose**: 課題を具体化し、同意を深める

### Content
- "既存ツールの限界" (Tertiary, section label)
- "PowerPoint / Keynote" → "図形の位置調整に時間を取られる"
- "reveal.js / Beamer" → "コードで書けるが、アニメーションが限定的"
- Progressive reveal で各行を順次表示

### Visual Elements
- ツール名は **Secondary (#BBBBBB)** で表示（後方席からの視認性を確保。#999999 では暗すぎる）
- 課題文は Primary (WHITE) で表示し、ツール名との視覚的対比をつける
- 左右のレイアウト: 左にツール名、右に課題文。矢印 (→) で接続

### Speaker Notes
「PowerPoint や Keynote は図形の位置調整に時間を取られます。コードで書ける reveal.js や Beamer もありますが、アニメーションを入れようとすると途端にハードルが上がります。」

---

## Slide 5: 提案 — manim-slides とは
**Type**: Reason (Staircase step-up)
**Purpose**: 解決策の第一要素を紹介

### Content
- "manim-slides" (Primary, Accent)
- "Python コードで書くアニメーション付きスライド" (Secondary)
- "Manim の描画力 × プレゼンの操作性" (Secondary)
- "HTML エクスポート → Playwright MCP で AI レビュー" (Secondary)

### Speaker Notes
「そこで manim-slides です。3Blue1Brown で有名な Manim をベースに、アニメーション付きスライドを Python コードだけで作れるツールです。HTML にエクスポートできるので、Playwright MCP でブラウザを自動操作してスライドを AI にレビューさせることもできます。これが manim-slides を選ぶ大きな理由の一つです。」

---

## Slide 5.5: アニメーションの威力 — ソートの可視化
**Type**: Evidence (Staircase)
**Purpose**: manim-slides のアニメーション力を、エンジニアに馴染みのある例で実証する

### Content
- "アニメーションの威力" (Tertiary, section label)
- "例: ソートの可視化" (Primary, Accent)
- バーチャートで未ソートの配列 [2, 5, 8, 1, 4] を表示
- バブルソートの比較・交換プロセスをアニメーションで段階表示
- 比較結果テキスト（例: "5 > 2 → 交換!"）を表示

### Visual Elements
- **レイアウト（上から下、余白を十分に確保）**:
  1. セクションラベル「アニメーションの威力」: 上部 (y=3.0)
  2. タイトル「例: ソートの可視化」: 上部中央 (y=2.0)
  3. バーチャート: 中央 (y=0.0)、各バーの高さで値を表現
  4. 比較結果テキスト: **中央やや下 (y=-2.0)**
- 各バーの下に数値ラベルを表示
- 比較中のバーをアクセントカラーでハイライト
- このスライドのみ段階的アニメーション（他スライドとの対比で manim-slides の威力を実感させる）

### Technical Notes
- 全要素の y 座標を明示的に指定し、要素間の重なりを防止する
- **比較結果テキストの y 座標は -2.0 以上とし、スライド番号 Canvas (y=-3.5付近) との干渉を防止する**
- Progressive reveal: バーチャート表示 → 比較ハイライト → 交換アニメーションの3段階

### Speaker Notes
「例えばソートアルゴリズム。静止画では処理の流れが伝わりにくいですが、アニメーションなら比較・交換の過程を直感的に理解できます。こういった可視化が数行の Python で作れるのが manim-slides の強みです。」

---

## Slide 6: でも Python を書くのも面倒？
**Type**: Shared ground (Staircase)
**Purpose**: 新たな課題を提示し、次の解決策への橋渡し

### Content
- "でも Python を書くのも面倒？" (Primary)

### Speaker Notes
「manim-slides は強力ですが、Python コードを書く必要があります。プレゼンの構成を考えて、アニメーションを組んで…。そこで Claude Code の出番です。」

---

## Slide 7: ワークフロー全体像
**Type**: Reason (Staircase step-up)
**Purpose**: ワークフローの全体を俯瞰する

### Content
ワークフローを7ステップのフロー図で表示:
1. "アイデアを伝える"
2. "対話で要件を詰める"
3. "slides.md 生成" + `/slides-composer` (Tertiary, スキル名)
4. "コード生成" + `/manim-slides-best-practices` (Tertiary, スキル名)
5. "レンダリング"
6. "レビュー & 改善" + `/slide-reviewer` (Tertiary, スキル名)
7. "発表 & エクスポート"

### Visual Elements
- 2行のフロー図（RoundedRectangle + Arrow）: 1行目に Step 1-4、2行目に Step 5-7
- **Claude Code が自動化するステップ（3, 4, 6）はブルー枠**で強調し、それ以外はグレー枠
- ブルー枠のステップには、枠内下部にスキル名（`/slides-composer` 等）を Tertiary サイズで表示
- 凡例: ブルー枠の四角 + "= Claude Code カスタムスキル"
- まず全体を一度に表示し、以降のスライドで各ステップを掘り下げる

### Speaker Notes
「ワークフローは全部で7ステップです。ブルーの枠がついているのは Claude Code のカスタムスキルが自動でやってくれる部分です。Claude Code にはプロジェクト固有の知識やルールを教えられるカスタムスキルという機能があり、このワークフローでは3つのスキルを使います。slides-composer が構成設計、manim-slides-best-practices がコード生成、slide-reviewer がレビューを担当します。」

---

## Slide 8: Step 1 — アイデアを伝える
**Type**: Detail
**Purpose**: ワークフローの起点を説明

### Content
- "STEP 1" (Tertiary, label)
- "アイデアを伝える" (Primary)
- "「manim-slides の紹介 LT を作りたい」" (Secondary, コマンド例として表示)
- "トピックのイメージだけでOK" (Secondary)

### Visual Elements
- コマンド例をターミナルプロンプト風に表示: `>` マーク + モノスペースの角丸四角
- ターミナル風の背景（やや明るめのダークグレー #1A1A2E）でユーザー入力を表現
- プロンプト記号 `>` をアクセントカラーで表示

### Speaker Notes
「最初のステップは、Claude Code にアイデアを伝えるだけです。例えば『manim-slides の紹介 LT を作りたい』と一言伝えます。正確な構成や詳細はこの時点では不要です。」

---

## Slide 9: Step 2 — 対話で要件を詰める
**Type**: Detail
**Purpose**: Claude Code が質問して要件を明確化するプロセスを説明

### Content
- "STEP 2" (Tertiary, label)
- "対話で要件を詰める" (Primary)
- Claude Code からの質問例を段階的に表示:
  - "聴衆は誰ですか？"
  - "発表時間は？"
  - "何を伝えたいですか？"

### Visual Elements
- 吹き出し風のデザイン（RoundedRectangle）で質問を表現
- Progressive reveal で1つずつ表示

### Speaker Notes
「Claude Code が聴衆、発表時間、目的などを質問してきます。あいまいな部分を対話で明確にしていきます。選択肢から選ぶだけの場合も多いので、考え込む必要はありません。」

---

## Slide 10: Step 3 — slides.md 生成
**Type**: Detail
**Purpose**: 構成設計の自動化を説明

### Content
- "STEP 3" (Tertiary, label)
- "構成設計: slides.md" (Primary)
- slides.md の構造を簡略表示:
  - "Overview: トピック、Key Message、聴衆"
  - "Slide 1: タイトル"
  - "Slide 2: 結論（結論を最初に提示）" (「結論」をアクセントカラーで強調)
  - "Slide 3-N: 本文（段階的に合意を構築）"
  - "Design: 配色、フォント、トランジション"

### Visual Elements
- ドキュメントを表す角丸四角の中にテキスト一覧
- **フォントサイズは Secondary (24) 以上**を使用し、後方席からの可読性を確保
- Progressive reveal で構造を順次表示

### Speaker Notes
「対話が終わると、Claude Code が slides.md というスライド構成書を自動生成します。ここにはスライドごとの内容、話す順序、使うアニメーション、配色まで全て設計されています。結論を先に置いて、段階的に聴衆の合意を構築していく構造です。」

---

## Slide 11: Step 4 — コード生成
**Type**: Detail
**Purpose**: manim-slides コードの自動生成を説明

### Content
- "STEP 4" (Tertiary, label)
- "Python コードを自動生成" (Primary)
- コードスニペットの概要を表示:
  - "class Presentation(Slide):"
  - "    Canvas, Wipe, Progressive reveal..."
  - "    全て自動で構成"

### Visual Elements
- コードブロック風の表示（モノスペースフォント、背景色）

### Speaker Notes
「slides.md を元に、Claude Code が manim-slides の Python コードを自動生成します。Canvas でスライド番号を管理し、Wipe トランジションや Progressive reveal など、ベストプラクティスに沿ったコードが出力されます。」

---

## Slide 12: Step 5 — レンダリング & HTML エクスポート
**Type**: Detail
**Purpose**: コマンド2つでレンダリングとエクスポートが完了することを示す

### Content
- "STEP 5" (Tertiary, label)
- "レンダリング & HTML エクスポート" (Primary)
- "$ manim-slides render presentation.py" (Secondary, コマンド表示)
- "$ manim-slides convert --to html ... output.html" (Secondary, コマンド表示)
- "← Playwright MCP でレビューするために必要" (Accent, 注釈テキスト)

### Visual Elements
- ターミナルウィンドウ風のデザイン: 上部にウィンドウバー（3つのドット: 赤・黄・緑の小円）、下部にコマンド表示
- コマンドテキストはモノスペースフォント、`$` プロンプトをアクセントカラーで表示
- 2つ目のコマンドの下に注釈テキストで次のステップ（レビュー）への橋渡しを表現

### Speaker Notes
「コードが生成されたら、2つのコマンドでレンダリングと HTML エクスポートを行います。render でアニメーションを生成し、convert で HTML を出力します。この HTML が次のレビューステップで使われます。レンダリングは17スライドで数分程度です。」

---

## Slide 12.5: Step 6 — レビュー & 改善
**Type**: Detail
**Purpose**: Playwright MCP による自動レビューの仕組みを説明

### Content
- "STEP 6" (Tertiary, label)
- "Playwright MCP でレビュー" (Primary)
- チェックリスト形式で評価項目を表示:
  - "✓ メッセージ明確性" (グリーン)
  - "✓ 認知負荷" (グリーン)
  - "✓ 可読性・コントラスト" (グリーン)
  - "! 要素の重なり検出" (イエロー/オレンジ)
- "スクリーンショット × 聴衆視点の自動評価" (Secondary)

### Visual Elements
- ターミナルウィンドウ風のデザイン: 上部にウィンドウバー（3つのドット）
- チェックマークはグリーン、警告マークはイエロー/オレンジで色分け
- 画面下部に補足テキストで自動評価の仕組みを説明

### Speaker Notes
「HTML にエクスポートしたスライドを Playwright MCP でブラウザに表示し、各スライドのスクリーンショットを自動で撮影します。聴衆目線でメッセージ明確性、認知負荷、可読性などを評価し、改善点を特定してコードに反映します。このレビューステップが品質を大きく引き上げます。」

---

## Slide 13: Step 7 — 発表 & エクスポート
**Type**: Detail
**Purpose**: 複数の出力形式を紹介

### Content
- "STEP 7" (Tertiary, label)
- "発表 & エクスポート" (Primary)
- 出力形式を段階的に表示:
  - "manim-slides present" (Accent) + "ライブ発表" (Secondary)
  - "→ HTML" (Accent) + "ブラウザで共有" (Secondary)
  - "→ PPTX" (Accent) + "PowerPoint 互換" (Secondary)
  - "→ PDF" (Accent) + "静的バックアップ" (Secondary)

### Visual Elements
- フォーマット名（HTML, PPTX, PDF）をアクセントカラーで表示し、説明テキストと視覚的に区別
- 各フォーマットの左側に小さなアイコン的要素を追加:
  - present: 再生ボタン (Triangle)
  - HTML: `</>` テキスト
  - PPTX: 四角 (Square)
  - PDF: ドキュメントアイコン (Rectangle)
- Progressive reveal で出力形式を1つずつ表示

### Speaker Notes
「完成したスライドは、デスクトップアプリでライブ発表できるほか、HTML にエクスポートしてブラウザで共有したり、PowerPoint 形式で同僚に渡すこともできます。」

---

## Slide 14: 実証 — このスライド自体が成果物
**Type**: Evidence
**Purpose**: メタ演出で説得力を与える

### Content
- "このスライドも Claude Code + manim-slides で作りました" (Primary, Accent)

### Visual Elements
- 「このスライドも」「で作りました」は**白テキスト**、「Claude Code + manim-slides」のみ**ブルーアクセント**で表示し、プロジェクター環境での可読性を確保

### Speaker Notes
「実はこのスライド、今ご覧いただいているこのプレゼン自体が、Claude Code に指示して manim-slides で生成したものです。もちろん完璧に一発で出るわけではなく、レイアウトの微調整などは必要ですが、体感では8割は自動で、残り2割を手直しする程度です。ゼロから作るのとは比べものにならないほど早く仕上がります。Python の知識がなくても、Claude Code が書いてくれるので大丈夫です。技術系の発表に限らず、アイデアをテキストで説明できれば対応できます。」

---

## Slide 15: クロージング
<!-- 実装ではスライド17に対応 -->
**Type**: Closing slide
**Purpose**: Key Message の再提示と行動喚起

### Content
- "伝えたいことを伝えるだけ。スライドは Claude Code が作る。" (Primary)
- "pip install manim-slides" (Tertiary, コード風)

### Speaker Notes
「伝えたいことを言語化するだけで、あとは Claude Code と manim-slides が形にしてくれます。ぜひ次の発表で試してみてください。ありがとうございました。」

### Technical Notes
- このスライドがプレゼンテーションの最終スライドであること。この後に空白スライドが生成されないようにする
- クロージング後にスライドを送っても黒画面にならないよう、最終 `next_slide()` の後に余計な `self.wait()` やアニメーションを追加しない

---

## Design Specification

### Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Background | ダークグレー | #111111 | シーン背景 |
| Text Primary | ホワイト | #FFFFFF | 見出し、キーメッセージ |
| Text Secondary | ライトグレー | #BBBBBB | 補足テキスト（後方席からの視認性を確保） |
| Text Tertiary | ミディアムグレー | #666666 | ラベル、日付、メタ情報 |
| Accent | ブルー | #3B82F6 | キーワード強調（manim-slides、結論文） |

### Font Strategy

| Level | Size | Weight | Role | Example |
|-------|------|--------|------|---------|
| Primary | 44-48 | Bold | 核心メッセージ | 結論、Key Message |
| Secondary | 24-28 | Regular | 補足説明 | ワークフロー説明、課題の詳細 |
| Tertiary | 16-20 | Regular | メタ情報 | 発表者名、スライド番号、ラベル |

### Canvas Elements
- スライド番号: 右下に `font_size=18, GREY_C` で表示
- 全スライドで一貫して表示（Canvas で管理）

---

## Staircase Flow

| Slide | Type | Agreement Level |
|-------|------|-----------------|
| 1 | Title | -- |
| 2 | Conclusion | Key Message 提示 |
| 3 | Shared ground | 「発表資料作りは面倒だよね」→ 共感 |
| 4 | Shared ground | 「既存ツールにも限界があるよね」→ 課題の共有 |
| 5 | Step-up: Reason 1 | 「manim-slides なら Python でアニメーション付きスライド」 |
| 5.5 | Evidence | 「ソートの可視化でアニメーションの威力を実感」 |
| 6 | Shared ground | 「でも Python 書くのも面倒だよね」→ 再共感 |
| 7 | Step-up: Reason 2 | 「Claude Code との組み合わせで全自動化」→ 全体像 |
| 8 | Detail | Step 1: アイデアを伝える |
| 9 | Detail | Step 2: 対話で要件を詰める |
| 10 | Detail | Step 3: slides.md 自動生成 |
| 11 | Detail | Step 4: Python コード自動生成 |
| 12 | Detail | Step 5: レンダリング & HTML エクスポート |
| 12.5 | Detail | Step 6: レビュー & 改善（Playwright MCP） |
| 13 | Detail | Step 7: 発表 & エクスポート |
| 14 | Evidence | 「このスライド自体がその証拠」→ メタ実証 |
| 15 | Closing | Key Message 再提示 + 行動喚起 |

---

## Transition Plan

### Slide Transitions
- Slide 1 → 2: FadeOut + FadeIn
- Slide 2 → 3: FadeOut + FadeIn
- Slide 3 → 4: FadeOut + FadeIn
- Slide 4 → 5: Wipe（課題→解決策への転換）
- Slide 5 → 5.5: FadeOut + FadeIn
- Slide 5.5 → 6: FadeOut + FadeIn
- Slide 6 → 7: Wipe（再共感→全体像への転換）
- Slide 7 → 8: FadeOut + FadeIn（全体像→各ステップ詳細へ）
- Slide 8-13: FadeOut + FadeIn（ステップ間の連続性）
- Slide 13 → 14: FadeOut + FadeIn（ステップ完了→実証へ）
- Slide 14 → 15: Wipe（実証→クロージングへの転換）

---

## Checklist

- [x] 結論が最初の10%（Slide 2 = 全17枚中2枚目）に登場
- [x] 各スライドは1つのアイデアのみを伝える
- [x] すべてのスライドが「2秒テスト」をパスする（Slide 5.5 改善済み）
- [x] アクセントカラーは1色のみ（ブルー #3B82F6）
- [x] フォントファミリーは1つのみ
- [x] Progressive disclosure を計画（Slide 4, 5.5, 9, 10, 12, 13 で段階的表示）
- [x] Staircase flow で段階的に合意を構築
- [x] アニメーションはタイミング制御目的（演出ではない）
- [x] 全スライドに Speaker Notes を記載
- [x] 要素の重なりを防止するレイアウト座標を明示（Slide 5.5）
- [x] Secondary テキストのコントラスト比を改善（#999999 → #BBBBBB）
- [x] ステップ詳細区間の視覚的バリエーションを追加（Slide 8, 12, 12.5, 13）
- [x] 空白スライドの発生防止を Technical Notes に明記（Slide 15）
- [x] 聴衆の予想される疑問に Speaker Notes で対応（Slide 14: コスト、品質比率、汎用性）
- [x] slides.md と実装の整合性を確認（7ステップ/17スライド）
- [x] Slide 5.5 をソートの可視化に変更（聴衆により馴染みのある例）
- [x] Slide 10 の専門用語を簡略化（Pyramid Principle → 結論を最初に提示）
- [x] Slide 14 の可読性改善指示を追加（白+アクセントの混合）
- [ ] Slide 6 下部テキストの y 座標修正（実装時に対応: manim-slides-best-practices）
- [ ] Slide 11 ドキュメントボックス内のフォントサイズ拡大（実装時に対応: manim-slides-best-practices）

---

## Reference Material

- [manim-slides 公式ドキュメント](https://manim-slides.eertmans.be/)
- [manim-slides GitHub](https://github.com/jeertmans/manim-slides)
- [Manim Community Edition](https://www.manim.community/)
- [Claude Code](https://claude.com/claude-code)
