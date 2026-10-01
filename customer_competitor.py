from crewai import Agent
from llm import get_llm


def create_customer_competitor():

    return Agent(
        role="Customer and Competitor Analyst",

        goal=(
            "Analyze target customers, customer needs, customer pain points, "
            "competitors, competitive positioning, and differentiation opportunities."
        ),

        backstory=(
            "You are an experienced customer and competitive intelligence analyst. "
            "You specialize in customer segmentation, buyer needs, pain points, "
            "competitor analysis, positioning, and value propositions. "
            "You clearly distinguish assumptions from known information."
        ),

        llm=get_llm(),

        verbose=False,

        allow_delegation=False,
    )
