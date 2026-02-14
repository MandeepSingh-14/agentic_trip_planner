from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END,START
from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather_info_tool import WeatherInfoTool 
from tools.place_search_tool import PlaceSearchTool
from tools.expense_calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool 



class GraphBuilder():
    def __init__(self , model_provider: str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm_with_tools = self.model_loader.load_llm()
        self.tools = []
        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = CalculatorTool()
        self.currency_converter_tools = CurrencyConverterTool()

        self.tools.extend([* self.weather_tools.weather_tool_list,
                           * self.place_search_tools.place_search_tool_list,
                           * self.calculator_tools.calculator_tool_list,
                           * self.currency_converter_tools.currency_converter_tool_list
        ])

        self.llm_with_tools = self.llm.bind_tools(tools = self.tools)

        self.graph = None
        self.SYSTEM_PROMPT = SYSTEM_PROMPT


    def agent_function(self, state: MessagesState):
        "Main agent function that processes the input and generates a response. This is where the core logic of the agent will be implemented."
        user_query = state['messages']
        imput_question = {self.SYSTEM_PROMPT} + user_query
        response = self.llm_with_tools(imput_question)
        return {"response": response}


    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
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