#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFMedicalSummary(object):

    def __init__(self):
        self._diacrisis = None
        self._idea = None
        self._summary = None

    @property
    def diacrisis(self):
        return self._diacrisis

    @diacrisis.setter
    def diacrisis(self, value):
        self._diacrisis = value
    @property
    def idea(self):
        return self._idea

    @idea.setter
    def idea(self, value):
        self._idea = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value


    def to_alipay_dict(self):
        params = dict()
        if self.diacrisis:
            if hasattr(self.diacrisis, 'to_alipay_dict'):
                params['diacrisis'] = self.diacrisis.to_alipay_dict()
            else:
                params['diacrisis'] = self.diacrisis
        if self.idea:
            if hasattr(self.idea, 'to_alipay_dict'):
                params['idea'] = self.idea.to_alipay_dict()
            else:
                params['idea'] = self.idea
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFMedicalSummary()
        if 'diacrisis' in d:
            o.diacrisis = d['diacrisis']
        if 'idea' in d:
            o.idea = d['idea']
        if 'summary' in d:
            o.summary = d['summary']
        return o


