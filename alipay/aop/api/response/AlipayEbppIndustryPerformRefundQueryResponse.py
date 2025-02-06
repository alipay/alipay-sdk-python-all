#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PerformBill import PerformBill
from alipay.aop.api.domain.PerformRefundQueryRecord import PerformRefundQueryRecord


class AlipayEbppIndustryPerformRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryPerformRefundQueryResponse, self).__init__()
        self._bill_no = None
        self._perform_bill = None
        self._refund_record_list = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def perform_bill(self):
        return self._perform_bill

    @perform_bill.setter
    def perform_bill(self, value):
        if isinstance(value, PerformBill):
            self._perform_bill = value
        else:
            self._perform_bill = PerformBill.from_alipay_dict(value)
    @property
    def refund_record_list(self):
        return self._refund_record_list

    @refund_record_list.setter
    def refund_record_list(self, value):
        if isinstance(value, list):
            self._refund_record_list = list()
            for i in value:
                if isinstance(i, PerformRefundQueryRecord):
                    self._refund_record_list.append(i)
                else:
                    self._refund_record_list.append(PerformRefundQueryRecord.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryPerformRefundQueryResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'perform_bill' in response:
            self.perform_bill = response['perform_bill']
        if 'refund_record_list' in response:
            self.refund_record_list = response['refund_record_list']
