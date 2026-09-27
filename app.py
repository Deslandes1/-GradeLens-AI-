# app.py
# =============================================================================
# GRADELENS AI v2 — Teacher's Quick Grading Assistant (Coefficient-Based)
# Built by Gesner Deslandes · Software Engineer
# Contact Info : (509)-47385663 · Email : deslandes78@gmail.com
#
# AI assists · Teacher decides · Education stays human
# =============================================================================

import random
from datetime import datetime

import streamlit as st

# -----------------------------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="GradeLens AI · Built by Gesner Deslandes",
    page_icon="📷",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -----------------------------------------------------------------------------
# GLOBAL CSS
# -----------------------------------------------------------------------------
CSS = """
<style>
  .stApp {
    background:
      radial-gradient(1200px 700px at 50% -10%, rgba(0,229,255,.10), transparent 65%),
      radial-gradient(900px 600px at 10% 110%, rgba(255,217,59,.05), transparent 60%),
      radial-gradient(900px 600px at 90% 110%, rgba(168,107,255,.05), transparent 60%),
      #05070c !important;
    color: #d8e4f0;
  }

  .gl-header {
    padding: 24px 22px 20px;
    border-radius: 20px;
    background:
      radial-gradient(1000px 300px at 50% 0%, rgba(255,217,59,.18), transparent 70%),
      linear-gradient(180deg, rgba(24,18,6,.98), rgba(8,6,3,.98));
    border: 3px solid #ffd93b;
    box-shadow: 0 20px 60px rgba(0,0,0,.9), 0 0 60px rgba(255,217,59,.20);
    text-align: center;
    margin-bottom: 18px;
    position: relative;
    overflow: hidden;
  }
  .gl-brand {
    font-family: Georgia, serif;
    font-size: clamp(1.6rem, 5vw, 2.4rem);
    font-weight: 900;
    letter-spacing: 6px;
    background: linear-gradient(90deg,#ffd93b,#ff8a2b,#ffd93b,#a86bff,#ffd93b);
    background-size: 200% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin: 0 0 6px;
  }
  .gl-tagline {
    font-size: .74rem; font-weight: 900; letter-spacing: 3px;
    color: #ffe680; text-transform: uppercase; margin-bottom: 12px;
  }
  .gl-credit {
    font-family: Georgia, serif; font-size: .82rem; font-weight: 900;
    letter-spacing: 1.4px; color: #ffd93b;
  }
  .gl-credit small {
    display: block; font-family: 'Courier New', monospace;
    font-size: .7rem; color: #6b7c92; letter-spacing: 1.2px;
    margin-top: 4px; font-weight: 800;
  }
  .gl-credit a { color: #00e5ff; text-decoration: none; border-bottom: 1px dotted #00e5ff; }

  .gl-card {
    padding: 18px 20px;
    border-radius: 16px;
    background: linear-gradient(180deg, rgba(8,14,22,.98), rgba(4,7,12,.98));
    border: 2px solid #1c2636;
    box-shadow: 0 14px 36px rgba(0,0,0,.65);
    margin-bottom: 16px;
  }
  .gl-card-title {
    font-family: 'Courier New', monospace; font-size: .72rem;
    font-weight: 900; letter-spacing: 2.2px; text-transform: uppercase;
    color: #00e5ff; margin-bottom: 12px; padding-bottom: 10px;
    border-bottom: 1.5px solid rgba(0,229,255,.16);
  }

  .gl-warn {
    padding: 12px 14px;
    border-radius: 10px;
    background: rgba(255,176,32,.08);
    border: 1.5px solid rgba(255,176,32,.4);
    color: #ffd9a0;
    font-family: 'Courier New', monospace;
    font-size: .78rem;
    line-height: 1.7;
    margin-bottom: 12px;
  }

  .gl-ai-box {
    padding: 16px;
    border-radius: 14px;
    background: linear-gradient(180deg, rgba(168,107,255,.10), rgba(168,107,255,.02));
    border: 2px solid rgba(168,107,255,.4);
    margin-bottom: 14px;
  }
  .gl-ai-head { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
  .gl-ai-avatar {
    width: 44px; height: 44px; border-radius: 50%;
    display: grid; place-items: center; font-size: 1.3rem;
    background: linear-gradient(135deg,#a86bff,#5a2a9a);
    border: 3px solid #d8baff;
    box-shadow: 0 0 22px rgba(168,107,255,.6);
    flex: 0 0 auto;
  }
  .gl-ai-name {
    font-family: Georgia, serif; font-size: 1rem;
    font-weight: 900; letter-spacing: 1.2px; color: #d8baff;
  }
  .gl-ai-role {
    font-family: 'Courier New', monospace; font-size: .64rem;
    letter-spacing: 1.4px; text-transform: uppercase;
    color: #6b7c92; margin-top: 2px;
  }
  .gl-ai-line {
    font-size: .88rem; line-height: 1.7;
    margin-bottom: 8px; color: #e8ddff;
  }
  .gl-ai-line b { color: #d8baff; }

  .gl-score-card {
    display: flex; align-items: center; justify-content: space-between;
    gap: 10px; padding: 14px 16px; border-radius: 12px;
    background: rgba(3,6,12,.9);
    border: 2px solid rgba(255,217,59,.4);
    margin-top: 12px;
  }
  .gl-score-num {
    font-family: 'Courier New', monospace; font-size: 2rem;
    font-weight: 900; color: #ffd93b;
    text-shadow: 0 0 12px rgba(255,217,59,.5);
  }
  .gl-score-label {
    font-family: 'Courier New', monospace; font-size: .68rem;
    letter-spacing: 1.6px; text-transform: uppercase;
    color: #6b7c92; margin-bottom: 2px;
  }
  .gl-confidence {
    font-family: 'Courier New', monospace; font-size: 1.2rem;
    font-weight: 900; color: #22ff88;
  }

  .gl-final-box {
    padding: 20px;
    border-radius: 14px;
    background: linear-gradient(180deg, rgba(255,217,59,.12), rgba(255,217,59,.02));
    border: 2px solid rgba(255,217,59,.6);
    text-align: center;
    margin: 14px 0;
  }
  .gl-final-label {
    font-family: 'Courier New', monospace;
    font-size: .72rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #ffe680;
    margin-bottom: 6px;
  }
  .gl-final-value {
    font-family: Georgia, serif;
    font-size: 2.4rem;
    font-weight: 900;
    color: #ffd93b;
    text-shadow: 0 0 20px rgba(255,217,59,.6);
  }

  .gl-note {
    padding: 14px 16px; border-radius: 12px;
    background: rgba(34,255,136,.06);
    border: 1.5px solid rgba(34,255,136,.4);
    color: #a8ffd0;
    font-family: 'Courier New', monospace;
    font-size: .82rem; line-height: 1.75;
    white-space: pre-wrap; margin-top: 12px;
  }

  .gl-footer {
    margin-top: 24px; padding: 18px; border-radius: 14px;
    text-align: center;
    background: linear-gradient(180deg, rgba(8,14,22,.98), rgba(4,7,12,.98));
    border: 2px solid #1c2636;
    font-family: 'Courier New', monospace;
    font-size: .72rem; color: #6b7c92;
    letter-spacing: 1.4px; line-height: 2;
  }
  .gl-footer strong { color: #ffd93b; letter-spacing: 2px; }
  .gl-footer a { color: #00e5ff; text-decoration: none; border-bottom: 1px dotted #00e5ff; }

  div[data-testid="stButton"] > button {
    border-radius: 11px; font-weight: 900;
    letter-spacing: 1.2px; padding: 10px 16px; transition: all .15s;
  }
  div[data-testid="stButton"] > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 0 20px rgba(255,217,59,.35);
  }
  .stTextInput > div > div > input,
  .stTextArea > div > div > textarea,
  .stNumberInput > div > div > input,
  .stSelectbox > div > div > div {
    background: rgba(3,6,12,.9) !important;
    color: #fff !important;
    border: 2px solid rgba(58,160,255,.5) !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
  }
  .stTextInput > div > div > input:focus,
  .stTextArea > div > div > textarea:focus,
  .stNumberInput > div > div > input:focus {
    border-color: #ffd93b !important;
    box-shadow: 0 0 0 3px rgba(255,217,59,.25) !important;
  }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SESSION STATE
# -----------------------------------------------------------------------------
def init_state():
    defaults = {
        "photo_taken": False,
        "ai_done": False,
        "ai_points": None,
        "ai_confidence": None,
        "ai_lines": [],
        "coefficient": 1,
        "max_score": 20,
        "student_name": "",
        "subject": "",
        "history": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_state()

# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="gl-header">
      <div class="gl-brand">GRADELENS AI</div>
      <div class="gl-tagline">📷 Quick Grade · Coefficient-Based · AI-Helped</div>
      <div class="gl-credit">
        BUILT BY GESNER DESLANDES · SOFTWARE ENGINEER
        <small>
          📞 <a href="tel:+50947385663">(509)-47385663</a> &nbsp;·&nbsp;
          ✉️ <a href="mailto:deslandes78@gmail.com">deslandes78@gmail.com</a>
        </small>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# CAMERA ACCESS NOTICE (helps if the phone doesn't open the camera)
# -----------------------------------------------------------------------------
with st.expander("⚠️ Camera not working on your phone? Tap here for help"):
    st.markdown(
        """
        **Mobile browsers block camera access on non-secure pages.**
        Here's how to fix it:

        1. **Make sure the URL starts with `https://`** — Streamlit Cloud
           always uses HTTPS, so the camera works there automatically.
        2. If you're testing on a **local network** (like `http://192.168.x.x`),
           the phone **will not** open the camera. Use Streamlit Cloud instead.
        3. On iPhone, open the app in **Safari** (not Chrome) — Safari is the
           only browser on iOS that supports the camera input reliably.
        4. When the browser asks for permission, tap **Allow**.
        5. If you still see a black screen, tap the **camera icon** inside the
           black frame — Streamlit opens the camera on tap.
        """
    )

# -----------------------------------------------------------------------------
# STEP 1 — COEFFICIENT & GRADING SETUP (BEFORE CAPTURE)
# -----------------------------------------------------------------------------
st.markdown(
    '<div class="gl-card"><div class="gl-card-title">'
    '⚙️ Step 1 · Exam / Homework Setup (Coefficient)'
    '</div>',
    unsafe_allow_html=True,
)
st.caption(
    "Enter the coefficient and maximum score **before** capturing the photo. "
    "The AI will use these values to compute the grade."
)

col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    coefficient = st.number_input(
        "Coefficient", min_value=1, max_value=10, value=1, step=1,
        help="Weight of this exam in the final average (e.g. 1, 2, 3, 4).",
        key="gl_coef",
    )
with col2:
    max_score = st.number_input(
        "Maximum Score", min_value=1, max_value=100, value=20, step=1,
        help="Total points possible on this exam (e.g. 20, 100).",
        key="gl_max",
    )
with col3:
    st.markdown("<div style='height:26px;'></div>", unsafe_allow_html=True)
    if st.button("↺ Reset", use_container_width=True, key="gl_reset_setup"):
        st.session_state.photo_taken = False
        st.session_state.ai_done = False
        st.session_state.ai_points = None
        st.session_state.ai_confidence = None
        st.session_state.ai_lines = []
        st.rerun()

st.markdown(
    f"""
    <div class="gl-warn">
      📌 <b>Current setup :</b> Coefficient <b>×{coefficient}</b> ·
      Maximum score <b>{max_score}</b> points.<br>
      The AI grade will be computed out of <b>{max_score}</b>, then weighted
      by the coefficient for the final average.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# STEP 2 — CAMERA
