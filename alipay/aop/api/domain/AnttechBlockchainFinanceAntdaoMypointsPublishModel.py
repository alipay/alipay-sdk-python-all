#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceAntdaoMypointsPublishModel(object):

    def __init__(self):
        self._count = None
        self._memo = None
        self._method_name = None
        self._sku_id = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def method_name(self):
        return self._method_name

    @method_name.setter
    def method_name(self, value):
        self._method_name = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.method_name:
            if hasattr(self.method_name, 'to_alipay_dict'):
                params['method_name'] = self.method_name.to_alipay_dict()
            else:
                params['method_name'] = self.method_name
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceAntdaoMypointsPublishModel()
        if 'count' in d:
            o.count = d['count']
        if 'memo' in d:
            o.memo = d['memo']
        if 'method_name' in d:
            o.method_name = d['method_name']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


