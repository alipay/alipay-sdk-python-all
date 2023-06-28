#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceAntassistantLlmConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceAntassistantLlmConsultResponse, self).__init__()
        self._chat_id = None
        self._response = None
        self._session_id = None

    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceAntassistantLlmConsultResponse, self).parse_response_content(response_content)
        if 'chat_id' in response:
            self.chat_id = response['chat_id']
        if 'response' in response:
            self.response = response['response']
        if 'session_id' in response:
            self.session_id = response['session_id']
