#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodInstAuthConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodInstAuthConsultResponse, self).__init__()
        self._auth = None
        self._consult_result = None
        self._trace_id = None

    @property
    def auth(self):
        return self._auth

    @auth.setter
    def auth(self, value):
        self._auth = value
    @property
    def consult_result(self):
        return self._consult_result

    @consult_result.setter
    def consult_result(self, value):
        self._consult_result = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodInstAuthConsultResponse, self).parse_response_content(response_content)
        if 'auth' in response:
            self.auth = response['auth']
        if 'consult_result' in response:
            self.consult_result = response['consult_result']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
