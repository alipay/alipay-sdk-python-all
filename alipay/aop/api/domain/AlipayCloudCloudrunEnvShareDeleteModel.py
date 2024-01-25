#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunEnvShareDeleteModel(object):

    def __init__(self):
        self._env_id = None
        self._product_code = None
        self._share_app_id = None

    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def share_app_id(self):
        return self._share_app_id

    @share_app_id.setter
    def share_app_id(self, value):
        self._share_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.share_app_id:
            if hasattr(self.share_app_id, 'to_alipay_dict'):
                params['share_app_id'] = self.share_app_id.to_alipay_dict()
            else:
                params['share_app_id'] = self.share_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunEnvShareDeleteModel()
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'share_app_id' in d:
            o.share_app_id = d['share_app_id']
        return o


