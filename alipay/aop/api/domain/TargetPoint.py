#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TargetKeyValue import TargetKeyValue


class TargetPoint(object):

    def __init__(self):
        self._target_no = None
        self._target_no_attributes = None

    @property
    def target_no(self):
        return self._target_no

    @target_no.setter
    def target_no(self, value):
        self._target_no = value
    @property
    def target_no_attributes(self):
        return self._target_no_attributes

    @target_no_attributes.setter
    def target_no_attributes(self, value):
        if isinstance(value, list):
            self._target_no_attributes = list()
            for i in value:
                if isinstance(i, TargetKeyValue):
                    self._target_no_attributes.append(i)
                else:
                    self._target_no_attributes.append(TargetKeyValue.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.target_no:
            if hasattr(self.target_no, 'to_alipay_dict'):
                params['target_no'] = self.target_no.to_alipay_dict()
            else:
                params['target_no'] = self.target_no
        if self.target_no_attributes:
            if isinstance(self.target_no_attributes, list):
                for i in range(0, len(self.target_no_attributes)):
                    element = self.target_no_attributes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_no_attributes[i] = element.to_alipay_dict()
            if hasattr(self.target_no_attributes, 'to_alipay_dict'):
                params['target_no_attributes'] = self.target_no_attributes.to_alipay_dict()
            else:
                params['target_no_attributes'] = self.target_no_attributes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TargetPoint()
        if 'target_no' in d:
            o.target_no = d['target_no']
        if 'target_no_attributes' in d:
            o.target_no_attributes = d['target_no_attributes']
        return o


