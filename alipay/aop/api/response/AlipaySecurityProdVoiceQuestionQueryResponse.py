#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdVoiceQuestionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdVoiceQuestionQueryResponse, self).__init__()
        self._question_result = None

    @property
    def question_result(self):
        return self._question_result

    @question_result.setter
    def question_result(self, value):
        self._question_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdVoiceQuestionQueryResponse, self).parse_response_content(response_content)
        if 'question_result' in response:
            self.question_result = response['question_result']
