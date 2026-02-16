# manim-slides API & 使い方 調査レポート

## 概要

**manim-slides** は Manim (Community Edition) または ManimGL で作成したアニメーションを、PowerPoint のようなプレゼンテーションとして利用できるようにするツール。

- 最新バージョン: **v5.5.3**
- リポジトリ: https://github.com/jeertmans/manim-slides
- ドキュメント: https://manim-slides.eertmans.be/latest/
- PyPI: https://pypi.org/project/manim-slides/
- ライセンス: MIT

---

## 1. 基本概念

### Slide クラスと Scene の違い

- `Slide` は ManimCE の `Scene` を継承したサブクラス
- `ThreeDSlide` は `Slide` + `ThreeDScene` の多重継承
- Scene との違いは `next_slide()` メソッドが追加されている点のみ
- 既存の Manim コードに最小限の変更で対応可能

```python
# Before (通常の Manim)
from manim import *

class MyScene(Scene):
    def construct(self):
        self.play(...)

# After (manim-slides)
from manim import *
from manim_slides import Slide

class MyScene(Slide):
    def construct(self):
        self.play(...)
        self.next_slide()  # スライドの区切り
        self.play(...)
```

### 基本ワークフロー

1. `Slide` を継承したクラスを作成
2. `self.next_slide()` でスライドの区切りを挿入
3. `manim-slides render` でレンダリング
4. `manim-slides present` でプレゼンテーション表示
5. 必要に応じて `manim-slides convert` で HTML/PDF/PPTX に変換

---

## 2. コア API

### 2.1 Slide クラス

#### コンストラクタパラメータ

| パラメータ | 型 | デフォルト | 説明 |
|---|---|---|---|
| `output_folder` | Path | - | スライドアニメーションファイルの出力先 |
| `disable_caching` | bool | False | アニメーションファイルのキャッシュを無効化 |
| `flush_cache` | bool | False | レンダリング前にキャッシュをクリア |
| `skip_reversing` | bool | False | 逆再生用アニメーションの生成をスキップ |
| `max_duration_before_split_reverse` | float | 4.0 | 逆再生時に分割するビデオ長の閾値(秒) |
| `num_processes` | int | None | 並列処理数 (デフォルトはCPU数) |

#### `next_slide()` メソッド

スライドの区切りを作成し、次のスライドのオプションを設定する最も重要なメソッド。

```python
def next_slide(
    *,
    loop: bool = False,
    auto_next: bool = False,
    playback_rate: float = 1.0,
    reversed_playback_rate: float = 1.0,
    notes: str = '',
    dedent_notes: bool = True,
    skip_animations: bool = False,
    src: Path | None = None,
) -> None
```

| パラメータ | 型 | デフォルト | 説明 |
|---|---|---|---|
| `loop` | bool | False | スライドを無限ループさせる |
| `auto_next` | bool | False | スライド終了時に自動的に次へ進む (HTML/RevealJS のみ) |
| `playback_rate` | float | 1.0 | 順再生速度 (present モードのみ) |
| `reversed_playback_rate` | float | 1.0 | 逆再生速度 (present モードのみ) |
| `notes` | str | '' | Markdown 形式のプレゼンターノート |
| `dedent_notes` | bool | True | ノートのテキストインデントを除去 |
| `skip_animations` | bool | False | 次のスライドを出力から除外 |
| `src` | Path \| None | None | 外部ビデオファイルのパス (v5.5.0+) |

**重要な注意点:**
- `next_slide()` は construct() の最初と最後に自動的に追加されるため、明示的に呼ぶ必要はない
- `next_slide()` はスライドの「区切り」であり、呼び出した位置より**後**のアニメーションに設定が適用される

#### Canvas 関連メソッド

Canvas は複数スライドにまたがって存在し続けるオブジェクトを管理する仕組み。

```python
# Canvas にオブジェクトを追加
def add_to_canvas(**objects: Mobject) -> None

# Canvas の内容を取得 (名前 -> Mobject のマッピング)
@property
def canvas() -> MutableMapping[str, Mobject]

# Canvas 内の Mobject を取得
@property
def canvas_mobjects() -> ValuesView[Mobject]

# Canvas を除いたシーンのオブジェクトを取得
@property
def mobjects_without_canvas() -> Sequence[Mobject]

# Canvas からオブジェクトを削除
def remove_from_canvas(*names: str) -> None
```

#### Wipe & Zoom トランジション

