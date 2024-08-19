#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BotAnswer import BotAnswer


class AlipayEbppIndustryBotSessionConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryBotSessionConsultResponse, self).__init__()
        self._answer = None
        self._chat_id = None
        self._session_id = None

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        if isinstance(value, BotAnswer):
            self._answer = value
        else:
            self._answer = BotAnswer.from_alipay_dict(value)
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryBotSessionConsultResponse, self).parse_response_content(response_content)
        if 'answer' in response:
            self.answer = response['answer']
        if 'chat_id' in response:
            self.chat_id = response['chat_id']
        if 'session_id' in response:
            self.session_id = response['session_id']
