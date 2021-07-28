#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeOrderAggregateRefundResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeOrderAggregateRefundResponse, self).__init__()
        self._gmt_refund_time = None
        self._order_no = None
        self._order_status = None
        self._out_order_no = None
        self._out_refund_no = None
        self._refund_amount = None
        self._refund_buyer_amount = None
        self._refund_discount_amount = None
        self._refund_mdiscount_amount = None
        self._refund_order_id = None
        self._refund_real_amount = None
        self._trade_no = None

    @property
    def gmt_refund_time(self):
        return self._gmt_refund_time

    @gmt_refund_time.setter
    def gmt_refund_time(self, value):
        self._gmt_refund_time = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_buyer_amount(self):
        return self._refund_buyer_amount

    @refund_buyer_amount.setter
    def refund_buyer_amount(self, value):
        self._refund_buyer_amount = value
    @property
    def refund_discount_amount(self):
        return self._refund_discount_amount

    @refund_discount_amount.setter
    def refund_discount_amount(self, value):
        self._refund_discount_amount = value
    @property
    def refund_mdiscount_amount(self):
        return self._refund_mdiscount_amount

    @refund_mdiscount_amount.setter
    def refund_mdiscount_amount(self, value):
        self._refund_mdiscount_amount = value
    @property
    def refund_order_id(self):
        return self._refund_order_id

    @refund_order_id.setter
    def refund_order_id(self, value):
        self._refund_order_id = value
    @property
    def refund_real_amount(self):
        return self._refund_real_amount

    @refund_real_amount.setter
    def refund_real_amount(self, value):
        self._refund_real_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeOrderAggregateRefundResponse, self).parse_response_content(response_content)
        if 'gmt_refund_time' in response:
            self.gmt_refund_time = response['gmt_refund_time']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'out_refund_no' in response:
            self.out_refund_no = response['out_refund_no']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_buyer_amount' in response:
            self.refund_buyer_amount = response['refund_buyer_amount']
        if 'refund_discount_amount' in response:
            self.refund_discount_amount = response['refund_discount_amount']
        if 'refund_mdiscount_amount' in response:
            self.refund_mdiscount_amount = response['refund_mdiscount_amount']
        if 'refund_order_id' in response:
            self.refund_order_id = response['refund_order_id']
        if 'refund_real_amount' in response:
            self.refund_real_amount = response['refund_real_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
