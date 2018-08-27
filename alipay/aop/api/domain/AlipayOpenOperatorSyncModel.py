#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperatorSyncModel(object):

    def __init__(self):
        self._master_user_id = None
        self._product_code = None

    @property
    def master_user_id(self):
        return self._master_user_id

    @master_user_id.setter
    def master_user_id(self, value):
        self._master_user_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.master_user_id:
            if hasattr(self.master_user_id, 'to_alipay_dict'):
                params['master_user_id'] = self.master_user_id.to_alipay_dict()
            else:
                params['master_user_id'] = self.master_user_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperatorSyncModel()
        if 'master_user_id' in d:
            o.master_user_id = d['master_user_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


