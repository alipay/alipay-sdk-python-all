#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopIndustryLicense import ShopIndustryLicense


class AntMerchantExpandShopLicenseModifyModel(object):

    def __init__(self):
        self._audit_license_list = None
        self._ip_role_id = None
        self._shop_id = None
        self._store_id = None

    @property
    def audit_license_list(self):
        return self._audit_license_list

    @audit_license_list.setter
    def audit_license_list(self, value):
        if isinstance(value, list):
            self._audit_license_list = list()
            for i in value:
                if isinstance(i, ShopIndustryLicense):
                    self._audit_license_list.append(i)
                else:
                    self._audit_license_list.append(ShopIndustryLicense.from_alipay_dict(i))
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
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
        if self.audit_license_list:
            if isinstance(self.audit_license_list, list):
                for i in range(0, len(self.audit_license_list)):
                    element = self.audit_license_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.audit_license_list[i] = element.to_alipay_dict()
            if hasattr(self.audit_license_list, 'to_alipay_dict'):
                params['audit_license_list'] = self.audit_license_list.to_alipay_dict()
            else:
                params['audit_license_list'] = self.audit_license_list
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
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
        o = AntMerchantExpandShopLicenseModifyModel()
        if 'audit_license_list' in d:
            o.audit_license_list = d['audit_license_list']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


