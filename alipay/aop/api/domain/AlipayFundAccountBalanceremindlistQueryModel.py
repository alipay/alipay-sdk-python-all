#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundAccountBalanceremindlistQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._monitor_user_id = None
        self._monitor_user_open_id = None
        self._product_code = None
        self._third_biz_scene = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def monitor_user_id(self):
        return self._monitor_user_id

    @monitor_user_id.setter
    def monitor_user_id(self, value):
        self._monitor_user_id = value
    @property
    def monitor_user_open_id(self):
        return self._monitor_user_open_id

    @monitor_user_open_id.setter
    def monitor_user_open_id(self, value):
        self._monitor_user_open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def third_biz_scene(self):
        return self._third_biz_scene

    @third_biz_scene.setter
    def third_biz_scene(self, value):
        self._third_biz_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.monitor_user_id:
            if hasattr(self.monitor_user_id, 'to_alipay_dict'):
                params['monitor_user_id'] = self.monitor_user_id.to_alipay_dict()
            else:
                params['monitor_user_id'] = self.monitor_user_id
        if self.monitor_user_open_id:
            if hasattr(self.monitor_user_open_id, 'to_alipay_dict'):
                params['monitor_user_open_id'] = self.monitor_user_open_id.to_alipay_dict()
            else:
                params['monitor_user_open_id'] = self.monitor_user_open_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.third_biz_scene:
            if hasattr(self.third_biz_scene, 'to_alipay_dict'):
                params['third_biz_scene'] = self.third_biz_scene.to_alipay_dict()
            else:
                params['third_biz_scene'] = self.third_biz_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundAccountBalanceremindlistQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'monitor_user_id' in d:
            o.monitor_user_id = d['monitor_user_id']
        if 'monitor_user_open_id' in d:
            o.monitor_user_open_id = d['monitor_user_open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'third_biz_scene' in d:
            o.third_biz_scene = d['third_biz_scene']
        return o


