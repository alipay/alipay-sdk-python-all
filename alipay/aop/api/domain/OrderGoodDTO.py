#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnvironmentalDTO import EnvironmentalDTO


class OrderGoodDTO(object):

    def __init__(self):
        self._environmental_list = None
        self._goods_id = None

    @property
    def environmental_list(self):
        return self._environmental_list

    @environmental_list.setter
    def environmental_list(self, value):
        if isinstance(value, list):
            self._environmental_list = list()
            for i in value:
                if isinstance(i, EnvironmentalDTO):
                    self._environmental_list.append(i)
                else:
                    self._environmental_list.append(EnvironmentalDTO.from_alipay_dict(i))
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.environmental_list:
            if isinstance(self.environmental_list, list):
                for i in range(0, len(self.environmental_list)):
                    element = self.environmental_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.environmental_list[i] = element.to_alipay_dict()
            if hasattr(self.environmental_list, 'to_alipay_dict'):
                params['environmental_list'] = self.environmental_list.to_alipay_dict()
            else:
                params['environmental_list'] = self.environmental_list
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderGoodDTO()
        if 'environmental_list' in d:
            o.environmental_list = d['environmental_list']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        return o


