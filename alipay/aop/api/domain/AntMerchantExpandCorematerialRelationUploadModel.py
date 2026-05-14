#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SupplierRelData import SupplierRelData


class AntMerchantExpandCorematerialRelationUploadModel(object):

    def __init__(self):
        self._supplier_rel_list = None

    @property
    def supplier_rel_list(self):
        return self._supplier_rel_list

    @supplier_rel_list.setter
    def supplier_rel_list(self, value):
        if isinstance(value, list):
            self._supplier_rel_list = list()
            for i in value:
                if isinstance(i, SupplierRelData):
                    self._supplier_rel_list.append(i)
                else:
                    self._supplier_rel_list.append(SupplierRelData.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.supplier_rel_list:
            if isinstance(self.supplier_rel_list, list):
                for i in range(0, len(self.supplier_rel_list)):
                    element = self.supplier_rel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.supplier_rel_list[i] = element.to_alipay_dict()
            if hasattr(self.supplier_rel_list, 'to_alipay_dict'):
                params['supplier_rel_list'] = self.supplier_rel_list.to_alipay_dict()
            else:
                params['supplier_rel_list'] = self.supplier_rel_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandCorematerialRelationUploadModel()
        if 'supplier_rel_list' in d:
            o.supplier_rel_list = d['supplier_rel_list']
        return o


