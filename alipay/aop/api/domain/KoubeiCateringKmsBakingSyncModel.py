#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KmsBakingCheckDTO import KmsBakingCheckDTO
from alipay.aop.api.domain.KmsBakingInventoryDTO import KmsBakingInventoryDTO
from alipay.aop.api.domain.KmsBakingPromotionDTO import KmsBakingPromotionDTO


class KoubeiCateringKmsBakingSyncModel(object):

    def __init__(self):
        self._action = None
        self._check_data = None
        self._inventory_data = None
        self._promotion_data = None
        self._shop_id = None
        self._type = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def check_data(self):
        return self._check_data

    @check_data.setter
    def check_data(self, value):
        if isinstance(value, KmsBakingCheckDTO):
            self._check_data = value
        else:
            self._check_data = KmsBakingCheckDTO.from_alipay_dict(value)
    @property
    def inventory_data(self):
        return self._inventory_data

    @inventory_data.setter
    def inventory_data(self, value):
        if isinstance(value, list):
            self._inventory_data = list()
            for i in value:
                if isinstance(i, KmsBakingInventoryDTO):
                    self._inventory_data.append(i)
                else:
                    self._inventory_data.append(KmsBakingInventoryDTO.from_alipay_dict(i))
    @property
    def promotion_data(self):
        return self._promotion_data

    @promotion_data.setter
    def promotion_data(self, value):
        if isinstance(value, list):
            self._promotion_data = list()
            for i in value:
                if isinstance(i, KmsBakingPromotionDTO):
                    self._promotion_data.append(i)
                else:
                    self._promotion_data.append(KmsBakingPromotionDTO.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.check_data:
            if hasattr(self.check_data, 'to_alipay_dict'):
                params['check_data'] = self.check_data.to_alipay_dict()
            else:
                params['check_data'] = self.check_data
        if self.inventory_data:
            if isinstance(self.inventory_data, list):
                for i in range(0, len(self.inventory_data)):
                    element = self.inventory_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inventory_data[i] = element.to_alipay_dict()
            if hasattr(self.inventory_data, 'to_alipay_dict'):
                params['inventory_data'] = self.inventory_data.to_alipay_dict()
            else:
                params['inventory_data'] = self.inventory_data
        if self.promotion_data:
            if isinstance(self.promotion_data, list):
                for i in range(0, len(self.promotion_data)):
                    element = self.promotion_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promotion_data[i] = element.to_alipay_dict()
            if hasattr(self.promotion_data, 'to_alipay_dict'):
                params['promotion_data'] = self.promotion_data.to_alipay_dict()
            else:
                params['promotion_data'] = self.promotion_data
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringKmsBakingSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'check_data' in d:
            o.check_data = d['check_data']
        if 'inventory_data' in d:
            o.inventory_data = d['inventory_data']
        if 'promotion_data' in d:
            o.promotion_data = d['promotion_data']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'type' in d:
            o.type = d['type']
        return o


