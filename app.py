import prefect
from prefect import task, Flow, Parameter
from prefect.schedules import clocks, Schedule


@task
def hello_world():
    print("Hello, World!")


clock = clocks.CronClock("0 0 * * *")
schedule = Schedule(clocks=[clock])
with Flow("Star GitHub Repositories", schedule=schedule) as flow:
    hello_world()


flow.register(project_name="SOME PROJECT")
# flow.run()
