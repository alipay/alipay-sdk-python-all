#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskVerifyidentityApplyModel(object):

    def __init__(self):
        self._account_id = None
        self._account_name = None
        self._account_type = None
        self._biz_id = None
        self._biz_params = None
        self._scene_code = None
        self._validate_product_group = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_params(self):
        return self._biz_params

    @biz_params.setter
    def biz_params(self, value):
        self._biz_params = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def validate_product_group(self):
        return self._validate_product_group

    @validate_product_group.setter
    def validate_product_group(self, value):
        self._validate_product_group = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_params:
            if hasattr(self.biz_params, 'to_alipay_dict'):
                params['biz_params'] = self.biz_params.to_alipay_dict()
            else:
                params['biz_params'] = self.biz_params
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.validate_product_group:
            if hasattr(self.validate_product_group, 'to_alipay_dict'):
                params['validate_product_group'] = self.validate_product_group.to_alipay_dict()
            else:
                params['validate_product_group'] = self.validate_product_group
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskVerifyidentityApplyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_params' in d:
            o.biz_params = d['biz_params']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'validate_product_group' in d:
            o.validate_product_group = d['validate_product_group']
        return o


