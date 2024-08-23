#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpContactBaseInfo(object):

    def __init__(self):
        self._confidence_level = None
        self._contact_number = None

    @property
    def confidence_level(self):
        return self._confidence_level

    @confidence_level.setter
    def confidence_level(self, value):
        self._confidence_level = value
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.confidence_level:
            if hasattr(self.confidence_level, 'to_alipay_dict'):
                params['confidence_level'] = self.confidence_level.to_alipay_dict()
            else:
                params['confidence_level'] = self.confidence_level
        if self.contact_number:
            if hasattr(self.contact_number, 'to_alipay_dict'):
                params['contact_number'] = self.contact_number.to_alipay_dict()
            else:
                params['contact_number'] = self.contact_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpContactBaseInfo()
        if 'confidence_level' in d:
            o.confidence_level = d['confidence_level']
        if 'contact_number' in d:
            o.contact_number = d['contact_number']
        return o


