#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsSafetyInventory import GoodsSafetyInventory


class KoubeiRetailWmsGoodssafetyinventoryModifyModel(object):

    def __init__(self):
        self._goods_safety_inventorys = None

    @property
    def goods_safety_inventorys(self):
        return self._goods_safety_inventorys

    @goods_safety_inventorys.setter
    def goods_safety_inventorys(self, value):
        if isinstance(value, list):
            self._goods_safety_inventorys = list()
            for i in value:
                if isinstance(i, GoodsSafetyInventory):
                    self._goods_safety_inventorys.append(i)
                else:
                    self._goods_safety_inventorys.append(GoodsSafetyInventory.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.goods_safety_inventorys:
            if isinstance(self.goods_safety_inventorys, list):
                for i in range(0, len(self.goods_safety_inventorys)):
                    element = self.goods_safety_inventorys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_safety_inventorys[i] = element.to_alipay_dict()
            if hasattr(self.goods_safety_inventorys, 'to_alipay_dict'):
                params['goods_safety_inventorys'] = self.goods_safety_inventorys.to_alipay_dict()
            else:
                params['goods_safety_inventorys'] = self.goods_safety_inventorys
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsGoodssafetyinventoryModifyModel()
        if 'goods_safety_inventorys' in d:
            o.goods_safety_inventorys = d['goods_safety_inventorys']
        return o


