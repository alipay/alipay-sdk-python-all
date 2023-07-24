#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalEcodeOpenQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalEcodeOpenQueryResponse, self).__init__()
        self._login_name = None
        self._open = None

    @property
    def login_name(self):
        return self._login_name

    @login_name.setter
    def login_name(self, value):
        self._login_name = value
    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalEcodeOpenQueryResponse, self).parse_response_content(response_content)
        if 'login_name' in response:
            self.login_name = response['login_name']
        if 'open' in response:
            self.open = response['open']
