import streamlit as st

from crew import create_business_crew


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Business Consulting Team",
    page_icon="💼",
    layout="wide",
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    .agent-card {
        padding: 15px;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        margin-bottom: 10px;
        background-color: #fafafa;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="main-title">💼 AI Business Consulting Team</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="subtitle">
    A multi-agent business strategy system powered by CrewAI and Groq.
    </div>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.header("🤖 Consulting Team")

    st.markdown(
        """
        **5 AI Consultants**

        🔎 Market Researcher

        👥 Customer & Competitor Analyst

        📊 Business Analyst

        🧠 Strategy Consultant

        📝 Report Writer
        """
    )

    st.divider()

    st.info(
        "The system generates AI-based strategic analysis. "
        "Important business decisions should be validated with "
        "real market and financial data."
    )


# ==================================================
# BUSINESS INFORMATION
# ==================================================

st.header("🏢 Tell us about your business")

business_name = st.text_input(
    "Business Name",
    placeholder="Example: FreshBite",
)

business_description = st.text_area(
    "Business Description",
    placeholder=(
        "What does your business do? "
        "Describe your product or service and business model."
    ),
    height=120,
)


col1, col2 = st.columns(2)


with col1:

    industry = st.text_input(
        "Industry",
        placeholder="Example: Food Delivery",
    )

    target_market = st.text_input(
        "Target Customers",
        placeholder="Example: University students",
    )


with col2:

    location = st.text_input(
        "Location / Market",
        placeholder="Example: Lahore, Pakistan",
    )

    challenge = st.text_area(
        "Main Business Challenge",
        placeholder=(
            "Example: Low customer retention "
            "and increasing competition."
        ),
        height=100,
    )


additional_information = st.text_area(
    "Additional Information",
    placeholder=(
        "Add any other useful information such as team size, "
        "existing marketing channels, current revenue model, "
        "known competitors, business goals, etc."
    ),
    height=130,
)


# ==================================================
# GENERATE BUTTON
# ==================================================

st.divider()

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


    # ----------------------------------------------
    # Run CrewAI
    # ----------------------------------------------

    with st.status(
        "🤖 Consulting team is working...",
        expanded=True,
    ) as status:

        try:

            st.write("🔎 Market Researcher is analyzing the market...")

            crew = create_business_crew()

            result = crew.kickoff(inputs=inputs)

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

    st.header("📋 Business Strategy Report")

    st.markdown(result.raw)


    # ==================================================
    # DOWNLOAD REPORT
    # ==================================================

    st.download_button(
        label="⬇️ Download Report",
        data=result.raw,
        file_name="business_strategy_report.md",
        mime="text/markdown",
        use_container_width=True,
    )
