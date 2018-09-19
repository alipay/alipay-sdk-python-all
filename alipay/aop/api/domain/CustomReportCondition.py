#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DataTag import DataTag
from alipay.aop.api.domain.FilterTag import FilterTag


class CustomReportCondition(object):

    def __init__(self):
        self._condition_key = None
        self._data_tags = None
        self._filter_tags = None
        self._group_tags = None
        self._memo = None
        self._name = None
        self._sort_tags = None

    @property
    def condition_key(self):
        return self._condition_key

    @condition_key.setter
    def condition_key(self, value):
        self._condition_key = value
    @property
    def data_tags(self):
        return self._data_tags

    @data_tags.setter
    def data_tags(self, value):
        if isinstance(value, list):
            self._data_tags = list()
            for i in value:
                if isinstance(i, DataTag):
                    self._data_tags.append(i)
                else:
                    self._data_tags.append(DataTag.from_alipay_dict(i))
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
    def group_tags(self):
        return self._group_tags

    @group_tags.setter
    def group_tags(self, value):
        self._group_tags = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def sort_tags(self):
        return self._sort_tags

    @sort_tags.setter
    def sort_tags(self, value):
        self._sort_tags = value


    def to_alipay_dict(self):
        params = dict()
        if self.condition_key:
            if hasattr(self.condition_key, 'to_alipay_dict'):
                params['condition_key'] = self.condition_key.to_alipay_dict()
            else:
                params['condition_key'] = self.condition_key
        if self.data_tags:
            if isinstance(self.data_tags, list):
                for i in range(0, len(self.data_tags)):
                    element = self.data_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_tags[i] = element.to_alipay_dict()
            if hasattr(self.data_tags, 'to_alipay_dict'):
                params['data_tags'] = self.data_tags.to_alipay_dict()
            else:
                params['data_tags'] = self.data_tags
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
        if self.group_tags:
            if hasattr(self.group_tags, 'to_alipay_dict'):
                params['group_tags'] = self.group_tags.to_alipay_dict()
            else:
                params['group_tags'] = self.group_tags
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.sort_tags:
            if hasattr(self.sort_tags, 'to_alipay_dict'):
                params['sort_tags'] = self.sort_tags.to_alipay_dict()
            else:
                params['sort_tags'] = self.sort_tags
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomReportCondition()
        if 'condition_key' in d:
            o.condition_key = d['condition_key']
        if 'data_tags' in d:
            o.data_tags = d['data_tags']
        if 'filter_tags' in d:
            o.filter_tags = d['filter_tags']
        if 'group_tags' in d:
            o.group_tags = d['group_tags']
        if 'memo' in d:
            o.memo = d['memo']
        if 'name' in d:
            o.name = d['name']
        if 'sort_tags' in d:
            o.sort_tags = d['sort_tags']
        return o


