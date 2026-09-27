# app.py
# =============================================================================
# GRADELENS AI v4 — Real AI Vision Grading · Light Blue Theme
# Built by Gesner Deslandes · Software Engineer
# Contact Info : (509)-47385663 · Email : deslandes78@gmail.com
#
# AI assists · Teacher decides · Education stays human
# =============================================================================

import base64
import json
import re
import random
from datetime import datetime
from io import BytesIO

import streamlit as st
from PIL import Image

# -----------------------------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="GradeLens AI · Built by Gesner Deslandes",
    page_icon="📷",
    layout="centered",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# GLOBAL CSS — LIGHT BLUE THEME
# -----------------------------------------------------------------------------
CSS = """
<style>
  /* ===== PAGE BACKGROUND ===== */
  .stApp {
    background:
      radial-gradient(1200px 700px at 50% -10%, rgba(255,255,255,.85), transparent 65%),
      radial-gradient(900px 600px at 10% 110%, rgba(180,220,255,.55), transparent 60%),
      radial-gradient(900px 600px at 90% 110%, rgba(200,230,255,.50), transparent 60%),
      #d4eaff !important;
    color: #0a2540;
  }
  .stApp, .stApp p, .stApp span, .stApp label, .stApp div,
  .stMarkdown, .stText, .stCaption, .stAlert {
    color: #0a2540 !important;
  }
  .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
    color: #06357a !important;
  }
  .stApp .stCaption, .stApp small {
    color: #35608f !important;
  }
  section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #eaf4ff, #cfe6ff) !important;
    border-right: 2px solid #9cc8ff !important;
  }
  section[data-testid="stSidebar"] * {
    color: #0a2540 !important;
  }
  details summary {
    color: #06357a !important;
    font-weight: 800 !important;
  }

  /* ===== HEADER ===== */
  .gl-header {
    padding: 22px 20px 18px;
    border-radius: 20px;
    background:
      radial-gradient(1000px 300px at 50% 0%, rgba(255,255,255,.9), transparent 70%),
      linear-gradient(180deg, #eaf4ff, #cfe6ff);
    border: 3px solid #3aa0ff;
    box-shadow: 0 20px 60px rgba(58,160,255,.25), 0 0 40px rgba(58,160,255,.15);
    text-align: center; margin-bottom: 18px;
    position: relative; overflow: hidden;
  }
  .gl-brand {
    font-family: Georgia, serif;
    font-size: clamp(1.5rem, 5vw, 2.3rem);
    font-weight: 900; letter-spacing: 6px;
    background: linear-gradient(90deg,#06357a,#1060a0,#06357a,#3a6bd0,#06357a);
    background-size: 200% 100%;
    -webkit-background-clip: text; background-clip: text; color: transparent;
    margin: 0 0 6px;
  }
  .gl-tagline {
    font-size: .72rem; font-weight: 900; letter-spacing: 3px;
    color: #1060a0; text-transform: uppercase; margin-bottom: 12px;
  }
  .gl-credit {
    font-family: Georgia, serif; font-size: .82rem; font-weight: 900;
    letter-spacing: 1.4px; color: #06357a;
  }
  .gl-credit small {
    display: block; font-family: 'Courier New', monospace;
    font-size: .7rem; color: #35608f; letter-spacing: 1.2px;
    margin-top: 4px; font-weight: 800;
  }
  .gl-credit a {
    color: #1060a0; text-decoration: none;
    border-bottom: 1px dotted #1060a0;
  }
  .gl-credit a:hover { color: #06357a; }

  /* ===== CARDS ===== */
  .gl-card {
    padding: 18px 20px; border-radius: 16px;
    background: linear-gradient(180deg, #ffffff, #eef6ff);
    border: 2px solid #9cc8ff;
    box-shadow: 0 14px 36px rgba(58,160,255,.18);
    margin-bottom: 16px;
  }
  .gl-card-title {
    font-family: 'Courier New', monospace; font-size: .72rem;
    font-weight: 900; letter-spacing: 2.2px; text-transform: uppercase;
    color: #1060a0; margin-bottom: 12px; padding-bottom: 10px;
    border-bottom: 1.5px solid rgba(16,96,160,.25);
  }

  /* ===== MESSAGE BOXES ===== */
  .gl-warn {
    padding: 12px 14px; border-radius: 10px;
    background: rgba(255,176,32,.14);
    border: 1.5px solid rgba(214,136,0,.55);
    color: #6b4400;
    font-family: 'Courier New', monospace;
    font-size: .78rem; line-height: 1.7; margin-bottom: 12px;
  }
  .gl-tip {
    padding: 12px 14px; border-radius: 10px;
    background: rgba(58,160,255,.10);
    border: 1.5px solid rgba(58,160,255,.5);
    color: #06357a;
    font-family: 'Courier New', monospace;
    font-size: .78rem; line-height: 1.7; margin-bottom: 12px;
  }
  .gl-ok {
    padding: 12px 14px; border-radius: 10px;
    background: rgba(34,180,100,.14);
    border: 1.5px solid rgba(20,150,80,.55);
    color: #0a4b26;
    font-family: 'Courier New', monospace;
    font-size: .78rem; line-height: 1.7; margin-bottom: 12px;
  }

  /* ===== AI PANEL ===== */
  .gl-ai-box {
    padding: 16px; border-radius: 14px;
    background: linear-gradient(180deg, #ede5ff, #ddd0f7);
    border: 2px solid #9a72d9;
    margin-bottom: 14px;
  }
  .gl-ai-head { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
  .gl-ai-avatar {
    width: 44px; height: 44px; border-radius: 50%;
    display: grid; place-items: center; font-size: 1.3rem;
    background: linear-gradient(135deg,#a86bff,#5a2a9a);
    border: 3px solid #d8baff;
    box-shadow: 0 0 22px rgba(168,107,255,.5);
    flex: 0 0 auto;
  }
  .gl-ai-name {
    font-family: Georgia, serif; font-size: 1rem;
    font-weight: 900; letter-spacing: 1.2px; color: #4a1d8a;
  }
  .gl-ai-role {
    font-family: 'Courier New', monospace; font-size: .64rem;
    letter-spacing: 1.4px; text-transform: uppercase;
    color: #6a5a8a; margin-top: 2px;
  }
  .gl-ai-line {
    font-size: .88rem; line-height: 1.7;
    margin-bottom: 8px; color: #2a1a50;
  }
  .gl-ai-line b { color: #4a1d8a; }

  .gl-score-card {
    display: flex; align-items: center; justify-content: space-between;
    gap: 10px; padding: 14px 16px; border-radius: 12px;
    background: #ffffff;
    border: 2px solid #ffb020;
    margin-top: 12px;
  }
  .gl-score-num {
    font-family: 'Courier New', monospace; font-size: 2rem;
    font-weight: 900; color: #b06f00;
    text-shadow: 0 0 12px rgba(255,176,32,.4);
  }
  .gl-score-label {
    font-family: 'Courier New', monospace; font-size: .68rem;
    letter-spacing: 1.6px; text-transform: uppercase;
    color: #6b7c92; margin-bottom: 2px;
  }
  .gl-confidence {
    font-family: 'Courier New', monospace; font-size: 1.2rem;
    font-weight: 900; color: #0a8f4a;
  }

  /* ===== FINAL GRADE BOX ===== */
  .gl-final-box {
    padding: 20px; border-radius: 14px;
    background: linear-gradient(180deg, #fff5c4, #ffe89a);
    border: 2px solid #d6a300;
    text-align: center; margin: 14px 0;
  }
  .gl-final-label {
    font-family: 'Courier New', monospace; font-size: .72rem;
    letter-spacing: 2px; text-transform: uppercase;
    color: #6b4400; margin-bottom: 6px;
  }
  .gl-final-value {
    font-family: Georgia, serif; font-size: 2.4rem;
    font-weight: 900; color: #b06f00;
    text-shadow: 0 0 20px rgba(255,176,32,.5);
  }

  /* ===== SAVED GRADE NOTE ===== */
  .gl-note {
    padding: 14px 16px; border-radius: 12px;
    background: rgba(34,180,100,.10);
    border: 1.5px solid rgba(20,150,80,.45);
    color: #0a4b26;
    font-family: 'Courier New', monospace;
    font-size: .82rem; line-height: 1.75;
    white-space: pre-wrap; margin-top: 12px;
  }

  /* ===== PER-QUESTION BREAKDOWN ===== */
  .gl-q-row {
    padding: 10px 12px; border-radius: 10px;
    background: #ffffff;
    border-left: 4px solid #3aa0ff;
    margin-bottom: 8px;
    font-size: .84rem;
    line-height: 1.6;
    color: #0a2540;
  }
  .gl-q-row.ok  { border-left-color: #14a860; }
  .gl-q-row.bad { border-left-color: #e03a30; }

  /* ===== FOOTER ===== */
  .gl-footer {
    margin-top: 24px; padding: 18px; border-radius: 14px;
    text-align: center;
    background: linear-gradient(180deg, #ffffff, #e6f1ff);
    border: 2px solid #9cc8ff;
    font-family: 'Courier New', monospace;
    font-size: .72rem; color: #35608f;
    letter-spacing: 1.4px; line-height: 2;
  }
  .gl-footer strong { color: #06357a; letter-spacing: 2px; }
  .gl-footer a {
    color: #1060a0; text-decoration: none;
    border-bottom: 1px dotted #1060a0;
  }

  /* ===== BUTTONS ===== */
  div[data-testid="stButton"] > button {
    border-radius: 11px; font-weight: 900;
    letter-spacing: 1.2px; padding: 10px 16px;
    background: linear-gradient(180deg, #eaf4ff, #cfe6ff) !important;
    color: #06357a !important;
    border: 2px solid #3aa0ff !important;
    transition: all .15s;
  }
  div[data-testid="stButton"] > button:hover {
    transform: translateY(-1px);
    background: linear-gradient(180deg, #d3e9ff, #b3d8ff) !important;
    box-shadow: 0 6px 18px rgba(58,160,255,.35);
  }

  /* ===== INPUTS ===== */
  .stTextInput > div > div > input,
  .stTextArea > div > div > textarea,
  .stNumberInput > div > div > input,
  .stSelectbox > div > div > div,
  div[data-baseweb="select"] > div {
    background: #ffffff !important;
    color: #0a2540 !important;
    border: 2px solid #9cc8ff !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
  }
  .stTextInput > div > div > input:focus,
  .stTextArea > div > div > textarea:focus,
  .stNumberInput > div > div > input:focus {
    border-color: #3aa0ff !important;
    box-shadow: 0 0 0 3px rgba(58,160,255,.25) !important;
  }
  .stTextInput input::placeholder,
  .stTextArea textarea::placeholder {
    color: #7a9cbf !important;
    opacity: 1 !important;
  }

  /* ===== FILE UPLOADER / CAMERA ===== */
  div[data-testid="stFileUploader"] {
    background: #ffffff !important;
    border: 2px dashed #3aa0ff !important;
    border-radius: 12px !important;
    padding: 12px !important;
  }
  div[data-testid="stFileUploader"] * {
    color: #06357a !important;
  }

  /* ===== ALERTS ===== */
  .stAlert {
    border-radius: 12px !important;
    border-width: 2px !important;
  }
  div[data-testid="stAlert"] {
    background: #ffffff !important;
    color: #0a2540 !important;
  }

  /* ===== TABS ===== */
  button[data-baseweb="tab"] {
    background: #eaf4ff !important;
    color: #06357a !important;
    border: 1.5px solid #9cc8ff !important;
    border-radius: 10px 10px 0 0 !important;
    font-weight: 800 !important;
  }
  button[data-baseweb="tab"][aria-selected="true"] {
    background: #ffffff !important;
    color: #1060a0 !important;
    border-bottom-color: #3aa0ff !important;
  }

  /* ===== SPINNER / CAPTION ===== */
  .stSpinner > div { border-top-color: #3aa0ff !important; }
  .stCaption, div[data-testid="stCaptionContainer"] {
    color: #35608f !important;
  }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SESSION STATE
# -----------------------------------------------------------------------------
def init_state():
    defaults = {
        "api_provider": "google",
        "api_key": "",
        "api_model": "",
        "api_verified": False,
        "answer_key": "",
        "coefficient": 1,
        "max_score": 20,
        "ai_done": False,
        "ai_points": None,
        "ai_max": 20,
        "ai_coefficient": 1,
        "ai_confidence": None,
        "ai_overall_feedback": "",
        "ai_per_question": [],
        "ai_raw": "",
        "student_name": "",
        "subject": "",
        "history": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_state()

# -----------------------------------------------------------------------------
# MODEL OPTIONS
# -----------------------------------------------------------------------------
PROVIDER_MODELS = {
    "google": [
        "gemini-1.5-flash",
        "gemini-1.5-pro",
        "gemini-2.0-flash-exp",
    ],
    "openai": [
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4-turbo",
    ],
    "anthropic": [
        "claude-3-5-sonnet-20241022",
        "claude-3-5-haiku-20241022",
        "claude-3-opus-20240229",
    ],
}

PROVIDER_LABELS = {
    "google": "🟢 Google Gemini (free tier available)",
    "openai": "🔵 OpenAI GPT-4 Vision",
    "anthropic": "🟣 Anthropic Claude Vision",
}

# -----------------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------------
def _verify_api_key(provider: str, key: str, model: str):
    try:
        if provider == "openai":
            from openai import OpenAI
            client = OpenAI(api_key=key)
            client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "ping"}],
                max_tokens=2,
            )
            return True, "OK"
        if provider == "anthropic":
            from anthropic import Anthropic
            client = Anthropic(api_key=key)
            client.messages.create(
                model=model, max_tokens=2,
                messages=[{"role": "user", "content": "ping"}],
            )
            return True, "OK"
        if provider == "google":
            import google.generativeai as genai
            genai.configure(api_key=key)
            m = genai.GenerativeModel(model)
            m.generate_content("ping")
            return True, "OK"
        return False, "Unknown provider"
    except Exception as e:
        return False, str(e)[:200]


def _image_to_base64(image_file) -> tuple[str, str]:
    img = Image.open(image_file)
    if img.mode != "RGB":
        img = img.convert("RGB")
    max_dim = 1600
    if max(img.size) > max_dim:
        ratio = max_dim / max(img.size)
        img = img.resize((int(img.width * ratio), int(img.height * ratio)))
    buf = BytesIO()
    img.save(buf, format="JPEG", quality=85)
    return base64.b64encode(buf.getvalue()).decode("utf-8"), "image/jpeg"


PROMPT_TEMPLATE = """You are a strict but fair teacher's assistant grading a student's
answer sheet photographed by the teacher.

