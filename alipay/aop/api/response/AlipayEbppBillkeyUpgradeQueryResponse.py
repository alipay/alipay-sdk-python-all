#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppBillkeyUpgradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppBillkeyUpgradeQueryResponse, self).__init__()
        self._bill_key = None
        self._biz_type = None
        self._charge_inst = None
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
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppBillkeyUpgradeQueryResponse, self).parse_response_content(response_content)
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'charge_inst' in response:
            self.charge_inst = response['charge_inst']
        if 'sub_biz_type' in response:
            self.sub_biz_type = response['sub_biz_type']
