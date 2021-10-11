#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPayafteruseCreditbizorderOrderResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPayafteruseCreditbizorderOrderResponse, self).__init__()
        self._credit_biz_order_id = None
        self._out_order_no = None

    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPayafteruseCreditbizorderOrderResponse, self).parse_response_content(response_content)
        if 'credit_biz_order_id' in response:
            self.credit_biz_order_id = response['credit_biz_order_id']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
