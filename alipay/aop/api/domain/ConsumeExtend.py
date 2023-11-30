#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsumeExtend(object):

    def __init__(self):
        self._mall_assign_store = None
        self._recycle_industry = None

    @property
    def mall_assign_store(self):
        return self._mall_assign_store

    @mall_assign_store.setter
    def mall_assign_store(self, value):
        self._mall_assign_store = value
    @property
    def recycle_industry(self):
        return self._recycle_industry

    @recycle_industry.setter
    def recycle_industry(self, value):
        self._recycle_industry = value


    def to_alipay_dict(self):
        params = dict()
        if self.mall_assign_store:
            if hasattr(self.mall_assign_store, 'to_alipay_dict'):
                params['mall_assign_store'] = self.mall_assign_store.to_alipay_dict()
            else:
                params['mall_assign_store'] = self.mall_assign_store
        if self.recycle_industry:
            if hasattr(self.recycle_industry, 'to_alipay_dict'):
                params['recycle_industry'] = self.recycle_industry.to_alipay_dict()
            else:
                params['recycle_industry'] = self.recycle_industry
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumeExtend()
        if 'mall_assign_store' in d:
            o.mall_assign_store = d['mall_assign_store']
        if 'recycle_industry' in d:
            o.recycle_industry = d['recycle_industry']
        return o


