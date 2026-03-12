import streamlit as st
import random

# --- Page Config ---
st.set_page_config(page_title="✨ Tech Facts!", page_icon="💻", layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&family=Fredoka+One&display=swap');

    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #fff9f0 0%, #ffeef8 50%, #eef6ff 100%);
    }

    h1, h2, h3 {
        font-family: 'Fredoka One', cursive !important;
    }

    .fact-card {
        background: white;
        border-radius: 20px;
        padding: 22px 26px;
        margin: 10px 0;
        border-left: 6px solid #ff6fb7;
        box-shadow: 4px 4px 0px #ffb3d9;
        font-size: 16px;
        font-weight: 600;
        color: #333;
        display: flex;
        align-items: flex-start;
        gap: 12px;
        transition: transform 0.2s;
    }

    .fact-card:hover {
        transform: translateY(-2px);
    }

    .fact-card.favorited {
        border-left: 6px solid #ffaa33;
        box-shadow: 4px 4px 0px #ffe0a0;
    }

    .big-fact {
        background: linear-gradient(135deg, #ff6fb7, #a78bfa);
        border-radius: 24px;
        padding: 28px 30px;
        color: white;
        font-size: 20px;
        font-weight: 800;
        text-align: center;
        box-shadow: 6px 6px 0px #c44b8a;
        margin: 16px 0;
        font-family: 'Fredoka One', cursive;
        line-height: 1.5;
    }

    .stat-box {
        background: white;
        border-radius: 16px;
        padding: 14px 20px;
        text-align: center;
        box-shadow: 3px 3px 0px #e0e0e0;
        font-weight: 700;
    }

    .stat-num {
        font-family: 'Fredoka One', cursive;
        font-size: 32px;
        color: #ff6fb7;
    }

    .stat-label {
        font-size: 13px;
        color: #888;
        margin-top: 2px;
    }

    div[data-testid="stButton"] button {
        border-radius: 50px !important;
        font-family: 'Fredoka One', cursive !important;
        font-size: 16px !important;
        font-weight: 400 !important;
        border: none !important;
    }

    .stTextInput > div > div > input {
        border-radius: 50px !important;
        border: 3px solid #ffb3d9 !important;
        padding: 10px 18px !important;
        font-family: 'Nunito', sans-serif !important;
        font-weight: 600 !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #ff6fb7 !important;
        box-shadow: 0 0 0 2px #ffb3d9 !important;
    }

    .tab-content {
        padding-top: 12px;
    }

    .empty-state {
        text-align: center;
        padding: 40px;
        color: #bbb;
        font-size: 18px;
        font-weight: 700;
    }

    .header-emoji {
        font-size: 48px;
        text-align: center;
        display: block;
    }
</style>
""", unsafe_allow_html=True)


# --- Session State Init ---
if "facts" not in st.session_state:
    st.session_state.facts = [
        "The first domain name ever registered was 'symbolics.com' on March 15, 1985.",
        "The entire Apollo 11 guidance computer code was less than 64KB — smaller than a smartphone photo.",
        "IBM's Deep Blue beat world chess champion Garry Kasparov in 1997.",
        "The term 'Wi-Fi' doesn't stand for anything — it's just a brand name.",
        "A 20TB hard drive can store about 5000 HD movies.",
        "A single Google search needs more power than the whole Apollo 11 mission.",
        "Error '404' was named after room 404 at CERN, birthplace of the web.",
        "Siri comes from a Norwegian word meaning 'beautiful victory'.",
        "Hi I'm Laiba 👋",
    ]

if "favorites" not in st.session_state:
    st.session_state.favorites = set()

if "shown_fact" not in st.session_state:
    st.session_state.shown_fact = None


# --- Header ---
st.markdown("<span class='header-emoji'>💻</span>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color:#ff6fb7; font-size:42px;'>Tech Facts!</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; font-size:15px; margin-top:-10px;'>Learn something new every click ✨</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Stats Row ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class='stat-box'>
        <div class='stat-num'>{len(st.session_state.facts)}</div>
        <div class='stat-label'>Total Facts</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class='stat-box'>
        <div class='stat-num' style='color:#ffaa33;'>❤️ {len(st.session_state.favorites)}</div>
        <div class='stat-label'>Favorites</div>
    </div>""", unsafe_allow_html=True)
