#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NewsAggregationValue import NewsAggregationValue
from alipay.aop.api.domain.NewsAggregationValue import NewsAggregationValue
from alipay.aop.api.domain.NewsAggregationValue import NewsAggregationValue


class NewsEntityAggregation(object):

    def __init__(self):
        self._cows = None
        self._ogws = None
        self._ppws = None

    @property
    def cows(self):
        return self._cows

    @cows.setter
    def cows(self, value):
        if isinstance(value, list):
            self._cows = list()
            for i in value:
                if isinstance(i, NewsAggregationValue):
                    self._cows.append(i)
                else:
                    self._cows.append(NewsAggregationValue.from_alipay_dict(i))
    @property
    def ogws(self):
        return self._ogws

    @ogws.setter
    def ogws(self, value):
        if isinstance(value, list):
            self._ogws = list()
            for i in value:
                if isinstance(i, NewsAggregationValue):
                    self._ogws.append(i)
                else:
                    self._ogws.append(NewsAggregationValue.from_alipay_dict(i))
    @property
    def ppws(self):
        return self._ppws

    @ppws.setter
    def ppws(self, value):
        if isinstance(value, list):
            self._ppws = list()
            for i in value:
                if isinstance(i, NewsAggregationValue):
                    self._ppws.append(i)
                else:
                    self._ppws.append(NewsAggregationValue.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.cows:
            if isinstance(self.cows, list):
                for i in range(0, len(self.cows)):
                    element = self.cows[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cows[i] = element.to_alipay_dict()
            if hasattr(self.cows, 'to_alipay_dict'):
                params['cows'] = self.cows.to_alipay_dict()
            else:
                params['cows'] = self.cows
        if self.ogws:
            if isinstance(self.ogws, list):
                for i in range(0, len(self.ogws)):
                    element = self.ogws[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ogws[i] = element.to_alipay_dict()
            if hasattr(self.ogws, 'to_alipay_dict'):
                params['ogws'] = self.ogws.to_alipay_dict()
            else:
                params['ogws'] = self.ogws
        if self.ppws:
            if isinstance(self.ppws, list):
                for i in range(0, len(self.ppws)):
                    element = self.ppws[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ppws[i] = element.to_alipay_dict()
            if hasattr(self.ppws, 'to_alipay_dict'):
                params['ppws'] = self.ppws.to_alipay_dict()
            else:
                params['ppws'] = self.ppws
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NewsEntityAggregation()
        if 'cows' in d:
            o.cows = d['cows']
        if 'ogws' in d:
            o.ogws = d['ogws']
        if 'ppws' in d:
            o.ppws = d['ppws']
        return o


