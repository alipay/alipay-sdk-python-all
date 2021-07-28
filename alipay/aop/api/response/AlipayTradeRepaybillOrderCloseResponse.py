#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeRepaybillOrderCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeRepaybillOrderCloseResponse, self).__init__()
        self._bill_no = None
        self._paid_amount = None
        self._repay_fund_order_no = None
        self._repay_order_status = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        self._paid_amount = value
    @property
    def repay_fund_order_no(self):
        return self._repay_fund_order_no

    @repay_fund_order_no.setter
    def repay_fund_order_no(self, value):
        self._repay_fund_order_no = value
    @property
    def repay_order_status(self):
        return self._repay_order_status

    @repay_order_status.setter
    def repay_order_status(self, value):
        self._repay_order_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeRepaybillOrderCloseResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'paid_amount' in response:
            self.paid_amount = response['paid_amount']
        if 'repay_fund_order_no' in response:
            self.repay_fund_order_no = response['repay_fund_order_no']
        if 'repay_order_status' in response:
            self.repay_order_status = response['repay_order_status']