RULES:
- Read the handwritten student work carefully.
- Compare it against the reference answer key provided below.
- Award partial credit where the method is right but a small mistake occurs.
- Be honest about uncertainty — set confidence lower if the image is unclear.
- Never invent answers that aren't on the sheet.
- Return ONLY valid JSON (no markdown, no commentary).

REFERENCE ANSWER KEY:
\"\"\"{answer_key}\"\"\"

GRADING SCALE:
- Maximum score: {max_score} points
- Coefficient: ×{coefficient}
- Subject: {subject}

RETURN JSON with EXACTLY this structure:
{{
  "score": <number out of max_score>,
  "max_score": <number>,
  "confidence": <integer 0-100>,
  "overall_feedback": "<2-4 sentences of feedback for the student>",
  "per_question": [
    {{
      "question": "<short label e.g. Q1 or Exercise 2a>",
      "student_answer": "<what the student wrote>",
      "correct_answer": "<expected answer from the key>",
      "correct": <true|false>,
      "points_earned": <number>,
      "points_possible": <number>,
      "comment": "<short comment>"
    }}
  ]
}}
"""


def _extract_json(text: str) -> dict:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except Exception:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(text[start:end + 1])
        except Exception:
            pass
    raise ValueError("Could not parse JSON from AI response.")


def analyze_sheet_real(image_file, answer_key, max_score, coefficient, subject):
    provider = st.session_state.api_provider
    key = st.session_state.api_key
    model = st.session_state.api_model

    b64, mime = _image_to_base64(image_file)
    prompt = PROMPT_TEMPLATE.format(
        answer_key=answer_key or "(no answer key — grade on general correctness)",
        max_score=max_score,
        coefficient=coefficient,
        subject=subject or "—",
    )

    if provider == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=key)
        resp = client.chat.completions.create(
            model=model,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url",
                     "image_url": {"url": f"data:{mime};base64,{b64}"}},
                ],
            }],
            max_tokens=2000,
        )
        raw = resp.choices[0].message.content

    elif provider == "anthropic":
        from anthropic import Anthropic
        client = Anthropic(api_key=key)
        resp = client.messages.create(
            model=model,
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image",
                     "source": {"type": "base64", "media_type": mime, "data": b64}},
                ],
            }],
        )
        raw = resp.content[0].text

    elif provider == "google":
        import google.generativeai as genai
        genai.configure(api_key=key)
        m = genai.GenerativeModel(model)
        resp = m.generate_content([
            prompt,
            {"mime_type": mime, "data": base64.b64decode(b64)},
        ])
        raw = resp.text

    else:
        raise ValueError("Unknown provider.")

    return _extract_json(raw), raw


def analyze_sheet_demo(max_score, coefficient):
    ratio = random.uniform(0.70, 0.95)
    points = round(max_score * ratio)
    if coefficient >= 3:
        points = max(1, points - 1)
    return {
        "score": points,
        "max_score": max_score,
        "confidence": random.randint(88, 97),
        "overall_feedback": (
            "Working is mostly complete. Minor errors on the final steps. "
            "Review the last section before the next exam. "
            "(DEMO MODE — no real analysis.)"
        ),
        "per_question": [
            {
                "question": "Q1",
                "student_answer": "—",
                "correct_answer": "—",
                "correct": True,
                "points_earned": round(points * 0.4, 1),
                "points_possible": round(max_score * 0.4, 1),
                "comment": "Demo entry.",
            },
            {
                "question": "Q2",
                "student_answer": "—",
                "correct_answer": "—",
                "correct": False,
                "points_earned": round(points * 0.6, 1),
                "points_possible": round(max_score * 0.6, 1),
                "comment": "Demo entry.",
            },
        ],
    }, "(DEMO MODE — no real analysis)"


# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="gl-header">
      <div class="gl-brand">GRADELENS AI</div>
      <div class="gl-tagline">📷 Real AI Vision · Coefficient-Based · Teacher-Controlled</div>
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
# SIDEBAR — API CONFIG
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🔑 AI Configuration")
    st.caption("Your API key is stored **only in this browser session**.")

    provider = st.selectbox(
        "AI Provider",
        options=list(PROVIDER_MODELS.keys()),
        format_func=lambda k: PROVIDER_LABELS[k],
        index=0,
        key="gl_provider",
    )

    model_options = PROVIDER_MODELS[provider]
    model = st.selectbox("Model", options=model_options, index=0, key="gl_model")

    api_key_input = st.text_input(
        "API Key",
        type="password",
        value=st.session_state.api_key,
        placeholder="Paste your API key here",
        key="gl_api_key_input",
    )

    col_v, col_c = st.columns(2)
    with col_v:
        if st.button("✅ Verify", use_container_width=True):
            if not api_key_input.strip():
                st.error("Enter an API key first.")
            else:
                with st.spinner("Verifying…"):
                    ok, msg = _verify_api_key(provider, api_key_input.strip(), model)
                    if ok:
                        st.session_state.api_key = api_key_input.strip()
                        st.session_state.api_provider = provider
                        st.session_state.api_model = model
                        st.session_state.api_verified = True
                        st.success("✅ Key verified")
                    else:
                        st.session_state.api_verified = False
                        st.error(f"❌ {msg}")
    with col_c:
        if st.button("🗑 Clear", use_container_width=True):
            st.session_state.api_key = ""
            st.session_state.api_verified = False
            st.rerun()

    if st.session_state.api_verified:
        st.markdown(
            f"""
            <div class="gl-ok">
              🟢 <b>Active:</b> {PROVIDER_LABELS.get(provider,'')}<br>
              <b>Model:</b> {st.session_state.api_model}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="gl-warn">
              ⚠️ No API key verified. Running in <b>DEMO mode</b>.
              Add a key to enable real AI grading.
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### 💡 Where to get a key")
    st.markdown(
        """
        - **Google Gemini** (free tier): [aistudio.google.com](https://aistudio.google.com/app/apikey)
        - **OpenAI**: [platform.openai.com](https://platform.openai.com/api-keys)
        - **Anthropic**: [console.anthropic.com](https://console.anthropic.com/settings/keys)
        """
    )
    st.caption("💵 ~$0.01–$0.05 per sheet graded · Gemini Flash has free tier.")


