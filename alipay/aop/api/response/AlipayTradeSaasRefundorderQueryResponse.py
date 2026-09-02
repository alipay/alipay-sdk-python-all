#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SaasTradeFundBill import SaasTradeFundBill


class AlipayTradeSaasRefundorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasRefundorderQueryResponse, self).__init__()
        self._gmt_refund_pay = None
        self._out_request_no = None
        self._out_trade_no = None
        self._refund_amount = None
        self._refund_detail_item_list = None
        self._refund_reason = None
        self._refund_status = None
        self._send_back_fee = None
        self._total_amount = None
        self._trade_no = None

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
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
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
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def send_back_fee(self):
        return self._send_back_fee

    @send_back_fee.setter
    def send_back_fee(self, value):
        self._send_back_fee = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasRefundorderQueryResponse, self).parse_response_content(response_content)
        if 'gmt_refund_pay' in response:
            self.gmt_refund_pay = response['gmt_refund_pay']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_detail_item_list' in response:
            self.refund_detail_item_list = response['refund_detail_item_list']
        if 'refund_reason' in response:
            self.refund_reason = response['refund_reason']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
        if 'send_back_fee' in response:
            self.send_back_fee = response['send_back_fee']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
