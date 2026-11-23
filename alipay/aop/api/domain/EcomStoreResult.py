#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomStoreInfo import EcomStoreInfo


class EcomStoreResult(object):

    def __init__(self):
        self._sales_amount_12_m = None
        self._sales_volume_12_m = None
        self._shop_count = None
        self._shop_list = None
        self._truncated_flag = None

    @property
    def sales_amount_12_m(self):
        return self._sales_amount_12_m

    @sales_amount_12_m.setter
    def sales_amount_12_m(self, value):
        self._sales_amount_12_m = value
    @property
    def sales_volume_12_m(self):
        return self._sales_volume_12_m

    @sales_volume_12_m.setter
    def sales_volume_12_m(self, value):
        self._sales_volume_12_m = value
    @property
    def shop_count(self):
        return self._shop_count

    @shop_count.setter
    def shop_count(self, value):
        self._shop_count = value
    @property
    def shop_list(self):
        return self._shop_list

    @shop_list.setter
    def shop_list(self, value):
        if isinstance(value, list):
            self._shop_list = list()
            for i in value:
                if isinstance(i, EcomStoreInfo):
                    self._shop_list.append(i)
                else:
                    self._shop_list.append(EcomStoreInfo.from_alipay_dict(i))
    @property
    def truncated_flag(self):
        return self._truncated_flag

    @truncated_flag.setter
    def truncated_flag(self, value):
        self._truncated_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.sales_amount_12_m:
            if hasattr(self.sales_amount_12_m, 'to_alipay_dict'):
                params['sales_amount_12_m'] = self.sales_amount_12_m.to_alipay_dict()
            else:
                params['sales_amount_12_m'] = self.sales_amount_12_m
        if self.sales_volume_12_m:
            if hasattr(self.sales_volume_12_m, 'to_alipay_dict'):
                params['sales_volume_12_m'] = self.sales_volume_12_m.to_alipay_dict()
            else:
                params['sales_volume_12_m'] = self.sales_volume_12_m
        if self.shop_count:
            if hasattr(self.shop_count, 'to_alipay_dict'):
                params['shop_count'] = self.shop_count.to_alipay_dict()
            else:
                params['shop_count'] = self.shop_count
        if self.shop_list:
            if isinstance(self.shop_list, list):
                for i in range(0, len(self.shop_list)):
                    element = self.shop_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_list, 'to_alipay_dict'):
                params['shop_list'] = self.shop_list.to_alipay_dict()
            else:
                params['shop_list'] = self.shop_list
        if self.truncated_flag:
            if hasattr(self.truncated_flag, 'to_alipay_dict'):
                params['truncated_flag'] = self.truncated_flag.to_alipay_dict()
            else:
                params['truncated_flag'] = self.truncated_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomStoreResult()
        if 'sales_amount_12_m' in d:
            o.sales_amount_12_m = d['sales_amount_12_m']
        if 'sales_volume_12_m' in d:
            o.sales_volume_12_m = d['sales_volume_12_m']
        if 'shop_count' in d:
            o.shop_count = d['shop_count']
        if 'shop_list' in d:
            o.shop_list = d['shop_list']
        if 'truncated_flag' in d:
            o.truncated_flag = d['truncated_flag']
        return o


