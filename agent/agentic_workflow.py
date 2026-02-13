from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessageState, END,START
from langgraph.prebuilt import ToolNode, tools_condition

class GraphBuilder():
    def __init__(self):
        self.tools = [
            #Weather
        ]
        self.SYSTEM_PROMPT = SYSTEM_PROMPT


    def agent_function(self, state: MessageState):
        "Main agent function that processes the input and generates a response. This is where the core logic of the agent will be implemented."
        user_query = state['messages']
        imput_question = {self.SYSTEM_PROMPT} + user_query
        response = self.llm_with_tools(imput_question)
        return {"response": response}


    def build_graph(self):
        graph_builder = StateGraph(MessageState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools = self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edge("agent", "tools", tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent", END)


        self.graph = graph_builder.compile()
        return self.graph 
    

    def __call__(self):
        return self.build_graph()