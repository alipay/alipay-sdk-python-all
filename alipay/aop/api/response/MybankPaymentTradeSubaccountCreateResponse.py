#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeSubaccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeSubaccountCreateResponse, self).__init__()
        self._account_name = None
        self._branch_name = None
        self._branch_no = None
        self._currency_value = None
        self._open_account_time = None
        self._out_channel_id = None
        self._parent_card_no = None
        self._request_no = None
        self._retry = None
        self._sub_card_no = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def branch_no(self):
        return self._branch_no

    @branch_no.setter
    def branch_no(self, value):
        self._branch_no = value
    @property
    def currency_value(self):
        return self._currency_value

    @currency_value.setter
    def currency_value(self, value):
        self._currency_value = value
    @property
    def open_account_time(self):
        return self._open_account_time

    @open_account_time.setter
    def open_account_time(self, value):
        self._open_account_time = value
    @property
    def out_channel_id(self):
        return self._out_channel_id

    @out_channel_id.setter
    def out_channel_id(self, value):
        self._out_channel_id = value
    @property
    def parent_card_no(self):
        return self._parent_card_no

    @parent_card_no.setter
    def parent_card_no(self, value):
        self._parent_card_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def sub_card_no(self):
        return self._sub_card_no

    @sub_card_no.setter
    def sub_card_no(self, value):
        self._sub_card_no = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeSubaccountCreateResponse, self).parse_response_content(response_content)
        if 'account_name' in response:
            self.account_name = response['account_name']
        if 'branch_name' in response:
            self.branch_name = response['branch_name']
        if 'branch_no' in response:
            self.branch_no = response['branch_no']
        if 'currency_value' in response:
            self.currency_value = response['currency_value']
        if 'open_account_time' in response:
            self.open_account_time = response['open_account_time']
        if 'out_channel_id' in response:
            self.out_channel_id = response['out_channel_id']
        if 'parent_card_no' in response:
            self.parent_card_no = response['parent_card_no']
        if 'request_no' in response:
            self.request_no = response['request_no']
        if 'retry' in response:
            self.retry = response['retry']
        if 'sub_card_no' in response:
            self.sub_card_no = response['sub_card_no']
