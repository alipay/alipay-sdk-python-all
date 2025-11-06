#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VaccinationHistory(object):

    def __init__(self):
        self._vaccines_name = None
        self._vaccines_time = None

    @property
    def vaccines_name(self):
        return self._vaccines_name

    @vaccines_name.setter
    def vaccines_name(self, value):
        self._vaccines_name = value
    @property
    def vaccines_time(self):
        return self._vaccines_time

    @vaccines_time.setter
    def vaccines_time(self, value):
        self._vaccines_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.vaccines_name:
            if hasattr(self.vaccines_name, 'to_alipay_dict'):
                params['vaccines_name'] = self.vaccines_name.to_alipay_dict()
            else:
                params['vaccines_name'] = self.vaccines_name
        if self.vaccines_time:
            if hasattr(self.vaccines_time, 'to_alipay_dict'):
                params['vaccines_time'] = self.vaccines_time.to_alipay_dict()
            else:
                params['vaccines_time'] = self.vaccines_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VaccinationHistory()
        if 'vaccines_name' in d:
            o.vaccines_name = d['vaccines_name']
        if 'vaccines_time' in d:
            o.vaccines_time = d['vaccines_time']
        return o


