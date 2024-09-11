from django.apps import AppConfig

class DjangoSecurityQuestionsConfig(AppConfig):
	name = 'django_security_questions'
	def ready(self):
		from .models import SecurityQuestion, SecurityAnswer
		from .serializers import SecurityQuestionSerializer, SecurityAnswerSerializer
