from abc import ABC, abstractmethod


class BaseCampaign(ABC):
    _VALID_ID = set()

    def __init__(self, campaign_id, brand, budget, required_engagement):
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers = []

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")
        if value in BaseCampaign._VALID_ID:
            raise ValueError(f"Campaign with ID {value} already exists. Campaign IDs must be unique.")
        BaseCampaign._VALID_ID.add(value)
        self._campaign_id = value

    @abstractmethod
    def check_eligibility(self, engagement_rate):
        pass




