#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExportBillkey(object):

    def __init__(self):
        self._address = None
        self._billkey = None
        self._biz_type = None
        self._inst_code = None
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
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.billkey:
            if hasattr(self.billkey, 'to_alipay_dict'):
                params['billkey'] = self.billkey.to_alipay_dict()
            else:
                params['billkey'] = self.billkey
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExportBillkey()
        if 'address' in d:
            o.address = d['address']
        if 'billkey' in d:
            o.billkey = d['billkey']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


