#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserLoginCodeGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserLoginCodeGetResponse, self).__init__()
        self._login_code = None

    @property
    def login_code(self):
        return self._login_code

    @login_code.setter
    def login_code(self, value):
        self._login_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserLoginCodeGetResponse, self).parse_response_content(response_content)
        if 'login_code' in response:
            self.login_code = response['login_code']
