#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DrugItemInfo import DrugItemInfo
from alipay.aop.api.domain.HealthSymptom import HealthSymptom


class DiagnosisDisease(object):

    def __init__(self):
        self._drug_item_infos = None
        self._icd_code = None
        self._icd_name = None
        self._symptoms = None

    @property
    def drug_item_infos(self):
        return self._drug_item_infos

    @drug_item_infos.setter
    def drug_item_infos(self, value):
        if isinstance(value, list):
            self._drug_item_infos = list()
            for i in value:
                if isinstance(i, DrugItemInfo):
                    self._drug_item_infos.append(i)
                else:
                    self._drug_item_infos.append(DrugItemInfo.from_alipay_dict(i))
    @property
    def icd_code(self):
        return self._icd_code

    @icd_code.setter
    def icd_code(self, value):
        self._icd_code = value
    @property
    def icd_name(self):
        return self._icd_name

    @icd_name.setter
    def icd_name(self, value):
        self._icd_name = value
    @property
    def symptoms(self):
        return self._symptoms

    @symptoms.setter
    def symptoms(self, value):
        if isinstance(value, list):
            self._symptoms = list()
            for i in value:
                if isinstance(i, HealthSymptom):
                    self._symptoms.append(i)
                else:
                    self._symptoms.append(HealthSymptom.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.drug_item_infos:
            if isinstance(self.drug_item_infos, list):
                for i in range(0, len(self.drug_item_infos)):
                    element = self.drug_item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.drug_item_infos[i] = element.to_alipay_dict()
            if hasattr(self.drug_item_infos, 'to_alipay_dict'):
                params['drug_item_infos'] = self.drug_item_infos.to_alipay_dict()
            else:
                params['drug_item_infos'] = self.drug_item_infos
        if self.icd_code:
            if hasattr(self.icd_code, 'to_alipay_dict'):
                params['icd_code'] = self.icd_code.to_alipay_dict()
            else:
                params['icd_code'] = self.icd_code
        if self.icd_name:
            if hasattr(self.icd_name, 'to_alipay_dict'):
                params['icd_name'] = self.icd_name.to_alipay_dict()
            else:
                params['icd_name'] = self.icd_name
        if self.symptoms:
            if isinstance(self.symptoms, list):
                for i in range(0, len(self.symptoms)):
                    element = self.symptoms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.symptoms[i] = element.to_alipay_dict()
            if hasattr(self.symptoms, 'to_alipay_dict'):
                params['symptoms'] = self.symptoms.to_alipay_dict()
            else:
                params['symptoms'] = self.symptoms
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiagnosisDisease()
        if 'drug_item_infos' in d:
            o.drug_item_infos = d['drug_item_infos']
        if 'icd_code' in d:
            o.icd_code = d['icd_code']
        if 'icd_name' in d:
            o.icd_name = d['icd_name']
        if 'symptoms' in d:
            o.symptoms = d['symptoms']
        return o


