#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PresetQuesiton import PresetQuesiton


class AlipayCloudCloudpromoAssistantPresetquestionConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAssistantPresetquestionConsultResponse, self).__init__()
        self._answer_content = None
        self._ask_time = None
        self._customer_id = None
        self._request_id = None
        self._session_id = None
        self._suggestion_questions = None

    @property
    def answer_content(self):
        return self._answer_content

    @answer_content.setter
    def answer_content(self, value):
        self._answer_content = value
    @property
    def ask_time(self):
        return self._ask_time

    @ask_time.setter
    def ask_time(self, value):
        self._ask_time = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def suggestion_questions(self):
        return self._suggestion_questions

    @suggestion_questions.setter
    def suggestion_questions(self, value):
        if isinstance(value, list):
            self._suggestion_questions = list()
            for i in value:
                if isinstance(i, PresetQuesiton):
                    self._suggestion_questions.append(i)
                else:
                    self._suggestion_questions.append(PresetQuesiton.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAssistantPresetquestionConsultResponse, self).parse_response_content(response_content)
        if 'answer_content' in response:
            self.answer_content = response['answer_content']
        if 'ask_time' in response:
            self.ask_time = response['ask_time']
        if 'customer_id' in response:
            self.customer_id = response['customer_id']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'session_id' in response:
            self.session_id = response['session_id']
        if 'suggestion_questions' in response:
            self.suggestion_questions = response['suggestion_questions']
