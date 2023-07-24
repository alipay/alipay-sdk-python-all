#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiagnosisDisease import DiagnosisDisease


class Diagnosis(object):

    def __init__(self):
        self._diseases = None

    @property
    def diseases(self):
        return self._diseases

    @diseases.setter
    def diseases(self, value):
        if isinstance(value, list):
            self._diseases = list()
            for i in value:
                if isinstance(i, DiagnosisDisease):
                    self._diseases.append(i)
                else:
                    self._diseases.append(DiagnosisDisease.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.diseases:
            if isinstance(self.diseases, list):
                for i in range(0, len(self.diseases)):
                    element = self.diseases[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.diseases[i] = element.to_alipay_dict()
            if hasattr(self.diseases, 'to_alipay_dict'):
                params['diseases'] = self.diseases.to_alipay_dict()
            else:
                params['diseases'] = self.diseases
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Diagnosis()
        if 'diseases' in d:
            o.diseases = d['diseases']
        return o


