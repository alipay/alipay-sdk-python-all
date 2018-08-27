#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FilterTag import FilterTag


class KoubeiMarketingDataCustomreportQueryModel(object):

    def __init__(self):
        self._condition_key = None
        self._filter_tags = None
        self._max_count = None

    @property
    def condition_key(self):
        return self._condition_key

    @condition_key.setter
    def condition_key(self, value):
        self._condition_key = value
    @property
    def filter_tags(self):
        return self._filter_tags

    @filter_tags.setter
    def filter_tags(self, value):
        if isinstance(value, list):
            self._filter_tags = list()
            for i in value:
                if isinstance(i, FilterTag):
                    self._filter_tags.append(i)
                else:
                    self._filter_tags.append(FilterTag.from_alipay_dict(i))
    @property
    def max_count(self):
        return self._max_count

    @max_count.setter
    def max_count(self, value):
        self._max_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition_key:
            if hasattr(self.condition_key, 'to_alipay_dict'):
                params['condition_key'] = self.condition_key.to_alipay_dict()
            else:
                params['condition_key'] = self.condition_key
        if self.filter_tags:
            if isinstance(self.filter_tags, list):
                for i in range(0, len(self.filter_tags)):
                    element = self.filter_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.filter_tags[i] = element.to_alipay_dict()
            if hasattr(self.filter_tags, 'to_alipay_dict'):
                params['filter_tags'] = self.filter_tags.to_alipay_dict()
            else:
                params['filter_tags'] = self.filter_tags
        if self.max_count:
            if hasattr(self.max_count, 'to_alipay_dict'):
                params['max_count'] = self.max_count.to_alipay_dict()
            else:
                params['max_count'] = self.max_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataCustomreportQueryModel()
        if 'condition_key' in d:
            o.condition_key = d['condition_key']
        if 'filter_tags' in d:
            o.filter_tags = d['filter_tags']
        if 'max_count' in d:
            o.max_count = d['max_count']
        return o


