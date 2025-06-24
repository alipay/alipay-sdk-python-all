#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InternetbarDeviceActivityData(object):

    def __init__(self):
        self._awake_app = None
        self._biz_date = None
        self._device_dau = None
        self._device_pv = None
        self._shop_code = None
        self._shop_id = None
        self._shop_name = None
        self._tag_id = None

    @property
    def awake_app(self):
        return self._awake_app

    @awake_app.setter
    def awake_app(self, value):
        self._awake_app = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def device_dau(self):
        return self._device_dau

    @device_dau.setter
    def device_dau(self, value):
        self._device_dau = value
    @property
    def device_pv(self):
        return self._device_pv

    @device_pv.setter
    def device_pv(self, value):
        self._device_pv = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def tag_id(self):
        return self._tag_id

    @tag_id.setter
    def tag_id(self, value):
        self._tag_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.awake_app:
            if hasattr(self.awake_app, 'to_alipay_dict'):
                params['awake_app'] = self.awake_app.to_alipay_dict()
            else:
                params['awake_app'] = self.awake_app
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.device_dau:
            if hasattr(self.device_dau, 'to_alipay_dict'):
                params['device_dau'] = self.device_dau.to_alipay_dict()
            else:
                params['device_dau'] = self.device_dau
        if self.device_pv:
            if hasattr(self.device_pv, 'to_alipay_dict'):
                params['device_pv'] = self.device_pv.to_alipay_dict()
            else:
                params['device_pv'] = self.device_pv
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.tag_id:
            if hasattr(self.tag_id, 'to_alipay_dict'):
                params['tag_id'] = self.tag_id.to_alipay_dict()
            else:
                params['tag_id'] = self.tag_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InternetbarDeviceActivityData()
        if 'awake_app' in d:
            o.awake_app = d['awake_app']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'device_dau' in d:
            o.device_dau = d['device_dau']
        if 'device_pv' in d:
            o.device_pv = d['device_pv']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'tag_id' in d:
            o.tag_id = d['tag_id']
        return o


