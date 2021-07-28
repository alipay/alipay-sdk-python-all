#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantPayforprivilegeMerchantremainingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantPayforprivilegeMerchantremainingQueryResponse, self).__init__()
        self._unused_benefit = None
        self._unused_principal = None
        self._used_benefit = None
        self._used_principal = None

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
    @property
    def used_benefit(self):
        return self._used_benefit

    @used_benefit.setter
    def used_benefit(self, value):
        self._used_benefit = value
    @property
    def used_principal(self):
        return self._used_principal

    @used_principal.setter
    def used_principal(self, value):
        self._used_principal = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantPayforprivilegeMerchantremainingQueryResponse, self).parse_response_content(response_content)
        if 'unused_benefit' in response:
            self.unused_benefit = response['unused_benefit']
        if 'unused_principal' in response:
            self.unused_principal = response['unused_principal']
        if 'used_benefit' in response:
            self.used_benefit = response['used_benefit']
        if 'used_principal' in response:
            self.used_principal = response['used_principal']
