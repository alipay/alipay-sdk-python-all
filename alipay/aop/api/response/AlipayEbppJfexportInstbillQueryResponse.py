#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JfExportInstBillModel import JfExportInstBillModel


class AlipayEbppJfexportInstbillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfexportInstbillQueryResponse, self).__init__()
        self._bill_key = None
        self._biz_type = None
        self._cache_key = None
        self._charge_inst = None
        self._charge_mode = None
        self._extend_field = None
        self._inst_bills = None
        self._owner_name = None
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
    def cache_key(self):
        return self._cache_key

    @cache_key.setter
    def cache_key(self, value):
        self._cache_key = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def charge_mode(self):
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, value):
        self._charge_mode = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def inst_bills(self):
        return self._inst_bills

    @inst_bills.setter
    def inst_bills(self, value):
        if isinstance(value, list):
            self._inst_bills = list()
            for i in value:
                if isinstance(i, JfExportInstBillModel):
                    self._inst_bills.append(i)
                else:
                    self._inst_bills.append(JfExportInstBillModel.from_alipay_dict(i))
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
        response = super(AlipayEbppJfexportInstbillQueryResponse, self).parse_response_content(response_content)
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'cache_key' in response:
            self.cache_key = response['cache_key']
        if 'charge_inst' in response:
            self.charge_inst = response['charge_inst']
        if 'charge_mode' in response:
            self.charge_mode = response['charge_mode']
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'inst_bills' in response:
            self.inst_bills = response['inst_bills']
        if 'owner_name' in response:
            self.owner_name = response['owner_name']
        if 'sub_biz_type' in response:
            self.sub_biz_type = response['sub_biz_type']
