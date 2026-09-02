#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppleVoucherQueryItem import AppleVoucherQueryItem


class AlipayPcreditHuabeiAppleVoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAppleVoucherQueryResponse, self).__init__()
        self._credit_amount = None
        self._end_date = None
        self._instance_no = None
        self._start_date = None
        self._status = None
        self._vouchers = None

    @property
    def credit_amount(self):
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, value):
        self._credit_amount = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def instance_no(self):
        return self._instance_no

    @instance_no.setter
    def instance_no(self, value):
        self._instance_no = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def vouchers(self):
        return self._vouchers

    @vouchers.setter
    def vouchers(self, value):
        if isinstance(value, list):
            self._vouchers = list()
            for i in value:
                if isinstance(i, AppleVoucherQueryItem):
                    self._vouchers.append(i)
                else:
                    self._vouchers.append(AppleVoucherQueryItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAppleVoucherQueryResponse, self).parse_response_content(response_content)
        if 'credit_amount' in response:
            self.credit_amount = response['credit_amount']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'instance_no' in response:
            self.instance_no = response['instance_no']
        if 'start_date' in response:
            self.start_date = response['start_date']
        if 'status' in response:
            self.status = response['status']
        if 'vouchers' in response:
            self.vouchers = response['vouchers']