# -----------------------------------------------------------------------------
# STEP 1 — SETUP
# -----------------------------------------------------------------------------
st.markdown(
    '<div class="gl-card"><div class="gl-card-title">'
    '⚙️ Step 1 · Exam Setup + Answer Key</div>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)
with col1:
    coefficient = st.number_input(
        "Coefficient", min_value=1, max_value=10, value=1, step=1,
        help="Weight of this exam in the final average.", key="gl_coef",
    )
with col2:
    max_score = st.number_input(
        "Maximum Score", min_value=1, max_value=100, value=20, step=1,
        help="Total points possible on this exam.", key="gl_max",
    )

subject_input = st.text_input(
    "Subject / Title", placeholder="e.g. Math · Chapter 3 · Exercise 5",
    key="gl_subject_top",
)

answer_key = st.text_area(
    "📋 Reference Answer Key (paste the correct answers)",
    value=st.session_state.answer_key,
    placeholder=(
        "Example:\n"
        "Q1: x = 7\n"
        "Q2: 2x + 3 = 11, so x = 4\n"
        "Q3a: derivative = 3x²\n"
        "Q3b: derivative = 6x"
    ),
    height=160,
    key="gl_answer_key",
)
st.session_state.answer_key = answer_key

st.markdown(
    f"""
    <div class="gl-warn">
      📌 Setup: Coefficient <b>×{coefficient}</b> · Max <b>{max_score}</b> points ·
      Answer key: <b>{"provided" if answer_key.strip() else "NOT provided"}</b>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# STEP 2 — CAPTURE
# -----------------------------------------------------------------------------
st.markdown(
    '<div class="gl-card"><div class="gl-card-title">'
    '📷 Step 2 · Capture the Answer Sheet</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="gl-tip">
      📱 <b>Tip:</b> Use the <b>rear camera</b> for a paper sheet.
      On <b>Quick Capture</b>, tap the flip icon ↺ inside the camera preview.
      On <b>Native Camera</b>, your phone's own camera app opens with a proper flip button.
    </div>
    """,
    unsafe_allow_html=True,
)

tab1, tab2 = st.tabs(["📸 Quick Capture", "📁 Use Phone Camera (Native)"])
photo_file = None

with tab1:
    quick = st.camera_input("Camera", key="gl_camera",
                            label_visibility="collapsed")
    if quick is not None:
        photo_file = quick

with tab2:
    uploaded = st.file_uploader(
        "Take or upload a photo",
        type=["jpg", "jpeg", "png", "heic", "heif", "webp"],
        key="gl_upload",
        label_visibility="collapsed",
    )
    if uploaded is not None:
        photo_file = uploaded

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# STEP 3 — AI ANALYSIS
# -----------------------------------------------------------------------------
if photo_file is not None:
    st.markdown(
        '<div class="gl-card"><div class="gl-card-title">'
        '🖼️ Captured Sheet</div>',
        unsafe_allow_html=True,
    )
    st.image(photo_file, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="gl-card"><div class="gl-card-title">'
        '🤖 Step 3 · AI Vision Analysis</div>',
        unsafe_allow_html=True,
    )

    if st.session_state.api_verified:
        st.success(
            f"🔬 Real AI grading enabled · "
            f"{PROVIDER_LABELS[st.session_state.api_provider]} · "
            f"{st.session_state.api_model}"
        )
    else:
        st.warning(
            "⚠️ **DEMO mode** — add a key in the sidebar to enable real AI grading."
        )

    if st.button("🔍 Analyze Sheet & Compute Grade",
                 use_container_width=True, key="gl_analyze"):
        with st.spinner("AI is reading the sheet and grading…"):
            try:
                if st.session_state.api_verified:
                    result, raw = analyze_sheet_real(
                        photo_file, answer_key,
                        int(max_score), int(coefficient), subject_input,
                    )
                else:
                    result, raw = analyze_sheet_demo(
                        int(max_score), int(coefficient),
                    )

                st.session_state.ai_done = True
                st.session_state.ai_points = float(result.get("score", 0))
                st.session_state.ai_max = int(result.get("max_score", max_score))
                st.session_state.ai_coefficient = int(coefficient)
                st.session_state.ai_confidence = int(result.get("confidence", 0))
                st.session_state.ai_overall_feedback = result.get("overall_feedback", "")
                st.session_state.ai_per_question = result.get("per_question", [])
                st.session_state.ai_raw = raw

            except Exception as e:
                st.error(f"❌ Analysis failed: {str(e)[:300]}")
                st.session_state.ai_done = False

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
              <div class="gl-ai-line"><b>Overall feedback:</b>
                {st.session_state.ai_overall_feedback or "—"}
              </div>

              <div class="gl-score-card">
                <div>
                  <div class="gl-score-label">AI Suggested Grade</div>
                  <div class="gl-score-num">{pts:g}/{maxs}</div>
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

        if st.session_state.ai_per_question:
            st.markdown("##### 📋 Per-Question Breakdown")
            for q in st.session_state.ai_per_question:
                ok = bool(q.get("correct"))
                cls = "ok" if ok else "bad"
                icon = "✅" if ok else "❌"
                st.markdown(
                    f"""
                    <div class="gl-q-row {cls}">
                      {icon} <b>{q.get('question','?')}</b> —
                      {q.get('points_earned','?')}/{q.get('points_possible','?')} pts<br>
                      <b>Student:</b> {q.get('student_answer','—')}<br>
                      <b>Expected:</b> {q.get('correct_answer','—')}<br>
                      <i>{q.get('comment','')}</i>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.info(
            f"✍️ **Teacher step:** Write **{pts:g}/{maxs}** on the student's paper, "
            "then confirm below."
        )
    else:
        st.info("Click **Analyze Sheet & Compute Grade** to run the AI.")

    st.markdown('</div>', unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # STEP 4 — TEACHER CONFIRMATION
    # -------------------------------------------------------------------------
    st.markdown(
        '<div class="gl-card"><div class="gl-card-title">'
        '✏️ Step 4 · Teacher Confirms the Grade</div>',
        unsafe_allow_html=True,
    )

    col_a, col_b = st.columns(2)
    with col_a:
        student_name = st.text_input(
            "Student Name", value=st.session_state.student_name,
            placeholder="e.g. Marie Jean", key="gl_name",
        )
    with col_b:
        subject_final = st.text_input(
            "Subject", value=st.session_state.subject or subject_input,
            placeholder="e.g. Math · Ex 5", key="gl_subject_final",
        )

    default_ai_grade = ""
    if st.session_state.ai_done and st.session_state.ai_points is not None:
        default_ai_grade = f"{st.session_state.ai_points:g}/{st.session_state.ai_max}"

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
        value=st.session_state.ai_overall_feedback,
        placeholder="Write your own feedback for the student…",
        key="gl_comment", height=90,
    )

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
                    "subject": subject_final.strip(),
                    "coefficient": coefficient,
                    "max": max_score,
                    "ai": ai_value or "—",
                    "final": teacher_grade.strip(),
                    "feedback": teacher_comment.strip() or "—",
                }
                st.session_state.history.append(record)
                st.session_state.student_name = student_name.strip()
                st.session_state.subject = subject_final.strip()
                st.success(f"💾 Grade saved for **{record['student']}**.")
    with b2:
        if st.button("📋 Copy Summary", use_container_width=True, key="gl_copy"):
            if not student_name.strip():
                st.warning("Enter the student's name first.")
            else:
                summary = (
                    f"📋 GradeLens AI Summary\n"
                    f"───────────────────────\n"
                    f"Student     : {student_name.strip()}\n"
                    f"Subject     : {subject_final.strip() or '—'}\n"
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
            for k in ["ai_done", "ai_points", "ai_confidence",
                      "ai_per_question", "ai_overall_feedback", "ai_raw"]:
                st.session_state[k] = (
                    False if k == "ai_done" else
                    None if k in ("ai_points", "ai_confidence") else
                    [] if k == "ai_per_question" else ""
                )
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
