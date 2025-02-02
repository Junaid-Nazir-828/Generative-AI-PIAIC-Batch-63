### Crew AI

Create project
```
crewai create flow *project_name*
```

scripts are placed in src, just like nextjs (80% code is in src)

install required dependencies and run the project

```
uv run kickoff
```

This will install dependencies specified in pyproject.toml and run the project.

**@start** decorator defines the methods that are supposed to run at the start

When a Flow is started, all the methods decorated with **@start()** are executed in parallel

The **@listen()** decorator is used to mark a method as a listener for the output of another task in the Flow.

**state** is an input to the agent and output from the agent