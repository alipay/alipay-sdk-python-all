#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotGroupBatchqueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._limit = None
        self._offset = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotGroupBatchqueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'limit' in d:
            o.limit = d['limit']
        if 'offset' in d:
            o.offset = d['offset']
        return o


