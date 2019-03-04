#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LegalRepresentativeVO(object):

    def __init__(self):
        self._duty = None
        self._name = None

    @property
    def duty(self):
        return self._duty

    @duty.setter
    def duty(self, value):
        self._duty = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.duty:
            if hasattr(self.duty, 'to_alipay_dict'):
                params['duty'] = self.duty.to_alipay_dict()
            else:
                params['duty'] = self.duty
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LegalRepresentativeVO()
        if 'duty' in d:
            o.duty = d['duty']
        if 'name' in d:
            o.name = d['name']
        return o


