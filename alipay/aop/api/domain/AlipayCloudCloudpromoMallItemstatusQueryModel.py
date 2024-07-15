#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMallItemstatusQueryModel(object):

    def __init__(self):
        self._division_code = None
        self._product_ids = None
        self._purchaser_id = None

    @property
    def division_code(self):
        return self._division_code

    @division_code.setter
    def division_code(self, value):
        self._division_code = value
    @property
    def product_ids(self):
        return self._product_ids

    @product_ids.setter
    def product_ids(self, value):
        if isinstance(value, list):
            self._product_ids = list()
            for i in value:
                self._product_ids.append(i)
    @property
    def purchaser_id(self):
        return self._purchaser_id

    @purchaser_id.setter
    def purchaser_id(self, value):
        self._purchaser_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.division_code:
            if hasattr(self.division_code, 'to_alipay_dict'):
                params['division_code'] = self.division_code.to_alipay_dict()
            else:
                params['division_code'] = self.division_code
        if self.product_ids:
            if isinstance(self.product_ids, list):
                for i in range(0, len(self.product_ids)):
                    element = self.product_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_ids[i] = element.to_alipay_dict()
            if hasattr(self.product_ids, 'to_alipay_dict'):
                params['product_ids'] = self.product_ids.to_alipay_dict()
            else:
                params['product_ids'] = self.product_ids
        if self.purchaser_id:
            if hasattr(self.purchaser_id, 'to_alipay_dict'):
                params['purchaser_id'] = self.purchaser_id.to_alipay_dict()
            else:
                params['purchaser_id'] = self.purchaser_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMallItemstatusQueryModel()
        if 'division_code' in d:
            o.division_code = d['division_code']
        if 'product_ids' in d:
            o.product_ids = d['product_ids']
        if 'purchaser_id' in d:
            o.purchaser_id = d['purchaser_id']
        return o


