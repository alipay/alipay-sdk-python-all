#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJfBillkeyConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfBillkeyConsultResponse, self).__init__()
        self._address = None
        self._billkey = None
        self._biz_type = None
        self._charge_inst = None
        self._out_biz_no = None
        self._owner_name = None
        self._sub_biz_type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def billkey(self):
        return self._billkey

    @billkey.setter
    def billkey(self, value):
        self._billkey = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
        response = super(AlipayEbppJfBillkeyConsultResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'billkey' in response:
            self.billkey = response['billkey']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'charge_inst' in response:
            self.charge_inst = response['charge_inst']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'owner_name' in response:
            self.owner_name = response['owner_name']
        if 'sub_biz_type' in response:
            self.sub_biz_type = response['sub_biz_type']
