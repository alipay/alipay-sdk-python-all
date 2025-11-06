#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFChronicDisease(object):

    def __init__(self):
        self._chronic_desc = None
        self._have_time = None
        self._treatment = None
        self._type = None

    @property
    def chronic_desc(self):
        return self._chronic_desc

    @chronic_desc.setter
    def chronic_desc(self, value):
        self._chronic_desc = value
    @property
    def have_time(self):
        return self._have_time

    @have_time.setter
    def have_time(self, value):
        self._have_time = value
    @property
    def treatment(self):
        return self._treatment

    @treatment.setter
    def treatment(self, value):
        self._treatment = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.chronic_desc:
            if hasattr(self.chronic_desc, 'to_alipay_dict'):
                params['chronic_desc'] = self.chronic_desc.to_alipay_dict()
            else:
                params['chronic_desc'] = self.chronic_desc
        if self.have_time:
            if hasattr(self.have_time, 'to_alipay_dict'):
                params['have_time'] = self.have_time.to_alipay_dict()
            else:
                params['have_time'] = self.have_time
        if self.treatment:
            if hasattr(self.treatment, 'to_alipay_dict'):
                params['treatment'] = self.treatment.to_alipay_dict()
            else:
                params['treatment'] = self.treatment
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFChronicDisease()
        if 'chronic_desc' in d:
            o.chronic_desc = d['chronic_desc']
        if 'have_time' in d:
            o.have_time = d['have_time']
        if 'treatment' in d:
            o.treatment = d['treatment']
        if 'type' in d:
            o.type = d['type']
        return o


