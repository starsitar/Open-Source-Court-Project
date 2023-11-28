from judge import JudgeAgent
from lawyer import LawyerAgent


class PreTrialHearingSimulator:
    def __init__(self, judge_agent, lawyer_agents):
        """
        Initializes the PreTrialHearingSimulator with a judge agent and lawyer agents.
        
        :param judge_agent: An instance of JudgeAgent handling the decision-making.
        :param lawyer_agents: A list of LawyerAgent instances representing the legal parties.
        """
        self.judge_agent = judge_agent
        self.lawyer_agents = lawyer_agents
        self.motions = []

    def submit_motion(self, lawyer_agent, motion_text):
        """
        Allows a lawyer agent to submit a pre-trial motion.

        :param lawyer_agent: The LawyerAgent submitting the motion.
        :param motion_text: The text of the motion being submitted.
        """
        self.motions.append((lawyer_agent, motion_text))

    def review_motions(self):
        """
        The judge agent reviews all submitted motions.
        """
        for lawyer_agent, motion in self.motions:
            print(f"Reviewing motion from {lawyer_agent.name}: {motion}")
            # Simulate the judge's review process
            decision = self.judge_agent.review_motion(motion)
            print(f"Judge's decision on the motion: {decision}")

    def conduct_hearing(self):
        """
        Conducts the pre-trial hearing where motions are discussed and ruled on.
        """
        if not self.motions:
            print("No motions to review.")
            return

        print("Pre-Trial Hearing Started")
        self.review_motions()
        print("Pre-Trial Hearing Concluded")

# Example usage
# judge = JudgeAgent(openai_api_key="your-openai-api-key")
# lawyer1 = LawyerAgent(name="Lawyer 1", openai_api_key="your-openai-api-key")
# lawyer2 = LawyerAgent(name="Lawyer 2", openai_api_key="your-openai-api-key")
# simulator = PreTrialHearingSimulator(judge, [lawyer1, lawyer2])
# simulator.submit_motion(lawyer1, "Motion to dismiss due to lack of evidence")
# simulator.conduct_hearing()
