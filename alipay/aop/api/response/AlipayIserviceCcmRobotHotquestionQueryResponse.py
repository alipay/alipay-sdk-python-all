#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuestionInfo import QuestionInfo


class AlipayIserviceCcmRobotHotquestionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmRobotHotquestionQueryResponse, self).__init__()
        self._questions = None

    @property
    def questions(self):
        return self._questions

    @questions.setter
    def questions(self, value):
        if isinstance(value, list):
            self._questions = list()
            for i in value:
                if isinstance(i, QuestionInfo):
                    self._questions.append(i)
                else:
                    self._questions.append(QuestionInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmRobotHotquestionQueryResponse, self).parse_response_content(response_content)
        if 'questions' in response:
            self.questions = response['questions']
