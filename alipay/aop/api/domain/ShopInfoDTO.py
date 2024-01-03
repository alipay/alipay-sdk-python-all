#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopInfoDTO(object):

    def __init__(self):
        self._address = None
        self._alipay_shop_id = None
        self._merchant_shop_id = None
        self._name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def alipay_shop_id(self):
        return self._alipay_shop_id

    @alipay_shop_id.setter
    def alipay_shop_id(self, value):
        self._alipay_shop_id = value
    @property
    def merchant_shop_id(self):
        return self._merchant_shop_id

    @merchant_shop_id.setter
    def merchant_shop_id(self, value):
        self._merchant_shop_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.alipay_shop_id:
            if hasattr(self.alipay_shop_id, 'to_alipay_dict'):
                params['alipay_shop_id'] = self.alipay_shop_id.to_alipay_dict()
            else:
                params['alipay_shop_id'] = self.alipay_shop_id
        if self.merchant_shop_id:
            if hasattr(self.merchant_shop_id, 'to_alipay_dict'):
                params['merchant_shop_id'] = self.merchant_shop_id.to_alipay_dict()
            else:
                params['merchant_shop_id'] = self.merchant_shop_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopInfoDTO()
        if 'address' in d:
            o.address = d['address']
        if 'alipay_shop_id' in d:
            o.alipay_shop_id = d['alipay_shop_id']
        if 'merchant_shop_id' in d:
            o.merchant_shop_id = d['merchant_shop_id']
        if 'name' in d:
            o.name = d['name']
        return o


