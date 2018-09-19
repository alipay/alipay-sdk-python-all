#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Matcher import Matcher


class AlipayOpenPublicMatchuserLabelCreateModel(object):

    def __init__(self):
        self._label_id = None
        self._label_value = None
        self._matchers = None

    @property
    def label_id(self):
        return self._label_id

    @label_id.setter
    def label_id(self, value):
        self._label_id = value
    @property
    def label_value(self):
        return self._label_value

    @label_value.setter
    def label_value(self, value):
        self._label_value = value
    @property
    def matchers(self):
        return self._matchers

    @matchers.setter
    def matchers(self, value):
        if isinstance(value, list):
            self._matchers = list()
            for i in value:
                if isinstance(i, Matcher):
                    self._matchers.append(i)
                else:
                    self._matchers.append(Matcher.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.label_id:
            if hasattr(self.label_id, 'to_alipay_dict'):
                params['label_id'] = self.label_id.to_alipay_dict()
            else:
                params['label_id'] = self.label_id
        if self.label_value:
            if hasattr(self.label_value, 'to_alipay_dict'):
                params['label_value'] = self.label_value.to_alipay_dict()
            else:
                params['label_value'] = self.label_value
        if self.matchers:
            if isinstance(self.matchers, list):
                for i in range(0, len(self.matchers)):
                    element = self.matchers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.matchers[i] = element.to_alipay_dict()
            if hasattr(self.matchers, 'to_alipay_dict'):
                params['matchers'] = self.matchers.to_alipay_dict()
            else:
                params['matchers'] = self.matchers
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicMatchuserLabelCreateModel()
        if 'label_id' in d:
            o.label_id = d['label_id']
        if 'label_value' in d:
            o.label_value = d['label_value']
        if 'matchers' in d:
            o.matchers = d['matchers']
        return o


