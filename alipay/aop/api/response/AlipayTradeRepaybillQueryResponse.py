#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeRepaybillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeRepaybillQueryResponse, self).__init__()
        self._bill_amount = None
        self._bill_no = None
        self._bill_overdue_amount = None
        self._bill_paid_amount = None
        self._bill_paid_revoked_amount = None
        self._bill_revoked_amount = None
        self._bill_status = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_overdue_amount(self):
        return self._bill_overdue_amount

    @bill_overdue_amount.setter
    def bill_overdue_amount(self, value):
        self._bill_overdue_amount = value
    @property
    def bill_paid_amount(self):
        return self._bill_paid_amount

    @bill_paid_amount.setter
    def bill_paid_amount(self, value):
        self._bill_paid_amount = value
    @property
    def bill_paid_revoked_amount(self):
        return self._bill_paid_revoked_amount

    @bill_paid_revoked_amount.setter
    def bill_paid_revoked_amount(self, value):
        self._bill_paid_revoked_amount = value
    @property
    def bill_revoked_amount(self):
        return self._bill_revoked_amount

    @bill_revoked_amount.setter
    def bill_revoked_amount(self, value):
        self._bill_revoked_amount = value
    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeRepaybillQueryResponse, self).parse_response_content(response_content)
        if 'bill_amount' in response:
            self.bill_amount = response['bill_amount']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'bill_overdue_amount' in response:
            self.bill_overdue_amount = response['bill_overdue_amount']
        if 'bill_paid_amount' in response:
            self.bill_paid_amount = response['bill_paid_amount']
        if 'bill_paid_revoked_amount' in response:
            self.bill_paid_revoked_amount = response['bill_paid_revoked_amount']
        if 'bill_revoked_amount' in response:
            self.bill_revoked_amount = response['bill_revoked_amount']
        if 'bill_status' in response:
            self.bill_status = response['bill_status']
