#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantInstConfig(object):

    def __init__(self):
        self._en_name = None
        self._order_type = None
        self._scene = None
        self._zh_name = None

    @property
    def en_name(self):
        return self._en_name

    @en_name.setter
    def en_name(self, value):
        self._en_name = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def zh_name(self):
        return self._zh_name

    @zh_name.setter
    def zh_name(self, value):
        self._zh_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.en_name:
            if hasattr(self.en_name, 'to_alipay_dict'):
                params['en_name'] = self.en_name.to_alipay_dict()
            else:
                params['en_name'] = self.en_name
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.zh_name:
            if hasattr(self.zh_name, 'to_alipay_dict'):
                params['zh_name'] = self.zh_name.to_alipay_dict()
            else:
                params['zh_name'] = self.zh_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantInstConfig()
        if 'en_name' in d:
            o.en_name = d['en_name']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'scene' in d:
            o.scene = d['scene']
        if 'zh_name' in d:
            o.zh_name = d['zh_name']
        return o


