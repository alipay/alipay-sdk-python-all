#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserTaxRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserTaxRefundResponse, self).__init__()
        self._order_id = None
        self._pay_fund_order_id = None
        self._trans_date = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def pay_fund_order_id(self):
        return self._pay_fund_order_id

    @pay_fund_order_id.setter
    def pay_fund_order_id(self, value):
        self._pay_fund_order_id = value
    @property
    def trans_date(self):
        return self._trans_date

    @trans_date.setter
    def trans_date(self, value):
        self._trans_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserTaxRefundResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'pay_fund_order_id' in response:
            self.pay_fund_order_id = response['pay_fund_order_id']
        if 'trans_date' in response:
            self.trans_date = response['trans_date']
