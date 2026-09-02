#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAppleVoucherReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAppleVoucherReceiveResponse, self).__init__()
        self._credit_amount = None
        self._end_date = None
        self._idempotent = None
        self._instance_no = None
        self._start_date = None

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
    def idempotent(self):
        return self._idempotent

    @idempotent.setter
    def idempotent(self, value):
        self._idempotent = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAppleVoucherReceiveResponse, self).parse_response_content(response_content)
        if 'credit_amount' in response:
            self.credit_amount = response['credit_amount']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'idempotent' in response:
            self.idempotent = response['idempotent']
        if 'instance_no' in response:
            self.instance_no = response['instance_no']
        if 'start_date' in response:
            self.start_date = response['start_date']
