#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopExtInfo import ShopExtInfo


class AntMerchantExpandShopCloseModel(object):

    def __init__(self):
        self._ext_infos = None
        self._ip_role_id = None
        self._shop_id = None
        self._store_id = None

    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        if isinstance(value, list):
            self._ext_infos = list()
            for i in value:
                if isinstance(i, ShopExtInfo):
                    self._ext_infos.append(i)
                else:
                    self._ext_infos.append(ShopExtInfo.from_alipay_dict(i))
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
        if self.ext_infos:
            if isinstance(self.ext_infos, list):
                for i in range(0, len(self.ext_infos)):
                    element = self.ext_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_infos[i] = element.to_alipay_dict()
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
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
        o = AntMerchantExpandShopCloseModel()
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