```python
# Wipe: オブジェクトをスライドさせて切り替え
def wipe(
    *args,
    direction: np.ndarray = LEFT,  # array([-1., 0., 0.])
    return_animation: bool = False,
    **kwargs
) -> Wipe | None

# Zoom: フェード+スケールで切り替え
def zoom(
    *args,
    return_animation: bool = False,
    **kwargs
) -> Zoom | None
```

**wipe() の使い方:**
```python
# 基本: 現在のオブジェクトを新しいオブジェクトに切り替え
self.wipe(old_mobject, new_mobject)

# 方向指定
self.wipe(old, new, direction=UP)

# アニメーションオブジェクトとして取得
anim = self.wipe(old, new, return_animation=True)
self.play(anim)

# Canvas を除くすべてのオブジェクトを切り替え
self.wipe(self.mobjects_without_canvas, new_mobject)

# すべてのオブジェクトをクリア
self.wipe(self.mobjects_without_canvas, [])
```

#### アニメーションスキップ

```python
# 以降のスライドを自動的にスキップ
def start_skip_animations() -> None

# スキップを停止
def stop_skip_animations() -> None
```

#### wait_time_between_slides

```python
# スライド間の待機時間 (秒) - デフォルトは 0
@property
def wait_time_between_slides() -> float

# 設定例
self.wait_time_between_slides = 0.1
```

#### next_section()

`next_slide()` のエイリアス (Manim API との互換性のため)。

### 2.2 ThreeDSlide クラス

`Slide` + `ThreeDScene` の多重継承。3D カメラ操作が可能。

```python
from manim import *
from manim_slides import ThreeDSlide

class My3DPresentation(ThreeDSlide):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        ...
```

### 2.3 Animation クラス

`manim_slides.slide.animation` モジュールで提供される独立したアニメーションクラス。

```python
from manim_slides.slide.animation import Wipe, Zoom

# Wipe アニメーション
class Wipe:
    def __init__(
        self,
        current: Sequence[Mobject] | None,
        future: Sequence[Mobject] | None,
        shift: ndarray,
        fade_in_kwargs: Mapping[str, Any] | None = None,
        fade_out_kwargs: Mapping[str, Any] | None = None,
        **kwargs
    )

# Zoom アニメーション
class Zoom:
    def __init__(
        self,
        current: Sequence[Mobject] | None,
        future: Sequence[Mobject] | None,
        scale: float,
        out: bool = False,
        fade_in_kwargs: Mapping[str, Any] | None = None,
        fade_out_kwargs: Mapping[str, Any] | None = None,
        **kwargs
    )
```

### 2.4 カスタムシーンのサブクラス化

Slide を他の Scene タイプと組み合わせて使用可能:

```python
from manim import *
from manim_slides import Slide

class MovingCameraSlide(Slide, MovingCameraScene):
    pass

class MyPresentation(MovingCameraSlide):
    def construct(self):
        self.camera.frame.save_state()
        # ... MovingCameraScene のメソッドが使える
```

---

## 3. CLI コマンド

### 3.1 `manim-slides render`

Manim のレンダラーをラップしてアニメーションをレンダリング。

```bash
# ManimCE でレンダリング (デフォルト)
manim-slides render example.py MySlide

# ManimGL でレンダリング
manim-slides render --GL example.py MySlide

# Manim のオプションも渡せる
manim-slides render -qh example.py MySlide
```

環境変数:
- `MANIM_RENDERER`: デフォルトレンダラーの設定
- `MANIMGL_RENDERER`: ManimGL のデフォルト設定

### 3.2 `manim-slides present`

レンダリング済みスライドをプレゼンテーション表示。

```bash
# 基本
manim-slides present MySlide

# 短縮形 (present はデフォルトコマンド)
manim-slides MySlide

# フルスクリーン
manim-slides present -F MySlide

# 特定のスライドから開始
manim-slides present --start-at 0,2 MySlide

# マウスカーソルを非表示
manim-slides present -H MySlide
```

主要オプション:

| オプション | 説明 |
|---|---|
| `-c, --config <FILE>` | 設定ファイルパス (デフォルト: .manim-slides.toml) |
| `--folder <DIR>` | slides ディレクトリ (デフォルト: slides/) |
| `--start-paused` | 一時停止状態で開始 |
| `-F, --full-screen` | フルスクリーン |
| `-s, --skip-all` | 全スライドをスキップ (テスト用) |
| `--exit-after-last-slide` | 最後のスライドで終了 |
| `-H, --hide-mouse` | マウスカーソルを非表示 |
| `--aspect-ratio {keep,ignore}` | アスペクト比の扱い |
| `--start-at <SCENE,SLIDE>` | 開始位置を指定 |
| `-S, --screen <NUMBER>` | 表示ディスプレイを選択 |
| `--playback-rate <RATE>` | 再生速度 |
| `--next-terminates-loop` | next ボタンでループを停止 |
| `--hide-info-window` | 情報パネルを非表示 |
| `--show-info-window` | 情報パネルを表示 |
| `--info-window-screen <NUMBER>` | 情報パネルのディスプレイ |

