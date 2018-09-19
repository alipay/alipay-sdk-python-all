#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext


class KoubeiRetailWmsSupplierQueryModel(object):

    def __init__(self):
        self._operate_context = None
        self._supplier_ids = None

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
    def supplier_ids(self):
        return self._supplier_ids

    @supplier_ids.setter
    def supplier_ids(self, value):
        if isinstance(value, list):
            self._supplier_ids = list()
            for i in value:
                self._supplier_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
        if self.supplier_ids:
            if isinstance(self.supplier_ids, list):
                for i in range(0, len(self.supplier_ids)):
                    element = self.supplier_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.supplier_ids[i] = element.to_alipay_dict()
            if hasattr(self.supplier_ids, 'to_alipay_dict'):
                params['supplier_ids'] = self.supplier_ids.to_alipay_dict()
            else:
                params['supplier_ids'] = self.supplier_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsSupplierQueryModel()
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'supplier_ids' in d:
            o.supplier_ids = d['supplier_ids']
        return o


