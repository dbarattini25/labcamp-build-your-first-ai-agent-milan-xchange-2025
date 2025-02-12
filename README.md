# 💻 LABCAMP - Build your first AI Agent

Welcome! 🚀

In this labcamp, you will learn the basic concepts of AI agents and how to build your first AI agent using [LangGraph](https://www.langchain.com/langgraph).
This repository contains the source code for the three labs that we will be working on during the labcamp. Each lab is defined in a Jupyter notebook with the necessary instructions and code snippets to guide you through the process of building your first AI agent.

This roadmap of this labcamp is as follows:

- 17:30 - 18:45: Introduction to AI agents
- 18:45 - 19:00: Break
- 19:00 - 20:00: Hands-On - Build your first AI agent

## Pre-requisites

Before we start, make sure you have the following prerequisites installed on your machine:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python](https://www.python.org/downloads/)

**N.B.**: During the labcamp, we will provide you with an API key to access the OpenAI API. The API key should be stored in a file named `.env` in the root directory of the project. See the `.env.example` file for an example of how to store the API key.

### Setup the environment:

#### 1. Create a new [python virtual environment](https://docs.python.org/3/tutorial/venv.html) in the project directory.

For Linux/Mac users:

```bash
python -m venv .venv
source .venv/bin/activate
```

For Windows users:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

You can check if the virtual environment is activated by looking at the terminal prompt. If the virtual environment is activated, you should see the name of the virtual environment in the terminal prompt (e.g., `(.venv)`).

#### 2. After activating the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

**N.B.**: Make sure that the virtual environment is activated in your current terminal session before running the above command.

#### 3. Install the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions for VSCode

#### 4. Open the project folder in VSCode and open the notebook `0 - Environment Test.ipynb`.

#### 5. Check (in the top right corner) if the kernel is set to the virtual environment you created in the previous step. If not, change the kernel to the virtual environment.

#### 6. Run the first cell of the notebook `0 - Environment Test.ipynb` to test the setup.

If you need help or have any questions, feel free to reach out to us. We are here to help you! 🤗

Good luck and have fun! 🎉

## 🔗 Some useful links

- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_create-or-open-a-jupyter-notebook)
- [More on LLM agents](https://www.promptingguide.ai/it/research/llm-agents)
- [More on agents reasoning](https://www.promptingguide.ai/it/techniques/react)
- [More on LangGraph](https://www.langchain.com/langgraph)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)