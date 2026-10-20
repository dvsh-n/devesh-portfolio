"""Render the replacement opening title using the original Manim wordmark.

Render at 3840x2160, 30 fps. Composite only its upper 1660 pixels onto
muMPC_full.mp4 through 5.1 s, retaining the original animated footer.
"""
from manim import (
    Scene, Text, VGroup, RoundedRectangle, DOWN, UP, RIGHT,
    FadeIn, FadeOut, GrowFromCenter, AnimationGroup, config, rate_functions,
)
config.background_color = '#000000'
config.frame_width = 128 / 9
config.frame_height = 8

class ReplacementIntro(Scene):
    def construct(self):
        tile = RoundedRectangle(width=1.18, height=1.18, corner_radius=0.22,
                                stroke_color='#50D6FF', stroke_width=2.6,
                                fill_color='#50D6FF', fill_opacity=0.08)
        mu = Text('μ', font='Lato', weight='BOLD', font_size=65, color='#50D6FF')
        mu.move_to(tile.get_center())
        mpc = Text('MPC', font='Lato', weight='BOLD', font_size=70, color='#F4F7FB')
        mpc.next_to(tile, RIGHT, buff=0.25)
        logo = VGroup(tile, mu, mpc).scale(1.1).move_to(0.58 * UP)
        subtitle = VGroup(
            Text('Safe Nonlinear and World Model Control in', font='Lato', font_size=30, color='#F4F7FB'),
            Text('Microseconds via Koopman-Linearized Pre-Compilation', font='Lato', font_size=30, color='#F4F7FB', t2c={'Microseconds': '#50D6FF'}),
        ).arrange(DOWN, buff=0.15)
        if subtitle.width > 12.9:
            subtitle.scale_to_fit_width(12.9)
        subtitle.next_to(logo, DOWN, buff=0.48)
        self.play(GrowFromCenter(tile), FadeIn(mu, shift=0.12 * UP),
                  FadeIn(mpc, shift=0.22 * RIGHT), run_time=0.95,
                  rate_func=rate_functions.ease_out_cubic)
        self.play(AnimationGroup(*(FadeIn(line, shift=0.12 * UP) for line in subtitle), lag_ratio=0.18), run_time=1.05)
        self.wait(2.35)
        self.play(FadeOut(VGroup(logo, subtitle), shift=0.10 * UP), run_time=0.65)
        self.wait(0.1)
