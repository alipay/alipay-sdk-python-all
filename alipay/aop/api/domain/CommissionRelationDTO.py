#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommissionRelationDTO(object):

    def __init__(self):
        self._auth_result = None
        self._merchant_role_id = None
        self._shop_id = None

    @property
    def auth_result(self):
        return self._auth_result

    @auth_result.setter
    def auth_result(self, value):
        self._auth_result = value
    @property
    def merchant_role_id(self):
        return self._merchant_role_id

    @merchant_role_id.setter
    def merchant_role_id(self, value):
        self._merchant_role_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_result:
            if hasattr(self.auth_result, 'to_alipay_dict'):
                params['auth_result'] = self.auth_result.to_alipay_dict()
            else:
                params['auth_result'] = self.auth_result
        if self.merchant_role_id:
            if hasattr(self.merchant_role_id, 'to_alipay_dict'):
                params['merchant_role_id'] = self.merchant_role_id.to_alipay_dict()
            else:
                params['merchant_role_id'] = self.merchant_role_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommissionRelationDTO()
        if 'auth_result' in d:
            o.auth_result = d['auth_result']
        if 'merchant_role_id' in d:
            o.merchant_role_id = d['merchant_role_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


