#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodPrepaymentApplyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodPrepaymentApplyResponse, self).__init__()
        self._accept_repay = None
        self._biz_type = None
        self._fail_reason = None
        self._prepayment_amt = None
        self._prepayment_apply_no = None
        self._prepayment_int_amt = None
        self._prepayment_pen_amt = None
        self._prepayment_prin_amt = None
        self._retry = None
        self._trace_id = None
        self._trade_status = None

    @property
    def accept_repay(self):
        return self._accept_repay

    @accept_repay.setter
    def accept_repay(self, value):
        self._accept_repay = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def prepayment_amt(self):
        return self._prepayment_amt

    @prepayment_amt.setter
    def prepayment_amt(self, value):
        self._prepayment_amt = value
    @property
    def prepayment_apply_no(self):
        return self._prepayment_apply_no

    @prepayment_apply_no.setter
    def prepayment_apply_no(self, value):
        self._prepayment_apply_no = value
    @property
    def prepayment_int_amt(self):
        return self._prepayment_int_amt

    @prepayment_int_amt.setter
    def prepayment_int_amt(self, value):
        self._prepayment_int_amt = value
    @property
    def prepayment_pen_amt(self):
        return self._prepayment_pen_amt

    @prepayment_pen_amt.setter
    def prepayment_pen_amt(self, value):
        self._prepayment_pen_amt = value
    @property
    def prepayment_prin_amt(self):
        return self._prepayment_prin_amt

    @prepayment_prin_amt.setter
    def prepayment_prin_amt(self, value):
        self._prepayment_prin_amt = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodPrepaymentApplyResponse, self).parse_response_content(response_content)
        if 'accept_repay' in response:
            self.accept_repay = response['accept_repay']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'prepayment_amt' in response:
            self.prepayment_amt = response['prepayment_amt']
        if 'prepayment_apply_no' in response:
            self.prepayment_apply_no = response['prepayment_apply_no']
        if 'prepayment_int_amt' in response:
            self.prepayment_int_amt = response['prepayment_int_amt']
        if 'prepayment_pen_amt' in response:
            self.prepayment_pen_amt = response['prepayment_pen_amt']
        if 'prepayment_prin_amt' in response:
            self.prepayment_prin_amt = response['prepayment_prin_amt']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
