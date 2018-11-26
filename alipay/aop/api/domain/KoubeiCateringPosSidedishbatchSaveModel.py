#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PosDishMaterialModel import PosDishMaterialModel


class KoubeiCateringPosSidedishbatchSaveModel(object):

    def __init__(self):
        self._dish_ids = None
        self._dish_material_list = None
        self._merchant_id = None
        self._shop_id = None

    @property
    def dish_ids(self):
        return self._dish_ids

    @dish_ids.setter
    def dish_ids(self, value):
        if isinstance(value, list):
            self._dish_ids = list()
            for i in value:
                self._dish_ids.append(i)
    @property
    def dish_material_list(self):
        return self._dish_material_list

    @dish_material_list.setter
    def dish_material_list(self, value):
        if isinstance(value, list):
            self._dish_material_list = list()
            for i in value:
                if isinstance(i, PosDishMaterialModel):
                    self._dish_material_list.append(i)
                else:
                    self._dish_material_list.append(PosDishMaterialModel.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dish_ids:
            if isinstance(self.dish_ids, list):
                for i in range(0, len(self.dish_ids)):
                    element = self.dish_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_ids[i] = element.to_alipay_dict()
            if hasattr(self.dish_ids, 'to_alipay_dict'):
                params['dish_ids'] = self.dish_ids.to_alipay_dict()
            else:
                params['dish_ids'] = self.dish_ids
        if self.dish_material_list:
            if isinstance(self.dish_material_list, list):
                for i in range(0, len(self.dish_material_list)):
                    element = self.dish_material_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_material_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_material_list, 'to_alipay_dict'):
                params['dish_material_list'] = self.dish_material_list.to_alipay_dict()
            else:
                params['dish_material_list'] = self.dish_material_list
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosSidedishbatchSaveModel()
        if 'dish_ids' in d:
            o.dish_ids = d['dish_ids']
        if 'dish_material_list' in d:
            o.dish_material_list = d['dish_material_list']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


