#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiseaseBaseData(object):

    def __init__(self):
        self._clinical_symptoms = None
        self._common_disease = None
        self._complication = None
        self._department_info = None
        self._disease_alias = None
        self._disease_cycle = None
        self._disease_introduction = None
        self._disease_name_cn = None
        self._disease_name_en = None
        self._disease_position = None
        self._disease_symptom = None
        self._genetic = None
        self._infectivity = None
        self._multiple_population = None

    @property
    def clinical_symptoms(self):
        return self._clinical_symptoms

    @clinical_symptoms.setter
    def clinical_symptoms(self, value):
        self._clinical_symptoms = value
    @property
    def common_disease(self):
        return self._common_disease

    @common_disease.setter
    def common_disease(self, value):
        self._common_disease = value
    @property
    def complication(self):
        return self._complication

    @complication.setter
    def complication(self, value):
        self._complication = value
    @property
    def department_info(self):
        return self._department_info

    @department_info.setter
    def department_info(self, value):
        self._department_info = value
    @property
    def disease_alias(self):
        return self._disease_alias

    @disease_alias.setter
    def disease_alias(self, value):
        self._disease_alias = value
    @property
    def disease_cycle(self):
        return self._disease_cycle

    @disease_cycle.setter
    def disease_cycle(self, value):
        self._disease_cycle = value
    @property
    def disease_introduction(self):
        return self._disease_introduction

    @disease_introduction.setter
    def disease_introduction(self, value):
        self._disease_introduction = value
    @property
    def disease_name_cn(self):
        return self._disease_name_cn

    @disease_name_cn.setter
    def disease_name_cn(self, value):
        self._disease_name_cn = value
    @property
    def disease_name_en(self):
        return self._disease_name_en

    @disease_name_en.setter
    def disease_name_en(self, value):
        self._disease_name_en = value
    @property
    def disease_position(self):
        return self._disease_position

    @disease_position.setter
    def disease_position(self, value):
        self._disease_position = value
    @property
    def disease_symptom(self):
        return self._disease_symptom

    @disease_symptom.setter
    def disease_symptom(self, value):
        self._disease_symptom = value
    @property
    def genetic(self):
        return self._genetic

    @genetic.setter
    def genetic(self, value):
        self._genetic = value
    @property
    def infectivity(self):
        return self._infectivity

    @infectivity.setter
    def infectivity(self, value):
        self._infectivity = value
    @property
    def multiple_population(self):
        return self._multiple_population

    @multiple_population.setter
    def multiple_population(self, value):
        self._multiple_population = value


    def to_alipay_dict(self):
        params = dict()
        if self.clinical_symptoms:
            if hasattr(self.clinical_symptoms, 'to_alipay_dict'):
                params['clinical_symptoms'] = self.clinical_symptoms.to_alipay_dict()
            else:
                params['clinical_symptoms'] = self.clinical_symptoms
        if self.common_disease:
            if hasattr(self.common_disease, 'to_alipay_dict'):
                params['common_disease'] = self.common_disease.to_alipay_dict()
            else:
                params['common_disease'] = self.common_disease
        if self.complication:
            if hasattr(self.complication, 'to_alipay_dict'):
                params['complication'] = self.complication.to_alipay_dict()
            else:
                params['complication'] = self.complication
        if self.department_info:
            if hasattr(self.department_info, 'to_alipay_dict'):
                params['department_info'] = self.department_info.to_alipay_dict()
            else:
                params['department_info'] = self.department_info
        if self.disease_alias:
            if hasattr(self.disease_alias, 'to_alipay_dict'):
                params['disease_alias'] = self.disease_alias.to_alipay_dict()
            else:
                params['disease_alias'] = self.disease_alias
        if self.disease_cycle:
            if hasattr(self.disease_cycle, 'to_alipay_dict'):
                params['disease_cycle'] = self.disease_cycle.to_alipay_dict()
            else:
                params['disease_cycle'] = self.disease_cycle
        if self.disease_introduction:
            if hasattr(self.disease_introduction, 'to_alipay_dict'):
                params['disease_introduction'] = self.disease_introduction.to_alipay_dict()
            else:
                params['disease_introduction'] = self.disease_introduction
        if self.disease_name_cn:
            if hasattr(self.disease_name_cn, 'to_alipay_dict'):
                params['disease_name_cn'] = self.disease_name_cn.to_alipay_dict()
            else:
                params['disease_name_cn'] = self.disease_name_cn
        if self.disease_name_en:
            if hasattr(self.disease_name_en, 'to_alipay_dict'):
                params['disease_name_en'] = self.disease_name_en.to_alipay_dict()
            else:
                params['disease_name_en'] = self.disease_name_en
        if self.disease_position:
            if hasattr(self.disease_position, 'to_alipay_dict'):
                params['disease_position'] = self.disease_position.to_alipay_dict()
            else:
                params['disease_position'] = self.disease_position
        if self.disease_symptom:
            if hasattr(self.disease_symptom, 'to_alipay_dict'):
                params['disease_symptom'] = self.disease_symptom.to_alipay_dict()
            else:
                params['disease_symptom'] = self.disease_symptom
        if self.genetic:
            if hasattr(self.genetic, 'to_alipay_dict'):
                params['genetic'] = self.genetic.to_alipay_dict()
            else:
                params['genetic'] = self.genetic
        if self.infectivity:
            if hasattr(self.infectivity, 'to_alipay_dict'):
                params['infectivity'] = self.infectivity.to_alipay_dict()
            else:
                params['infectivity'] = self.infectivity
        if self.multiple_population:
            if hasattr(self.multiple_population, 'to_alipay_dict'):
                params['multiple_population'] = self.multiple_population.to_alipay_dict()
            else:
                params['multiple_population'] = self.multiple_population
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiseaseBaseData()
        if 'clinical_symptoms' in d:
            o.clinical_symptoms = d['clinical_symptoms']
        if 'common_disease' in d:
            o.common_disease = d['common_disease']
        if 'complication' in d:
            o.complication = d['complication']
        if 'department_info' in d:
            o.department_info = d['department_info']
        if 'disease_alias' in d:
            o.disease_alias = d['disease_alias']
        if 'disease_cycle' in d:
            o.disease_cycle = d['disease_cycle']
        if 'disease_introduction' in d:
            o.disease_introduction = d['disease_introduction']
        if 'disease_name_cn' in d:
            o.disease_name_cn = d['disease_name_cn']
        if 'disease_name_en' in d:
            o.disease_name_en = d['disease_name_en']
        if 'disease_position' in d:
            o.disease_position = d['disease_position']
        if 'disease_symptom' in d:
            o.disease_symptom = d['disease_symptom']
        if 'genetic' in d:
            o.genetic = d['genetic']
        if 'infectivity' in d:
            o.infectivity = d['infectivity']
        if 'multiple_population' in d:
            o.multiple_population = d['multiple_population']
        return o


