from graph import graph
initial_state = {
    "message": "Hello LangGraph",
    "step": 0,
}
result = graph.invoke(initial_state )
print("\n")
print("Workflow Completed Successfully")
print(result)