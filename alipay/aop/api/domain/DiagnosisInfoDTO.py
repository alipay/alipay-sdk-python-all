#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiagnosisInfoDTO(object):

    def __init__(self):
        self._diacrisis = None
        self._title = None

    @property
    def diacrisis(self):
        return self._diacrisis

    @diacrisis.setter
    def diacrisis(self, value):
        self._diacrisis = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.diacrisis:
            if hasattr(self.diacrisis, 'to_alipay_dict'):
                params['diacrisis'] = self.diacrisis.to_alipay_dict()
            else:
                params['diacrisis'] = self.diacrisis
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiagnosisInfoDTO()
        if 'diacrisis' in d:
            o.diacrisis = d['diacrisis']
        if 'title' in d:
            o.title = d['title']
        return o


