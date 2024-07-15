#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GuessQuestion import GuessQuestion


class AlipayCloudCloudpromoAssistantGuessquestionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAssistantGuessquestionQueryResponse, self).__init__()
        self._questions = None

    @property
    def questions(self):
        return self._questions

    @questions.setter
    def questions(self, value):
        if isinstance(value, GuessQuestion):
            self._questions = value
        else:
            self._questions = GuessQuestion.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAssistantGuessquestionQueryResponse, self).parse_response_content(response_content)
        if 'questions' in response:
            self.questions = response['questions']
