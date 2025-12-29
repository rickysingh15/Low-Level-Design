
from abc import ABC, abstractmethod
from questionService import QuestionService

class SearchStrategy:

    @abstractmethod
    def search(self, key: str, question_service: QuestionService):
        pass


class KeywordBasedSearch(SearchStrategy):

    def search(self, key: str, question_service: QuestionService):
        print("search called for keyword based search")
        results = []
        questions_dict = question_service.get_all_questions()
        for _id, question in questions_dict.items():
            if key.lower() in question.get_content.lower():
                results.append(question)

        return results

class TagBasedSearch(SearchStrategy):

    def search(self, key: str, question_service: QuestionService):
        print("search called for tag based search")
        results = []
        tags = question_service.get_tag_to_questions_map()
        for v in tags.get(key, None).values():
            results.append(v)
        return results


class UserBasedSearch(SearchStrategy):

    def search(self, key: str, question_service: QuestionService):
        print("search called for user based search")
        results = []
        questions_dict = question_service.get_all_questions()
        for _id, question in questions_dict.items():
            if key.lower() in question.get_user.get_name.lower() or key.lower() in question.get_user.get_email.lower():
                results.append(question)
        return results