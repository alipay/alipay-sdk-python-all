#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantPayforprivilegeMemberremainingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantPayforprivilegeMemberremainingQueryResponse, self).__init__()
        self._unused_benefit = None
        self._unused_principal = None

    @property
    def unused_benefit(self):
        return self._unused_benefit

    @unused_benefit.setter
    def unused_benefit(self, value):
        self._unused_benefit = value
    @property
    def unused_principal(self):
        return self._unused_principal

    @unused_principal.setter
    def unused_principal(self, value):
        self._unused_principal = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantPayforprivilegeMemberremainingQueryResponse, self).parse_response_content(response_content)
        if 'unused_benefit' in response:
            self.unused_benefit = response['unused_benefit']
        if 'unused_principal' in response:
            self.unused_principal = response['unused_principal']
