#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SaasTradeFundBill import SaasTradeFundBill


class AlipayTradeSaasOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasOrderRefundResponse, self).__init__()
        self._fund_change = None
        self._gmt_refund_pay = None
        self._out_request_no = None
        self._out_trade_no = None
        self._refund_detail_item_list = None
        self._refund_fee = None
        self._trade_no = None

    @property
    def fund_change(self):
        return self._fund_change

    @fund_change.setter
    def fund_change(self, value):
        self._fund_change = value
    @property
    def gmt_refund_pay(self):
        return self._gmt_refund_pay

    @gmt_refund_pay.setter
    def gmt_refund_pay(self, value):
        self._gmt_refund_pay = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def refund_detail_item_list(self):
        return self._refund_detail_item_list

    @refund_detail_item_list.setter
    def refund_detail_item_list(self, value):
        if isinstance(value, list):
            self._refund_detail_item_list = list()
            for i in value:
                if isinstance(i, SaasTradeFundBill):
                    self._refund_detail_item_list.append(i)
                else:
                    self._refund_detail_item_list.append(SaasTradeFundBill.from_alipay_dict(i))
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasOrderRefundResponse, self).parse_response_content(response_content)
        if 'fund_change' in response:
            self.fund_change = response['fund_change']
        if 'gmt_refund_pay' in response:
            self.gmt_refund_pay = response['gmt_refund_pay']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'refund_detail_item_list' in response:
            self.refund_detail_item_list = response['refund_detail_item_list']
        if 'refund_fee' in response:
            self.refund_fee = response['refund_fee']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
