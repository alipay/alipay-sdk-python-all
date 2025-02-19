#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SkuCodeMappingParam import SkuCodeMappingParam


class AlipayCommerceMedicalSkuCodeModifyModel(object):

    def __init__(self):
        self._sku_code_mapping_list = None
        self._store_code = None

    @property
    def sku_code_mapping_list(self):
        return self._sku_code_mapping_list

    @sku_code_mapping_list.setter
    def sku_code_mapping_list(self, value):
        if isinstance(value, list):
            self._sku_code_mapping_list = list()
            for i in value:
                if isinstance(i, SkuCodeMappingParam):
                    self._sku_code_mapping_list.append(i)
                else:
                    self._sku_code_mapping_list.append(SkuCodeMappingParam.from_alipay_dict(i))
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.sku_code_mapping_list:
            if isinstance(self.sku_code_mapping_list, list):
                for i in range(0, len(self.sku_code_mapping_list)):
                    element = self.sku_code_mapping_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_code_mapping_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_code_mapping_list, 'to_alipay_dict'):
                params['sku_code_mapping_list'] = self.sku_code_mapping_list.to_alipay_dict()
            else:
                params['sku_code_mapping_list'] = self.sku_code_mapping_list
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalSkuCodeModifyModel()
        if 'sku_code_mapping_list' in d:
            o.sku_code_mapping_list = d['sku_code_mapping_list']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


