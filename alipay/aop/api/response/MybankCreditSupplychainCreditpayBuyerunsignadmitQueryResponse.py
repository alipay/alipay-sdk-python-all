#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSupplychainCreditpayBuyerunsignadmitQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainCreditpayBuyerunsignadmitQueryResponse, self).__init__()
        self._admit = None
        self._trace_id = None
        self._unadmit_reason = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def unadmit_reason(self):
        return self._unadmit_reason

    @unadmit_reason.setter
    def unadmit_reason(self, value):
        self._unadmit_reason = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainCreditpayBuyerunsignadmitQueryResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
        if 'unadmit_reason' in response:
            self.unadmit_reason = response['unadmit_reason']