### 3.3 `manim-slides convert`

スライドを HTML, PDF, PPTX, ZIP に変換。

```bash
# HTML に変換
manim-slides convert MySlide output.html

# 単一ファイル HTML
manim-slides convert --one-file MySlide output.html

# オフライン対応 HTML
manim-slides convert --offline --one-file MySlide output.html

# PDF に変換
manim-slides convert --to=pdf MySlide output.pdf

# PowerPoint に変換
manim-slides convert --to=pptx MySlide output.pptx

# ZIP に変換 (HTML + アセット)
manim-slides convert --to=zip MySlide output.zip

# 設定オプションの確認
manim-slides convert --to=html --show-config

# テンプレートの確認
manim-slides convert --to=html --show-template

# カスタムテンプレートの使用
manim-slides convert --use-template my_template.html MySlide output.html

# RevealJS オプションの設定
manim-slides convert -cslide_number=true -ctransition=fade MySlide output.html
```

### 3.4 その他のコマンド

```bash
# ヘルスチェック
manim-slides checkhealth

# 利用可能なシーンの一覧
manim-slides list-scenes

# 設定ファイルの初期化
manim-slides init

# 設定ウィザード
manim-slides wizard
```

---

## 4. エクスポート形式の比較

| 機能 | present | HTML | PPTX | PDF |
|---|---|---|---|---|
| 基本ナビゲーション | O | O | O | O |
| スライドのリプレイ | O | X | X | N/A |
| アニメーション一時停止 | O | O | X | N/A |
| 逆再生 | O | X | X | N/A |
| 自動再生 | O | O | O | N/A |
| ループ | O | O | O | N/A |
| カスタマイズ性 | X | O | X | X |
| 必要環境 | Python + manim-slides | ブラウザ | PowerPoint/LibreOffice | PDFリーダー |

### HTML 変換の特徴
- RevealJS ベース
- 豊富な設定オプション (-c オプション)
- `--one-file`: 単一ファイルに全アセットを埋め込み
- `--offline`: JS/CSS をインラインに埋め込み
- GitHub Pages でのホスティングが可能
- スピーカーノートは常に利用可能 (v5.5.1+)

### PPTX 変換の特徴
- 実験的ステータス
- ビデオはすべてファイル内に埋め込み
- デフォルトでは各スライドの最初のフレームがポスター画像
- PowerPoint のメモリ制限に注意 (大量のスライドで問題発生の可能性)

### PDF 変換の特徴
- アニメーションは失われる (バックアップ用途)
- デフォルトでは各スライドの最後のフレームを使用
- `frame_index`: フレーム選択オプション
- `resolution`: 画像品質 (デフォルト: 100.0)

---

## 5. ManimCE との互換性・共存方法

### インポートパターン

```python
# 推奨: 先に Manim をインポート、次に manim-slides
from manim import *
from manim_slides import Slide

# ManimGL の場合
from manimlib import *
from manim_slides import Slide
```

### 自動検出

manim-slides は `sys.modules` を確認して、どちらのパッケージがロードされているかを自動検出する。`manim` (CE) が `manimlib` (GL) より優先される。

### 環境変数による制御

```bash
# ManimCE を強制
MANIM_API=manim python my_script.py

# ManimGL を強制
MANIM_API=manimgl python my_script.py

# 自動検出をオーバーライド
FORCE_MANIM_API=1 MANIM_API=manim python my_script.py
```

---

## 6. インストール方法

### 推奨 (pipx)

```bash
# Qt バインディング付き (プレゼンテーション機能に必要)
pipx install -U "manim-slides[pyside6-full]"

# ManimCE も一緒に
pipx install -U "manim-slides[manim,pyside6-full]"
```

### pip

```bash
pip install manim-slides
pip install "manim-slides[pyside6-full]"
```

### オプション依存関係 (extras)

