#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopAppRelation import ShopAppRelation


class AlipayMerchantStoreMiniappBindModel(object):

    def __init__(self):
        self._operation = None
        self._shop_app_relation = None

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value
    @property
    def shop_app_relation(self):
        return self._shop_app_relation

    @shop_app_relation.setter
    def shop_app_relation(self, value):
        if isinstance(value, list):
            self._shop_app_relation = list()
            for i in value:
                if isinstance(i, ShopAppRelation):
                    self._shop_app_relation.append(i)
                else:
                    self._shop_app_relation.append(ShopAppRelation.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        if self.shop_app_relation:
            if isinstance(self.shop_app_relation, list):
                for i in range(0, len(self.shop_app_relation)):
                    element = self.shop_app_relation[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_app_relation[i] = element.to_alipay_dict()
            if hasattr(self.shop_app_relation, 'to_alipay_dict'):
                params['shop_app_relation'] = self.shop_app_relation.to_alipay_dict()
            else:
                params['shop_app_relation'] = self.shop_app_relation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantStoreMiniappBindModel()
        if 'operation' in d:
            o.operation = d['operation']
        if 'shop_app_relation' in d:
            o.shop_app_relation = d['shop_app_relation']
        return o


