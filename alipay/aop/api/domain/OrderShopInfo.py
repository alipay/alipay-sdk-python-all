#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderShopInfo(object):

    def __init__(self):
        self._address = None
        self._merchant_shop_id = None
        self._merchant_shop_link_page = None
        self._name = None
        self._phone_num = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def merchant_shop_id(self):
        return self._merchant_shop_id

    @merchant_shop_id.setter
    def merchant_shop_id(self, value):
        self._merchant_shop_id = value
    @property
    def merchant_shop_link_page(self):
        return self._merchant_shop_link_page

    @merchant_shop_link_page.setter
    def merchant_shop_link_page(self, value):
        self._merchant_shop_link_page = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone_num(self):
        return self._phone_num

    @phone_num.setter
    def phone_num(self, value):
        self._phone_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.merchant_shop_id:
            if hasattr(self.merchant_shop_id, 'to_alipay_dict'):
                params['merchant_shop_id'] = self.merchant_shop_id.to_alipay_dict()
            else:
                params['merchant_shop_id'] = self.merchant_shop_id
        if self.merchant_shop_link_page:
            if hasattr(self.merchant_shop_link_page, 'to_alipay_dict'):
                params['merchant_shop_link_page'] = self.merchant_shop_link_page.to_alipay_dict()
            else:
                params['merchant_shop_link_page'] = self.merchant_shop_link_page
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone_num:
            if hasattr(self.phone_num, 'to_alipay_dict'):
                params['phone_num'] = self.phone_num.to_alipay_dict()
            else:
                params['phone_num'] = self.phone_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderShopInfo()
        if 'address' in d:
            o.address = d['address']
        if 'merchant_shop_id' in d:
            o.merchant_shop_id = d['merchant_shop_id']
        if 'merchant_shop_link_page' in d:
            o.merchant_shop_link_page = d['merchant_shop_link_page']
        if 'name' in d:
            o.name = d['name']
        if 'phone_num' in d:
            o.phone_num = d['phone_num']
        return o


