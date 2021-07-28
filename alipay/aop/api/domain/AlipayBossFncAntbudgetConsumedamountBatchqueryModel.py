#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncAntbudgetConsumedamountBatchqueryModel(object):

    def __init__(self):
        self._biz_uk_ids = None
        self._ns = None

    @property
    def biz_uk_ids(self):
        return self._biz_uk_ids

    @biz_uk_ids.setter
    def biz_uk_ids(self, value):
        if isinstance(value, list):
            self._biz_uk_ids = list()
            for i in value:
                self._biz_uk_ids.append(i)
    @property
    def ns(self):
        return self._ns

    @ns.setter
    def ns(self, value):
        self._ns = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_uk_ids:
            if isinstance(self.biz_uk_ids, list):
                for i in range(0, len(self.biz_uk_ids)):
                    element = self.biz_uk_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_uk_ids[i] = element.to_alipay_dict()
            if hasattr(self.biz_uk_ids, 'to_alipay_dict'):
                params['biz_uk_ids'] = self.biz_uk_ids.to_alipay_dict()
            else:
                params['biz_uk_ids'] = self.biz_uk_ids
        if self.ns:
            if hasattr(self.ns, 'to_alipay_dict'):
                params['ns'] = self.ns.to_alipay_dict()
            else:
                params['ns'] = self.ns
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncAntbudgetConsumedamountBatchqueryModel()
        if 'biz_uk_ids' in d:
            o.biz_uk_ids = d['biz_uk_ids']
        if 'ns' in d:
            o.ns = d['ns']
        return o


