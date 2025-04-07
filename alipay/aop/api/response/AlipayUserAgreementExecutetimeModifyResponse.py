#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementExecutetimeModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementExecutetimeModifyResponse, self).__init__()
        self._execute_time = None

    @property
    def execute_time(self):
        return self._execute_time

    @execute_time.setter
    def execute_time(self, value):
        self._execute_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementExecutetimeModifyResponse, self).parse_response_content(response_content)
        if 'execute_time' in response:
            self.execute_time = response['execute_time']
