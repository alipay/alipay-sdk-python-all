#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainysComplexTypeWeakRefFifth(object):

    def __init__(self):
        self._demo_date = None

    @property
    def demo_date(self):
        return self._demo_date

    @demo_date.setter
    def demo_date(self, value):
        self._demo_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_date:
            if hasattr(self.demo_date, 'to_alipay_dict'):
                params['demo_date'] = self.demo_date.to_alipay_dict()
            else:
                params['demo_date'] = self.demo_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainysComplexTypeWeakRefFifth()
        if 'demo_date' in d:
            o.demo_date = d['demo_date']
        return o


