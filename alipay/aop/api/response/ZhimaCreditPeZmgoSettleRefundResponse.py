#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoSettleRefundResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoSettleRefundResponse, self).__init__()
        self._fail_reason = None
        self._out_request_no = None
        self._refund_amount = None
        self._refund_opt_no = None
        self._retry = None
        self._withhold_plan_no = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_opt_no(self):
        return self._refund_opt_no

    @refund_opt_no.setter
    def refund_opt_no(self, value):
        self._refund_opt_no = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def withhold_plan_no(self):
        return self._withhold_plan_no

    @withhold_plan_no.setter
    def withhold_plan_no(self, value):
        self._withhold_plan_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoSettleRefundResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_opt_no' in response:
            self.refund_opt_no = response['refund_opt_no']
        if 'retry' in response:
            self.retry = response['retry']
        if 'withhold_plan_no' in response:
            self.withhold_plan_no = response['withhold_plan_no']
