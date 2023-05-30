#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundFlexiblestaffingEmployeehomeUnsignModel(object):

    def __init__(self):
        self._biz_scene = None
        self._principal_open_id = None
        self._principal_user_id = None
        self._product_code = None
        self._target_id = None
        self._terminate_type = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def principal_open_id(self):
        return self._principal_open_id

    @principal_open_id.setter
    def principal_open_id(self, value):
        self._principal_open_id = value
    @property
    def principal_user_id(self):
        return self._principal_user_id

    @principal_user_id.setter
    def principal_user_id(self, value):
        self._principal_user_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def terminate_type(self):
        return self._terminate_type

    @terminate_type.setter
    def terminate_type(self, value):
        self._terminate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.principal_open_id:
            if hasattr(self.principal_open_id, 'to_alipay_dict'):
                params['principal_open_id'] = self.principal_open_id.to_alipay_dict()
            else:
                params['principal_open_id'] = self.principal_open_id
        if self.principal_user_id:
            if hasattr(self.principal_user_id, 'to_alipay_dict'):
                params['principal_user_id'] = self.principal_user_id.to_alipay_dict()
            else:
                params['principal_user_id'] = self.principal_user_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.terminate_type:
            if hasattr(self.terminate_type, 'to_alipay_dict'):
                params['terminate_type'] = self.terminate_type.to_alipay_dict()
            else:
                params['terminate_type'] = self.terminate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundFlexiblestaffingEmployeehomeUnsignModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'principal_open_id' in d:
            o.principal_open_id = d['principal_open_id']
        if 'principal_user_id' in d:
            o.principal_user_id = d['principal_user_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'terminate_type' in d:
            o.terminate_type = d['terminate_type']
        return o


