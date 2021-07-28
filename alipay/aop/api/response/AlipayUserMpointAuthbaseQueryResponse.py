#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserMpointAuthbaseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserMpointAuthbaseQueryResponse, self).__init__()
        self._balance = None
        self._grade = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserMpointAuthbaseQueryResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
        if 'grade' in response:
            self.grade = response['grade']
