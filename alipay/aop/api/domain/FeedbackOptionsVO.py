#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FeedbackSuboption import FeedbackSuboption


class FeedbackOptionsVO(object):

    def __init__(self):
        self._primary_class = None
        self._primary_class_code = None
        self._suboption = None

    @property
    def primary_class(self):
        return self._primary_class

    @primary_class.setter
    def primary_class(self, value):
        self._primary_class = value
    @property
    def primary_class_code(self):
        return self._primary_class_code

    @primary_class_code.setter
    def primary_class_code(self, value):
        self._primary_class_code = value
    @property
    def suboption(self):
        return self._suboption

    @suboption.setter
    def suboption(self, value):
        if isinstance(value, list):
            self._suboption = list()
            for i in value:
                if isinstance(i, FeedbackSuboption):
                    self._suboption.append(i)
                else:
                    self._suboption.append(FeedbackSuboption.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.primary_class:
            if hasattr(self.primary_class, 'to_alipay_dict'):
                params['primary_class'] = self.primary_class.to_alipay_dict()
            else:
                params['primary_class'] = self.primary_class
        if self.primary_class_code:
            if hasattr(self.primary_class_code, 'to_alipay_dict'):
                params['primary_class_code'] = self.primary_class_code.to_alipay_dict()
            else:
                params['primary_class_code'] = self.primary_class_code
        if self.suboption:
            if isinstance(self.suboption, list):
                for i in range(0, len(self.suboption)):
                    element = self.suboption[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.suboption[i] = element.to_alipay_dict()
            if hasattr(self.suboption, 'to_alipay_dict'):
                params['suboption'] = self.suboption.to_alipay_dict()
            else:
                params['suboption'] = self.suboption
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FeedbackOptionsVO()
        if 'primary_class' in d:
            o.primary_class = d['primary_class']
        if 'primary_class_code' in d:
            o.primary_class_code = d['primary_class_code']
        if 'suboption' in d:
            o.suboption = d['suboption']
        return o


