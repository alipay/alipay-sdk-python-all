#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductRelationDTO import ProductRelationDTO


class AlipayCommerceRetailCashbackrelationSyncModel(object):

    def __init__(self):
        self._batch_id = None
        self._delivery_plan_id = None
        self._operate_type = None
        self._product_relation_list = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def delivery_plan_id(self):
        return self._delivery_plan_id

    @delivery_plan_id.setter
    def delivery_plan_id(self, value):
        self._delivery_plan_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def product_relation_list(self):
        return self._product_relation_list

    @product_relation_list.setter
    def product_relation_list(self, value):
        if isinstance(value, list):
            self._product_relation_list = list()
            for i in value:
                if isinstance(i, ProductRelationDTO):
                    self._product_relation_list.append(i)
                else:
                    self._product_relation_list.append(ProductRelationDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.delivery_plan_id:
            if hasattr(self.delivery_plan_id, 'to_alipay_dict'):
                params['delivery_plan_id'] = self.delivery_plan_id.to_alipay_dict()
            else:
                params['delivery_plan_id'] = self.delivery_plan_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.product_relation_list:
            if isinstance(self.product_relation_list, list):
                for i in range(0, len(self.product_relation_list)):
                    element = self.product_relation_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_relation_list[i] = element.to_alipay_dict()
            if hasattr(self.product_relation_list, 'to_alipay_dict'):
                params['product_relation_list'] = self.product_relation_list.to_alipay_dict()
            else:
                params['product_relation_list'] = self.product_relation_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailCashbackrelationSyncModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'delivery_plan_id' in d:
            o.delivery_plan_id = d['delivery_plan_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'product_relation_list' in d:
            o.product_relation_list = d['product_relation_list']
        return o


