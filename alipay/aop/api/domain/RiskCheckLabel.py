#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CheckSubLabel import CheckSubLabel


class RiskCheckLabel(object):

    def __init__(self):
        self._check_sub_labels = None
        self._label = None
        self._rate = None

    @property
    def check_sub_labels(self):
        return self._check_sub_labels

    @check_sub_labels.setter
    def check_sub_labels(self, value):
        if isinstance(value, list):
            self._check_sub_labels = list()
            for i in value:
                if isinstance(i, CheckSubLabel):
                    self._check_sub_labels.append(i)
                else:
                    self._check_sub_labels.append(CheckSubLabel.from_alipay_dict(i))
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_sub_labels:
            if isinstance(self.check_sub_labels, list):
                for i in range(0, len(self.check_sub_labels)):
                    element = self.check_sub_labels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_sub_labels[i] = element.to_alipay_dict()
            if hasattr(self.check_sub_labels, 'to_alipay_dict'):
                params['check_sub_labels'] = self.check_sub_labels.to_alipay_dict()
            else:
                params['check_sub_labels'] = self.check_sub_labels
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskCheckLabel()
        if 'check_sub_labels' in d:
            o.check_sub_labels = d['check_sub_labels']
        if 'label' in d:
            o.label = d['label']
        if 'rate' in d:
            o.rate = d['rate']
        return o


