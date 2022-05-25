#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePromoterRelationCreateModel(object):

    def __init__(self):
        self._merchant_pid = None
        self._mini_app_id = None
        self._promoter_id = None
        self._role = None
        self._shop_id = None
        self._store_id = None

    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def promoter_id(self):
        return self._promoter_id

    @promoter_id.setter
    def promoter_id(self, value):
        self._promoter_id = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.promoter_id:
            if hasattr(self.promoter_id, 'to_alipay_dict'):
                params['promoter_id'] = self.promoter_id.to_alipay_dict()
            else:
                params['promoter_id'] = self.promoter_id
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePromoterRelationCreateModel()
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'promoter_id' in d:
            o.promoter_id = d['promoter_id']
        if 'role' in d:
            o.role = d['role']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


