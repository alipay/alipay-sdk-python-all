#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneHealthSymptomQueryModel(object):

    def __init__(self):
        self._ant_ser_contract_no = None
        self._symptom_search_keyword = None

    @property
    def ant_ser_contract_no(self):
        return self._ant_ser_contract_no

    @ant_ser_contract_no.setter
    def ant_ser_contract_no(self, value):
        self._ant_ser_contract_no = value
    @property
    def symptom_search_keyword(self):
        return self._symptom_search_keyword

    @symptom_search_keyword.setter
    def symptom_search_keyword(self, value):
        self._symptom_search_keyword = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_contract_no:
            if hasattr(self.ant_ser_contract_no, 'to_alipay_dict'):
                params['ant_ser_contract_no'] = self.ant_ser_contract_no.to_alipay_dict()
            else:
                params['ant_ser_contract_no'] = self.ant_ser_contract_no
        if self.symptom_search_keyword:
            if hasattr(self.symptom_search_keyword, 'to_alipay_dict'):
                params['symptom_search_keyword'] = self.symptom_search_keyword.to_alipay_dict()
            else:
                params['symptom_search_keyword'] = self.symptom_search_keyword
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneHealthSymptomQueryModel()
        if 'ant_ser_contract_no' in d:
            o.ant_ser_contract_no = d['ant_ser_contract_no']
        if 'symptom_search_keyword' in d:
            o.symptom_search_keyword = d['symptom_search_keyword']
        return o


