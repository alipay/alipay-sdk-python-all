#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayPaysharingprodSharepeerpayApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayPaysharingprodSharepeerpayApplyResponse, self).__init__()
        self._peerpay_order_no = None

    @property
    def peerpay_order_no(self):
        return self._peerpay_order_no

    @peerpay_order_no.setter
    def peerpay_order_no(self, value):
        self._peerpay_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayPaysharingprodSharepeerpayApplyResponse, self).parse_response_content(response_content)
        if 'peerpay_order_no' in response:
            self.peerpay_order_no = response['peerpay_order_no']
