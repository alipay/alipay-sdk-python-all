#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJfexportBillCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfexportBillCreateResponse, self).__init__()
        self._amount = None
        self._bill_date = None
        self._bill_key = None
        self._bill_no = None
        self._biz_type = None
        self._charge_inst = None
        self._extend_field = None
        self._merchant_order_no = None
        self._owner_name = None
        self._sub_biz_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfexportBillCreateResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'bill_date' in response:
            self.bill_date = response['bill_date']
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'charge_inst' in response:
            self.charge_inst = response['charge_inst']
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'owner_name' in response:
            self.owner_name = response['owner_name']
        if 'sub_biz_type' in response:
            self.sub_biz_type = response['sub_biz_type']