with col3:
    non_fav = len(st.session_state.facts) - len(st.session_state.favorites)
    st.markdown(f"""
    <div class='stat-box'>
        <div class='stat-num' style='color:#a78bfa;'>{non_fav}</div>
        <div class='stat-label'>To Explore</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Random Fact Section ---
st.markdown("### 🎲 Random Fact Generator")

col_btn, col_fav = st.columns([2, 1])
with col_btn:
    if st.button("✨ Surprise Me!", use_container_width=True):
        st.session_state.shown_fact = random.choice(st.session_state.facts)

if st.session_state.shown_fact:
    st.markdown(f"<div class='big-fact'>💡 {st.session_state.shown_fact}</div>", unsafe_allow_html=True)
    fact = st.session_state.shown_fact
    is_fav = fact in st.session_state.favorites
    fav_label = "💔 Remove from Favorites" if is_fav else "❤️ Add to Favorites"
    if st.button(fav_label, key="fav_random"):
        if is_fav:
            st.session_state.favorites.discard(fact)
            st.toast("Removed from favorites!", icon="💔")
        else:
            st.session_state.favorites.add(fact)
            st.toast("Added to favorites! ❤️")
        st.rerun()

st.divider()

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["🔍 All Facts", "❤️ Favorites", "➕ Add Fact"])

# --- Tab 1: All Facts with Search ---
with tab1:
    search = st.text_input("🔍 Search facts...", placeholder="e.g. Google, Apollo, Wi-Fi")
    facts_to_show = st.session_state.facts
    if search.strip():
        facts_to_show = [f for f in st.session_state.facts if search.lower() in f.lower()]

    if not facts_to_show:
        st.markdown("<div class='empty-state'>😅 No facts match your search!</div>", unsafe_allow_html=True)
    else:
        for i, fact in enumerate(facts_to_show):
            is_fav = fact in st.session_state.favorites
            card_class = "fact-card favorited" if is_fav else "fact-card"
            icon = "❤️" if is_fav else "📌"
            col_fact, col_action = st.columns([5, 1])
            with col_fact:
                st.markdown(f"<div class='{card_class}'>{icon} {fact}</div>", unsafe_allow_html=True)
            with col_action:
                btn_label = "💔" if is_fav else "❤️"
                btn_help = "Remove favorite" if is_fav else "Add to favorites"
                if st.button(btn_label, key=f"fav_{i}", help=btn_help):
                    if is_fav:
                        st.session_state.favorites.discard(fact)
                        st.toast("Removed! 💔")
                    else:
                        st.session_state.favorites.add(fact)
                        st.toast("Favorited! ❤️")
                    st.rerun()

# --- Tab 2: Favorites ---
with tab2:
    if not st.session_state.favorites:
        st.markdown("<div class='empty-state'>No favorites yet!<br>Hit ❤️ on any fact to save it here 🌟</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p style='color:#888; font-weight:700;'>You have {len(st.session_state.favorites)} favorite(s) ❤️</p>", unsafe_allow_html=True)
        for i, fact in enumerate(st.session_state.favorites):
            col_fact, col_action = st.columns([5, 1])
            with col_fact:
                st.markdown(f"<div class='fact-card favorited'>❤️ {fact}</div>", unsafe_allow_html=True)
            with col_action:
                if st.button("💔", key=f"unfav_{i}", help="Remove from favorites"):
                    st.session_state.favorites.discard(fact)
                    st.toast("Removed! 💔")
                    st.rerun()

# --- Tab 3: Add Fact ---
with tab3:
    st.markdown("##### Got a cool fact? Share it! 🤓")
    new_fact = st.text_input("Type your fact here:", placeholder="e.g. The first computer bug was an actual bug!")
    if st.button("🚀 Add My Fact!", use_container_width=True):
        if new_fact.strip():
            if new_fact.strip() in st.session_state.facts:
                st.warning("This fact already exists! Try something new 🤔")
            else:
                st.session_state.facts.append(new_fact.strip())
                st.success("🎉 Your fact has been added!")
                st.balloons()
        else:
            st.warning("Please type a fact first! 📝")

st.markdown("<br><p style='text-align:center; color:#ccc; font-size:13px;'>Made with 💻 + ❤️ by Laiba</p>", unsafe_allow_html=True)