#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceBatchdepositApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceBatchdepositApplyResponse, self).__init__()
        self._batch_deposit_id = None
        self._deposit_amount = None
        self._deposit_count = None
        self._deposit_status = None
        self._fail_reason = None
        self._pay_url = None

    @property
    def batch_deposit_id(self):
        return self._batch_deposit_id

    @batch_deposit_id.setter
    def batch_deposit_id(self, value):
        self._batch_deposit_id = value
    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def deposit_count(self):
        return self._deposit_count

    @deposit_count.setter
    def deposit_count(self, value):
        self._deposit_count = value
    @property
    def deposit_status(self):
        return self._deposit_status

    @deposit_status.setter
    def deposit_status(self, value):
        self._deposit_status = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceBatchdepositApplyResponse, self).parse_response_content(response_content)
        if 'batch_deposit_id' in response:
            self.batch_deposit_id = response['batch_deposit_id']
        if 'deposit_amount' in response:
            self.deposit_amount = response['deposit_amount']
        if 'deposit_count' in response:
            self.deposit_count = response['deposit_count']
        if 'deposit_status' in response:
            self.deposit_status = response['deposit_status']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'pay_url' in response:
            self.pay_url = response['pay_url']
