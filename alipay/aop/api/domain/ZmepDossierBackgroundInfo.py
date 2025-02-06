#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmepDossierBackgroundInfo(object):

    def __init__(self):
        self._label = None

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        if isinstance(value, list):
            self._label = list()
            for i in value:
                self._label.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.label:
            if isinstance(self.label, list):
                for i in range(0, len(self.label)):
                    element = self.label[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.label[i] = element.to_alipay_dict()
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmepDossierBackgroundInfo()
        if 'label' in d:
            o.label = d['label']
        return o


