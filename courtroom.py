import os
import time
import lawyer
import judge

class Courtroom:
    def __init__(self, openai_api_key, log_file_path, aspects):
        self.log_file_path = log_file_path
        self.llm = OpenAI(api_key=openai_api_key)
        self.judge = JudgeAgent(llm=self.llm)
        self.lawyers = [LawyerAgent(name=f"Lawyer {i+1}", llm=self.llm) for i in range(2)]
        self.aspects = aspects

    def write_to_log(self, text):
        with open(self.log_file_path, 'a') as file:
            file.write(text + "\n")

    def start_proceedings(self):
        self.write_to_log("Court is now in session.")
        for aspect in self.aspects:
            self.write_to_log(f"Discussion on aspect: {aspect}")
            round_arguments = []
            for lawyer in self.lawyers:
                argument = lawyer.present_argument(aspect)
                round_arguments.append(argument)
                self.write_to_log(argument)
                time.sleep(1)  # Simulate time for presenting the argument

            judge_comment = self.judge.consider_arguments(round_arguments)
            self.write_to_log(judge_comment)

        final_decision = self.judge.make_final_decision()
        self.write_to_log(final_decision)
        self.write_to_log("Court is adjourned.")

# Usage
aspects_of_case = ["Liability", "Damages", "Compliance"]
courtroom = Courtroom(openai_api_key='your-openai-api-key', log_file_path='path/to/court_transcript.txt', aspects=aspects_of_case)
courtroom.start_proceedings()
