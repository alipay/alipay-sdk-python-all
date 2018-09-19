#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppBillRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppBillRefundResponse, self).__init__()
        self._alipay_bill_no = None
        self._extend_field = None
        self._out_order_no = None
        self._result = None

    @property
    def alipay_bill_no(self):
        return self._alipay_bill_no

    @alipay_bill_no.setter
    def alipay_bill_no(self, value):
        self._alipay_bill_no = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppBillRefundResponse, self).parse_response_content(response_content)
        if 'alipay_bill_no' in response:
            self.alipay_bill_no = response['alipay_bill_no']
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'result' in response:
            self.result = response['result']
