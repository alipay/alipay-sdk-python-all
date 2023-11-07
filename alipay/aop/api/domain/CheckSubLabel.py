#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CheckSubLabel(object):

    def __init__(self):
        self._rate = None
        self._sub_label = None

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def sub_label(self):
        return self._sub_label

    @sub_label.setter
    def sub_label(self, value):
        self._sub_label = value


    def to_alipay_dict(self):
        params = dict()
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.sub_label:
            if hasattr(self.sub_label, 'to_alipay_dict'):
                params['sub_label'] = self.sub_label.to_alipay_dict()
            else:
                params['sub_label'] = self.sub_label
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CheckSubLabel()
        if 'rate' in d:
            o.rate = d['rate']
        if 'sub_label' in d:
            o.sub_label = d['sub_label']
        return o


