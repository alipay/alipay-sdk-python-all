#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozAuthenticationCustomerFaceverifyMatchResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationCustomerFaceverifyMatchResponse, self).__init__()
        self._attack = None
        self._result = None

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(ZolozAuthenticationCustomerFaceverifyMatchResponse, self).parse_response_content(response_content)
        if 'attack' in response:
            self.attack = response['attack']
        if 'result' in response:
            self.result = response['result']
