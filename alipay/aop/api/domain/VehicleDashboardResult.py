#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleDashboardResult(object):

    def __init__(self):
        self._class_name = None
        self._label = None
        self._score = None

    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = value
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.class_name:
            if hasattr(self.class_name, 'to_alipay_dict'):
                params['class_name'] = self.class_name.to_alipay_dict()
            else:
                params['class_name'] = self.class_name
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleDashboardResult()
        if 'class_name' in d:
            o.class_name = d['class_name']
        if 'label' in d:
            o.label = d['label']
        if 'score' in d:
            o.score = d['score']
        return o


