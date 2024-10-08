#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LuggagePolicy(object):

    def __init__(self):
        self._airline_no = None
        self._desc = None
        self._type = None

    @property
    def airline_no(self):
        return self._airline_no

    @airline_no.setter
    def airline_no(self, value):
        self._airline_no = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.airline_no:
            if hasattr(self.airline_no, 'to_alipay_dict'):
                params['airline_no'] = self.airline_no.to_alipay_dict()
            else:
                params['airline_no'] = self.airline_no
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
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
        o = LuggagePolicy()
        if 'airline_no' in d:
            o.airline_no = d['airline_no']
        if 'desc' in d:
            o.desc = d['desc']
        if 'type' in d:
            o.type = d['type']
        return o


