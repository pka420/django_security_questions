from django.contrib.auth import hashers
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_bleach.models import BleachField

from .compat import user_model_label


class SecurityQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    question = BleachField(max_length=150, null=False, blank=False)

    class Meta:
        db_table = "security_questions"

    def __str__(self):
        return f"{self.question}"


class SecurityAnswer(models.Model):
    user = models.ForeignKey(user_model_label, on_delete=models.CASCADE, related_name='user_security_answers', default=1)
    question = models.ForeignKey("SecurityQuestion", verbose_name=_("Security Question"), on_delete=models.CASCADE)
    answer = BleachField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = "security_answer"
        unique_together = ('user', 'question')

    def __str__(self):
        return f"{self.user} - {self.question}"

    def hash_current_answer(self):
        self.set_answer(self.answer)

    def set_answer(self, raw_answer):
        if not bool(getattr(settings, "QUESTIONS_CASE_SENSITIVE", False)):
            raw_answer = raw_answer.upper()
        self.answer = hashers.make_password(raw_answer)

    def check_answer(self, raw_answer):
        if not bool(getattr(settings, "QUESTIONS_CASE_SENSITIVE", False)):
            raw_answer = raw_answer.upper()

        def setter(raw_answer):
            self.set_answer(raw_answer)
            self.save(update_fields=["answer"])
        return hashers.check_password(raw_answer, self.answer, setter)

    def set_unusable_answer(self):
        self.answer = hashers.make_password(None)

    def has_usable_answer(self):
        return hashers.is_password_usable(self.answer)

    def hash_current_answer(self):
        self.set_answer(self.answer)

    def set_answer(self, raw_answer):
        if not bool(getattr(settings, "QUESTIONS_CASE_SENSITIVE", False)):
            raw_answer = raw_answer.upper()
        self.answer = hashers.make_password(raw_answer)

    def check_answer(self, raw_answer):
        if not bool(getattr(settings, "QUESTIONS_CASE_SENSITIVE", False)):
            raw_answer = raw_answer.upper()

    def setter(raw_answer):
        self.set_answer(raw_answer)
        self.save(update_fields=["answer"])
        return hashers.check_password(raw_answer, self.answer, setter)

    def set_unusable_answer(self):
        self.answer = hashers.make_password(None)

    def has_usable_answer(self):
        return hashers.is_password_usable(self.answer)
