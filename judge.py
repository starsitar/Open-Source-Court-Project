import openai
from langchain.llms import OpenAI
from langchain.chains import SimpleChain
from langchain.memories import VectorStoreRetrieverMemory
from langchain.processors import LastTurnProcessor

class JudgeAgent:
    def __init__(self, openai_api_key):
        self.llm = OpenAI(api_key=openai_api_key)
        self.chain = SimpleChain(llm=self.llm, preprocessor=LastTurnProcessor())
        self.case_memory = VectorStoreRetrieverMemory(llm=self.llm)

    def consider_arguments(self, arguments):
        # Add all arguments to the judge's memory
        for argument in arguments:
            self.case_memory.add(argument)

        # Simulating the process of considering arguments
        context = "\n".join([entry for entry in self.case_memory.retrieve_recent(len(arguments))])
        decision_prompt = "Given these arguments, what would be a fair and just decision?"
        full_prompt = context + "\n" + decision_prompt

        try:
            decision = self.chain.run_chain(full_prompt)
        except Exception as e:
            print(f"Error in making a decision: {e}")
            decision = "Unable to make a decision due to an error."

        return decision

    def make_final_decision(self):
        # Retrieve all the information from the case
        context = "\n".join([entry for entry in self.case_memory.retrieve_recent(len(self.case_memory))])
        final_decision_prompt = "Considering all the information and arguments, what is the final verdict?"
        full_prompt = context + "\n" + final_decision_prompt

        try:
            final_decision = self.chain.run_chain(full_prompt)
        except Exception as e:
            print(f"Error in making a final decision: {e}")
            final_decision = "Unable to make a final decision due to an error."

        return final_decision

# Example usage
# judge = JudgeAgent(openai_api_key="your-openai-api-key")
# arguments = ["Argument 1 from Lawyer 1", "Argument 2 from Lawyer 2", ...]
# interim_decision = judge.consider_arguments(arguments)
# print(interim_decision)
# final_decision = judge.make_final_decision()
# print(final_decision)