| Extra | 説明 |
|---|---|
| `full` | magic, manim, sphinx-directive を含む |
| `magic` | Jupyter notebook サポート |
| `manim` | ManimCE を含める |
| `manimgl` | ManimGL を含める |
| `pyqt6` / `pyqt6-full` | PyQt6 バインディング |
| `pyside6` / `pyside6-full` | PySide6 バインディング |
| `sphinx-directive` | Sphinx ドキュメント生成 |

**重要:** v5.1 以降、`manim-slides present` と `manim-slides wizard` には Qt バインディングが必要。

---

## 7. コード例集

### 7.1 基本例

```python
from manim import *
from manim_slides import Slide

class BasicExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.next_slide()

        self.next_slide(loop=True)
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide()

        self.play(dot.animate.move_to(ORIGIN))
```

### 7.2 ループ例

```python
from manim import *
from manim_slides import Slide

class LoopExample(Slide):
    def construct(self):
        dot = Dot(color=BLUE, radius=1)
        self.play(FadeIn(dot))
        self.next_slide(loop=True)
        self.play(Indicate(dot, scale_factor=2))
        self.next_slide()
        self.play(FadeOut(dot))
```

### 7.3 自動進行例

```python
from manim import *
from manim_slides import Slide

class AutoNextExample(Slide):
    def construct(self):
        square = Square(color=RED, side_length=2)
        self.play(GrowFromCenter(square))
        self.next_slide(auto_next=True)
        self.play(Wiggle(square))
        self.next_slide()
        self.wipe(square)
```

### 7.4 スピーカーノート例

```python
from manim import *
from manim_slides import Slide

class SpeakerNotesExample(Slide):
    def construct(self):
        self.next_slide(notes="Some introduction")
        square = Square(color=GREEN, side_length=2)
        self.play(GrowFromCenter(square))
        self.next_slide(notes="We now rotate the slide")
        self.play(Rotate(square, PI / 2))
        self.next_slide(notes="Bye bye")
        self.zoom(square)
```

### 7.5 Canvas 例

```python
from manim import *
from manim_slides import Slide

class CanvasExample(Slide):
    def update_canvas(self):
        self.counter += 1
        old_slide_number = self.canvas["slide_number"]
        new_slide_number = Text(f"{self.counter}").move_to(old_slide_number)
        self.play(Transform(old_slide_number, new_slide_number))

    def construct(self):
        title = Text("My Title").to_corner(UL)
        self.counter = 1
        slide_number = Text("1").to_corner(DL)
        self.add_to_canvas(title=title, slide_number=slide_number)
        self.play(FadeIn(title), FadeIn(slide_number))
        self.next_slide()

        circle = Circle(radius=2)
        dot = Dot()
        self.update_canvas()
        self.play(Create(circle))
        self.play(MoveAlongPath(dot, circle))
        self.next_slide()

        self.update_canvas()
        square = Square()
        self.wipe(self.mobjects_without_canvas, square)
        self.next_slide()

        self.update_canvas()
        self.play(Transform(self.canvas["title"],
                           Text("New Title").to_corner(UL)))
        self.next_slide()

        self.remove_from_canvas("title", "slide_number")
        self.wipe(self.mobjects_without_canvas, [])
```

### 7.6 Wipe トランジション例

```python
from manim import *
from manim_slides import Slide

class WipeExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        square = Square()
        text = Text("This is a wipe example").next_to(square, DOWN)
        beautiful = Text("Beautiful, no?")

        self.play(FadeIn(circle))
        self.next_slide()
        self.wipe(circle, Group(square, text))
        self.next_slide()
        self.wipe(Group(square, text), beautiful, direction=UP)
        self.next_slide()
        anim = self.wipe(beautiful, circle, direction=DOWN + RIGHT,
                        return_animation=True)
        self.play(anim)
```

### 7.7 Zoom トランジション例

```python
from manim import *
from manim_slides import Slide

class ZoomExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        square = Square()
        self.play(FadeIn(circle))
        self.next_slide()
        self.zoom(circle, square)
        self.next_slide()
        anim = self.zoom(square, circle, out=True, scale=10.0,
                        return_animation=True)
        self.play(anim)
```

### 7.8 Animation クラス直接利用例

```python
from manim import *
from manim_slides import Slide
from manim_slides.slide.animation import Wipe, Zoom

class WipeClassExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        square = Square()
        self.play(FadeIn(circle))
        self.next_slide()
        self.play(Wipe(circle, square, shift=3 * LEFT))

class ZoomClassExample(Slide):
    def construct(self):
        circles = [Circle(radius=i) for i in range(1, 4)]
        self.play(FadeIn(circles[0]))
        self.next_slide()
        for i in range(2):
            self.play(Zoom(circles[i], circles[i+1]))
            self.next_slide()
```

