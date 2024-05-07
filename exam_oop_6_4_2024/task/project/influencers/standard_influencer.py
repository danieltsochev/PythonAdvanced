from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.45

    def __init__(self, username, followers, engagement_rate):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign):
        return campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type):
        if campaign_type == "HighBudgetCampaign":
            return int((self.followers * self.engagement_rate) * 1.2)
        elif campaign_type == "LowBudgetCampaign":
            return int((self.followers * self.engagement_rate) * 0.9)


