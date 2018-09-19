#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataItemGoodsList(object):

    def __init__(self):
        self._desc = None
        self._goods_list = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                self._goods_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.goods_list:
            if isinstance(self.goods_list, list):
                for i in range(0, len(self.goods_list)):
                    element = self.goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_list, 'to_alipay_dict'):
                params['goods_list'] = self.goods_list.to_alipay_dict()
            else:
                params['goods_list'] = self.goods_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataItemGoodsList()
        if 'desc' in d:
            o.desc = d['desc']
        if 'goods_list' in d:
            o.goods_list = d['goods_list']
        return o


