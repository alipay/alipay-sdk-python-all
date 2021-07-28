#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessRelationShopInfo(object):

    def __init__(self):
        self._real_shop_id = None
        self._real_shop_no = None
        self._shop_category = None
        self._shop_name = None

    @property
    def real_shop_id(self):
        return self._real_shop_id

    @real_shop_id.setter
    def real_shop_id(self, value):
        self._real_shop_id = value
    @property
    def real_shop_no(self):
        return self._real_shop_no

    @real_shop_no.setter
    def real_shop_no(self, value):
        self._real_shop_no = value
    @property
    def shop_category(self):
        return self._shop_category

    @shop_category.setter
    def shop_category(self, value):
        self._shop_category = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.real_shop_id:
            if hasattr(self.real_shop_id, 'to_alipay_dict'):
                params['real_shop_id'] = self.real_shop_id.to_alipay_dict()
            else:
                params['real_shop_id'] = self.real_shop_id
        if self.real_shop_no:
            if hasattr(self.real_shop_no, 'to_alipay_dict'):
                params['real_shop_no'] = self.real_shop_no.to_alipay_dict()
            else:
                params['real_shop_no'] = self.real_shop_no
        if self.shop_category:
            if hasattr(self.shop_category, 'to_alipay_dict'):
                params['shop_category'] = self.shop_category.to_alipay_dict()
            else:
                params['shop_category'] = self.shop_category
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessRelationShopInfo()
        if 'real_shop_id' in d:
            o.real_shop_id = d['real_shop_id']
        if 'real_shop_no' in d:
            o.real_shop_no = d['real_shop_no']
        if 'shop_category' in d:
            o.shop_category = d['shop_category']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


