#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerCreditinfoAuthawardQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerCreditinfoAuthawardQueryResponse, self).__init__()
        self._auth = None
        self._award = None
        self._send_award = None

    @property
    def auth(self):
        return self._auth

    @auth.setter
    def auth(self, value):
        self._auth = value
    @property
    def award(self):
        return self._award

    @award.setter
    def award(self, value):
        self._award = value
    @property
    def send_award(self):
        return self._send_award

    @send_award.setter
    def send_award(self, value):
        self._send_award = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerCreditinfoAuthawardQueryResponse, self).parse_response_content(response_content)
        if 'auth' in response:
            self.auth = response['auth']
        if 'award' in response:
            self.award = response['award']
        if 'send_award' in response:
            self.send_award = response['send_award']
