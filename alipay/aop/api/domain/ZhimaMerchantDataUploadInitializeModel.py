#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantDataUploadInitializeModel(object):

    def __init__(self):
        self._linked_merchant_id = None
        self._scene_code = None

    @property
    def linked_merchant_id(self):
        return self._linked_merchant_id

    @linked_merchant_id.setter
    def linked_merchant_id(self, value):
        self._linked_merchant_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.linked_merchant_id:
            if hasattr(self.linked_merchant_id, 'to_alipay_dict'):
                params['linked_merchant_id'] = self.linked_merchant_id.to_alipay_dict()
            else:
                params['linked_merchant_id'] = self.linked_merchant_id
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
        o = ZhimaMerchantDataUploadInitializeModel()
        if 'linked_merchant_id' in d:
            o.linked_merchant_id = d['linked_merchant_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


