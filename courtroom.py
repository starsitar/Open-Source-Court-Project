# courtroom.py
from judge import JudgeAgent
from lawyer import LawyerAgent
import time

from judge_agent import JudgeAgent
from lawyer_agent import LawyerAgent
from legal_database import LegalDatabase
from evidence_processing import EvidenceProcessing
from user_interface import UserInterface

class Courtroom:
    def __init__(self):
        self.legal_database = LegalDatabase()
        self.evidence_processing = EvidenceProcessing()
        self.judge_agent = JudgeAgent(self.legal_database)
        self.prosecution_agent = LawyerAgent(self.legal_database, "Prosecution")
        self.defense_agent = LawyerAgent(self.legal_database, "Defense")
        self.user_interface = UserInterface()

    def start_trial(self):
        # Simulate the trial process
        print("Trial started")

        # Example flow of the trial
        self.present_cases()
        self.judge_agent.make_decision()

        print("Trial concluded")

    def present_cases(self):
        # Prosecution and Defense present their cases
        prosecution_case = self.prosecution_agent.prepare_case()
        defense_case = self.defense_agent.prepare_case()

        # Display cases in the user interface
        self.user_interface.display_case(prosecution_case)
        self.user_interface.display_case(defense_case)

        # Judge reviews the cases
        self.judge_agent.review_case(prosecution_case, defense_case)

# Example Usage
# courtroom = Courtroom()
# courtroom.start_trial()
