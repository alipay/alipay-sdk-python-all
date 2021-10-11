#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAmpeUsersceneQueryModel(object):

    def __init__(self):
        self._device_id = None
        self._product_id = None
        self._user_key = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def user_key(self):
        return self._user_key

    @user_key.setter
    def user_key(self, value):
        self._user_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.user_key:
            if hasattr(self.user_key, 'to_alipay_dict'):
                params['user_key'] = self.user_key.to_alipay_dict()
            else:
                params['user_key'] = self.user_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAmpeUsersceneQueryModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'user_key' in d:
            o.user_key = d['user_key']
        return o


