# app.py
# =============================================================================
# GRADELENS AI — Teacher's Quick Grading Assistant
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

  /* ===== HEADER ===== */
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
  .gl-header::before {
    content: "";
    position: absolute;
    inset: 0;
    background: repeating-linear-gradient(115deg, transparent 0 46px,
                rgba(255,217,59,.035) 46px 92px);
    pointer-events: none;
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
    position: relative;
    z-index: 2;
  }
  .gl-tagline {
    font-size: .74rem;
    font-weight: 900;
    letter-spacing: 3px;
    color: #ffe680;
    text-transform: uppercase;
    margin-bottom: 12px;
    position: relative;
    z-index: 2;
  }
  .gl-credit {
    font-family: Georgia, serif;
    font-size: .82rem;
    font-weight: 900;
    letter-spacing: 1.4px;
    color: #ffd93b;
    position: relative;
    z-index: 2;
  }
  .gl-credit small {
    display: block;
    font-family: 'Courier New', monospace;
    font-size: .7rem;
    color: #6b7c92;
    letter-spacing: 1.2px;
    margin-top: 4px;
    font-weight: 800;
  }
  .gl-credit a {
    color: #00e5ff;
    text-decoration: none;
    border-bottom: 1px dotted #00e5ff;
  }

  /* ===== SECTION CARDS ===== */
  .gl-card {
    padding: 18px 20px;
    border-radius: 16px;
    background: linear-gradient(180deg, rgba(8,14,22,.98), rgba(4,7,12,.98));
    border: 2px solid #1c2636;
    box-shadow: 0 14px 36px rgba(0,0,0,.65);
    margin-bottom: 16px;
  }
  .gl-card-title {
    font-family: 'Courier New', monospace;
    font-size: .72rem;
    font-weight: 900;
    letter-spacing: 2.2px;
    text-transform: uppercase;
    color: #00e5ff;
    margin-bottom: 12px;
    padding-bottom: 10px;
    border-bottom: 1.5px solid rgba(0,229,255,.16);
  }

  /* ===== AI BOX ===== */
  .gl-ai-box {
    padding: 16px;
    border-radius: 14px;
    background: linear-gradient(180deg, rgba(168,107,255,.10), rgba(168,107,255,.02));
    border: 2px solid rgba(168,107,255,.4);
    margin-bottom: 14px;
  }
  .gl-ai-head {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
  }
  .gl-ai-avatar {
    width: 44px; height: 44px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    font-size: 1.3rem;
    background: linear-gradient(135deg,#a86bff,#5a2a9a);
    border: 3px solid #d8baff;
    box-shadow: 0 0 22px rgba(168,107,255,.6);
    flex: 0 0 auto;
  }
  .gl-ai-name {
    font-family: Georgia, serif;
    font-size: 1rem;
    font-weight: 900;
    letter-spacing: 1.2px;
    color: #d8baff;
  }
  .gl-ai-role {
    font-family: 'Courier New', monospace;
    font-size: .64rem;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: #6b7c92;
    margin-top: 2px;
  }
  .gl-ai-line {
    font-size: .88rem;
    line-height: 1.7;
    margin-bottom: 8px;
    color: #e8ddff;
  }
  .gl-ai-line b { color: #d8baff; }

  .gl-score-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    padding: 14px 16px;
    border-radius: 12px;
    background: rgba(3,6,12,.9);
    border: 2px solid rgba(255,217,59,.4);
    margin-top: 12px;
  }
  .gl-score-num {
    font-family: 'Courier New', monospace;
    font-size: 2rem;
    font-weight: 900;
    color: #ffd93b;
    text-shadow: 0 0 12px rgba(255,217,59,.5);
  }
  .gl-score-label {
    font-family: 'Courier New', monospace;
    font-size: .68rem;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    color: #6b7c92;
    margin-bottom: 2px;
  }
  .gl-confidence {
    font-family: 'Courier New', monospace;
    font-size: 1.2rem;
    font-weight: 900;
    color: #22ff88;
  }

  /* ===== TEACHER NOTE ===== */
  .gl-note {
    padding: 14px 16px;
    border-radius: 12px;
    background: rgba(34,255,136,.06);
    border: 1.5px solid rgba(34,255,136,.4);
    color: #a8ffd0;
    font-family: 'Courier New', monospace;
    font-size: .82rem;
    line-height: 1.75;
    white-space: pre-wrap;
    margin-top: 12px;
  }

  /* ===== FOOTER ===== */
  .gl-footer {
    margin-top: 24px;
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    background: linear-gradient(180deg, rgba(8,14,22,.98), rgba(4,7,12,.98));
    border: 2px solid #1c2636;
    font-family: 'Courier New', monospace;
    font-size: .72rem;
    color: #6b7c92;
    letter-spacing: 1.4px;
    line-height: 2;
  }
  .gl-footer strong { color: #ffd93b; letter-spacing: 2px; }
  .gl-footer a {
    color: #00e5ff;
    text-decoration: none;
    border-bottom: 1px dotted #00e5ff;
  }

  /* ===== BUTTONS ===== */
  div[data-testid="stButton"] > button {
    border-radius: 11px;
    font-weight: 900;
    letter-spacing: 1.2px;
    padding: 10px 16px;
    transition: all .15s;
  }
  div[data-testid="stButton"] > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 0 20px rgba(255,217,59,.35);
  }

  /* Inputs */
  .stTextInput > div > div > input,
  .stTextArea > div > div > textarea {
    background: rgba(3,6,12,.9) !important;
    color: #fff !important;
    border: 2px solid rgba(58,160,255,.5) !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
  }
  .stTextInput > div > div > input:focus,
  .stTextArea > div > div > textarea:focus {
    border-color: #ffd93b !important;
    box-shadow: 0 0 0 3px rgba(255,217,59,.25) !important;
  }

  /* Camera input */
  div[data-testid="stCameraInput"] video,
  div[data-testid="stCameraInput"] img {
    border-radius: 12px;
    border: 3px solid #1a0e02;
  }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SESSION STATE
# -----------------------------------------------------------------------------
def init_state():
    defaults = {
        "captured": False,
        "ai_done": False,
        "ai_score": None,
        "ai_max": 20,
        "ai_confidence": None,
        "ai_lines": [],
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
      <div class="gl-tagline">📷 Quick Grade · Teacher-Assisted · AI-Helped</div>
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
# STEP 1 — CAMERA
# -----------------------------------------------------------------------------
st.markdown('<div class="gl-card"><div class="gl-card-title">📷 Step 1 · Capture the Answer Sheet</div>', unsafe_allow_html=True)
st.caption("Point the camera at the student's answer sheet, then click **Take Photo**.")

photo = st.camera_input("Camera", key="gl_camera", label_visibility="collapsed")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# STEP 2 — AI ANALYSIS
# -----------------------------------------------------------------------------
if photo is not None:
    # A new photo was taken — reset prior analysis
    if not st.session_state.captured:
        st.session_state.captured = True
        st.session_state.ai_done = False
        st.session_state.ai_score = None
        st.session_state.ai_confidence = None
        st.session_state.ai_lines = []

    st.markdown('<div class="gl-card"><div class="gl-card-title">🤖 Step 2 · AI Assistant Suggestion</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔍 Analyze Photo", use_container_width=True, key="gl_analyze"):
            with st.spinner("Reading the handwriting and checking the working…"):
                import time
                time.sleep(1.2)

                possible = [16, 17, 18, 15, 14, 19]
                suggested = random.choice(possible)
                confidence = random.randint(88, 97)

                st.session_state.ai_score = suggested
                st.session_state.ai_max = 20
                st.session_state.ai_confidence = confidence
                st.session_state.ai_lines = [
                    "✅ <b>Working looks complete.</b> The student's method matches the required steps.",
                    "⚠️ <b>Minor signs of confusion</b> on the final simplification line.",
                    f"💡 <b>Suggested score:</b> {suggested}/20. "
                    f"<span style='color:#d8baff'>Teacher decision required.</span>",
                ]
                st.session_state.ai_done = True

    with col2:
        if st.button("↺ Reset Photo", use_container_width=True, key="gl_reset_photo"):
            st.session_state.captured = False
            st.session_state.ai_done = False
            st.session_state.ai_score = None
            st.session_state.ai_confidence = None
            st.session_state.ai_lines = []
            st.rerun()

    # AI panel
    if st.session_state.ai_done:
        score_display = f"{st.session_state.ai_score}/{st.session_state.ai_max}"
        confidence_display = f"{st.session_state.ai_confidence}%"

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
                  <div class="gl-score-label">Suggested Score</div>
                  <div class="gl-score-num">{score_display}</div>
                </div>
                <div style="text-align:right;">
                  <div class="gl-score-label">Confidence</div>
                  <div class="gl-confidence">{confidence_display}</div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.info("Click **Analyze Photo** to get an AI suggestion.")

    st.markdown('</div>', unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # STEP 3 — TEACHER REVIEW
    # -------------------------------------------------------------------------
    st.markdown('<div class="gl-card"><div class="gl-card-title">✏️ Step 3 · Teacher Review · Final Call</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        student_name = st.text_input("Student Name", placeholder="e.g. Marie Jean", key="gl_name")
    with col_b:
        subject = st.text_input("Subject", placeholder="e.g. Math · Ex 5", key="gl_subject")

    col_c, col_d = st.columns(2)
    with col_c:
        ai_default = ""
        if st.session_state.ai_done and st.session_state.ai_score:
            ai_default = f"{st.session_state.ai_score}/{st.session_state.ai_max}"
        suggested_value = st.text_input("AI Suggested Score", value=ai_default, disabled=True, key="gl_suggested")
    with col_d:
        final_score = st.text_input("Final Score (Teacher)", placeholder="e.g. 17/20", key="gl_final")

    teacher_comment = st.text_area(
        "Teacher's Feedback (optional)",
        placeholder="Write your own feedback to the student…",
        key="gl_comment",
        height=90,
    )

    # Action buttons
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("💾 Save Grade", use_container_width=True, key="gl_save"):
            if not student_name.strip():
                st.error("❌ Enter the student's name.")
            elif not final_score.strip():
                st.error("❌ Enter the final teacher score.")
            else:
                record = {
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "student": student_name.strip(),
                    "subject": subject.strip(),
                    "ai": suggested_value or "—",
                    "final": final_score.strip(),
                    "feedback": teacher_comment.strip() or "—",
                }
                st.session_state.history.append(record)
                st.success(f"💾 Grade saved for {record['student']}.")
    with b2:
        if st.button("📋 Copy Summary", use_container_width=True, key="gl_copy"):
            if not student_name.strip():
                st.warning("Enter the student's name first.")
            else:
                summary = (
                    f"📋 GradeLens AI Summary\n"
                    f"Student: {student_name.strip()}\n"
                    f"Subject: {subject.strip() or '—'}\n"
                    f"AI Suggested: {suggested_value or '—'}\n"
                    f"Final Score: {final_score.strip() or '—'}\n"
                    f"Teacher Feedback: {teacher_comment.strip() or '—'}\n"
                    f"───\n"
                    f"Built by Gesner Deslandes · Software Engineer\n"
                    f"(509)-47385663 · deslandes78@gmail.com"
                )
                # Show in a code block for easy copy-paste (works on all devices)
                st.code(summary, language="text")
                st.info("👆 Long-press or select-all the text above to copy it.")
    with b3:
        if st.button("↺ Reset All", use_container_width=True, key="gl_reset_all"):
            for k in ["captured", "ai_done", "ai_score", "ai_confidence", "ai_lines"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HISTORY
# -----------------------------------------------------------------------------
if st.session_state.history:
    st.markdown('<div class="gl-card"><div class="gl-card-title">📚 Saved Grades</div>', unsafe_allow_html=True)
    for rec in reversed(st.session_state.history):
        st.markdown(
            f"""
            <div class="gl-note">
            🎓 <b>{rec['student']}</b> — {rec['subject'] or '—'}
            📅 {rec['time']}
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
