#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishDetailInfo(object):

    def __init__(self):
        self._out_dish_id = None
        self._out_sku_id_list = None

    @property
    def out_dish_id(self):
        return self._out_dish_id

    @out_dish_id.setter
    def out_dish_id(self, value):
        self._out_dish_id = value
    @property
    def out_sku_id_list(self):
        return self._out_sku_id_list

    @out_sku_id_list.setter
    def out_sku_id_list(self, value):
        if isinstance(value, list):
            self._out_sku_id_list = list()
            for i in value:
                self._out_sku_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.out_dish_id:
            if hasattr(self.out_dish_id, 'to_alipay_dict'):
                params['out_dish_id'] = self.out_dish_id.to_alipay_dict()
            else:
                params['out_dish_id'] = self.out_dish_id
        if self.out_sku_id_list:
            if isinstance(self.out_sku_id_list, list):
                for i in range(0, len(self.out_sku_id_list)):
                    element = self.out_sku_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_sku_id_list[i] = element.to_alipay_dict()
            if hasattr(self.out_sku_id_list, 'to_alipay_dict'):
                params['out_sku_id_list'] = self.out_sku_id_list.to_alipay_dict()
            else:
                params['out_sku_id_list'] = self.out_sku_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishDetailInfo()
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        if 'out_sku_id_list' in d:
            o.out_sku_id_list = d['out_sku_id_list']
        return o


