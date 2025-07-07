#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PhysicalShopInfo(object):

    def __init__(self):
        self._mall_id = None
        self._out_shop_num = None
        self._physical_shop_id = None
        self._physical_shop_name = None

    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def out_shop_num(self):
        return self._out_shop_num

    @out_shop_num.setter
    def out_shop_num(self, value):
        self._out_shop_num = value
    @property
    def physical_shop_id(self):
        return self._physical_shop_id

    @physical_shop_id.setter
    def physical_shop_id(self, value):
        self._physical_shop_id = value
    @property
    def physical_shop_name(self):
        return self._physical_shop_name

    @physical_shop_name.setter
    def physical_shop_name(self, value):
        self._physical_shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.out_shop_num:
            if hasattr(self.out_shop_num, 'to_alipay_dict'):
                params['out_shop_num'] = self.out_shop_num.to_alipay_dict()
            else:
                params['out_shop_num'] = self.out_shop_num
        if self.physical_shop_id:
            if hasattr(self.physical_shop_id, 'to_alipay_dict'):
                params['physical_shop_id'] = self.physical_shop_id.to_alipay_dict()
            else:
                params['physical_shop_id'] = self.physical_shop_id
        if self.physical_shop_name:
            if hasattr(self.physical_shop_name, 'to_alipay_dict'):
                params['physical_shop_name'] = self.physical_shop_name.to_alipay_dict()
            else:
                params['physical_shop_name'] = self.physical_shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PhysicalShopInfo()
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'out_shop_num' in d:
            o.out_shop_num = d['out_shop_num']
        if 'physical_shop_id' in d:
            o.physical_shop_id = d['physical_shop_id']
        if 'physical_shop_name' in d:
            o.physical_shop_name = d['physical_shop_name']
        return o


