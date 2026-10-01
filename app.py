# import streamlit as st

# from crew import create_business_crew


# # ==================================================
# # PAGE CONFIGURATION
# # ==================================================

# st.set_page_config(
#     page_title="AI Business Consulting Team",
#     page_icon="💼",
#     layout="wide",
# )


# # ==================================================
# # CUSTOM CSS
# # ==================================================

# st.markdown(
#     """
#     <style>

#     .main-title {
#         font-size: 42px;
#         font-weight: 700;
#         margin-bottom: 5px;
#     }

#     .subtitle {
#         font-size: 18px;
#         color: #6b7280;
#         margin-bottom: 30px;
#     }

#     .agent-card {
#         padding: 15px;
#         border: 1px solid #e5e7eb;
#         border-radius: 10px;
#         margin-bottom: 10px;
#         background-color: #fafafa;
#     }

#     </style>
#     """,
#     unsafe_allow_html=True,
# )


# # ==================================================
# # HEADER
# # ==================================================

# st.markdown(
#     '<div class="main-title">💼 AI Business Consulting Team</div>',
#     unsafe_allow_html=True,
# )

# st.markdown(
#     """
#     <div class="subtitle">
#     A multi-agent business strategy system powered by CrewAI and Groq.
#     </div>
#     """,
#     unsafe_allow_html=True,
# )


# # ==================================================
# # SIDEBAR
# # ==================================================

# with st.sidebar:

#     st.header("🤖 Consulting Team")

#     st.markdown(
#         """
#         **5 AI Consultants**

#         🔎 Market Researcher

#         👥 Customer & Competitor Analyst

#         📊 Business Analyst

#         🧠 Strategy Consultant

#         📝 Report Writer
#         """
#     )

#     st.divider()

#     st.info(
#         "The system generates AI-based strategic analysis. "
#         "Important business decisions should be validated with "
#         "real market and financial data."
#     )


# # ==================================================
# # BUSINESS INFORMATION
# # ==================================================

# st.header("🏢 Tell us about your business")

# business_name = st.text_input(
#     "Business Name",
#     placeholder="Example: FreshBite",
# )

# business_description = st.text_area(
#     "Business Description",
#     placeholder=(
#         "What does your business do? "
#         "Describe your product or service and business model."
#     ),
#     height=120,
# )


# col1, col2 = st.columns(2)


# with col1:

#     industry = st.text_input(
#         "Industry",
#         placeholder="Example: Food Delivery",
#     )

#     target_market = st.text_input(
#         "Target Customers",
#         placeholder="Example: University students",
#     )


# with col2:

#     location = st.text_input(
#         "Location / Market",
#         placeholder="Example: Lahore, Pakistan",
#     )

#     challenge = st.text_area(
#         "Main Business Challenge",
#         placeholder=(
#             "Example: Low customer retention "
#             "and increasing competition."
#         ),
#         height=100,
#     )


# additional_information = st.text_area(
#     "Additional Information",
#     placeholder=(
#         "Add any other useful information such as team size, "
#         "existing marketing channels, current revenue model, "
#         "known competitors, business goals, etc."
#     ),
#     height=130,
# )


# # ==================================================
# # GENERATE BUTTON
# # ==================================================

# st.divider()

# generate = st.button(
#     "🚀 Generate Business Strategy",
#     type="primary",
#     use_container_width=True,
# )


# # ==================================================
# # RUN CREW
# # ==================================================

# if generate:

#     # ----------------------------------------------
#     # Validate required fields
#     # ----------------------------------------------

#     if not business_name.strip():

#         st.error("Please enter the business name.")

#         st.stop()


#     if not business_description.strip():

#         st.error("Please describe your business.")

#         st.stop()


#     if not industry.strip():

#         st.error("Please enter the industry.")

#         st.stop()


#     # ----------------------------------------------
#     # Prepare inputs
#     # ----------------------------------------------

#     inputs = {

#         "business_name": business_name,

#         "business_description": business_description,

#         "industry": industry,

#         "target_market": target_market,

#         "location": location,

#         "challenge": challenge,

#         "additional_information": additional_information,
#     }


#     # ----------------------------------------------
#     # Run CrewAI
#     # ----------------------------------------------

#     with st.status(
#         "🤖 Consulting team is working...",
#         expanded=True,
#     ) as status:

#         try:

#             st.write("🔎 Market Researcher is analyzing the market...")

#             crew = create_business_crew()

