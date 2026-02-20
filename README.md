# manim-slide-example

Claude Code + [manim-slides](https://github.com/jeertmans/manim-slides) を使って、アニメーション付きプレゼンテーションを自動生成するサンプルプロジェクトです。

## 必要なもの

- Python 3.10 以上
- [uv](https://docs.astral.sh/uv/)（パッケージマネージャー）
- LaTeX（MathTex を使う場合）
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)（スライドの自動生成に利用）

## セットアップ

```bash
git clone https://github.com/KUrushi/manim-slide-example.git
cd manim-slide-example
uv sync
```

## 使い方

### 1. スライド構成の設計（slides.md の生成）

Claude Code でプレゼンテーションの構成を設計します。トピックを伝えるだけで、対話を通じてスライド構成書（`slides.md`）が自動生成されます。

```
claude
> /slides-composer
> 「manim-slides の紹介 LT を作りたい」
```

Claude Code が聴衆・発表時間・目的などを質問し、回答に基づいて `slides.md` を生成します。

### 2. Python コードの生成

`slides.md` をもとに、manim-slides の Python コードを生成します。

```
claude
> slides.md をもとに presentation.py を実装して
```

### 3. レンダリング

生成された Python コードをレンダリングします。

```bash
uv run manim-slides render presentation.py ClaudeCodeManimSlides
```

### 4. プレゼンテーション

#### ライブ発表

```bash
uv run manim-slides present ClaudeCodeManimSlides
```

- 右矢印キー / クリック: 次のスライド
- 左矢印キー: 前のスライド
- `q`: 終了

#### HTML エクスポート

```bash
uv run manim-slides convert --one-file --offline ClaudeCodeManimSlides output.html
```

ブラウザで `output.html` を開いて発表できます。

#### その他のエクスポート形式

```bash
# PowerPoint
uv run manim-slides convert --to pptx ClaudeCodeManimSlides output.pptx

# PDF
uv run manim-slides convert --to pdf ClaudeCodeManimSlides output.pdf
```

### 5. レビュー & 改善

HTML エクスポート後、Claude Code でスライドをレビューできます。Playwright MCP を使って各スライドのスクリーンショットを撮影し、聴衆視点で評価します。

```
claude
> /slide-reviewer
> スライドをレビューして
```

レビュー結果に基づいて `presentation.py` を修正し、手順 3 からやり直します。

## ファイルの説明

### slides.md — スライド構成書

Claude Code の `/slides-composer` スキルが生成するスライド構成書です。プレゼンテーションの設計図として機能し、以下の情報を含みます。

- **Overview**: トピック、Key Message、対象聴衆、発表時間
- **各スライドの定義**: タイプ（Title / Conclusion / Detail など）、コンテンツ、Visual Elements、Speaker Notes
- **Presentation Structure**: Pyramid Principle（結論先行）と Staircase Method（段階的合意構築）に基づく構成設計
- **Design Specification**: カラーパレット（Background / Primary / Secondary / Tertiary / Accent）、フォント戦略（サイズ・ウェイト・用途）
- **Transition Plan**: スライド間のトランジション指定（FadeOut + FadeIn / Wipe）
- **Checklist**: 設計品質の確認項目

このファイルが presentation.py のコード生成の入力となります。自分のプレゼンテーションを作る場合は、このファイルを参考に構成を設計してください。

### presentation.py — manim-slides ソースコード

`slides.md` をもとに生成された manim-slides の Python コードです。主な構成要素:

- **`ClaudeCodeManimSlides(Slide)`**: メインのスライドクラス。`Slide` を継承し、`construct()` メソッドでスライドを定義
- **Canvas**: スライド番号を全スライド共通で右下に表示（`add_to_canvas()`）
- **`next_slide()`**: スライドの区切り。`notes=` 引数で Speaker Notes を設定
- **`switch_slide()`**: 前スライドの要素を除去して新しいコンテンツに切り替えるヘルパー
- **カラーパレット**: Apple HIG Dark Mode ベースの配色定数（`ACCENT`, `TEXT_PRIMARY` など）
- **アニメーション例**: バブルソートの可視化（バーチャートの比較・交換を段階的にアニメーション）

全17スライドで、タイトル → 結論 → 課題の共感 → manim-slides 紹介 → ソートアニメーション → ワークフロー7ステップの詳細 → メタ実証 → クロージング、という流れです。

## プロジェクト構成

```
.
├── README.md
├── pyproject.toml          # プロジェクト設定・依存関係
├── slides.md               # スライド構成書（Claude Code が生成）
├── presentation.py         # manim-slides のソースコード
├── output.html             # エクスポートされた HTML（git 管理外）
├── media/                  # レンダリング結果（git 管理外）
└── .agents/skills/         # Claude Code スキル定義
    ├── slides-composer/        # スライド構成の設計
    ├── manim-slides-best-practices/  # manim-slides 実装のベストプラクティス
    ├── manimce-best-practices/       # Manim CE のベストプラクティス
    ├── slide-reviewer/               # スライドの自動レビュー
    └── manim-composer/               # Manim 動画の構成設計
```

## ライセンス

MIT
