#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJobagentSessionInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJobagentSessionInitializeResponse, self).__init__()
        self._session_id = None
        self._welcome_speech = None

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def welcome_speech(self):
        return self._welcome_speech

    @welcome_speech.setter
    def welcome_speech(self, value):
        self._welcome_speech = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJobagentSessionInitializeResponse, self).parse_response_content(response_content)
        if 'session_id' in response:
            self.session_id = response['session_id']
        if 'welcome_speech' in response:
            self.welcome_speech = response['welcome_speech']
