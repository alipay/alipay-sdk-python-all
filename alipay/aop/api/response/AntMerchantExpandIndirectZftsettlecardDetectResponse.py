#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectZftsettlecardDetectResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectZftsettlecardDetectResponse, self).__init__()
        self._consistent = None
        self._inconsistency_reason = None

    @property
    def consistent(self):
        return self._consistent

    @consistent.setter
    def consistent(self, value):
        self._consistent = value
    @property
    def inconsistency_reason(self):
        return self._inconsistency_reason

    @inconsistency_reason.setter
    def inconsistency_reason(self, value):
        self._inconsistency_reason = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectZftsettlecardDetectResponse, self).parse_response_content(response_content)
        if 'consistent' in response:
            self.consistent = response['consistent']
        if 'inconsistency_reason' in response:
            self.inconsistency_reason = response['inconsistency_reason']
