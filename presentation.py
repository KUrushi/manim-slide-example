from manim import *
from manim_slides import Slide

# Apple HIG Dark Mode カラーパレット
ACCENT = "#0A84FF"          # systemBlue (Dark)
TEXT_PRIMARY = "#FFFFFF"     # label
TEXT_SECONDARY = "#8E8E93"   # systemGray
TEXT_TERTIARY = "#636366"    # systemGray2
TEXT_LABEL = "#CCCCCC"          # セクションタイトル・STEPラベル用（装飾的だが読む必要あり）
BG_COLOR = "#1C1C1E"        # secondarySystemBackground
HIG_GREEN = "#30D158"        # systemGreen (Dark)
HIG_YELLOW = "#FFD60A"       # systemYellow (Dark)
HIG_RED = "#FF453A"          # systemRed (Dark)
FONT_MAIN = "Hiragino Kaku Gothic Pro"
FONT_CODE = "UDEV Gothic 35NFLG"


class ClaudeCodeManimSlides(Slide):

    def update_slide_number(self):
        self.slide_count += 1
        old_num = self.canvas["slide_number"]
        new_num = (
            Text(str(self.slide_count), font_size=18, color=TEXT_TERTIARY, font=FONT_MAIN)
            .to_corner(DR)
        )
        self.play(Transform(old_num, new_num), run_time=0.3)

    def make_step_label(self, number):
        return Text(
            f"STEP {number}",
            font_size=18,
            color=TEXT_LABEL,
            weight=BOLD,
            font=FONT_MAIN,
        ).to_edge(UP, buff=0.8)

    def switch_slide(self, new_content):
        for m in list(self.mobjects_without_canvas):
            self.remove(m)
        self.add(new_content)

    def construct(self):
        self.camera.background_color = ManimColor(BG_COLOR)
        self.wait_time_between_slides = 0.1

        # Canvas
        self.slide_count = 1
        slide_number = Text("1", font_size=18, color=TEXT_TERTIARY, font=FONT_MAIN).to_corner(DR)
        self.add_to_canvas(slide_number=slide_number)
        self.add(slide_number)

        # ---- SLIDE 1: Title ----
        self.next_slide(notes="今日は、エンジニアの発表資料作りを劇的に楽にする方法についてお話しします。")

        title = Text(
            "Claude Code + manim-slides\nで発表資料を自動生成する",
            font_size=48, color=TEXT_PRIMARY, weight=BOLD, line_spacing=1.4, font=FONT_MAIN,
        )
        speaker_info = Text(
            "Kazuki Urushiyama / Reckit Team", font_size=18, color=TEXT_TERTIARY, font=FONT_CODE,
        ).to_corner(DR, buff=0.8)
        self.play(FadeIn(title), FadeIn(speaker_info))

        # ---- SLIDE 2: Conclusion ----
        self.next_slide(notes="結論から言います。Claude Code に自然言語で指示するだけで、アニメーション付きのスライドが完成します。")

        self.update_slide_number()
        # P1: 白文字ベース + キーワードのみ青で強調
        conc_l1a = Text("Claude Code", font_size=44, color=ACCENT, weight=BOLD, font=FONT_MAIN)
        conc_l1b = Text(" に指示するだけで", font_size=44, color=TEXT_PRIMARY, weight=BOLD, font=FONT_MAIN)
        conc_line1 = VGroup(conc_l1a, conc_l1b).arrange(RIGHT, buff=0.05)
        conc_line2 = Text(
            "アニメーション付きスライドが手に入る",
            font_size=44, color=TEXT_PRIMARY, weight=BOLD, font=FONT_MAIN,
        )
        conclusion = VGroup(conc_line1, conc_line2).arrange(DOWN, buff=0.5)
        self.switch_slide(conclusion)

        # ---- SLIDE 3: Shared Ground ----
        self.next_slide(notes="皆さん、発表って大事ですよね。でも正直、スライド作りは面倒じゃないですか？")

        self.update_slide_number()
        empathy = Text(
            "エンジニアにとって\n発表資料作りは面倒",
            font_size=48, color=TEXT_PRIMARY, weight=BOLD, line_spacing=1.4, font=FONT_MAIN,
        )
        self.switch_slide(empathy)

        # ---- SLIDE 4: Existing Tool Limitations ----
        self.next_slide(notes="PowerPoint は図形の位置調整に時間を取られます。reveal.js や Beamer はアニメーションが限定的です。")

        self.update_slide_number()

        section_label = Text(
            "既存ツールの限界", font_size=20, color=TEXT_LABEL, weight=BOLD, font=FONT_MAIN,
        ).to_edge(UP, buff=0.8)

        tool1_name = Text("PowerPoint / Keynote", font_size=26, color=TEXT_PRIMARY, font=FONT_MAIN)
        tool1_issue = Text("図形の位置調整に時間を取られる", font_size=26, color=TEXT_PRIMARY, font=FONT_MAIN)
        row1 = VGroup(tool1_name, tool1_issue).arrange(RIGHT, buff=0.6)

        tool2_name = Text("reveal.js / Beamer", font_size=26, color=TEXT_PRIMARY, font=FONT_MAIN)
        tool2_issue = Text("コードで書けるが、アニメーションが限定的", font_size=26, color=TEXT_PRIMARY, font=FONT_MAIN)
        row2 = VGroup(tool2_name, tool2_issue).arrange(RIGHT, buff=0.6)

        rows = VGroup(row1, row2).arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        slide4 = VGroup(section_label, rows).arrange(DOWN, buff=1.0)

        self.switch_slide(slide4)

        # ---- SLIDE 5: What is manim-slides? ----
        self.next_slide(notes="そこで manim-slides です。Manim をベースに、アニメーション付きスライドを Python コードだけで作れるツールです。")

        self.update_slide_number()
        manim_title = Text("manim-slides", font_size=52, color=ACCENT, weight=BOLD, font=FONT_MAIN)
        desc1 = Text("Python コードで書くアニメーション付きスライド", font_size=26, color=TEXT_PRIMARY, font=FONT_MAIN)
        desc2 = Text("Manim の描画力 × プレゼンの操作性", font_size=26, color=TEXT_PRIMARY, font=FONT_MAIN)
        slide5 = VGroup(manim_title, desc1, desc2).arrange(DOWN, buff=0.6)
        self.switch_slide(slide5)

        # ---- SLIDE 6: Animation Power — Sorting Example ----
        self.next_slide(notes="例えばソートアルゴリズム。静止画では処理の流れが伝わりにくいですが、アニメーションなら比較・交換の過程を直感的に理解できます。こういった可視化が数行の Python で作れるのが manim-slides の強みです。")

        self.update_slide_number()

        sort_section = Text(
            "アニメーションの威力", font_size=20, color=TEXT_LABEL, weight=BOLD, font=FONT_MAIN,
        ).move_to(UP * 3.0)

        sort_title = Text(
            "例: ソートの可視化", font_size=40, color=ACCENT, weight=BOLD, font=FONT_MAIN,
        ).move_to(UP * 2.0)

        # バーチャート: ソート前の配列 [5, 2, 8, 1, 4]
        values = [5, 2, 8, 1, 4]
        baseline_y = DOWN * 1.5
        bar_spacing = 1.3
        start_x = -2.6

        bar_items = []
        bar_group = VGroup()
        for i, v in enumerate(values):
            bar = RoundedRectangle(
                corner_radius=0.05, width=0.8, height=v * 0.4,
                color=ACCENT, fill_opacity=0.6, fill_color=ACCENT,
            )
            lbl = Text(str(v), font_size=20, color=TEXT_PRIMARY, font=FONT_CODE)
            # バーを下揃えで配置
            x_pos = start_x + i * bar_spacing
            bar.move_to(baseline_y, aligned_edge=DOWN).set_x(x_pos)
            lbl.next_to(bar, DOWN, buff=0.15)
            item = VGroup(bar, lbl)
            bar_items.append(item)
            bar_group.add(item)

        sort_static = VGroup(sort_section, sort_title, bar_group)
        self.switch_slide(sort_static)

        # バブルソート全体をアニメーション（各ステップに間隔を入れる）
        n = len(values)
        for pass_idx in range(n - 1):
            for j in range(n - 1 - pass_idx):
                left_val = int(bar_items[j][1].text)
                right_val = int(bar_items[j + 1][1].text)

                # ハイライト
                hl_left = SurroundingRectangle(bar_items[j], color=HIG_YELLOW, buff=0.08, corner_radius=0.1)
                hl_right = SurroundingRectangle(bar_items[j + 1], color=HIG_YELLOW, buff=0.08, corner_radius=0.1)
                self.play(Create(hl_left), Create(hl_right), run_time=0.4)

                if left_val > right_val:
                    cmp_text = Text(
                        f"{left_val} > {right_val} → 交換!", font_size=22, color=ACCENT, font=FONT_MAIN,
                    ).move_to(DOWN * 3.2)
                    self.play(FadeIn(cmp_text), run_time=0.3)

                    # ハイライトを先に消してから交換（枠の突き抜け防止）
                    self.play(FadeOut(hl_left), FadeOut(hl_right), run_time=0.2)

                    x_left = bar_items[j].get_x()
                    x_right = bar_items[j + 1].get_x()
                    self.play(
                        bar_items[j].animate.set_x(x_right),
                        bar_items[j + 1].animate.set_x(x_left),
                        run_time=0.6,
                    )
                    bar_items[j], bar_items[j + 1] = bar_items[j + 1], bar_items[j]

                    self.play(FadeOut(cmp_text), run_time=0.3)
                else:
                    cmp_text = Text(
                        f"{left_val} ≤ {right_val} → OK", font_size=22, color=TEXT_PRIMARY, font=FONT_MAIN,
                    ).move_to(DOWN * 3.2)
                    self.play(FadeIn(cmp_text), run_time=0.3)
                    self.play(FadeOut(hl_left), FadeOut(hl_right), FadeOut(cmp_text), run_time=0.3)

                # 各ステップ間に間隔をあける
                self.wait(0.5)

        # ソート完了の表示
        done_text = Text("ソート完了!", font_size=28, color=ACCENT, weight=BOLD, font=FONT_MAIN).move_to(DOWN * 3.2)
        self.play(FadeIn(done_text), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(done_text), run_time=0.3)

        # ---- SLIDE 7: But Python is tedious? ----
        self.next_slide(notes="manim-slides は強力ですが、このようなアニメーションも Python コードで書く必要があります。そこで Claude Code の出番です。")

        self.update_slide_number()
        bridge = Text(
            "でも Python を書くのも面倒？",
            font_size=48, color=TEXT_PRIMARY, weight=BOLD, font=FONT_MAIN,
        )
        self.switch_slide(bridge)

        # ---- SLIDE 7: Workflow Overview ----
        self.next_slide(notes="ワークフローは全部で7ステップです。まず全体像を見てから、各ステップを詳しく見ていきましょう。")

        self.update_slide_number()

        wf_section = Text(
            "ワークフロー全体像", font_size=20, color=TEXT_LABEL, weight=BOLD, font=FONT_MAIN,
        ).to_edge(UP, buff=0.8)

        step_labels = [
            "1. アイデアを伝える",
            "2. 対話で要件を詰める",
            "3. slides.md 生成",
            "4. コード生成",
            "5. レンダリング",
            "6. レビュー & 改善",
            "7. 発表 & エクスポート",
        ]
        step_colors = [
            TEXT_SECONDARY, TEXT_SECONDARY, ACCENT,
            ACCENT, TEXT_SECONDARY, ACCENT, TEXT_SECONDARY,
        ]

        boxes = VGroup()
        for label, color in zip(step_labels, step_colors):
            box = RoundedRectangle(
                corner_radius=0.1, width=2.5, height=1.0,
                color=color, fill_opacity=0.08,
            )
            txt = Text(label, font_size=18, color=TEXT_PRIMARY, font=FONT_MAIN)
            txt.move_to(box)
            boxes.add(VGroup(box, txt))

        def make_arrow():
            return Arrow(ORIGIN, RIGHT * 0.4, color=TEXT_TERTIARY, stroke_width=2,
                         max_tip_length_to_length_ratio=0.3)

        # Row 1: Steps 1-4
        row1 = VGroup()
        for i in range(4):
            row1.add(boxes[i])
            if i < 3:
                row1.add(make_arrow())
        row1.arrange(RIGHT, buff=0.15)

        # Row 2: Steps 5-7
        row2 = VGroup()
        for i in range(4, 7):
            row2.add(boxes[i])
            if i < 6:
                row2.add(make_arrow())
        row2.arrange(RIGHT, buff=0.15)

        flow = VGroup(row1, row2).arrange(DOWN, buff=0.5)

        # 凡例: アクセントカラーの意味を明示
        legend_box = RoundedRectangle(
            corner_radius=0.05, width=0.25, height=0.25,
            color=ACCENT, fill_opacity=0.08,
        )
        legend_text = Text("= Claude Code が自動化", font_size=14, color=TEXT_PRIMARY, font=FONT_MAIN)
        legend = VGroup(legend_box, legend_text).arrange(RIGHT, buff=0.2)
        legend.to_edge(DOWN, buff=0.8)

        slide7 = VGroup(wf_section, flow, legend).arrange(DOWN, buff=0.6)
        self.switch_slide(slide7)

        # ---- SLIDE: Steps 1-2 Combined — P4: 補足ステップ統合 ----
        self.next_slide(notes="最初のステップは Claude Code にアイデアを伝えるだけです。すると Claude Code が聴衆、発表時間、目的などを質問してきます。選択肢から選ぶだけで要件が整理されます。")

        self.update_slide_number()

        step12_label = Text(
            "STEP 1-2", font_size=18, color=TEXT_LABEL, weight=BOLD, font=FONT_MAIN,
        ).to_edge(UP, buff=0.8)
        step12_title = Text("アイデアから要件整理へ", font_size=44, color=TEXT_PRIMARY, weight=BOLD, font=FONT_MAIN)

        # Step 1: プロンプト（コンパクト版）
        prompt_bg = RoundedRectangle(
            corner_radius=0.15, width=9.0, height=0.7,
            color=TEXT_SECONDARY, fill_opacity=0.05, fill_color="#2C2C2E",
        )
        prompt_mark = Text(">", font_size=20, color=ACCENT, font=FONT_CODE)
        prompt_text = Text(
            "manim-slides の紹介 LT を作りたい", font_size=20, color=TEXT_PRIMARY, font=FONT_CODE,
        )
        prompt_content = VGroup(prompt_mark, prompt_text).arrange(RIGHT, buff=0.3)
        prompt_content.move_to(prompt_bg)
        prompt = VGroup(prompt_bg, prompt_content)

        # 矢印（Step 1 → Step 2 の流れを示す）
        down_arrow = Text("↓", font_size=28, color=TEXT_LABEL, font=FONT_MAIN)

        # Step 2: 対話の質問（コンパクト版）
        q_mobjects = VGroup()
        for q_text in ["聴衆は誰ですか？", "発表時間は？", "何を伝えたいですか？"]:
            bubble = RoundedRectangle(
                corner_radius=0.12, width=5.5, height=0.55,
                color=ACCENT, fill_opacity=0.08,
            )
            q = Text(q_text, font_size=18, color=TEXT_PRIMARY, font=FONT_MAIN)
            q.move_to(bubble)
            q_mobjects.add(VGroup(bubble, q))
        q_mobjects.arrange(DOWN, buff=0.2)

        step12_body = VGroup(step12_title, prompt, down_arrow, q_mobjects).arrange(DOWN, buff=0.35)
        slide_step12 = VGroup(step12_label, step12_body).arrange(DOWN, buff=0.6)

        self.switch_slide(slide_step12)

        # ---- SLIDE 10: Step 3 ----
        self.next_slide(notes="対話が終わると、Claude Code が slides.md というスライド構成書を自動生成します。配色やトランジションまで全て設計されています。")

        self.update_slide_number()

        step3_label = self.make_step_label(3)
        step3_title = Text("構成設計: slides.md", font_size=44, color=TEXT_PRIMARY, weight=BOLD, font=FONT_MAIN)

        doc_box = RoundedRectangle(
            corner_radius=0.15, width=8.0, height=3.5,
            color=TEXT_SECONDARY, fill_opacity=0.05,
        )
        doc_lines_data = [
            ("Overview:", "トピック、Key Message、聴衆", TEXT_SECONDARY, TEXT_PRIMARY),
            ("Slide 1:", "タイトル", TEXT_SECONDARY, TEXT_PRIMARY),
            ("Slide 2:", "結論（Pyramid Principle）", TEXT_SECONDARY, ACCENT),
            ("Slide 3-N:", "本文（Staircase Method）", TEXT_SECONDARY, TEXT_PRIMARY),
            ("Design:", "配色、フォント、トランジション", TEXT_SECONDARY, TEXT_PRIMARY),
        ]
        line_mobjects = VGroup()
        for key, val, kcolor, vcolor in doc_lines_data:
            k = Text(key, font_size=18, color=kcolor, weight=BOLD, font=FONT_MAIN)
            v = Text(val, font_size=18, color=vcolor, font=FONT_MAIN)
            line_mobjects.add(VGroup(k, v).arrange(RIGHT, buff=0.3))
        line_mobjects.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        line_mobjects.move_to(doc_box)
        doc = VGroup(doc_box, line_mobjects)

        slide10_body = VGroup(step3_title, doc).arrange(DOWN, buff=0.5)
        slide10 = VGroup(step3_label, slide10_body).arrange(DOWN, buff=0.8)

        self.switch_slide(slide10)

        # ---- SLIDE 11: Step 4 ----
        self.next_slide(notes="slides.md を元に、Claude Code が manim-slides の Python コードを自動生成します。ベストプラクティスに沿ったコードが出力されます。")

        self.update_slide_number()

        step4_label = self.make_step_label(4)
        step4_title = Text("Python コードを自動生成", font_size=44, color=TEXT_PRIMARY, weight=BOLD, font=FONT_MAIN)

        code_box = RoundedRectangle(
            corner_radius=0.15, width=9.0, height=3.0,
            color=TEXT_SECONDARY, fill_opacity=0.05,
        )
        code_line1 = Text("class Presentation(Slide):", font_size=18, color=ACCENT, font=FONT_CODE)
        code_line2 = Text("def construct(self):", font_size=18, color=TEXT_PRIMARY, font=FONT_CODE)
        code_line3 = Text("# Canvas, Wipe, Progressive reveal...", font_size=18, color=TEXT_SECONDARY, font=FONT_CODE)
        code_line4 = Text("# 全て自動で構成", font_size=18, color=TEXT_SECONDARY, font=FONT_CODE)
        code_lines = VGroup(code_line1, code_line2, code_line3, code_line4)
        code_lines.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        # Python のインデントを明示的に再現
        indent = 0.4
        code_line2.shift(RIGHT * indent)
        code_line3.shift(RIGHT * indent * 2)
        code_line4.shift(RIGHT * indent * 2)
        code_lines.move_to(code_box)
        code = VGroup(code_box, code_lines)

        slide11_body = VGroup(step4_title, code).arrange(DOWN, buff=0.5)
        slide11 = VGroup(step4_label, slide11_body).arrange(DOWN, buff=0.8)

        self.switch_slide(slide11)

        # ---- SLIDE: Steps 5&7 Combined — P4: 補足ステップ統合 ----
        self.next_slide(notes="コードが生成されたら、2つのコマンドでレンダリングと HTML エクスポートを行います。完成したスライドは HTML, PPTX, PDF にもエクスポートできます。")

        self.update_slide_number()

        step57_label = Text(
            "STEP 5 & 7", font_size=18, color=TEXT_LABEL, weight=BOLD, font=FONT_MAIN,
        ).to_edge(UP, buff=0.8)
        step57_title = Text("ビルド & デリバリー", font_size=44, color=TEXT_PRIMARY, weight=BOLD, font=FONT_MAIN)

        # ターミナル（コンパクト版）
        term_bg = RoundedRectangle(
            corner_radius=0.15, width=10.0, height=2.0,
            color=TEXT_SECONDARY, fill_opacity=0.05, fill_color="#2C2C2E",
        )
        dot_red = Dot(radius=0.05, color=HIG_RED).move_to(term_bg.get_corner(UL) + RIGHT * 0.35 + DOWN * 0.25)
        dot_yellow = Dot(radius=0.05, color=HIG_YELLOW).next_to(dot_red, RIGHT, buff=0.12)
        dot_green = Dot(radius=0.05, color=HIG_GREEN).next_to(dot_yellow, RIGHT, buff=0.12)

        dollar1 = Text("$", font_size=16, color=ACCENT, font=FONT_CODE)
        cmd1_text = Text("manim-slides render presentation.py", font_size=16, color=TEXT_PRIMARY, font=FONT_CODE)
        cmd1 = VGroup(dollar1, cmd1_text).arrange(RIGHT, buff=0.2)

        dollar2 = Text("$", font_size=16, color=ACCENT, font=FONT_CODE)
        cmd2_text = Text("manim-slides convert --to html ... output.html", font_size=16, color=TEXT_PRIMARY, font=FONT_CODE)
        cmd2 = VGroup(dollar2, cmd2_text).arrange(RIGHT, buff=0.2)

        cmds = VGroup(cmd1, cmd2).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        cmds.move_to(term_bg).shift(DOWN * 0.15)
        left_margin = term_bg.get_left()[0] + 0.4
        cmds.align_to(left_margin * RIGHT, LEFT)
        terminal = VGroup(term_bg, dot_red, dot_yellow, dot_green, cmds)

        # エクスポート形式（横並びコンパクト版）
        export_items = VGroup()
        for fmt, desc in [("▶ Live", "発表"), ("HTML", "共有"), ("PPTX", "互換"), ("PDF", "保存")]:
            f_text = Text(fmt, font_size=18, color=ACCENT, weight=BOLD, font=FONT_CODE)
            d_text = Text(desc, font_size=16, color=TEXT_PRIMARY, font=FONT_MAIN)
            export_items.add(VGroup(f_text, d_text).arrange(DOWN, buff=0.15))
        export_items.arrange(RIGHT, buff=0.8)

        step57_body = VGroup(step57_title, terminal, export_items).arrange(DOWN, buff=0.5)
        slide_step57 = VGroup(step57_label, step57_body).arrange(DOWN, buff=0.6)

        self.switch_slide(slide_step57)

        # ---- SLIDE 13: Step 6 — Review with Playwright MCP ----
        self.next_slide(notes="HTML にエクスポートしたスライドを Playwright MCP でブラウザに表示し、各スライドのスクリーンショットを自動で撮影します。聴衆目線でメッセージ明確性、認知負荷、可読性などを評価し、改善点を特定してコードに反映します。")

        self.update_slide_number()

        step6_label = self.make_step_label(6)
        step6_title = Text("Playwright MCP でレビュー", font_size=44, color=TEXT_PRIMARY, weight=BOLD, font=FONT_MAIN)
        # P7: Playwright MCP の補足説明を追加
        step6_subtitle = Text(
            "ブラウザ自動操作でスライドを聴衆目線で評価",
            font_size=20, color=TEXT_LABEL, font=FONT_MAIN,
        )

        # ブラウザウィンドウ風デザイン
        browser_bg = RoundedRectangle(
            corner_radius=0.15, width=9.0, height=3.5,
            color=TEXT_SECONDARY, fill_opacity=0.05,
            fill_color="#2C2C2E",
        )
        # ウィンドウバー
        b_dot_red = Dot(radius=0.06, color=HIG_RED).move_to(browser_bg.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.3)
        b_dot_yellow = Dot(radius=0.06, color=HIG_YELLOW).next_to(b_dot_red, RIGHT, buff=0.15)
        b_dot_green = Dot(radius=0.06, color=HIG_GREEN).next_to(b_dot_yellow, RIGHT, buff=0.15)
        b_window_bar = VGroup(b_dot_red, b_dot_yellow, b_dot_green)

        # レビュー項目
        review_items = VGroup()
        for check, criterion in [
            ("\u2713", "メッセージ明確性"),
            ("\u2713", "認知負荷"),
            ("\u2713", "可読性・コントラスト"),
            ("!", "要素の重なり検出"),
        ]:
            is_issue = check == "!"
            check_color = HIG_YELLOW if is_issue else HIG_GREEN
            mark = Text(check, font_size=20, color=check_color, font=FONT_MAIN)
            label = Text(criterion, font_size=20, color=TEXT_PRIMARY if not is_issue else ACCENT, font=FONT_MAIN)
            review_items.add(VGroup(mark, label).arrange(RIGHT, buff=0.3))
        review_items.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        review_items.move_to(browser_bg).shift(DOWN * 0.2)

        browser = VGroup(browser_bg, b_window_bar, review_items)

        review_note = Text("スクリーンショット × 聴衆視点の自動評価", font_size=20, color=TEXT_PRIMARY, font=FONT_MAIN)

        slide13_body = VGroup(step6_title, step6_subtitle, browser, review_note).arrange(DOWN, buff=0.35)
        slide13 = VGroup(step6_label, slide13_body).arrange(DOWN, buff=0.6)

        self.switch_slide(slide13)

        # ---- SLIDE: Evidence ----
        self.next_slide(notes="実はこのプレゼン自体が、Claude Code に指示して manim-slides で生成したものです。もちろん完璧に一発で出るわけではなく、レイアウトの微調整は必要ですが、ゼロから作るのとは比べものになりません。Python の知識がなくても Claude Code が書いてくれるので大丈夫です。")

        self.update_slide_number()
        # P1: 白文字ベース + ツール名のみ青で強調
        meta_l1 = Text("このスライドも", font_size=44, color=TEXT_PRIMARY, weight=BOLD, font=FONT_MAIN)
        meta_l2 = Text("Claude Code + manim-slides", font_size=44, color=ACCENT, weight=BOLD, font=FONT_MAIN)
        meta_l3 = Text("で作りました", font_size=44, color=TEXT_PRIMARY, weight=BOLD, font=FONT_MAIN)
        meta = VGroup(meta_l1, meta_l2, meta_l3).arrange(DOWN, buff=0.5)
        self.switch_slide(meta)

        # ---- SLIDE 15: Closing ----
        self.next_slide(notes="伝えたいことを言語化するだけで、あとは Claude Code と manim-slides が形にしてくれます。ぜひ試してみてください。")

        self.update_slide_number()
        closing_msg = Text(
            "伝えたいことを伝えるだけ。\nスライドは Claude Code が作る。",
            font_size=44, color=TEXT_PRIMARY, weight=BOLD, line_spacing=1.4, font=FONT_MAIN,
        )
        install_cmd = Text(
            "pip install manim-slides", font_size=20, color=TEXT_TERTIARY, font=FONT_CODE,
        )
        closing = VGroup(closing_msg, install_cmd).arrange(DOWN, buff=1.0)
        self.switch_slide(closing)

        # 最終スライド — クロージングで終了。空白スライドを生成しない
        self.next_slide()
