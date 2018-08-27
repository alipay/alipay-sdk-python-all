#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpFreedepositOrderriskQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpFreedepositOrderriskQueryResponse, self).__init__()
        self._decision = None
        self._lease_order_no = None
        self._merchant_lease_order_no = None
        self._reject_reason = None

    @property
    def decision(self):
        return self._decision

    @decision.setter
    def decision(self, value):
        self._decision = value
    @property
    def lease_order_no(self):
        return self._lease_order_no

    @lease_order_no.setter
    def lease_order_no(self, value):
        self._lease_order_no = value
    @property
    def merchant_lease_order_no(self):
        return self._merchant_lease_order_no

    @merchant_lease_order_no.setter
    def merchant_lease_order_no(self, value):
        self._merchant_lease_order_no = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpFreedepositOrderriskQueryResponse, self).parse_response_content(response_content)
        if 'decision' in response:
            self.decision = response['decision']
        if 'lease_order_no' in response:
            self.lease_order_no = response['lease_order_no']
        if 'merchant_lease_order_no' in response:
            self.merchant_lease_order_no = response['merchant_lease_order_no']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
