#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiseaseHistory(object):

    def __init__(self):
        self._diagnosis_date = None
        self._disease_name = None

    @property
    def diagnosis_date(self):
        return self._diagnosis_date

    @diagnosis_date.setter
    def diagnosis_date(self, value):
        self._diagnosis_date = value
    @property
    def disease_name(self):
        return self._disease_name

    @disease_name.setter
    def disease_name(self, value):
        self._disease_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.diagnosis_date:
            if hasattr(self.diagnosis_date, 'to_alipay_dict'):
                params['diagnosis_date'] = self.diagnosis_date.to_alipay_dict()
            else:
                params['diagnosis_date'] = self.diagnosis_date
        if self.disease_name:
            if hasattr(self.disease_name, 'to_alipay_dict'):
                params['disease_name'] = self.disease_name.to_alipay_dict()
            else:
                params['disease_name'] = self.disease_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiseaseHistory()
        if 'diagnosis_date' in d:
            o.diagnosis_date = d['diagnosis_date']
        if 'disease_name' in d:
            o.disease_name = d['disease_name']
        return o


