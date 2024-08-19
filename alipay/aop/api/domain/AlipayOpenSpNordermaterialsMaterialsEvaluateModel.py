#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopMaterialsValidInfo import ShopMaterialsValidInfo


class AlipayOpenSpNordermaterialsMaterialsEvaluateModel(object):

    def __init__(self):
        self._production_order_no = None
        self._shop_materials_valid_info = None

    @property
    def production_order_no(self):
        return self._production_order_no

    @production_order_no.setter
    def production_order_no(self, value):
        self._production_order_no = value
    @property
    def shop_materials_valid_info(self):
        return self._shop_materials_valid_info

    @shop_materials_valid_info.setter
    def shop_materials_valid_info(self, value):
        if isinstance(value, list):
            self._shop_materials_valid_info = list()
            for i in value:
                if isinstance(i, ShopMaterialsValidInfo):
                    self._shop_materials_valid_info.append(i)
                else:
                    self._shop_materials_valid_info.append(ShopMaterialsValidInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.production_order_no:
            if hasattr(self.production_order_no, 'to_alipay_dict'):
                params['production_order_no'] = self.production_order_no.to_alipay_dict()
            else:
                params['production_order_no'] = self.production_order_no
        if self.shop_materials_valid_info:
            if isinstance(self.shop_materials_valid_info, list):
                for i in range(0, len(self.shop_materials_valid_info)):
                    element = self.shop_materials_valid_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_materials_valid_info[i] = element.to_alipay_dict()
            if hasattr(self.shop_materials_valid_info, 'to_alipay_dict'):
                params['shop_materials_valid_info'] = self.shop_materials_valid_info.to_alipay_dict()
            else:
                params['shop_materials_valid_info'] = self.shop_materials_valid_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordermaterialsMaterialsEvaluateModel()
        if 'production_order_no' in d:
            o.production_order_no = d['production_order_no']
        if 'shop_materials_valid_info' in d:
            o.shop_materials_valid_info = d['shop_materials_valid_info']
        return o


