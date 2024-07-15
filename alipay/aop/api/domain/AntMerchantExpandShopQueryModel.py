#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandShopQueryModel(object):

    def __init__(self):
        self._address_version = None
        self._ip_role_id = None
        self._need_industry_info = None
        self._need_industry_license = None
        self._need_recommend = None
        self._shop_id = None
        self._store_id = None

    @property
    def address_version(self):
        return self._address_version

    @address_version.setter
    def address_version(self, value):
        self._address_version = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def need_industry_info(self):
        return self._need_industry_info

    @need_industry_info.setter
    def need_industry_info(self, value):
        self._need_industry_info = value
    @property
    def need_industry_license(self):
        return self._need_industry_license

    @need_industry_license.setter
    def need_industry_license(self, value):
        self._need_industry_license = value
    @property
    def need_recommend(self):
        return self._need_recommend

    @need_recommend.setter
    def need_recommend(self, value):
        self._need_recommend = value
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
        if self.address_version:
            if hasattr(self.address_version, 'to_alipay_dict'):
                params['address_version'] = self.address_version.to_alipay_dict()
            else:
                params['address_version'] = self.address_version
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.need_industry_info:
            if hasattr(self.need_industry_info, 'to_alipay_dict'):
                params['need_industry_info'] = self.need_industry_info.to_alipay_dict()
            else:
                params['need_industry_info'] = self.need_industry_info
        if self.need_industry_license:
            if hasattr(self.need_industry_license, 'to_alipay_dict'):
                params['need_industry_license'] = self.need_industry_license.to_alipay_dict()
            else:
                params['need_industry_license'] = self.need_industry_license
        if self.need_recommend:
            if hasattr(self.need_recommend, 'to_alipay_dict'):
                params['need_recommend'] = self.need_recommend.to_alipay_dict()
            else:
                params['need_recommend'] = self.need_recommend
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
        o = AntMerchantExpandShopQueryModel()
        if 'address_version' in d:
            o.address_version = d['address_version']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'need_industry_info' in d:
            o.need_industry_info = d['need_industry_info']
        if 'need_industry_license' in d:
            o.need_industry_license = d['need_industry_license']
        if 'need_recommend' in d:
            o.need_recommend = d['need_recommend']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


