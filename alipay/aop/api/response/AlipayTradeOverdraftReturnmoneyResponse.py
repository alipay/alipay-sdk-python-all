#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeOverdraftReturnmoneyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeOverdraftReturnmoneyResponse, self).__init__()
        self._exchange_rate = None
        self._out_request_no = None
        self._receive_account = None
        self._refund_out_request_no = None
        self._return_amount = None
        self._return_foreign_amount = None
        self._return_foreign_currency = None
        self._return_result = None
        self._success_time = None

    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self._exchange_rate = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def receive_account(self):
        return self._receive_account

    @receive_account.setter
    def receive_account(self, value):
        self._receive_account = value
    @property
    def refund_out_request_no(self):
        return self._refund_out_request_no

    @refund_out_request_no.setter
    def refund_out_request_no(self, value):
        self._refund_out_request_no = value
    @property
    def return_amount(self):
        return self._return_amount

    @return_amount.setter
    def return_amount(self, value):
        self._return_amount = value
    @property
    def return_foreign_amount(self):
        return self._return_foreign_amount

    @return_foreign_amount.setter
    def return_foreign_amount(self, value):
        self._return_foreign_amount = value
    @property
    def return_foreign_currency(self):
        return self._return_foreign_currency

    @return_foreign_currency.setter
    def return_foreign_currency(self, value):
        self._return_foreign_currency = value
    @property
    def return_result(self):
        return self._return_result

    @return_result.setter
    def return_result(self, value):
        self._return_result = value
    @property
    def success_time(self):
        return self._success_time

    @success_time.setter
    def success_time(self, value):
        self._success_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeOverdraftReturnmoneyResponse, self).parse_response_content(response_content)
        if 'exchange_rate' in response:
            self.exchange_rate = response['exchange_rate']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'receive_account' in response:
            self.receive_account = response['receive_account']
        if 'refund_out_request_no' in response:
            self.refund_out_request_no = response['refund_out_request_no']
        if 'return_amount' in response:
            self.return_amount = response['return_amount']
        if 'return_foreign_amount' in response:
            self.return_foreign_amount = response['return_foreign_amount']
        if 'return_foreign_currency' in response:
            self.return_foreign_currency = response['return_foreign_currency']
        if 'return_result' in response:
            self.return_result = response['return_result']
        if 'success_time' in response:
            self.success_time = response['success_time']
