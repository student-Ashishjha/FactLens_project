from app.core.llm import llm
from app.schemas.claim_analysis import ClaimAnalysis

structured_llm = llm.with_structured_output(ClaimAnalysis)


def parse_claim(claim_text: str) -> ClaimAnalysis:
    prompt = f"""Analyze this claim and break it down for fact-checking:

Claim: "{claim_text}"

Identify the claim type, break it into verifiable sub-claims, and suggest search keywords."""

    result = structured_llm.invoke(prompt)
    return result