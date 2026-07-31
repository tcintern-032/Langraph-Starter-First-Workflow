# LangGraph Starter First Workflow

A beginner-friendly project demonstrating the fundamentals of LangGraph.
## Overview
This project introduces the core concepts of LangGraph by creating a simple workflow consisting of three connected nodes.
The workflow demonstrates:
- Nodes
- Edges
- Shared State
- Workflow Execution
- State Updates
## Technologies Used
- Python 3.11+
- LangGraph
- LangChain Core
## Project Structure

```
langgraph Starter-First-workflow
│
├── app.py
├── graph.py
├── state.py
├── requirements.txt
├── README.md
└── screenshots
```
## Run the Project

```bash
python app.py
```
## Workflow

```
Start
   │
   ▼
Process
   │
   ▼
End
```

---

## Nodes
### Node 1

- Receives the initial state
- Updates the message
- Increments the step counter

### Node 2

- Receives the updated state
- Processes the data
- Updates the state again

### Node 3

- Receives the processed state
- Finalizes the workflow
- Returns the completed state

---

## State

The workflow shares the following state between all nodes.

```python
{
    "message": str,
    "step": int
}
```

---

## Example Output

```
Node 1 : Start
Incoming State:
{'message': 'Hello LangGraph', 'step': 0}

Updated State:
{'message': 'Hello LangGraph -> Started', 'step': 1}

Node 2 : Processing

Updated State:
{'message': 'Hello LangGraph -> Started -> Processing', 'step': 2}

Node 3 : End

Final State:
{'message': 'Hello LangGraph -> Started -> Processing -> Finished', 'step': 3}

Workflow Completed Successfully
```

---

## LangGraph Concepts Demonstrated

- StateGraph
- Nodes
- Edges
- State
- Workflow Execution
- Graph Compilation

---

## Learning Objectives

- Understand LangGraph architecture
- Learn how state flows between nodes
- Build a basic workflow
- Understand graph execution

---

## Future Improvements

- Conditional Edges
- AI Model Integration
- Memory
- Human-in-the-loop
- Multi-Agent Workflows

---

## Author
**Muhammad Zeeshan**
