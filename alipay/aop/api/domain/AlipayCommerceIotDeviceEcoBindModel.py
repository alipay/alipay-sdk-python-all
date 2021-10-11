#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDeviceEcoBindModel(object):

    def __init__(self):
        self._bind_type = None
        self._bind_user_id = None
        self._biz_tid = None
        self._identify_type = None
        self._sn = None
        self._supplier_id = None

    @property
    def bind_type(self):
        return self._bind_type

    @bind_type.setter
    def bind_type(self, value):
        self._bind_type = value
    @property
    def bind_user_id(self):
        return self._bind_user_id

    @bind_user_id.setter
    def bind_user_id(self, value):
        self._bind_user_id = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def identify_type(self):
        return self._identify_type

    @identify_type.setter
    def identify_type(self, value):
        self._identify_type = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_type:
            if hasattr(self.bind_type, 'to_alipay_dict'):
                params['bind_type'] = self.bind_type.to_alipay_dict()
            else:
                params['bind_type'] = self.bind_type
        if self.bind_user_id:
            if hasattr(self.bind_user_id, 'to_alipay_dict'):
                params['bind_user_id'] = self.bind_user_id.to_alipay_dict()
            else:
                params['bind_user_id'] = self.bind_user_id
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.identify_type:
            if hasattr(self.identify_type, 'to_alipay_dict'):
                params['identify_type'] = self.identify_type.to_alipay_dict()
            else:
                params['identify_type'] = self.identify_type
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceEcoBindModel()
        if 'bind_type' in d:
            o.bind_type = d['bind_type']
        if 'bind_user_id' in d:
            o.bind_user_id = d['bind_user_id']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'identify_type' in d:
            o.identify_type = d['identify_type']
        if 'sn' in d:
            o.sn = d['sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