#             result = crew.kickoff(inputs=inputs)

#             status.update(
#                 label="✅ Business strategy completed!",
#                 state="complete",
#                 expanded=False,
#             )

#         except Exception as error:

#             status.update(
#                 label="❌ Something went wrong.",
#                 state="error",
#                 expanded=True,
#             )

#             st.error(
#                 "The consulting team could not complete the analysis."
#             )

#             st.exception(error)

#             st.stop()


#     # ==================================================
#     # DISPLAY REPORT
#     # ==================================================

#     st.divider()

#     st.header("📋 Business Strategy Report")

#     st.markdown(result.raw)


#     # ==================================================
#     # DOWNLOAD REPORT
#     # ==================================================

#     st.download_button(
#         label="⬇️ Download Report",
#         data=result.raw,
#         file_name="business_strategy_report.md",
#         mime="text/markdown",
#         use_container_width=True,
#     )





import streamlit as st

from crew import create_business_crew


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Business Consulting Team",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
<style>

/* ==============================
   GLOBAL
================================= */

.stApp {
    background-color: #f8fafc;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ==============================
   HERO
================================= */

.hero {
    background: linear-gradient(
        135deg,
        #4f46e5 0%,
        #2563eb 100%
    );

    padding: 40px;
    border-radius: 24px;

    margin-bottom: 30px;

    color: white;

    box-shadow:
        0 15px 35px rgba(37, 99, 235, 0.20);
}

.hero-badge {
    display: inline-block;

    padding: 6px 12px;

    border-radius: 999px;

    background: rgba(255,255,255,0.16);

    font-size: 12px;
    font-weight: 700;

    margin-bottom: 14px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    line-height: 1.15;

    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 16px;

    line-height: 1.6;

    max-width: 750px;

    opacity: 0.9;
}


/* ==============================
   SECTION TITLES
================================= */

.section-title {
    font-size: 25px;
    font-weight: 750;

    color: #111827;

    margin-top: 15px;
    margin-bottom: 5px;
}

.section-description {
    color: #6b7280;

    font-size: 14px;

    margin-bottom: 20px;
}


/* ==============================
   CARDS
================================= */

.card {
    background: white;

    border: 1px solid #e5e7eb;

    border-radius: 18px;

    padding: 22px;

    margin-bottom: 18px;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.04);
}


/* ==============================
   AGENT CARD
================================= */

.agent-card {
    background: white;

    border: 1px solid #e5e7eb;

    border-radius: 14px;

    padding: 14px 15px;

    margin-bottom: 10px;
}

.agent-title {
    font-size: 14px;

    font-weight: 700;

    color: #111827;
}

.agent-description {
    font-size: 12px;

    color: #6b7280;

    margin-top: 3px;
}


/* ==============================
   ACTIVE AGENT
================================= */

.active-agent {
    background: #eef2ff;

    border: 1px solid #6366f1;

    border-radius: 14px;

    padding: 15px;

    margin-bottom: 10px;

    box-shadow:
        0 0 0 3px rgba(99,102,241,0.08);
}

.active-title {
    font-size: 14px;

    font-weight: 700;

    color: #3730a3;
}

.active-status {
    font-size: 11px;

    font-weight: 700;

    color: #4f46e5;

    margin-top: 5px;
}


/* ==============================
   SIDEBAR
================================= */

section[data-testid="stSidebar"] {
    background-color: #ffffff;

    border-right: 1px solid #e5e7eb;
}


/* ==============================
   BUTTON
================================= */

.stButton > button {
    border-radius: 12px;

    font-weight: 700;

    min-height: 48px;
}


/* ==============================
   INPUTS
================================= */

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
    border-radius: 10px;
}


/* ==============================
   REPORT
================================= */

.report-card {
    background: white;

    border: 1px solid #e5e7eb;

    border-radius: 18px;

    padding: 28px;

    margin-top: 10px;

    box-shadow:
        0 5px 18px rgba(15, 23, 42, 0.04);
}


/* ==============================
   FOOTER
================================= */

.footer {
    text-align: center;

    color: #9ca3af;

    font-size: 12px;

    margin-top: 50px;

    padding-top: 20px;

    border-top: 1px solid #e5e7eb;
}

</style>
""",
    unsafe_allow_html=True,
)


# ==================================================
# HERO HEADER
# ==================================================

st.markdown(
    """
