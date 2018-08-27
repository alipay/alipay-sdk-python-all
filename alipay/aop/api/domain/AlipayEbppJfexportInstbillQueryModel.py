#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppJfexportInstbillQueryModel(object):

    def __init__(self):
        self._bill_date = None
        self._bill_key = None
        self._biz_type = None
        self._charge_inst = None
        self._extend_field = None
        self._owner_name = None
        self._sub_biz_type = None

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
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
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
        o = AlipayEbppJfexportInstbillQueryModel()
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


