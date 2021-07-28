#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotDeviceQueryModel(object):

    def __init__(self):
        self._biz_tid = None
        self._device_id_type = None
        self._device_sn = None
        self._mini_app_id = None
        self._supplier_id = None
        self._type = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def device_id_type(self):
        return self._device_id_type

    @device_id_type.setter
    def device_id_type(self, value):
        self._device_id_type = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.device_id_type:
            if hasattr(self.device_id_type, 'to_alipay_dict'):
                params['device_id_type'] = self.device_id_type.to_alipay_dict()
            else:
                params['device_id_type'] = self.device_id_type
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotDeviceQueryModel()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'device_id_type' in d:
            o.device_id_type = d['device_id_type']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'type' in d:
            o.type = d['type']
        return o