<div class="hero">

    <div class="hero-badge">
        🤖 MULTI-AGENT AI SYSTEM
    </div>

    <div class="hero-title">
        AI Business Consulting Team
    </div>

    <div class="hero-subtitle">
        Get structured business analysis from a team of
        specialized AI consultants powered by CrewAI and Groq.
    </div>

</div>
""",
    unsafe_allow_html=True,
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("## 💼 Consulting Team")

    st.caption("Your AI-powered strategy department")

    st.divider()

    # Agent 1
    st.markdown("### 🔎 Market Researcher")
    st.caption("Market & industry analysis")

    # Agent 2
    st.markdown("### 👥 Customer & Competitor Analyst")
    st.caption("Customers and competition")

    # Agent 3
    st.markdown("### 📊 Business Analyst")
    st.caption("Business performance analysis")

    # Agent 4
    st.markdown("### 🧠 Strategy Consultant")
    st.caption("Strategic recommendations")

    # Agent 5
    st.markdown("### 📝 Report Writer")
    st.caption("Final consulting report")

    st.divider()

    st.markdown("### ⚡ How it works")

    st.caption(
        "Your business information is passed through "
        "multiple specialized AI consultants before the "
        "final strategy report is generated."
    )

    st.divider()

    st.info(
        "💡 AI-generated analysis should be validated "
        "with real market, customer, and financial data "
        "before making important business decisions."
    )


# ==================================================
# BUSINESS INFORMATION
# ==================================================

st.markdown(
    '<div class="section-title">🏢 Tell us about your business</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-description">'
    'Provide your business details so the consulting team '
    'can build a tailored strategic analysis.'
    '</div>',
    unsafe_allow_html=True,
)


# ==================================================
# BASIC INFORMATION
# ==================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:

    business_name = st.text_input(
        "Business Name",
        placeholder="e.g. FreshBite",
    )

with col2:

    industry = st.text_input(
        "Industry",
        placeholder="e.g. Food Delivery",
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True,
)


# ==================================================
# DESCRIPTION
# ==================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True,
)

business_description = st.text_area(
    "📄 Business Description",
    placeholder=(
        "What does your business do?\n\n"
        "Describe your product or service, "
        "business model, and what makes the business unique."
    ),
    height=140,
)

st.markdown(
    '</div>',
    unsafe_allow_html=True,
)


# ==================================================
# MARKET INFORMATION
# ==================================================

st.markdown(
    '<div class="section-title">🎯 Market & Customers</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-description">'
    'Help the consultants understand who you serve and where '
    'your business operates.'
    '</div>',
    unsafe_allow_html=True,
)


st.markdown(
    '<div class="card">',
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:

    target_market = st.text_input(
        "Target Customers",
        placeholder="e.g. University students",
    )

with col2:

    location = st.text_input(
        "Location / Market",
        placeholder="e.g. Lahore, Pakistan",
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True,
)


# ==================================================
# BUSINESS CHALLENGE
# ==================================================

st.markdown(
    '<div class="section-title">⚠️ Business Challenge</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-description">'
    'Tell the consulting team what problem you want to solve.'
    '</div>',
    unsafe_allow_html=True,
)


st.markdown(
    '<div class="card">',
    unsafe_allow_html=True,
)

challenge = st.text_area(
    "Main Business Challenge",
    placeholder=(
        "Example:\n"
        "Customer retention is low and competition "
        "has increased significantly."
    ),
    height=120,
)

st.markdown(
    '</div>',
    unsafe_allow_html=True,
)


# ==================================================
# ADDITIONAL INFORMATION
# ==================================================

with st.expander("➕ Add more business information (optional)"):

    additional_information = st.text_area(
        "Additional Information",
        placeholder=(
            "You can include:\n"
            "• Team size\n"
            "• Revenue model\n"
            "• Current marketing channels\n"
            "• Known competitors\n"
            "• Business goals\n"
            "• Existing products\n"
            "• Other useful information"
        ),
        height=160,
    )


# ==================================================
# GENERATE BUTTON
# ==================================================

st.divider()

st.markdown(
    """
<div style="text-align:center; margin-bottom:10px;">
    <span style="color:#6b7280; font-size:14px;">
        Ready to consult your AI strategy team?
    </span>
