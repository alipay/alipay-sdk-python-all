#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeRepaybillOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeRepaybillOrderCreateResponse, self).__init__()
        self._bill_no = None
        self._cashier_order_id = None
        self._repay_fund_order_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def cashier_order_id(self):
        return self._cashier_order_id

    @cashier_order_id.setter
    def cashier_order_id(self, value):
        self._cashier_order_id = value
    @property
    def repay_fund_order_no(self):
        return self._repay_fund_order_no

    @repay_fund_order_no.setter
    def repay_fund_order_no(self, value):
        self._repay_fund_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeRepaybillOrderCreateResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'cashier_order_id' in response:
            self.cashier_order_id = response['cashier_order_id']
        if 'repay_fund_order_no' in response:
            self.repay_fund_order_no = response['repay_fund_order_no']
