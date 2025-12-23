from taskManagementService import TaskManagementService
from datetime import date
from priorityEnum import PriorityLevel


app = TaskManagementService()

mgmt_service = app.get_service()
print(mgmt_service)

tl1 = mgmt_service.create_task_list("enhancements")
tl2 = mgmt_service.create_task_list("bug_fixes")

sam = mgmt_service.create_user("sam")
cory = mgmt_service.create_user("cory")
jake = mgmt_service.create_user("jake")
tom = mgmt_service.create_user("tom")

t1 = mgmt_service.create_task("Enhancement task", "Launch new feature",
                             date.today().replace(day=date.today().day + 2), PriorityLevel.LOW.value,
                             sam)

t2 = mgmt_service.create_task("Bug fix task", "temp fix for new feature",
                             date.today().replace(day=date.today().day + 5), PriorityLevel.MEDIUM.value,
                             cory)

t3 = mgmt_service.create_task("Expand feature task", "add new feature",
                             date.today().replace(day=date.today().day + 1), PriorityLevel.HIGH.value,
                             tom)

tl1.add_task(t1)
tl1.add_task(t3)
tl2.add_task(t2)

t1.assign_user(jake)
t1.start_progress()
print(t1.get_state())
t1.complete_task()
print(t1.get_state())

t2.start_progress()




