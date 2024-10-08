#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiAgentServiceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiAgentServiceQueryResponse, self).__init__()
        self._answer = None
        self._answer_end = None
        self._message_id = None

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        self._answer = value
    @property
    def answer_end(self):
        return self._answer_end

    @answer_end.setter
    def answer_end(self, value):
        self._answer_end = value
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiAgentServiceQueryResponse, self).parse_response_content(response_content)
        if 'answer' in response:
            self.answer = response['answer']
        if 'answer_end' in response:
            self.answer_end = response['answer_end']
        if 'message_id' in response:
            self.message_id = response['message_id']
