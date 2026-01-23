#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMerchantcardRedeemRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardRedeemRefundResponse, self).__init__()
        self._actual_refund_amount = None
        self._deduction_order_id = None
        self._original_deduction_order_id = None
        self._refund_remark = None
        self._refund_status = None
        self._refund_time = None
        self._trade_no = None

    @property
    def actual_refund_amount(self):
        return self._actual_refund_amount

    @actual_refund_amount.setter
    def actual_refund_amount(self, value):
        self._actual_refund_amount = value
    @property
    def deduction_order_id(self):
        return self._deduction_order_id

    @deduction_order_id.setter
    def deduction_order_id(self, value):
        self._deduction_order_id = value
    @property
    def original_deduction_order_id(self):
        return self._original_deduction_order_id

    @original_deduction_order_id.setter
    def original_deduction_order_id(self, value):
        self._original_deduction_order_id = value
    @property
    def refund_remark(self):
        return self._refund_remark

    @refund_remark.setter
    def refund_remark(self, value):
        self._refund_remark = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardRedeemRefundResponse, self).parse_response_content(response_content)
        if 'actual_refund_amount' in response:
            self.actual_refund_amount = response['actual_refund_amount']
        if 'deduction_order_id' in response:
            self.deduction_order_id = response['deduction_order_id']
        if 'original_deduction_order_id' in response:
            self.original_deduction_order_id = response['original_deduction_order_id']
        if 'refund_remark' in response:
            self.refund_remark = response['refund_remark']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
        if 'refund_time' in response:
            self.refund_time = response['refund_time']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
