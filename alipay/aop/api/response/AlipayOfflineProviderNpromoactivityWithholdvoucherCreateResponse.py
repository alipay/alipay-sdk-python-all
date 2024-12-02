#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNpromoactivityWithholdvoucherCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpromoactivityWithholdvoucherCreateResponse, self).__init__()
        self._agreement_no = None
        self._credit_order_no = None
        self._debiting_amount = None
        self._debiting_order_no = None
        self._trade_no = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def credit_order_no(self):
        return self._credit_order_no

    @credit_order_no.setter
    def credit_order_no(self, value):
        self._credit_order_no = value
    @property
    def debiting_amount(self):
        return self._debiting_amount

    @debiting_amount.setter
    def debiting_amount(self, value):
        self._debiting_amount = value
    @property
    def debiting_order_no(self):
        return self._debiting_order_no

    @debiting_order_no.setter
    def debiting_order_no(self, value):
        self._debiting_order_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpromoactivityWithholdvoucherCreateResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'credit_order_no' in response:
            self.credit_order_no = response['credit_order_no']
        if 'debiting_amount' in response:
            self.debiting_amount = response['debiting_amount']
        if 'debiting_order_no' in response:
            self.debiting_order_no = response['debiting_order_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
