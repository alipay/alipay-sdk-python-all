#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainArAdmitQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainArAdmitQueryResponse, self).__init__()
        self._admit = None
        self._context = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainArAdmitQueryResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'context' in response:
            self.context = response['context']
