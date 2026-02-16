# Playwright MCP による RevealJS HTML ナビゲーション

## RevealJS HTML の構造

manim-slides が生成する `output.html` は RevealJS 5.2.0 をベースとしている。

```html
<div class="reveal">
  <div class="slides">
    <section data-background-video="data:video/mp4;base64,...">
      <aside class="notes" data-markdown>スピーカーノート</aside>
    </section>
    <section data-background-video="data:video/mp4;base64,...">
      <aside class="notes" data-markdown>スピーカーノート</aside>
    </section>
    <!-- ... -->
  </div>
</div>
```

### 特徴

- 各 `<section>` が1スライドに対応
- 動画は `data-background-video` 属性に Base64 エンコードで埋め込み
- スピーカーノートは `<aside class="notes" data-markdown>` 内
- `--one-file --offline` オプションで全リソースがインライン化される

## ナビゲーション手順

### Step 1: ビューポート設定

プレゼンテーションの実際の見た目を再現するため、標準的な解像度に設定する。

```
mcp__playwright__browser_resize(width=1920, height=1080)
```

### Step 2: HTML ファイルを開く

`file://` プロトコルで絶対パスを指定する。

```
mcp__playwright__browser_navigate(url="file:///absolute/path/to/output.html")
```

**注意**: パスは必ず絶対パスを使用すること。相対パスは動作しない。

### Step 3: 総スライド数を取得

```
mcp__playwright__browser_evaluate(expression="Reveal.getTotalSlides()")
```

### Step 4: 各スライドをキャプチャ

各スライド (i = 0 ~ N-1) について以下を順に実行:

#### 4a. スライドへ移動

```
mcp__playwright__browser_evaluate(expression="Reveal.slide(i)")
```

#### 4b. 動画読み込み待機

動画がバックグラウンドに埋め込まれている場合、読み込みを待つ必要がある。

```javascript
// browser_evaluate で実行
(function() {
  const slide = Reveal.getCurrentSlide();
  const video = slide.slideBackgroundContentElement?.querySelector('video');
  if (!video) return 'no-video';
  return video.readyState >= 2 ? 'ready' : 'loading';
})()
```

`loading` が返った場合は 1-2 秒待機してから再チェックする。

#### 4c. スクリーンショット取得

```
mcp__playwright__browser_take_screenshot()
```

**設定**: fullPage は false（プレゼンビューのみキャプチャ）

#### 4d. スピーカーノート抽出

```javascript
// browser_evaluate で実行
(function() {
  const notes = Reveal.getCurrentSlide().querySelector('aside.notes');
  return notes ? notes.textContent.trim() : null;
})()
```

## RevealJS API リファレンス

### ナビゲーション

| メソッド | 説明 |
|---------|------|
| `Reveal.getTotalSlides()` | 総スライド数を返す |
| `Reveal.slide(indexH, indexV)` | 指定スライドへ移動（0-based） |
| `Reveal.next()` | 次のスライド/フラグメントへ |
| `Reveal.prev()` | 前のスライド/フラグメントへ |
| `Reveal.getCurrentSlide()` | 現在のスライド DOM 要素を返す |
| `Reveal.getIndices()` | 現在のインデックス `{ h, v, f }` を返す |

### スライド情報

| メソッド | 説明 |
|---------|------|
| `Reveal.getSlidePastCount()` | 通過済みスライド数 |
| `Reveal.isFirstSlide()` | 最初のスライドか |
| `Reveal.isLastSlide()` | 最後のスライドか |

### 動画関連

```javascript
// 動画要素の取得
const bg = Reveal.getCurrentSlide().slideBackgroundContentElement;
const video = bg?.querySelector('video');

// readyState の値
// 0: HAVE_NOTHING
// 1: HAVE_METADATA
// 2: HAVE_CURRENT_DATA（最低限表示可能）
// 3: HAVE_FUTURE_DATA
// 4: HAVE_ENOUGH_DATA
```

## ベストプラクティス

1. **ビューポートは 1920x1080** に設定する。これがプレゼンテーションの標準解像度
2. **スライド遷移後は最低1秒待機** してから動画の読み込み状態をチェックする
3. **`file://` URL は必ず絶対パス** を使用する
4. **スクリーンショットは fullPage: false** でプレゼンビューのみをキャプチャする
5. **動画の読み込みが完了してからスクリーンショット** を取得する（`readyState >= 2`）
6. **連続取得時は各スライド間に待機時間** を入れ、レンダリング完了を確保する
