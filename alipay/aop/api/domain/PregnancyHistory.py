#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PregnancyHistory(object):

    def __init__(self):
        self._last_menstruation = None
        self._pregnancy_status = None

    @property
    def last_menstruation(self):
        return self._last_menstruation

    @last_menstruation.setter
    def last_menstruation(self, value):
        self._last_menstruation = value
    @property
    def pregnancy_status(self):
        return self._pregnancy_status

    @pregnancy_status.setter
    def pregnancy_status(self, value):
        self._pregnancy_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.last_menstruation:
            if hasattr(self.last_menstruation, 'to_alipay_dict'):
                params['last_menstruation'] = self.last_menstruation.to_alipay_dict()
            else:
                params['last_menstruation'] = self.last_menstruation
        if self.pregnancy_status:
            if hasattr(self.pregnancy_status, 'to_alipay_dict'):
                params['pregnancy_status'] = self.pregnancy_status.to_alipay_dict()
            else:
                params['pregnancy_status'] = self.pregnancy_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PregnancyHistory()
        if 'last_menstruation' in d:
            o.last_menstruation = d['last_menstruation']
        if 'pregnancy_status' in d:
            o.pregnancy_status = d['pregnancy_status']
        return o


