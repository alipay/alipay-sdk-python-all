#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext


class KoubeiRetailWmsInventoryBatchqueryModel(object):

    def __init__(self):
        self._goods_code_list = None
        self._inventory_type = None
        self._operate_context = None
        self._warehouse_code = None

    @property
    def goods_code_list(self):
        return self._goods_code_list

    @goods_code_list.setter
    def goods_code_list(self, value):
        if isinstance(value, list):
            self._goods_code_list = list()
            for i in value:
                self._goods_code_list.append(i)
    @property
    def inventory_type(self):
        return self._inventory_type

    @inventory_type.setter
    def inventory_type(self, value):
        self._inventory_type = value
    @property
    def operate_context(self):
        return self._operate_context

    @operate_context.setter
    def operate_context(self, value):
        if isinstance(value, OperateContext):
            self._operate_context = value
        else:
            self._operate_context = OperateContext.from_alipay_dict(value)
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_code_list:
            if isinstance(self.goods_code_list, list):
                for i in range(0, len(self.goods_code_list)):
                    element = self.goods_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_code_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_code_list, 'to_alipay_dict'):
                params['goods_code_list'] = self.goods_code_list.to_alipay_dict()
            else:
                params['goods_code_list'] = self.goods_code_list
        if self.inventory_type:
            if hasattr(self.inventory_type, 'to_alipay_dict'):
                params['inventory_type'] = self.inventory_type.to_alipay_dict()
            else:
                params['inventory_type'] = self.inventory_type
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsInventoryBatchqueryModel()
        if 'goods_code_list' in d:
            o.goods_code_list = d['goods_code_list']
        if 'inventory_type' in d:
            o.inventory_type = d['inventory_type']
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


