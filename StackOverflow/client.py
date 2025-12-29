from stackOverflowService import StackOverflowService
from tag import Tag
from searchStrategy import KeywordBasedSearch, UserBasedSearch, TagBasedSearch

service = StackOverflowService()


dek = service.create_user("dek", "dek@gmail.com")
jake = service.create_user("jake", "jake@gmail.com")
tim = service.create_user("tim", "tim@gmail.com")
ben = service.create_user("ben", "ben@gmail.com")
perry = service.create_user("perry", "perry@gmail.com")

question1 = service.post_question("How to install python on your machine", dek, Tag.PYTHON.value)
question2 = service.post_question("is there a garbage collector in java?", jake, Tag.JAVA.value)
question3 = service.post_question("lld vs hld", dek, Tag.SYSTEM_DESIGN.value)
question4 = service.post_question("what is __init__", tim, Tag.PYTHON.value)
question5 = service.post_question("how do collect garbage in java", tim, Tag.JAVA.value)


print(question1)
print(question2)
print(question3)
print(question4)

ans1 = service.answer_question(question3, jake, "lld is writing classes and hld is explaining concepts")
ans2 = service.answer_question(question3, tim, "lld is hard and hld is harder")
ans3 = service.answer_question(question3, perry, "do more hld than lld")
ans4 = service.answer_question(question1, perry, "Just goto the official python page and follow the steps")

com1 = service.comment("very precise", ben, ans3)

# vote1 = service.upvote(ben, question1)
# vote2 = service.upvote(tim, question2)
# vote31 = service.upvote(ben, question1)
# vote3 = service.downvote(perry, question2)
# vote4 = service.downvote(ben, ans1)
# vote4 = service.downvote(tim, ans1)
# vote4 = service.vote(ben, ans2)
# vote4 = service.vote(ben, ans2)
# vote4 = service.vote(ben, ans2)
# vote4 = service.vote(ben, ans2)
# vote4 = service.vote(ben, ans2)
# vote4 = service.vote(ben, ans2)

# dek_score = service.user_service.get_score(dek)
# tim_Score = service.user_service.get_score(tim)
# jake_Score = service.user_service.get_score(jake)
# ben_score = service.user_service.get_score(ben)

# print(dek_score)
# print(tim_Score)
# print(jake_Score)
# print(ben_score)


# results = service.search(Tag.PYTHON.value, TagBasedSearch())
# for question in results:
#     print(question.get_content)