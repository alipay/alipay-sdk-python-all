#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RobotAnswer import RobotAnswer


class AlipayIserviceCcmRobotSessionConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmRobotSessionConsultResponse, self).__init__()
        self._answer = None
        self._answer_type = None
        self._chat_uuid = None
        self._session_id = None

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        if isinstance(value, RobotAnswer):
            self._answer = value
        else:
            self._answer = RobotAnswer.from_alipay_dict(value)
    @property
    def answer_type(self):
        return self._answer_type

    @answer_type.setter
    def answer_type(self, value):
        self._answer_type = value
    @property
    def chat_uuid(self):
        return self._chat_uuid

    @chat_uuid.setter
    def chat_uuid(self, value):
        self._chat_uuid = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmRobotSessionConsultResponse, self).parse_response_content(response_content)
        if 'answer' in response:
            self.answer = response['answer']
        if 'answer_type' in response:
            self.answer_type = response['answer_type']
        if 'chat_uuid' in response:
            self.chat_uuid = response['chat_uuid']
        if 'session_id' in response:
            self.session_id = response['session_id']
