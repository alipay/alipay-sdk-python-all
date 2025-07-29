#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAffinitycardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAffinitycardQueryResponse, self).__init__()
        self._available_amount = None
        self._opened = None
        self._repay_date = None
        self._total_amount = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def opened(self):
        return self._opened

    @opened.setter
    def opened(self, value):
        self._opened = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAffinitycardQueryResponse, self).parse_response_content(response_content)
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'opened' in response:
            self.opened = response['opened']
        if 'repay_date' in response:
            self.repay_date = response['repay_date']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
