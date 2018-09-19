#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataTradeHabbitQueryModel(object):

    def __init__(self):
        self._biz_date = None
        self._store_ids = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def store_ids(self):
        return self._store_ids

    @store_ids.setter
    def store_ids(self, value):
        self._store_ids = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.store_ids:
            if hasattr(self.store_ids, 'to_alipay_dict'):
                params['store_ids'] = self.store_ids.to_alipay_dict()
            else:
                params['store_ids'] = self.store_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataTradeHabbitQueryModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'store_ids' in d:
            o.store_ids = d['store_ids']
        return o


