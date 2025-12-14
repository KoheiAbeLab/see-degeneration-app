"""
SEE Degeneration App (Kinematic Dictionary)
-------------------------------------------

This application visualizes the degeneration structure used in the Spiral
Exponential Equation (SEE) framework.

For a selected derivative order n (1 to 10), it displays:
- SEE rotation rule:           f^(n)(t) = e^{i n θ} f(t)
- Degenerate (projected) form: f^(n)(t) = cos(nθ) f(t)
- Degenerate angle:            θ = π/(2n)
- Final form at that angle:    f^(n)(t) = 0

On the right, the app draws n+1 unit vectors in the complex plane whose
directions are equally spaced by θ (0·θ, 1·θ, 2·θ, ...), making the
equal-angle derivative arrangement explicit. The kinematic-state panel
summarizes the corresponding motion class (up to snap) implied by the
degeneration structure.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Circle, Arc, FancyBboxPatch

# ---------- Main update function ----------

def update(val):
    # Get current n from slider (integer in [1, 10])
    n = int(round(s_n.val))
    n = max(1, min(10, n))

    # Degeneration angle θ = π / (2n)
    theta = np.pi / (2.0 * n)          # radians
    theta_deg = theta * 180.0 / np.pi  # degrees

    # --- Left-hand text (two-column layout: label | content) ---

    text_label_n.set_text("Order of derivative:")
    text_value_n.set_text(rf"$n={n}$")

    text_label_see.set_text("SEE:")
    text_value_see.set_text(rf"$f^{{({n})}}(t)=e^{{i\,{n}\theta}}\,f(t)$")

    text_label_deg.set_text("Degenerate form:")
    text_value_deg.set_text(rf"$f^{{({n})}}(t)=\cos({n}\theta)\,f(t)$")

    text_label_theta.set_text("Degenerate angle:")
    text_value_theta.set_text(
        rf"$\theta=\frac{{\pi}}{{2\cdot {n}}}"
        rf"\approx {theta:.4f}\,\mathrm{{rad}}"
        rf"\approx {theta_deg:.2f}^\circ$"
    )

    text_label_final.set_text("Final form:")
    text_value_final.set_text(rf"$f^{{({n})}}(t)=0$")

    # --- Kinematic state (title + body, manual line breaks) ---
    if n == 1:
        body = "position $f(t)$ is constant\n(rest)"
    elif n == 2:
        body = "velocity $f'(t)$ is constant\n(uniform motion)"
    elif n == 3:
        body = "acceleration $f''(t)$ is constant\n(uniformly accelerated motion)"
    elif n == 4:
        body = "jerk $f^{(3)}(t)$ is constant\n(constant jerk)"
    elif n == 5:
        body = "snap $f^{(4)}(t)$ is constant\n(constant snap)"
    else:
        body = rf"$f^{{({n-1})}}(t)$ is constant"

    text_kin_title.set_text("Kinematic state:")
    text_kin_body.set_text(body)

    # --- Right-hand complex plane: derivative directions ---

    ax_plane.clear()

    # Axes
    ax_plane.axhline(0, color="black", linewidth=0.8)
    ax_plane.axvline(0, color="black", linewidth=0.8)

    # Unit circle for reference
    circle = Circle((0, 0), 1.0, fill=False, linestyle="--", alpha=0.4)
    ax_plane.add_patch(circle)

    # Draw n+1 vectors: k = 0..n, angle = k * θ, length = 1
    for k in range(n + 1):
        angle = k * theta
        x = np.cos(angle)
        y = np.sin(angle)

        # Color and label by order of derivative
        if k == 0:
            color = "green"   # position
            label = "Position (0·θ)"
        elif k == 1:
            color = "blue"    # velocity
            label = "Velocity (1·θ)"
        elif k == 2:
            color = "red"     # acceleration
            label = "Acceleration (2·θ)"
        elif k == 3:
            color = "purple"  # jerk
            label = "Jerk (3·θ)"
        elif k == 4:
            color = "#f1c40f"  # snap (muted yellow)
            label = "Snap (4·θ)"
        else:
            color = "gray"    # higher derivatives
            label = "Higher derivatives"

        # Arrow from origin
        ax_plane.arrow(
            0, 0, x, y,
            length_includes_head=True,
            head_width=0.06,
            head_length=0.12,
            color=color,
            alpha=0.8,
        )

        # Mark tip of vector
        ax_plane.scatter([x], [y], color=color, s=30)

        # Dummy handle for legend
        ax_plane.plot([], [], color=color, label=label)

    # Draw small arcs between consecutive vectors to indicate angle θ
    r_arc = 0.35
    r_label = 0.45

    for k in range(n):
        start_deg = (k * theta) * 180.0 / np.pi
        end_deg = ((k + 1) * theta) * 180.0 / np.pi

        arc = Arc(
            (0, 0),
            width=2 * r_arc,
            height=2 * r_arc,
            angle=0,
            theta1=start_deg,
            theta2=end_deg,
            color="black",
            linewidth=0.7,
            alpha=0.7,
        )
        ax_plane.add_patch(arc)

        mid_angle = (k + 0.5) * theta
        x_text = r_label * np.cos(mid_angle)
        y_text = r_label * np.sin(mid_angle)
        ax_plane.text(
            x_text, y_text,
            r"$\theta$",
            fontsize=9,
            ha="center",
            va="center",
        )

    # Axis limits and style
    ax_plane.set_xlim(-1.4, 1.4)
    ax_plane.set_ylim(-1.4, 1.4)
    ax_plane.set_aspect("equal", "box")
    ax_plane.set_xlabel("Re")
    ax_plane.set_ylabel("Im")
    ax_plane.set_title(
        rf"Directions of derivatives at $\theta = \frac{{\pi}}{{2\cdot {n}}}$"
    )

    # Legend outside the plot area on the right.
    handles, labels = ax_plane.get_legend_handles_labels()
    seen = set()
    unique_handles = []
    unique_labels = []
    for h, lab in zip(handles, labels):
        if lab not in seen:
            seen.add(lab)
            unique_handles.append(h)
            unique_labels.append(lab)

    ax_plane.legend(
        unique_handles, unique_labels,
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        borderaxespad=0.0,
        fontsize=9,
    )

    fig.canvas.draw_idle()


# ---------- Main figure setup ----------

fig = plt.figure(figsize=(12, 5))

# Window title (replaces "Form1" in many matplotlib backends)
fig.canvas.manager.set_window_title("SEE Degeneration (Kinematic Dictionary)")

# Two main axes: left for text, right for complex plane
ax_text  = plt.axes([0.05, 0.25, 0.4, 0.7])
ax_plane = plt.axes([0.5, 0.25, 0.4, 0.7])

# Slider axis (bottom)
ax_n = plt.axes([0.2, 0.1, 0.6, 0.04])

# Left side: text only
ax_text.set_axis_off()

# Initial n
n0 = 4
theta0 = np.pi / (2.0 * n0)
theta0_deg = theta0 * 180.0 / np.pi

# ---- Left layout coordinates (axes coords) ----
x_label = 0.00   # label column x
x_value = 0.43   # value column x (push right to avoid overlap)

y0 = 0.92
dy = 0.12

fs_label = 14
fs_value_big = 18
fs_value = 16

# Row 1: n
text_label_n = ax_text.text(x_label, y0, "", transform=ax_text.transAxes,
                            fontsize=fs_label, va="center")
text_value_n = ax_text.text(x_value, y0, "", transform=ax_text.transAxes,
                            fontsize=fs_value_big, va="center")

# Row 2: SEE
text_label_see = ax_text.text(x_label, y0 - dy, "", transform=ax_text.transAxes,
                              fontsize=fs_label, va="center")
text_value_see = ax_text.text(x_value, y0 - dy, "", transform=ax_text.transAxes,
                              fontsize=fs_value_big, va="center")

# Row 3: Degenerate form
text_label_deg = ax_text.text(x_label, y0 - 2*dy, "", transform=ax_text.transAxes,
                              fontsize=fs_label, va="center")
text_value_deg = ax_text.text(x_value, y0 - 2*dy, "", transform=ax_text.transAxes,
                              fontsize=fs_value_big, va="center")

# Row 4: Degenerate angle
text_label_theta = ax_text.text(x_label, y0 - 3*dy, "", transform=ax_text.transAxes,
                                fontsize=fs_label, va="center")
text_value_theta = ax_text.text(x_value, y0 - 3*dy, "", transform=ax_text.transAxes,
                                fontsize=fs_value, va="center")

# Row 5: Final form
text_label_final = ax_text.text(x_label, y0 - 4*dy, "", transform=ax_text.transAxes,
                                fontsize=fs_label, va="center")
text_value_final = ax_text.text(x_value, y0 - 4*dy, "", transform=ax_text.transAxes,
                                fontsize=fs_value_big, va="center")

# Kinematic state box (moved down so it never collides with the lines above)
kin_box = FancyBboxPatch(
    (0.033, 0.06),   # (x, y) in axes coordinates
    0.92,           # width
    0.26,           # height
    boxstyle="round,pad=0.03",
    linewidth=1,
    edgecolor="gray",
    facecolor="#f7f7f7",
    alpha=0.85,
    transform=ax_text.transAxes,
)
ax_text.add_patch(kin_box)

text_kin_title = ax_text.text(
    0.05, 0.26,
    "Kinematic state:",
    transform=ax_text.transAxes,
    fontsize=13,
    fontweight="bold",
    va="center",
)

text_kin_body = ax_text.text(
    0.05, 0.16,
    "",
    transform=ax_text.transAxes,
    fontsize=12,
    va="center",
)

# Slider for n (1 to 10)
s_n = Slider(ax_n, "n", 1, 10, valinit=n0, valstep=1)

# Connect slider
s_n.on_changed(update)

# Initial draw
update(None)

plt.show()
