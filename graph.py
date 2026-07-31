from langgraph.graph import StateGraph, END
from state import WorkflowState
# Node 1
def start_node(state: WorkflowState):
    print("=" * 50)
    print("Node 1 : Start")
    print("Incoming State:", state)

    state["message"] += " -> Started"
    state["step"] += 1

    print("Updated State:", state)
    print("=" * 50)

    return state
# Node 2
def process_node(state: WorkflowState):
    print("=" * 50)
    print("Node 2 : Processing")
    print("Incoming State:", state)

    state["message"] += " -> Processing"
    state["step"] += 1

    print("Updated State:", state)
    print("=" * 50)

    return state
# Node 3
def end_node(state: WorkflowState):
    print("=" * 50)
    print("Node 3 : End")
    print("Incoming State:", state)

    state["message"] += " -> Finished"
    state["step"] += 1

    print("Final State:", state)
    print("=" * 50)

    return state


# Create Graph
workflow = StateGraph(WorkflowState)

# Add Nodes
workflow.add_node("start", start_node)
workflow.add_node("process", process_node)
workflow.add_node("end", end_node)

# Entry Point
workflow.set_entry_point("start")

# Add Edges
workflow.add_edge("start", "process")
workflow.add_edge("process", "end")
workflow.add_edge("end", END)

# Compile
graph = workflow.compile()