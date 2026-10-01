from crewai import Agent
from llm import get_llm


def create_business_analyst():

    return Agent(
        role="Business and SWOT Analyst",

        goal=(
            "Analyze the business model, strengths, weaknesses, opportunities, "
            "threats, revenue opportunities, operational issues, and business risks."
        ),

        backstory=(
            "You are a senior business analyst specializing in business models, "
            "SWOT analysis, operational analysis, revenue opportunities, "
            "and risk identification. "
            "You transform business information into structured insights."
        ),

        llm=get_llm(),

        verbose=False,

        allow_delegation=False,
    )
