# orchestrator/workflow.py

from langgraph.graph import StateGraph

# Define each agent function as a node in LangGraph
# Connect them into a pipeline using .add_edge()
# Compile and run using .compile().invoke(input_state)
