#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NfcPointRefreshExposureRule(object):

    def __init__(self):
        self._process_open = None

    @property
    def process_open(self):
        return self._process_open

    @process_open.setter
    def process_open(self, value):
        self._process_open = value


    def to_alipay_dict(self):
        params = dict()
        if self.process_open:
            if hasattr(self.process_open, 'to_alipay_dict'):
                params['process_open'] = self.process_open.to_alipay_dict()
            else:
                params['process_open'] = self.process_open
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NfcPointRefreshExposureRule()
        if 'process_open' in d:
            o.process_open = d['process_open']
        return o


