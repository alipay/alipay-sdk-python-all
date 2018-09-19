#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FilterTag import FilterTag


class DataEnumValue(object):

    def __init__(self):
        self._filter_tags = None
        self._label = None
        self._value = None

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
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataEnumValue()
        if 'filter_tags' in d:
            o.filter_tags = d['filter_tags']
        if 'label' in d:
            o.label = d['label']
        if 'value' in d:
            o.value = d['value']
        return o


