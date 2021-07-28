#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotSnApplyBatchqueryModel(object):

    def __init__(self):
        self._limit = None
        self._offset = None
        self._supplier_id = None

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        self._limit = value
    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.limit:
            if hasattr(self.limit, 'to_alipay_dict'):
                params['limit'] = self.limit.to_alipay_dict()
            else:
                params['limit'] = self.limit
        if self.offset:
            if hasattr(self.offset, 'to_alipay_dict'):
                params['offset'] = self.offset.to_alipay_dict()
            else:
                params['offset'] = self.offset
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotSnApplyBatchqueryModel()
        if 'limit' in d:
            o.limit = d['limit']
        if 'offset' in d:
            o.offset = d['offset']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


