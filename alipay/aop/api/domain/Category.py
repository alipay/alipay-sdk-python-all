#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Category(object):

    def __init__(self):
        self._shop_cate_ids = None
        self._shop_cate_name = None

    @property
    def shop_cate_ids(self):
        return self._shop_cate_ids

    @shop_cate_ids.setter
    def shop_cate_ids(self, value):
        if isinstance(value, list):
            self._shop_cate_ids = list()
            for i in value:
                self._shop_cate_ids.append(i)
    @property
    def shop_cate_name(self):
        return self._shop_cate_name

    @shop_cate_name.setter
    def shop_cate_name(self, value):
        self._shop_cate_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_cate_ids:
            if isinstance(self.shop_cate_ids, list):
                for i in range(0, len(self.shop_cate_ids)):
                    element = self.shop_cate_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_cate_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_cate_ids, 'to_alipay_dict'):
                params['shop_cate_ids'] = self.shop_cate_ids.to_alipay_dict()
            else:
                params['shop_cate_ids'] = self.shop_cate_ids
        if self.shop_cate_name:
            if hasattr(self.shop_cate_name, 'to_alipay_dict'):
                params['shop_cate_name'] = self.shop_cate_name.to_alipay_dict()
            else:
                params['shop_cate_name'] = self.shop_cate_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Category()
        if 'shop_cate_ids' in d:
            o.shop_cate_ids = d['shop_cate_ids']
        if 'shop_cate_name' in d:
            o.shop_cate_name = d['shop_cate_name']
        return o


