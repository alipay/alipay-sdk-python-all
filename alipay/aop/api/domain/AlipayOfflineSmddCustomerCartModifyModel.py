#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CodeExtBean import CodeExtBean
from alipay.aop.api.domain.SkuBean import SkuBean


class AlipayOfflineSmddCustomerCartModifyModel(object):

    def __init__(self):
        self._buyer_id = None
        self._code_ext = None
        self._operation_type = None
        self._shop_id = None
        self._sku_list = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def code_ext(self):
        return self._code_ext

    @code_ext.setter
    def code_ext(self, value):
        if isinstance(value, CodeExtBean):
            self._code_ext = value
        else:
            self._code_ext = CodeExtBean.from_alipay_dict(value)
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, SkuBean):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(SkuBean.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.code_ext:
            if hasattr(self.code_ext, 'to_alipay_dict'):
                params['code_ext'] = self.code_ext.to_alipay_dict()
            else:
                params['code_ext'] = self.code_ext
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sku_list:
            if isinstance(self.sku_list, list):
                for i in range(0, len(self.sku_list)):
                    element = self.sku_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_list, 'to_alipay_dict'):
                params['sku_list'] = self.sku_list.to_alipay_dict()
            else:
                params['sku_list'] = self.sku_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineSmddCustomerCartModifyModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'code_ext' in d:
            o.code_ext = d['code_ext']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        return o


