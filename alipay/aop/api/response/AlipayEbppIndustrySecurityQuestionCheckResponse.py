#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySecurityQuestionCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySecurityQuestionCheckResponse, self).__init__()
        self._safe = None
        self._session_action = None

    @property
    def safe(self):
        return self._safe

    @safe.setter
    def safe(self, value):
        self._safe = value
    @property
    def session_action(self):
        return self._session_action

    @session_action.setter
    def session_action(self, value):
        self._session_action = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySecurityQuestionCheckResponse, self).parse_response_content(response_content)
        if 'safe' in response:
            self.safe = response['safe']
        if 'session_action' in response:
            self.session_action = response['session_action']
