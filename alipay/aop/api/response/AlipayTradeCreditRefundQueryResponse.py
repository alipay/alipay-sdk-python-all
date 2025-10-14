#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeCreditRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCreditRefundQueryResponse, self).__init__()
        self._credit_biz_order_id = None
        self._gmt_refund = None
        self._order_amount = None
        self._refund_amount = None
        self._trade_no = None

    @property
    def credit_biz_order_id(self):
        return self._credit_biz_order_id

    @credit_biz_order_id.setter
    def credit_biz_order_id(self, value):
        self._credit_biz_order_id = value
    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCreditRefundQueryResponse, self).parse_response_content(response_content)
        if 'credit_biz_order_id' in response:
            self.credit_biz_order_id = response['credit_biz_order_id']
        if 'gmt_refund' in response:
            self.gmt_refund = response['gmt_refund']
        if 'order_amount' in response:
            self.order_amount = response['order_amount']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
