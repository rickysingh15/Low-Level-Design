from topicService import TopicService
from publisherService import PublisherService
from subscriberService import SubscriberService


pub_service = PublisherService()
topic_service = TopicService()
sub_service = SubscriberService()


work = topic_service.create_topic()
personal = topic_service.create_topic()

office = pub_service.create_publisher()
fam = pub_service.create_publisher()

work_related_subscriber = sub_service.create_subscriber()
sub_service.subscribe(work_related_subscriber, work)

family_related_subscriber = sub_service.create_subscriber()
sub_service.subscribe(family_related_subscriber, personal)

office.publish("dsm postponed", work)
office.publish("new dsm time set to 02:00PM", work)
fam.publish("Road trip comming up", personal)
