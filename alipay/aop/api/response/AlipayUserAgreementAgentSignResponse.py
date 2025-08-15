#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementAgentSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementAgentSignResponse, self).__init__()
        self._orderStr = None

    @property
    def orderStr(self):
        return self._orderStr

    @orderStr.setter
    def orderStr(self, value):
        self._orderStr = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementAgentSignResponse, self).parse_response_content(response_content)
        if 'orderStr' in response:
            self.orderStr = response['orderStr']
