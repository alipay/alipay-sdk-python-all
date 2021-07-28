#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainCreditpayBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainCreditpayBillQueryResponse, self).__init__()
        self._balance_amt = None
        self._balance_int_amt = None
        self._balance_prin_amt = None
        self._bill_amt = None
        self._bill_date = None
        self._bill_int_amt = None
        self._bill_prin_amt = None
        self._buyer = None
        self._buyer_scene_id = None
        self._status = None
        self._trace_id = None

    @property
    def balance_amt(self):
        return self._balance_amt

    @balance_amt.setter
    def balance_amt(self, value):
        self._balance_amt = value
    @property
    def balance_int_amt(self):
        return self._balance_int_amt

    @balance_int_amt.setter
    def balance_int_amt(self, value):
        self._balance_int_amt = value
    @property
    def balance_prin_amt(self):
        return self._balance_prin_amt

    @balance_prin_amt.setter
    def balance_prin_amt(self, value):
        self._balance_prin_amt = value
    @property
    def bill_amt(self):
        return self._bill_amt

    @bill_amt.setter
    def bill_amt(self, value):
        self._bill_amt = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_int_amt(self):
        return self._bill_int_amt

    @bill_int_amt.setter
    def bill_int_amt(self, value):
        self._bill_int_amt = value
    @property
    def bill_prin_amt(self):
        return self._bill_prin_amt

    @bill_prin_amt.setter
    def bill_prin_amt(self, value):
        self._bill_prin_amt = value
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, Member):
            self._buyer = value
        else:
            self._buyer = Member.from_alipay_dict(value)
    @property
    def buyer_scene_id(self):
        return self._buyer_scene_id

    @buyer_scene_id.setter
    def buyer_scene_id(self, value):
        self._buyer_scene_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainCreditpayBillQueryResponse, self).parse_response_content(response_content)
        if 'balance_amt' in response:
            self.balance_amt = response['balance_amt']
        if 'balance_int_amt' in response:
            self.balance_int_amt = response['balance_int_amt']
        if 'balance_prin_amt' in response:
            self.balance_prin_amt = response['balance_prin_amt']
        if 'bill_amt' in response:
            self.bill_amt = response['bill_amt']
        if 'bill_date' in response:
            self.bill_date = response['bill_date']
        if 'bill_int_amt' in response:
            self.bill_int_amt = response['bill_int_amt']
        if 'bill_prin_amt' in response:
            self.bill_prin_amt = response['bill_prin_amt']
        if 'buyer' in response:
            self.buyer = response['buyer']
        if 'buyer_scene_id' in response:
            self.buyer_scene_id = response['buyer_scene_id']
        if 'status' in response:
            self.status = response['status']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
