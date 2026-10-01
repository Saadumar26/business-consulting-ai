from crewai import Crew, Process, Task

from market_researcher import create_market_researcher
from customer_competitor import create_customer_competitor
from business_analyst import create_business_analyst
from strategy_consultant import create_strategy_consultant
from report_writer import create_report_writer


def create_business_crew():

    # ==================================================
    # CREATE AGENTS
    # ==================================================

    market_researcher = create_market_researcher()

    customer_competitor = create_customer_competitor()

    business_analyst = create_business_analyst()

    strategy_consultant = create_strategy_consultant()

    report_writer = create_report_writer()


    # ==================================================
    # TASK 1 — MARKET RESEARCH
    # ==================================================

    market_task = Task(

        description="""
        Analyze the following business.

        BUSINESS NAME:
        {business_name}

        BUSINESS DESCRIPTION:
        {business_description}

        INDUSTRY:
        {industry}

        LOCATION / MARKET:
        {location}

        TARGET CUSTOMERS:
        {target_market}

        MAIN BUSINESS CHALLENGE:
        {challenge}

        ADDITIONAL INFORMATION:
        {additional_information}

        Perform a market research analysis.

        Cover:

        1. Industry overview
        2. Important industry trends
        3. Potential market opportunities
        4. Potential market threats
        5. Possible market gaps
        6. Growth opportunities
        7. Important assumptions
        8. Information that should be validated with real-world research

        Do not invent specific statistics.

        If exact market data is unavailable, clearly say that
        additional research is required.
        """,

        expected_output="""
        A structured market research analysis containing:

        - Industry overview
        - Industry trends
        - Market opportunities
        - Market threats
        - Market gaps
        - Growth opportunities
        - Assumptions
        - Research limitations
        """,

        agent=market_researcher,
    )


    # ==================================================
    # TASK 2 — CUSTOMER & COMPETITOR ANALYSIS
    # ==================================================

    customer_task = Task(

        description="""
        Analyze the customers and competitive environment for this business.

        BUSINESS NAME:
        {business_name}

        BUSINESS DESCRIPTION:
        {business_description}

        INDUSTRY:
        {industry}

        LOCATION / MARKET:
        {location}

        TARGET CUSTOMERS:
        {target_market}

        MAIN BUSINESS CHALLENGE:
        {challenge}

        ADDITIONAL INFORMATION:
        {additional_information}

        Analyze:

        1. Ideal customer segments
        2. Customer needs
        3. Customer pain points
        4. Customer motivations
        5. Potential competitor categories
        6. Competitive positioning
        7. Differentiation opportunities
        8. Value proposition opportunities
        9. Customer acquisition considerations

        Do not invent precise competitor statistics or financial information.
        Clearly identify assumptions.
        """,

        expected_output="""
        A structured customer and competitor analysis containing:

        - Customer segments
        - Customer needs
        - Customer pain points
        - Buyer motivations
        - Competitor categories
        - Competitive positioning
        - Differentiation opportunities
        - Value proposition
        - Customer acquisition considerations
        """,

        agent=customer_competitor,
    )


    # ==================================================
    # TASK 3 — BUSINESS ANALYSIS
    # ==================================================

    business_task = Task(

        description="""
        Analyze the business itself.

        BUSINESS NAME:
        {business_name}

        BUSINESS DESCRIPTION:
        {business_description}

        INDUSTRY:
        {industry}

        LOCATION / MARKET:
        {location}

        TARGET CUSTOMERS:
        {target_market}

        MAIN BUSINESS CHALLENGE:
        {challenge}

        ADDITIONAL INFORMATION:
        {additional_information}

        Perform:

        1. SWOT analysis
        2. Business model analysis
        3. Revenue opportunity analysis
        4. Operational analysis
        5. Key business risks
        6. Resource considerations
        7. Areas requiring validation

        Do not invent financial numbers.
        Use only information supplied by the user and reasonable
        strategic assumptions.
        """,

        expected_output="""
        A structured business analysis containing:

        - Strengths
        - Weaknesses
        - Opportunities
        - Threats
        - Business model observations
        - Revenue opportunities
        - Operational considerations
        - Key risks
        - Validation requirements
        """,

        agent=business_analyst,
    )


    # ==================================================
    # TASK 4 — BUSINESS STRATEGY
    # ==================================================

    strategy_task = Task(

        description="""
        Develop the overall business strategy.

        BUSINESS NAME:
        {business_name}

        BUSINESS DESCRIPTION:
        {business_description}

        INDUSTRY:
        {industry}

        LOCATION / MARKET:
        {location}

        TARGET CUSTOMERS:
        {target_market}

        MAIN BUSINESS CHALLENGE:
        {challenge}

        Use the market research, customer/competitor analysis,
        and business analysis provided by the other consultants.

        Develop:

        1. Strategic direction
        2. Business positioning
        3. Value proposition
        4. Go-to-market strategy
        5. Customer acquisition strategy
        6. Marketing strategy
        7. Pricing considerations
        8. Revenue growth opportunities
        9. Operational priorities
        10. Risk mitigation
        11. 30-day action plan
        12. 90-day action plan
        13. Long-term strategic priorities

        Recommendations must be connected to the previous analyses.

        Avoid unsupported numerical claims.
        """,

        expected_output="""
        A comprehensive business strategy containing:

        - Strategic direction
        - Positioning
        - Value proposition
        - Go-to-market strategy
        - Customer acquisition strategy
        - Marketing strategy
        - Pricing considerations
        - Revenue opportunities
        - Operational priorities
        - Risk mitigation
        - 30-day action plan
        - 90-day action plan
        - Long-term priorities
        """,

        agent=strategy_consultant,

        context=[
            market_task,
            customer_task,
            business_task,
        ],
    )


    # ==================================================
    # TASK 5 — FINAL REPORT
    # ==================================================

    report_task = Task(

        description="""
        Create the final Business Strategy Consulting Report.

        BUSINESS NAME:
        {business_name}

        BUSINESS DESCRIPTION:
        {business_description}

        INDUSTRY:
        {industry}

        LOCATION / MARKET:
        {location}

        TARGET CUSTOMERS:
        {target_market}

        MAIN BUSINESS CHALLENGE:
        {challenge}

        Produce a professional consulting report using all
        previous research and analysis.

        Use this structure:

        # Executive Summary

        # Business Overview

        # Market Analysis

        # Customer Analysis

        # Competitive Analysis

        # SWOT Analysis

        # Strategic Positioning

        # Recommended Business Strategy

        # Go-To-Market Strategy

        # Marketing Strategy

        # Pricing and Revenue Considerations

        # Operational Priorities

        # Risk Analysis

        # 30-Day Action Plan

        # 90-Day Action Plan

        # Long-Term Strategic Priorities

        # Key Assumptions and Limitations

        # Final Strategic Considerations

        The report should be:

        - Professional
        - Practical
        - Structured
        - Easy to understand
        - Action-oriented

        Do not fabricate statistics, financial figures,
        market shares, or competitor facts.
        """,

        expected_output="""
        A polished Markdown business strategy report containing
        all requested sections and synthesizing the work of
        the entire consulting team.
        """,

        agent=report_writer,

        context=[
            market_task,
            customer_task,
            business_task,
            strategy_task,
        ],
    )


    # ==================================================
    # CREATE CREW
    # ==================================================

    crew = Crew(

        agents=[
            market_researcher,
            customer_competitor,
            business_analyst,
            strategy_consultant,
            report_writer,
        ],

        tasks=[
            market_task,
            customer_task,
            business_task,
            strategy_task,
            report_task,
        ],

        process=Process.sequential,

        verbose=False,
    )

    return crew