</div>
""",
    unsafe_allow_html=True,
)

generate = st.button(
    "🚀 Generate Business Strategy",
    type="primary",
    use_container_width=True,
)


# ==================================================
# RUN CREW
# ==================================================

if generate:

    # ----------------------------------------------
    # VALIDATION
    # ----------------------------------------------

    if not business_name.strip():

        st.error("Please enter the business name.")

        st.stop()

    if not business_description.strip():

        st.error("Please describe your business.")

        st.stop()

    if not industry.strip():

        st.error("Please enter the industry.")

        st.stop()


    # ----------------------------------------------
    # INPUTS
    # ----------------------------------------------

    inputs = {

        "business_name": business_name,

        "business_description": business_description,

        "industry": industry,

        "target_market": target_market,

        "location": location,

        "challenge": challenge,

        "additional_information": additional_information,
    }


    # ==================================================
    # AGENT WORKFLOW
    # ==================================================

    st.divider()

    st.markdown(
        '<div class="section-title">🔄 Agent Workflow</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Your AI consulting team is processing the request."
    )


    # --------------------------------------------------
    # Workflow containers
    # --------------------------------------------------

    agent_placeholder = st.empty()


    def render_agent_workflow(active_agent=None, completed=False):

        agents = [

            (
                "🔎",
                "Market Researcher",
                "Analyzing market and industry",
            ),

            (
                "👥",
                "Customer & Competitor Analyst",
                "Analyzing customers and competition",
            ),

            (
                "📊",
                "Business Analyst",
                "Evaluating the business",
            ),

            (
                "🧠",
                "Strategy Consultant",
                "Developing strategic recommendations",
            ),

            (
                "📝",
                "Report Writer",
                "Preparing final report",
            ),

        ]

        html = ""

        for icon, name, description in agents:

            if completed:

                html += f"""
<div class="agent-card">

    <div class="agent-title">
        ✅ {icon} {name}
    </div>

    <div class="agent-description">
        Completed
    </div>

</div>
"""

            elif name == active_agent:

                html += f"""
<div class="active-agent">

    <div class="active-title">
        🔵 {icon} {name}
    </div>

    <div class="active-status">
        CURRENTLY RUNNING
    </div>

    <div class="agent-description">
        {description}...
    </div>

</div>
"""

            else:

                html += f"""
<div class="agent-card">

    <div class="agent-title">
        ⏳ {icon} {name}
    </div>

    <div class="agent-description">
        Waiting
    </div>

</div>
"""

        return html


    # ==================================================
    # CREWAI EXECUTION
    # ==================================================

    with st.status(
        "🤖 Consulting team is working...",
        expanded=True,
    ) as status:

        try:

            # ------------------------------------------
            # Show first agent
            # ------------------------------------------

            agent_placeholder.markdown(
                render_agent_workflow(
                    "Market Researcher"
                ),
                unsafe_allow_html=True,
            )

            st.write(
                "🔎 Market Researcher is analyzing the market..."
            )


            # ------------------------------------------
            # CREATE CREW
            # ------------------------------------------

            crew = create_business_crew()


            # ------------------------------------------
            # RUN CREW
            # ------------------------------------------

            result = crew.kickoff(
                inputs=inputs
            )


            # ------------------------------------------
            # COMPLETED
            # ------------------------------------------

            agent_placeholder.markdown(
                render_agent_workflow(
                    completed=True
                ),
                unsafe_allow_html=True,
            )


            status.update(
                label="✅ Business strategy completed!",
                state="complete",
                expanded=False,
            )


        except Exception as error:

            status.update(
                label="❌ Something went wrong.",
                state="error",
                expanded=True,
            )

            st.error(
                "The consulting team could not complete the analysis."
            )

            st.exception(error)

            st.stop()


    # ==================================================
    # REPORT
    # ==================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '📋 Business Strategy Report'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-description">'
        'AI-generated strategic analysis based on the '
        'information provided.'
        '</div>',
        unsafe_allow_html=True,
    )


    st.markdown(
        '<div class="report-card">',
        unsafe_allow_html=True,
    )

    st.markdown(result.raw)

    st.markdown(
        '</div>',
        unsafe_allow_html=True,
    )


    # ==================================================
    # DOWNLOAD
    # ==================================================

    st.divider()

    st.download_button(
        label="⬇️ Download Strategy Report",
        data=result.raw,
        file_name="business_strategy_report.md",
        mime="text/markdown",
        use_container_width=True,
    )


# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
<div class="footer">
    💼 AI Business Consulting Team
    &nbsp;•&nbsp;
    Powered by CrewAI + Groq + Streamlit
</div>
""",
    unsafe_allow_html=True,
)

