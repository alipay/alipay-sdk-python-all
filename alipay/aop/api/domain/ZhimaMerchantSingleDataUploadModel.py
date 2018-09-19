#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantSingleDataUploadModel(object):

    def __init__(self):
        self._biz_ext_params = None
        self._data = None
        self._linked_merchant_id = None
        self._primary_keys = None
        self._scene_code = None

    @property
    def biz_ext_params(self):
        return self._biz_ext_params

    @biz_ext_params.setter
    def biz_ext_params(self, value):
        self._biz_ext_params = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def linked_merchant_id(self):
        return self._linked_merchant_id

    @linked_merchant_id.setter
    def linked_merchant_id(self, value):
        self._linked_merchant_id = value
    @property
    def primary_keys(self):
        return self._primary_keys

    @primary_keys.setter
    def primary_keys(self, value):
        self._primary_keys = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_ext_params:
            if hasattr(self.biz_ext_params, 'to_alipay_dict'):
                params['biz_ext_params'] = self.biz_ext_params.to_alipay_dict()
            else:
                params['biz_ext_params'] = self.biz_ext_params
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.linked_merchant_id:
            if hasattr(self.linked_merchant_id, 'to_alipay_dict'):
                params['linked_merchant_id'] = self.linked_merchant_id.to_alipay_dict()
            else:
                params['linked_merchant_id'] = self.linked_merchant_id
        if self.primary_keys:
            if hasattr(self.primary_keys, 'to_alipay_dict'):
                params['primary_keys'] = self.primary_keys.to_alipay_dict()
            else:
                params['primary_keys'] = self.primary_keys
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantSingleDataUploadModel()
        if 'biz_ext_params' in d:
            o.biz_ext_params = d['biz_ext_params']
        if 'data' in d:
            o.data = d['data']
        if 'linked_merchant_id' in d:
            o.linked_merchant_id = d['linked_merchant_id']
        if 'primary_keys' in d:
            o.primary_keys = d['primary_keys']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


