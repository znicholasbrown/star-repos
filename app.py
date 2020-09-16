import prefect
from prefect import task, Flow, Parameter
from prefect.schedules import clocks, Schedule
from prefect.environments.storage import GitHub


@task
def hello_world():
    print("Hello, World!")


clock = clocks.CronClock("0 0 * * *")
schedule = Schedule(clocks=[clock])
with Flow("Star GitHub Repositories", schedule=schedule) as flow:
    hello_world()


flow.storage = GitHub(
    repo="znicholasbrown/star-repos",
    path="app.py",
    secrets=["GITHUB_AUTH_TOKEN"],  # Change this to your own GitHub auth token secret
)

flow.register(project_name="SOME PROJECT")
# flow.run()
