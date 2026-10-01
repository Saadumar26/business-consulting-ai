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
# MODERN CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    /* ----------------------------------------------
       GLOBAL
    ---------------------------------------------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(99, 102, 241, 0.08),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(14, 165, 233, 0.07),
                transparent 25%
            ),
            #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }


    /* ----------------------------------------------
       HEADER
    ---------------------------------------------- */

    .hero {
        padding: 35px 40px;
        border-radius: 24px;
        margin-bottom: 30px;

        background:
            linear-gradient(
                135deg,
                rgba(79, 70, 229, 0.95),
                rgba(37, 99, 235, 0.90)
            );

        color: white;

        box-shadow:
            0 20px 45px rgba(37, 99, 235, 0.20);
    }

    .hero-badge {
        display: inline-block;

        padding: 6px 12px;

        border-radius: 999px;

        background: rgba(255,255,255,0.15);

        font-size: 13px;
        font-weight: 600;

        margin-bottom: 14px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0;
    }

    .hero-subtitle {
        font-size: 17px;
        opacity: 0.90;
        margin-top: 10px;
        max-width: 720px;
        line-height: 1.6;
    }


    /* ----------------------------------------------
       SECTION HEADERS
    ---------------------------------------------- */

    .section-title {
        font-size: 25px;
        font-weight: 750;
        color: #111827;
        margin-top: 12px;
        margin-bottom: 5px;
    }

    .section-description {
        color: #6b7280;
        font-size: 14px;
        margin-bottom: 20px;
    }


    /* ----------------------------------------------
       AGENT CARDS
    ---------------------------------------------- */

    .agent-card {
        background: white;

        border: 1px solid #e5e7eb;

        border-radius: 16px;

        padding: 16px;

        margin-bottom: 12px;

        box-shadow:
            0 4px 14px rgba(15, 23, 42, 0.04);

        transition: all 0.2s ease;
    }

    .agent-card:hover {
        transform: translateY(-2px);

        box-shadow:
            0 8px 20px rgba(15, 23, 42, 0.08);
    }

    .agent-icon {
        font-size: 24px;
        margin-right: 8px;
    }

    .agent-name {
        font-weight: 700;
        color: #111827;
        font-size: 15px;
    }

    .agent-description {
        color: #6b7280;
        font-size: 12px;
        margin-top: 4px;
    }


    /* ----------------------------------------------
       ACTIVE AGENT
    ---------------------------------------------- */

    .active-agent {
        background:
            linear-gradient(
                135deg,
                rgba(79, 70, 229, 0.08),
                rgba(59, 130, 246, 0.05)
            );

        border: 1px solid rgba(79, 70, 229, 0.35);

        border-radius: 16px;

        padding: 17px;

        margin-bottom: 12px;

        box-shadow:
            0 0 0 3px rgba(79, 70, 229, 0.05);
    }

    .active-label {
        color: #4f46e5;
        font-size: 12px;
        font-weight: 700;
        margin-top: 5px;
    }


    /* ----------------------------------------------
       INPUT CARDS
    ---------------------------------------------- */

    .input-card {
        background: white;

        border: 1px solid #e5e7eb;

        border-radius: 18px;

        padding: 22px;

        margin-bottom: 18px;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.04);
    }


    /* ----------------------------------------------
       STATUS BOX
    ---------------------------------------------- */

    .running-box {
        padding: 18px;

        border-radius: 16px;

        background:
            linear-gradient(
                135deg,
                rgba(79, 70, 229, 0.08),
                rgba(14, 165, 233, 0.06)
            );

        border: 1px solid rgba(79, 70, 229, 0.20);

        margin-bottom: 20px;
    }


    /* ----------------------------------------------
       REPORT
    ---------------------------------------------- */

    .report-header {
        background: white;

        border: 1px solid #e5e7eb;

        border-radius: 18px;

        padding: 20px 24px;

        margin-bottom: 18px;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.04);
    }


    /* ----------------------------------------------
       BUTTONS
    ---------------------------------------------- */

    div.stButton > button {

        border-radius: 12px;

        font-weight: 700;

        padding: 12px 20px;

        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-1px);
    }


    /* ----------------------------------------------
       SIDEBAR
    ---------------------------------------------- */

    section[data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #ffffff 0%,
                #f8fafc 100%
            );

        border-right: 1px solid #e5e7eb;
    }


    /* ----------------------------------------------
       FOOTER
    ---------------------------------------------- */

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

    agents = [
        (
            "🔎",
            "Market Researcher",
            "Market & industry analysis",
        ),
        (
            "👥",
            "Customer & Competitor Analyst",
            "Customers and competition",
        ),
        (
            "📊",
            "Business Analyst",
            "Business performance analysis",
        ),
        (
            "🧠",
            "Strategy Consultant",
            "Strategic recommendations",
        ),
        (
            "📝",
            "Report Writer",
            "Final consulting report",
        ),
    ]

    for icon, name, description in agents:

        st.markdown(
            f"""
            <div class="agent-card">

                <div>
                    <span class="agent-icon">{icon}</span>
                    <span class="agent-name">{name}</span>
                </div>

                <div class="agent-description">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

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
    """
    <div class="section-description">
        Provide your business details so the consulting team
        can build a tailored strategic analysis.
    </div>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# BASIC BUSINESS INFORMATION
# ==================================================

st.markdown('<div class="input-card">', unsafe_allow_html=True)

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

st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# BUSINESS DESCRIPTION
# ==================================================

st.markdown('<div class="input-card">', unsafe_allow_html=True)

business_description = st.text_area(
    "📄 Business Description",
    placeholder=(
        "What does your business do?\n\n"
        "Describe your product or service, "
        "business model, and what makes the business unique."
    ),
    height=140,
)

st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# MARKET INFORMATION
# ==================================================

st.markdown(
    '<div class="section-title">🎯 Market & Customers</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-description">
        Help the consultants understand who you serve and where
        your business operates.
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="input-card">', unsafe_allow_html=True)

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

st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# BUSINESS CHALLENGE
# ==================================================

st.markdown(
    '<div class="section-title">⚠️ Business Challenge</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-description">
        Tell the consulting team what problem you want to solve.
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="input-card">', unsafe_allow_html=True)

challenge = st.text_area(
    "Main Business Challenge",
    placeholder=(
        "Example:\n"
        "Customer retention is low and competition "
        "has increased significantly."
    ),
    height=120,
)

st.markdown("</div>", unsafe_allow_html=True)


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
    <div style="
        text-align:center;
        margin-bottom:10px;
    ">
        <span style="
            color:#6b7280;
            font-size:14px;
        ">
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
    # Validate required fields
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
    # Prepare inputs
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
    # CONSULTING TEAM STATUS
    # ==================================================

    st.markdown(
        """
        <div class="running-box">

            <strong>🤖 Consulting team is working...</strong>

            <div style="
                color:#6b7280;
                font-size:13px;
                margin-top:5px;
            ">
                Your business is being analyzed by multiple
                specialized AI consultants.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    # ==================================================
    # AGENT PROGRESS
    # ==================================================

    st.markdown(
        '<div class="section-title">🔄 Agent Workflow</div>',
        unsafe_allow_html=True,
    )

    progress_placeholder = st.empty()


    # ----------------------------------------------
    # Initial Agent State
    # ----------------------------------------------

    agent_steps = [
        ("🔎", "Market Researcher", "Analyzing market and industry"),
        (
            "👥",
            "Customer & Competitor Analyst",
            "Analyzing customers and competitors",
        ),
        (
            "📊",
            "Business Analyst",
            "Evaluating business situation",
        ),
        (
            "🧠",
            "Strategy Consultant",
            "Developing strategic recommendations",
        ),
        (
            "📝",
            "Report Writer",
            "Preparing final consulting report",
        ),
    ]


    # ----------------------------------------------
    # Show workflow
    # ----------------------------------------------

    def render_agents(active_index):

        html = ""

        for index, (icon, name, description) in enumerate(agent_steps):

            if index < active_index:

                html += f"""
                <div class="agent-card">

                    <div>
                        <span class="agent-icon">✅</span>
                        <span class="agent-name">
                            {name}
                        </span>
                    </div>

                    <div class="agent-description">
                        Completed
                    </div>

                </div>
                """

            elif index == active_index:

                html += f"""
                <div class="active-agent">

                    <div>
                        <span class="agent-icon">{icon}</span>
                        <span class="agent-name">
                            {name}
                        </span>
                    </div>

                    <div class="active-label">
                        🔵 CURRENTLY RUNNING
                    </div>

                    <div class="agent-description">
                        {description}...
                    </div>

                </div>
                """

            else:

                html += f"""
                <div class="agent-card">

                    <div>
                        <span class="agent-icon">⏳</span>
                        <span class="agent-name">
                            {name}
                        </span>
                    </div>

                    <div class="agent-description">
                        Waiting
                    </div>

                </div>
                """

        return html


    # ==================================================
    # RUN CREWAI
    # ==================================================

    with st.status(
        "🤖 Consulting team is working...",
        expanded=True,
    ) as status:

        try:

            # ------------------------------------------
            # Display workflow stages
            # ------------------------------------------

            progress_placeholder.markdown(
                render_agents(0),
                unsafe_allow_html=True,
            )

            st.write(
                "🔎 Market Researcher is analyzing the market..."
            )


            # ------------------------------------------
            # Create Crew
            # ------------------------------------------

            crew = create_business_crew()


            # ------------------------------------------
            # Run CrewAI
            # ------------------------------------------

            result = crew.kickoff(inputs=inputs)


            # ------------------------------------------
            # Completed
            # ------------------------------------------

            progress_placeholder.markdown(
                """
                <div class="agent-card">

                    <div>
                        <span class="agent-icon">✅</span>
                        <span class="agent-name">
                            Consulting Team
                        </span>
                    </div>

                    <div class="agent-description">
                        All consultants completed their analysis.
                    </div>

                </div>
                """,
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
    # DISPLAY REPORT
    # ==================================================

    st.divider()

    st.markdown(
        """
        <div class="report-header">

            <div style="
                font-size:25px;
                font-weight:750;
                color:#111827;
            ">
                📋 Business Strategy Report
            </div>

            <div style="
                color:#6b7280;
                font-size:14px;
                margin-top:5px;
            ">
                AI-generated strategic analysis based on the
                information provided.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    # ----------------------------------------------
    # Report
    # ----------------------------------------------

    st.markdown(result.raw)


    # ==================================================
    # DOWNLOAD REPORT
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
