# Class 8

**Agenda**

Our main purpose is to get started with crew ai

**Getting Started with uv**

Install uv for package management
```
pip install uv
```
Initialize uv project
```
uv init --package uv_project
```
create virtual environment
```
uv venv
```
make sure to move project scripts below the build-system
```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project.scripts]
uv_project = "uv_project.FILE_NAME:ENTRY_POINT_FUNCTION_NAME"
```
make hello.py file inside src/uv_project/ and write main function and run the project

```
def main():
    print('Hello World!')
```
```
uv run uv_project
```
*Make sure current directory is uv_project*

to sync changes in .toml file
```
uv sync
```

**Getting Started lite llm**

install using litellm
```
uv add litellm
```

**Getting Started Crewai**

Important Concepts in Crewai:
> FLOW, CREW, AGENTS, TASKS

> PROCESSES -> Sequential Processes and Hierarchical Processes

install crewai
```
pip install crewai crewai-tools
```
create crewai project
```
crewai create flow crewai
```