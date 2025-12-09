from EventCalendar.entities.user import User
from EventCalendar.entities.participant import Participant
from EventCalendar.entities.event import Event
from EventCalendar.entities.team import Team


current_Day = 0
user1 = User("A", 1, "10:00am", "07:00pm")
user2 = User("B", 2, "09:30am", "05:30pm")
user3 = User("C", 3, "11:30am", "06:30pm")
user4 = User("D", 4, "10:00am", "06:00pm")
user5 = User("E", 5, "11:00am", "07:30pm")
user6 = User("F", 6, "11:00am", "06:30pm")

team1 = Team("T1", 1)
team2 = Team("T2", 2)

team1.add_member(user3)
team1.add_member(user5)

team2.add_member(user2)
team2.add_member(user4)
team2.add_member(user6)

event1 = Event("discussion", 1, "02:00pm", "03:00pm" , 2)
event1.addParticipant(user1)
event1.addParticipant(team1)



event2 = Event("dsm", 1, "02:00pm", "03:00pm" , 2)
event2.addParticipant(user3)


event3 = Event("integration", 0, "03:00pm", "04:00pm" , 2)
event3.addParticipant(team1)
event3.addParticipant(team2)


event4 = Event("CatchUp", 0, "03:00pm", "04:00pm", 1)
event4.addParticipant(user1)
event4.addParticipant(team2)



event5 = Event("Standup", 0, "10:00am", "11:00am", 1)
event5.addParticipant(user1)
event5.addParticipant(user6)

print("\n\n")

print("Final events for each user are as follows: \n")
events1 = user1._events
events2 = user3._events
events3 = user5._events
print("user1 events are as follows: \n")
for event in events1:
    print(event.title)
    print(event.participants)
    print("start_time ", event.start_time, " end_time ", event.end_time, " required ", event.required)

print("\nuser3 events are as follows: \n")
for event in events2:
    print(event.title)
    print(event.participants)
    print("start_time ", event.start_time, " end_time ", event.end_time, " required ", event.required)

print("\nuser5 events are as follows: \n")
for event in events3:
    print(event.title)
    print(event.participants)
    print("start_time ", event.start_time, " end_time ", event.end_time, " required ", event.required)

print("\nuser2 events are as follows : \n")
for event in user2._events:
    print(event.title)
    print(event.participants)
    print("start_time ", event.start_time, " end_time ", event.end_time, " required ", event.required)

print("\nuser4 events are as follows : \n")
for event in user4._events:
    print(event.title)
    print(event.participants)
    print("start_time ", event.start_time, " end_time ", event.end_time, " required ", event.required)

print("\nuser6 events are as follows : \n")
for event in user6._events:
    print(event.title)
    print(event.participants)
    print("start_time ", event.start_time, " end_time ", event.end_time, " required ", event.required)

