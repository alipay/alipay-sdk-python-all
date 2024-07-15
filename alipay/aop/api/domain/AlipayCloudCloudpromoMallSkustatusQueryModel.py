#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SkuQueryParam import SkuQueryParam


class AlipayCloudCloudpromoMallSkustatusQueryModel(object):

    def __init__(self):
        self._division_code = None
        self._purchaser_id = None
        self._sku_query_params = None

    @property
    def division_code(self):
        return self._division_code

    @division_code.setter
    def division_code(self, value):
        self._division_code = value
    @property
    def purchaser_id(self):
        return self._purchaser_id

    @purchaser_id.setter
    def purchaser_id(self, value):
        self._purchaser_id = value
    @property
    def sku_query_params(self):
        return self._sku_query_params

    @sku_query_params.setter
    def sku_query_params(self, value):
        if isinstance(value, list):
            self._sku_query_params = list()
            for i in value:
                if isinstance(i, SkuQueryParam):
                    self._sku_query_params.append(i)
                else:
                    self._sku_query_params.append(SkuQueryParam.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.division_code:
            if hasattr(self.division_code, 'to_alipay_dict'):
                params['division_code'] = self.division_code.to_alipay_dict()
            else:
                params['division_code'] = self.division_code
        if self.purchaser_id:
            if hasattr(self.purchaser_id, 'to_alipay_dict'):
                params['purchaser_id'] = self.purchaser_id.to_alipay_dict()
            else:
                params['purchaser_id'] = self.purchaser_id
        if self.sku_query_params:
            if isinstance(self.sku_query_params, list):
                for i in range(0, len(self.sku_query_params)):
                    element = self.sku_query_params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_query_params[i] = element.to_alipay_dict()
            if hasattr(self.sku_query_params, 'to_alipay_dict'):
                params['sku_query_params'] = self.sku_query_params.to_alipay_dict()
            else:
                params['sku_query_params'] = self.sku_query_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMallSkustatusQueryModel()
        if 'division_code' in d:
            o.division_code = d['division_code']
        if 'purchaser_id' in d:
            o.purchaser_id = d['purchaser_id']
        if 'sku_query_params' in d:
            o.sku_query_params = d['sku_query_params']
        return o


