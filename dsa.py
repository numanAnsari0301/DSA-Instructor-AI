import streamlit as st
from google import genai
from google.genai import types


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="DSA Instructor AI",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# GEMINI CLIENT
# ==========================================

client = genai.Client()


# ==========================================
# SYSTEM INSTRUCTION
# ==========================================

system_instruction_text = """
You are an expert Data Structures and Algorithms Instructor.

Your job is to answer questions related only to:

- Data Structures
- Algorithms
- Arrays
- Strings
- Linked Lists
- Stacks
- Queues
- Trees
- Graphs
- Hashing
- Recursion
- Dynamic Programming
- Searching
- Sorting
- Greedy Algorithms
- Backtracking
- Time Complexity
- Space Complexity
- Competitive Programming
- Coding Interview Questions

Teaching Rules:

1. Explain concepts clearly and simply.
2. Use examples whenever helpful.
3. Explain intuition before code.
4. Mention time and space complexity.
5. Help the student understand instead of only giving answers.
6. If the user asks something unrelated to Data Structures and Algorithms,
   politely redirect them back to DSA.

Do not be unnecessarily rude.

For unrelated questions, respond like:

"I am your DSA Instructor 🤓. Let's focus on improving your Data Structures
and Algorithms skills for your interviews. Ask me a DSA question!"

"""


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("⚙️ DSA Instructor")

    st.divider()

    st.markdown("### 📚 Topics I Can Teach")

    topics = [
        "📦 Arrays",
        "🔤 Strings",
        "🔗 Linked Lists",
        "📚 Stacks",
        "🚶 Queues",
        "🌳 Trees",
        "🕸️ Graphs",
        "🔁 Recursion",
        "🧠 Dynamic Programming",
        "⚡ Sorting & Searching"
    ]

    for topic in topics:
        st.write(topic)

    st.divider()

    st.caption("Powered by Gemini AI 🤖")


# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<p class="main-title">🧠 DSA Instructor AI</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Learn Data Structures and Algorithms with AI</p>',
    unsafe_allow_html=True
)

st.divider()


# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ==========================================
# DISPLAY CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ==========================================
# CHAT INPUT
# ==========================================

user_question = st.chat_input(
    "Ask me any DSA question..."
)


# ==========================================
# GENERATE RESPONSE
# ==========================================

if user_question:

    # Store user message

    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })


    # Display user message

    with st.chat_message("user"):

        st.markdown(user_question)


    # AI response

    with st.chat_message("assistant"):

        with st.spinner("🤔 Thinking..."):

            try:

                response = client.models.generate_content(

                    model="gemini-2.5-flash",

                    contents=user_question,

                    config=types.GenerateContentConfig(

                        system_instruction=system_instruction_text

                    )

                )


                answer = response.text


                st.markdown(answer)


                # Store AI response

                st.session_state.messages.append({

                    "role": "assistant",

                    "content": answer

                })


            except Exception as e:

                st.error(
                    f"❌ Error: {str(e)}"
                )