#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtraInfo import ExtraInfo
from alipay.aop.api.domain.Goods import Goods


class CateringGoodsInfo(object):

    def __init__(self):
        self._goods_extra_info = None
        self._goods_list = None

    @property
    def goods_extra_info(self):
        return self._goods_extra_info

    @goods_extra_info.setter
    def goods_extra_info(self, value):
        if isinstance(value, list):
            self._goods_extra_info = list()
            for i in value:
                if isinstance(i, ExtraInfo):
                    self._goods_extra_info.append(i)
                else:
                    self._goods_extra_info.append(ExtraInfo.from_alipay_dict(i))
    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                if isinstance(i, Goods):
                    self._goods_list.append(i)
                else:
                    self._goods_list.append(Goods.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.goods_extra_info:
            if isinstance(self.goods_extra_info, list):
                for i in range(0, len(self.goods_extra_info)):
                    element = self.goods_extra_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_extra_info[i] = element.to_alipay_dict()
            if hasattr(self.goods_extra_info, 'to_alipay_dict'):
                params['goods_extra_info'] = self.goods_extra_info.to_alipay_dict()
            else:
                params['goods_extra_info'] = self.goods_extra_info
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
        o = CateringGoodsInfo()
        if 'goods_extra_info' in d:
            o.goods_extra_info = d['goods_extra_info']
        if 'goods_list' in d:
            o.goods_list = d['goods_list']
        return o


