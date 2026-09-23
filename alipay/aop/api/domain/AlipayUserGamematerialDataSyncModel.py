#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserGamematerialDataSyncModel(object):

    def __init__(self):
        self._click_pv = None
        self._click_uv = None
        self._data_time = None
        self._expose_pv = None
        self._expose_uv = None
        self._material_id = None

    @property
    def click_pv(self):
        return self._click_pv

    @click_pv.setter
    def click_pv(self, value):
        self._click_pv = value
    @property
    def click_uv(self):
        return self._click_uv

    @click_uv.setter
    def click_uv(self, value):
        self._click_uv = value
    @property
    def data_time(self):
        return self._data_time

    @data_time.setter
    def data_time(self, value):
        self._data_time = value
    @property
    def expose_pv(self):
        return self._expose_pv

    @expose_pv.setter
    def expose_pv(self, value):
        self._expose_pv = value
    @property
    def expose_uv(self):
        return self._expose_uv

    @expose_uv.setter
    def expose_uv(self, value):
        self._expose_uv = value
    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.click_pv:
            if hasattr(self.click_pv, 'to_alipay_dict'):
                params['click_pv'] = self.click_pv.to_alipay_dict()
            else:
                params['click_pv'] = self.click_pv
        if self.click_uv:
            if hasattr(self.click_uv, 'to_alipay_dict'):
                params['click_uv'] = self.click_uv.to_alipay_dict()
            else:
                params['click_uv'] = self.click_uv
        if self.data_time:
            if hasattr(self.data_time, 'to_alipay_dict'):
                params['data_time'] = self.data_time.to_alipay_dict()
            else:
                params['data_time'] = self.data_time
        if self.expose_pv:
            if hasattr(self.expose_pv, 'to_alipay_dict'):
                params['expose_pv'] = self.expose_pv.to_alipay_dict()
            else:
                params['expose_pv'] = self.expose_pv
        if self.expose_uv:
            if hasattr(self.expose_uv, 'to_alipay_dict'):
                params['expose_uv'] = self.expose_uv.to_alipay_dict()
            else:
                params['expose_uv'] = self.expose_uv
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserGamematerialDataSyncModel()
        if 'click_pv' in d:
            o.click_pv = d['click_pv']
        if 'click_uv' in d:
            o.click_uv = d['click_uv']
        if 'data_time' in d:
            o.data_time = d['data_time']
        if 'expose_pv' in d:
            o.expose_pv = d['expose_pv']
        if 'expose_uv' in d:
            o.expose_uv = d['expose_uv']
        if 'material_id' in d:
            o.material_id = d['material_id']
        return o


