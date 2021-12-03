#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPayafteruseCreditbizorderFinishResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPayafteruseCreditbizorderFinishResponse, self).__init__()
        self._credit_biz_order_id = None
        self._order_status = None
        self._out_request_no = None

    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPayafteruseCreditbizorderFinishResponse, self).parse_response_content(response_content)
        if 'credit_biz_order_id' in response:
            self.credit_biz_order_id = response['credit_biz_order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
