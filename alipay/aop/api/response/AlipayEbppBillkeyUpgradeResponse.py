#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppBillkeyUpgradeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppBillkeyUpgradeResponse, self).__init__()
        self._bill_key = None
        self._biz_type = None
        self._charge_inst = None
        self._new_bill_key = None
        self._operation_type = None
        self._sub_biz_type = None

    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
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
    def new_bill_key(self):
        return self._new_bill_key

    @new_bill_key.setter
    def new_bill_key(self, value):
        self._new_bill_key = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppBillkeyUpgradeResponse, self).parse_response_content(response_content)
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'charge_inst' in response:
            self.charge_inst = response['charge_inst']
        if 'new_bill_key' in response:
            self.new_bill_key = response['new_bill_key']
        if 'operation_type' in response:
            self.operation_type = response['operation_type']
        if 'sub_biz_type' in response:
            self.sub_biz_type = response['sub_biz_type']
