#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiAdvertCommissionMissionPromoteModel(object):

    def __init__(self):
        self._identify = None
        self._identify_type = None
        self._name = None

    @property
    def identify(self):
        return self._identify

    @identify.setter
    def identify(self, value):
        self._identify = value
    @property
    def identify_type(self):
        return self._identify_type

    @identify_type.setter
    def identify_type(self, value):
        self._identify_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.identify:
            if hasattr(self.identify, 'to_alipay_dict'):
                params['identify'] = self.identify.to_alipay_dict()
            else:
                params['identify'] = self.identify
        if self.identify_type:
            if hasattr(self.identify_type, 'to_alipay_dict'):
                params['identify_type'] = self.identify_type.to_alipay_dict()
            else:
                params['identify_type'] = self.identify_type
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
        o = KoubeiAdvertCommissionMissionPromoteModel()
        if 'identify' in d:
            o.identify = d['identify']
        if 'identify_type' in d:
            o.identify_type = d['identify_type']
        if 'name' in d:
            o.name = d['name']
        return o


