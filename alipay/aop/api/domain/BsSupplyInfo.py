#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BsSupplyDiscountInfo import BsSupplyDiscountInfo
from alipay.aop.api.domain.BsSupplyItemInfo import BsSupplyItemInfo


class BsSupplyInfo(object):

    def __init__(self):
        self._benefit_discount = None
        self._benefit_item_info = None
        self._description_doc = None
        self._sub_type = None
        self._suppl_type = None
        self._supply_id = None
        self._supply_name = None

    @property
    def benefit_discount(self):
        return self._benefit_discount

    @benefit_discount.setter
    def benefit_discount(self, value):
        if isinstance(value, BsSupplyDiscountInfo):
            self._benefit_discount = value
        else:
            self._benefit_discount = BsSupplyDiscountInfo.from_alipay_dict(value)
    @property
    def benefit_item_info(self):
        return self._benefit_item_info

    @benefit_item_info.setter
    def benefit_item_info(self, value):
        if isinstance(value, BsSupplyItemInfo):
            self._benefit_item_info = value
        else:
            self._benefit_item_info = BsSupplyItemInfo.from_alipay_dict(value)
    @property
    def description_doc(self):
        return self._description_doc

    @description_doc.setter
    def description_doc(self, value):
        self._description_doc = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def suppl_type(self):
        return self._suppl_type

    @suppl_type.setter
    def suppl_type(self, value):
        self._suppl_type = value
    @property
    def supply_id(self):
        return self._supply_id

    @supply_id.setter
    def supply_id(self, value):
        self._supply_id = value
    @property
    def supply_name(self):
        return self._supply_name

    @supply_name.setter
    def supply_name(self, value):
        self._supply_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_discount:
            if hasattr(self.benefit_discount, 'to_alipay_dict'):
                params['benefit_discount'] = self.benefit_discount.to_alipay_dict()
            else:
                params['benefit_discount'] = self.benefit_discount
        if self.benefit_item_info:
            if hasattr(self.benefit_item_info, 'to_alipay_dict'):
                params['benefit_item_info'] = self.benefit_item_info.to_alipay_dict()
            else:
                params['benefit_item_info'] = self.benefit_item_info
        if self.description_doc:
            if hasattr(self.description_doc, 'to_alipay_dict'):
                params['description_doc'] = self.description_doc.to_alipay_dict()
            else:
                params['description_doc'] = self.description_doc
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.suppl_type:
            if hasattr(self.suppl_type, 'to_alipay_dict'):
                params['suppl_type'] = self.suppl_type.to_alipay_dict()
            else:
                params['suppl_type'] = self.suppl_type
        if self.supply_id:
            if hasattr(self.supply_id, 'to_alipay_dict'):
                params['supply_id'] = self.supply_id.to_alipay_dict()
            else:
                params['supply_id'] = self.supply_id
        if self.supply_name:
            if hasattr(self.supply_name, 'to_alipay_dict'):
                params['supply_name'] = self.supply_name.to_alipay_dict()
            else:
                params['supply_name'] = self.supply_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsSupplyInfo()
        if 'benefit_discount' in d:
            o.benefit_discount = d['benefit_discount']
        if 'benefit_item_info' in d:
            o.benefit_item_info = d['benefit_item_info']
        if 'description_doc' in d:
            o.description_doc = d['description_doc']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'suppl_type' in d:
            o.suppl_type = d['suppl_type']
        if 'supply_id' in d:
            o.supply_id = d['supply_id']
        if 'supply_name' in d:
            o.supply_name = d['supply_name']
        return o


