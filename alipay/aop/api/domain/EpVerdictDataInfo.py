#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpVerdictInfo import EpVerdictInfo


class EpVerdictDataInfo(object):

    def __init__(self):
        self._hits = None
        self._total = None

    @property
    def hits(self):
        return self._hits

    @hits.setter
    def hits(self, value):
        if isinstance(value, list):
            self._hits = list()
            for i in value:
                if isinstance(i, EpVerdictInfo):
                    self._hits.append(i)
                else:
                    self._hits.append(EpVerdictInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.hits:
            if isinstance(self.hits, list):
                for i in range(0, len(self.hits)):
                    element = self.hits[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hits[i] = element.to_alipay_dict()
            if hasattr(self.hits, 'to_alipay_dict'):
                params['hits'] = self.hits.to_alipay_dict()
            else:
                params['hits'] = self.hits
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpVerdictDataInfo()
        if 'hits' in d:
            o.hits = d['hits']
        if 'total' in d:
            o.total = d['total']
        return o


