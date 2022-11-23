#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubCheckLabel import SubCheckLabel


class DetectCheckLabel(object):

    def __init__(self):
        self._label = None
        self._rate = None
        self._sub_check_labels = None

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
    @property
    def sub_check_labels(self):
        return self._sub_check_labels

    @sub_check_labels.setter
    def sub_check_labels(self, value):
        if isinstance(value, list):
            self._sub_check_labels = list()
            for i in value:
                if isinstance(i, SubCheckLabel):
                    self._sub_check_labels.append(i)
                else:
                    self._sub_check_labels.append(SubCheckLabel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
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
        if self.sub_check_labels:
            if isinstance(self.sub_check_labels, list):
                for i in range(0, len(self.sub_check_labels)):
                    element = self.sub_check_labels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_check_labels[i] = element.to_alipay_dict()
            if hasattr(self.sub_check_labels, 'to_alipay_dict'):
                params['sub_check_labels'] = self.sub_check_labels.to_alipay_dict()
            else:
                params['sub_check_labels'] = self.sub_check_labels
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DetectCheckLabel()
        if 'label' in d:
            o.label = d['label']
        if 'rate' in d:
            o.rate = d['rate']
        if 'sub_check_labels' in d:
            o.sub_check_labels = d['sub_check_labels']
        return o


