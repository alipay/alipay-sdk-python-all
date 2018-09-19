#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArrangementNoQuerier(object):

    def __init__(self):
        self._ar_nos = None

    @property
    def ar_nos(self):
        return self._ar_nos

    @ar_nos.setter
    def ar_nos(self, value):
        if isinstance(value, list):
            self._ar_nos = list()
            for i in value:
                self._ar_nos.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ar_nos:
            if isinstance(self.ar_nos, list):
                for i in range(0, len(self.ar_nos)):
                    element = self.ar_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ar_nos[i] = element.to_alipay_dict()
            if hasattr(self.ar_nos, 'to_alipay_dict'):
                params['ar_nos'] = self.ar_nos.to_alipay_dict()
            else:
                params['ar_nos'] = self.ar_nos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArrangementNoQuerier()
        if 'ar_nos' in d:
            o.ar_nos = d['ar_nos']
        return o


