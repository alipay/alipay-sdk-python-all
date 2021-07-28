#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PriceDetailDTO import PriceDetailDTO


class MarketResult(object):

    def __init__(self):
        self._price_detail_list = None
        self._scene = None

    @property
    def price_detail_list(self):
        return self._price_detail_list

    @price_detail_list.setter
    def price_detail_list(self, value):
        if isinstance(value, list):
            self._price_detail_list = list()
            for i in value:
                if isinstance(i, PriceDetailDTO):
                    self._price_detail_list.append(i)
                else:
                    self._price_detail_list.append(PriceDetailDTO.from_alipay_dict(i))
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.price_detail_list:
            if isinstance(self.price_detail_list, list):
                for i in range(0, len(self.price_detail_list)):
                    element = self.price_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.price_detail_list, 'to_alipay_dict'):
                params['price_detail_list'] = self.price_detail_list.to_alipay_dict()
            else:
                params['price_detail_list'] = self.price_detail_list
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarketResult()
        if 'price_detail_list' in d:
            o.price_detail_list = d['price_detail_list']
        if 'scene' in d:
            o.scene = d['scene']
        return o


