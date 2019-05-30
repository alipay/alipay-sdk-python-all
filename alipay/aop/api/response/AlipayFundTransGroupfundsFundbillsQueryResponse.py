#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupFundBill import GroupFundBill
from alipay.aop.api.domain.GroupFundBill import GroupFundBill


class AlipayFundTransGroupfundsFundbillsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransGroupfundsFundbillsQueryResponse, self).__init__()
        self._batch_status = None
        self._current_fund_bill = None
        self._fund_bills = None
        self._timeout = None

    @property
    def batch_status(self):
        return self._batch_status

    @batch_status.setter
    def batch_status(self, value):
        self._batch_status = value
    @property
    def current_fund_bill(self):
        return self._current_fund_bill

    @current_fund_bill.setter
    def current_fund_bill(self, value):
        if isinstance(value, GroupFundBill):
            self._current_fund_bill = value
        else:
            self._current_fund_bill = GroupFundBill.from_alipay_dict(value)
    @property
    def fund_bills(self):
        return self._fund_bills

    @fund_bills.setter
    def fund_bills(self, value):
        if isinstance(value, list):
            self._fund_bills = list()
            for i in value:
                if isinstance(i, GroupFundBill):
                    self._fund_bills.append(i)
                else:
                    self._fund_bills.append(GroupFundBill.from_alipay_dict(i))
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransGroupfundsFundbillsQueryResponse, self).parse_response_content(response_content)
        if 'batch_status' in response:
            self.batch_status = response['batch_status']
        if 'current_fund_bill' in response:
            self.current_fund_bill = response['current_fund_bill']
        if 'fund_bills' in response:
            self.fund_bills = response['fund_bills']
        if 'timeout' in response:
            self.timeout = response['timeout']
