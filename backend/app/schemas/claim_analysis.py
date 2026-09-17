from pydantic import BaseModel, Field
from typing import List


class ClaimAnalysis(BaseModel):
    claim_type: str = Field(description="Type of claim: statistical, factual, prediction, or opinion")
    sub_claims: List[str] = Field(description="Key verifiable parts of the claim broken down")
    search_keywords: List[str] = Field(description="Keywords to search for evidence")