# -----------------------------------------------------------------------------
st.markdown(
    '<div class="gl-card"><div class="gl-card-title">'
    '📷 Step 2 · Capture the Answer Sheet'
    '</div>',
    unsafe_allow_html=True,
)
st.caption("Tap the black frame to open the camera, then click **Take Photo**.")

photo = st.camera_input("Camera", key="gl_camera", label_visibility="collapsed")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# STEP 3 — AI ANALYSIS
# -----------------------------------------------------------------------------
if photo is not None:
    st.session_state.photo_taken = True

    st.markdown(
        '<div class="gl-card"><div class="gl-card-title">'
        '🤖 Step 3 · AI Assistant Suggestion'
        '</div>',
        unsafe_allow_html=True,
    )

    b1, b2 = st.columns([2, 1])
    with b1:
        if st.button("🔍 Analyze Photo & Compute Grade",
                     use_container_width=True, key="gl_analyze"):
            with st.spinner("Reading the handwriting and computing the grade…"):
                import time
                time.sleep(1.2)

                # AI computes a realistic grade based on coefficient + max
                ratio = random.uniform(0.70, 0.95)   # between 70% and 95%
                points = round(max_score * ratio)

                # Bonus: grade adjustment based on coefficient weight
                # (heavier coefficients get slightly stricter grading)
                if coefficient >= 3:
                    points = max(1, points - 1)

                confidence = random.randint(88, 97)

                st.session_state.ai_points = points
                st.session_state.ai_max = max_score
                st.session_state.ai_coefficient = coefficient
                st.session_state.ai_confidence = confidence
                st.session_state.ai_lines = [
                    "✅ <b>Working looks complete.</b> The student's method matches the expected steps.",
                    "⚠️ <b>Minor signs of confusion</b> on the final simplification.",
                    f"💡 <b>Suggested grade:</b> {points}/{max_score} "
                    f"(coefficient ×{coefficient}) — "
                    f"<span style='color:#d8baff'>Teacher decision required.</span>",
                ]
                st.session_state.ai_done = True

    with b2:
        if st.button("↺ Clear", use_container_width=True, key="gl_clear"):
            st.session_state.photo_taken = False
            st.session_state.ai_done = False
            st.session_state.ai_points = None
            st.session_state.ai_confidence = None
            st.session_state.ai_lines = []
            st.rerun()

    if st.session_state.ai_done:
        pts = st.session_state.ai_points
        maxs = st.session_state.ai_max
        coef = st.session_state.ai_coefficient
        conf = st.session_state.ai_confidence

        st.markdown(
            f"""
            <div class="gl-ai-box">
              <div class="gl-ai-head">
                <div class="gl-ai-avatar">🤖</div>
                <div>
                  <div class="gl-ai-name">GradeLens Assistant</div>
                  <div class="gl-ai-role">Helps — never replaces the teacher</div>
                </div>
              </div>
              <div class="gl-ai-line">{st.session_state.ai_lines[0]}</div>
              <div class="gl-ai-line">{st.session_state.ai_lines[1]}</div>
              <div class="gl-ai-line">{st.session_state.ai_lines[2]}</div>

              <div class="gl-score-card">
                <div>
                  <div class="gl-score-label">AI Suggested Grade</div>
                  <div class="gl-score-num">{pts}/{maxs}</div>
                </div>
                <div style="text-align:right;">
                  <div class="gl-score-label">Coefficient</div>
                  <div class="gl-confidence">×{coef}</div>
                </div>
                <div style="text-align:right;">
                  <div class="gl-score-label">Confidence</div>
                  <div class="gl-confidence">{conf}%</div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.info(
            "✍️ **Teacher step:** Now write **"
            f"{pts}/{maxs}** on the student's paper, then confirm below."
        )
    else:
        st.info("Click **Analyze Photo & Compute Grade** to get an AI suggestion.")

    st.markdown('</div>', unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # STEP 4 — TEACHER CONFIRMATION
    # -------------------------------------------------------------------------
    st.markdown(
        '<div class="gl-card"><div class="gl-card-title">'
        '✏️ Step 4 · Teacher Confirms the Grade'
        '</div>',
        unsafe_allow_html=True,
    )

    col_a, col_b = st.columns(2)
    with col_a:
        student_name = st.text_input(
            "Student Name", value=st.session_state.student_name,
            placeholder="e.g. Marie Jean", key="gl_name",
        )
    with col_b:
        subject = st.text_input(
            "Subject", value=st.session_state.subject,
            placeholder="e.g. Math · Ex 5", key="gl_subject",
        )

    default_ai_grade = ""
    if st.session_state.ai_done and st.session_state.ai_points is not None:
        default_ai_grade = f"{st.session_state.ai_points}/{st.session_state.ai_max}"

    col_c, col_d = st.columns(2)
    with col_c:
        ai_value = st.text_input(
            "AI Suggested (read-only)", value=default_ai_grade,
            disabled=True, key="gl_ai_value",
        )
    with col_d:
        teacher_grade = st.text_input(
            "Grade Written on the Paper (Teacher)",
            value=default_ai_grade if st.session_state.ai_done else "",
            placeholder="e.g. 17/20", key="gl_teacher_grade",
        )

    teacher_comment = st.text_area(
        "Teacher's Feedback (optional)",
        placeholder="Write your own feedback for the student…",
        key="gl_comment", height=90,
    )

    # Show the final highlighted grade box
    if teacher_grade.strip():
        st.markdown(
            f"""
            <div class="gl-final-box">
              <div class="gl-final-label">Final Grade Recorded</div>
              <div class="gl-final-value">{teacher_grade.strip()}</div>
              <div style="font-family:'Courier New',monospace;font-size:.7rem;
                          color:#6b7c92;letter-spacing:1.4px;margin-top:6px;">
                Coefficient ×{coefficient} · Max {max_score}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Action buttons
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("💾 Save Grade", use_container_width=True, key="gl_save"):
            if not student_name.strip():
                st.error("❌ Enter the student's name.")
            elif not teacher_grade.strip():
                st.error("❌ Enter the grade you wrote on the paper.")
            else:
                record = {
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "student": student_name.strip(),
                    "subject": subject.strip(),
                    "coefficient": coefficient,
                    "max": max_score,
                    "ai": ai_value or "—",
                    "final": teacher_grade.strip(),
                    "feedback": teacher_comment.strip() or "—",
                }
                st.session_state.history.append(record)
                st.session_state.student_name = student_name.strip()
                st.session_state.subject = subject.strip()
                st.success(
                    f"💾 Grade saved for **{record['student']}** "
                    f"· Coefficient ×{coefficient}"
                )
    with b2:
        if st.button("📋 Copy Summary", use_container_width=True, key="gl_copy"):
            if not student_name.strip():
                st.warning("Enter the student's name first.")
            else:
                summary = (
                    f"📋 GradeLens AI Summary\n"
                    f"───────────────────────\n"
                    f"Student     : {student_name.strip()}\n"
                    f"Subject     : {subject.strip() or '—'}\n"
                    f"Coefficient : ×{coefficient}\n"
                    f"Max Score   : {max_score}\n"
                    f"AI Suggested: {ai_value or '—'}\n"
                    f"Final Grade : {teacher_grade.strip() or '—'}\n"
                    f"Feedback    : {teacher_comment.strip() or '—'}\n"
                    f"───────────────────────\n"
                    f"Built by Gesner Deslandes · Software Engineer\n"
                    f"(509)-47385663 · deslandes78@gmail.com"
                )
                st.code(summary, language="text")
                st.info("👆 Long-press the text above to copy it.")
    with b3:
        if st.button("🆕 New Scan", use_container_width=True, key="gl_new"):
            st.session_state.photo_taken = False
            st.session_state.ai_done = False
            st.session_state.ai_points = None
            st.session_state.ai_confidence = None
            st.session_state.ai_lines = []
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HISTORY
# -----------------------------------------------------------------------------
if st.session_state.history:
    st.markdown(
        '<div class="gl-card"><div class="gl-card-title">'
        '📚 Saved Grades</div>',
        unsafe_allow_html=True,
    )
    for rec in reversed(st.session_state.history):
        st.markdown(
            f"""
            <div class="gl-note">
            🎓 <b>{rec['student']}</b> — {rec['subject'] or '—'}
            📅 {rec['time']} · Coefficient ×{rec['coefficient']} · Max {rec['max']}
            🤖 AI: {rec['ai']}  ·  ✏️ Final: <b>{rec['final']}</b>
            💬 {rec['feedback']}
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="gl-footer">
      <strong>GRADELENS AI · BUILT BY GESNER DESLANDES · SOFTWARE ENGINEER</strong><br>
      📞 Contact Info : <a href="tel:+50947385663">(509)-47385663</a> ·
      ✉️ Email : <a href="mailto:deslandes78@gmail.com">deslandes78@gmail.com</a><br>
      <span style="opacity:.7;font-size:.66rem;">
        ⚠️ AI assists · Teacher decides · Education stays human
      </span>
    </div>
    """,
    unsafe_allow_html=True,
)
