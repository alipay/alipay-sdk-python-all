#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BatchDepositOrderOpenResult import BatchDepositOrderOpenResult


class AlipayCommerceEcRecyclinginvoiceBatchdepositQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceBatchdepositQueryResponse, self).__init__()
        self._batch_deposit_id = None
        self._deposit_account_no = None
        self._deposit_amount = None
        self._deposit_bank_name = None
        self._deposit_count = None
        self._deposit_status = None
        self._fail_reason = None
        self._order_list = None
        self._pay_url = None

    @property
    def batch_deposit_id(self):
        return self._batch_deposit_id

    @batch_deposit_id.setter
    def batch_deposit_id(self, value):
        self._batch_deposit_id = value
    @property
    def deposit_account_no(self):
        return self._deposit_account_no

    @deposit_account_no.setter
    def deposit_account_no(self, value):
        self._deposit_account_no = value
    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def deposit_bank_name(self):
        return self._deposit_bank_name

    @deposit_bank_name.setter
    def deposit_bank_name(self, value):
        self._deposit_bank_name = value
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
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, BatchDepositOrderOpenResult):
                    self._order_list.append(i)
                else:
                    self._order_list.append(BatchDepositOrderOpenResult.from_alipay_dict(i))
    @property
    def pay_url(self):
        return self._pay_url

    @pay_url.setter
    def pay_url(self, value):
        self._pay_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceBatchdepositQueryResponse, self).parse_response_content(response_content)
        if 'batch_deposit_id' in response:
            self.batch_deposit_id = response['batch_deposit_id']
        if 'deposit_account_no' in response:
            self.deposit_account_no = response['deposit_account_no']
        if 'deposit_amount' in response:
            self.deposit_amount = response['deposit_amount']
        if 'deposit_bank_name' in response:
            self.deposit_bank_name = response['deposit_bank_name']
        if 'deposit_count' in response:
            self.deposit_count = response['deposit_count']
        if 'deposit_status' in response:
            self.deposit_status = response['deposit_status']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'order_list' in response:
            self.order_list = response['order_list']
        if 'pay_url' in response:
            self.pay_url = response['pay_url']