### 7.9 3D スライド例

```python
from manim import *
from manim_slides import ThreeDSlide

class ThreeDExample(ThreeDSlide):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle(radius=3, color=BLUE)
        dot = Dot(color=RED)

        self.add(axes)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(GrowFromCenter(circle))
        self.begin_ambient_camera_rotation(rate=75 * DEGREES / 4)

        self.next_slide()
        self.next_slide(loop=True)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.next_slide()

        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(dot.animate.move_to(ORIGIN))
```

### 7.10 カスタムシーン (MovingCameraScene) 例

```python
from manim import *
from manim_slides import Slide

class MovingCameraSlide(Slide, MovingCameraScene):
    pass

class SubclassExample(MovingCameraSlide):
    def construct(self):
        self.camera.frame.save_state()
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=WHITE, x_range=[0, 3 * PI])
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        self.add(ax, graph, dot_1, dot_2)

        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
        self.next_slide()
        self.play(self.camera.frame.animate.move_to(dot_2))
        self.next_slide()
        self.play(Restore(self.camera.frame))
        self.wait()
```

### 7.11 wait_time_between_slides 例

```python
from manim import *
from manim_slides import Slide

class WithWaitExample(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1
        circle = Circle(radius=2)
        arrow = Arrow().next_to(circle, RIGHT).scale(-1)
        text = Text("No more\ngap").next_to(arrow, RIGHT)
        self.play(Create(arrow), FadeIn(text))
        self.play(Create(circle))
        self.next_slide()
        self.play(FadeOut(circle))
```

---

## 8. ベストプラクティス・Tips

### スライド設計

1. **`next_slide()` は区切り**: 最初と最後に呼ぶ必要はない (自動追加される)
2. **loop は次のスライドに適用**: `self.next_slide(loop=True)` の後のアニメーションがループする
3. **Canvas で永続オブジェクトを管理**: タイトルやスライド番号など複数スライドにまたがるオブジェクトには Canvas を使う
4. **`mobjects_without_canvas` でトランジション**: Canvas オブジェクト以外を一括で切り替えられる

### パフォーマンス

1. **`wait_time_between_slides`**: デフォルト 0 だとスライド間でギャップが生じることがある。`0.1` に設定すると改善
2. **`skip_reversing=True`**: 逆再生が不要なら設定して高速化
3. **PPTX のメモリ制限**: 多数のスライドでは PowerPoint のメモリ問題に注意

### エクスポート

1. **HTML 配布**: `--one-file --offline` で完全自己完結型 HTML を生成
2. **GitHub Pages**: 公式のスターターテンプレートと GitHub Actions が利用可能
3. **PDF はバックアップ**: アニメーションが失われるため、あくまでバックアップ

### 互換性

1. **ManimCE を推奨**: ManimGL サポートは限定的バージョンのみ保証
2. **インポート順序**: 先に manim/manimlib をインポートしてから manim_slides をインポート
3. **Qt バインディング必須**: v5.1+ で present/wizard を使うには PySide6 または PyQt6 が必要

---

## 9. FAQ・トラブルシューティング

- **インタラクティブスライド不可**: スライドは事前レンダリングされた静的ビデオ。インタラクティブ機能が必要な場合は OpenGL レンダラーのプレビュー機能を使用
- **黒画面**: Qt 関連の問題。v5.1.7+ で改善済み。v5.5.3 では macOS で絶対パスを強制して解決
- **Windows 解像度**: ディスプレイスケーリングを 100% に設定
- **HTML リンク切れ**: `--one-file` なしだとアセットフォルダが別途必要。HTML ファイルとアセットフォルダを一緒に移動する
- **PPTX メディア再生失敗**: ビデオ品質を下げる、スライド数を減らす、GPU アクセラレーションを無効化

---

## 10. バージョン履歴 (最新)

| バージョン | 主な変更 |
|---|---|
| v5.5.3 | シーンをアルファベット順にソート、macOS での黒ビデオ修正、特殊文字パス修正 |
| v5.5.2 | render が Manim の終了コードを返すように、ギャラリー追加 |
| v5.5.1 | HTML テンプレートに常にノートプラグインを含める、SPACE キーでスライド一時停止 |
| v5.5.0 | 外部ビデオ挿入 (src パラメータ)、大きなビデオの自動分割、RevealJS 5.2 に更新 |
| v5.4.2 | start_skip_animations が ManimCE に正しく引数を渡すよう修正 |
