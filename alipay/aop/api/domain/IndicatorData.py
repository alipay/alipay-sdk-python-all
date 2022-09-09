#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TestResult import TestResult
from alipay.aop.api.domain.TestResult import TestResult


class IndicatorData(object):

    def __init__(self):
        self._absolute = None
        self._id = None
        self._name = None
        self._relative = None

    @property
    def absolute(self):
        return self._absolute

    @absolute.setter
    def absolute(self, value):
        if isinstance(value, TestResult):
            self._absolute = value
        else:
            self._absolute = TestResult.from_alipay_dict(value)
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def relative(self):
        return self._relative

    @relative.setter
    def relative(self, value):
        if isinstance(value, TestResult):
            self._relative = value
        else:
            self._relative = TestResult.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.absolute:
            if hasattr(self.absolute, 'to_alipay_dict'):
                params['absolute'] = self.absolute.to_alipay_dict()
            else:
                params['absolute'] = self.absolute
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.relative:
            if hasattr(self.relative, 'to_alipay_dict'):
                params['relative'] = self.relative.to_alipay_dict()
            else:
                params['relative'] = self.relative
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndicatorData()
        if 'absolute' in d:
            o.absolute = d['absolute']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'relative' in d:
            o.relative = d['relative']
        return o


