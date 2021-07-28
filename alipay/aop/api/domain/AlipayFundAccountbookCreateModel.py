#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundAccountbookCreateModel(object):

    def __init__(self):
        self._ext_info = None
        self._merchant_user_id = None
        self._merchant_user_type = None
        self._scene_code = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def merchant_user_type(self):
        return self._merchant_user_type

    @merchant_user_type.setter
    def merchant_user_type(self, value):
        self._merchant_user_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.merchant_user_type:
            if hasattr(self.merchant_user_type, 'to_alipay_dict'):
                params['merchant_user_type'] = self.merchant_user_type.to_alipay_dict()
            else:
                params['merchant_user_type'] = self.merchant_user_type
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
        o = AlipayFundAccountbookCreateModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'merchant_user_type' in d:
            o.merchant_user_type = d['merchant_user_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


