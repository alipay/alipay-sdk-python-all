#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlcoholHistory import AlcoholHistory
from alipay.aop.api.domain.AllergyHistory import AllergyHistory
from alipay.aop.api.domain.DiseaseHistory import DiseaseHistory
from alipay.aop.api.domain.FamilyHistory import FamilyHistory
from alipay.aop.api.domain.MedicineHistory import MedicineHistory
from alipay.aop.api.domain.PregnancyHistory import PregnancyHistory
from alipay.aop.api.domain.SmokingHistory import SmokingHistory
from alipay.aop.api.domain.SurgicalHistory import SurgicalHistory
from alipay.aop.api.domain.VaccinationHistory import VaccinationHistory


class HealthHistory(object):

    def __init__(self):
        self._alcohol_history = None
        self._allergy_history_list = None
        self._disease_history_list = None
        self._family_history_list = None
        self._medicine_history_list = None
        self._pregnancy_history = None
        self._smoking_history = None
        self._surgical_history_list = None
        self._vaccination_history_list = None

    @property
    def alcohol_history(self):
        return self._alcohol_history

    @alcohol_history.setter
    def alcohol_history(self, value):
        if isinstance(value, AlcoholHistory):
            self._alcohol_history = value
        else:
            self._alcohol_history = AlcoholHistory.from_alipay_dict(value)
    @property
    def allergy_history_list(self):
        return self._allergy_history_list

    @allergy_history_list.setter
    def allergy_history_list(self, value):
        if isinstance(value, list):
            self._allergy_history_list = list()
            for i in value:
                if isinstance(i, AllergyHistory):
                    self._allergy_history_list.append(i)
                else:
                    self._allergy_history_list.append(AllergyHistory.from_alipay_dict(i))
    @property
    def disease_history_list(self):
        return self._disease_history_list

    @disease_history_list.setter
    def disease_history_list(self, value):
        if isinstance(value, list):
            self._disease_history_list = list()
            for i in value:
                if isinstance(i, DiseaseHistory):
                    self._disease_history_list.append(i)
                else:
                    self._disease_history_list.append(DiseaseHistory.from_alipay_dict(i))
    @property
    def family_history_list(self):
        return self._family_history_list

    @family_history_list.setter
    def family_history_list(self, value):
        if isinstance(value, list):
            self._family_history_list = list()
            for i in value:
                if isinstance(i, FamilyHistory):
                    self._family_history_list.append(i)
                else:
                    self._family_history_list.append(FamilyHistory.from_alipay_dict(i))
    @property
    def medicine_history_list(self):
        return self._medicine_history_list

    @medicine_history_list.setter
    def medicine_history_list(self, value):
        if isinstance(value, list):
            self._medicine_history_list = list()
            for i in value:
                if isinstance(i, MedicineHistory):
                    self._medicine_history_list.append(i)
                else:
                    self._medicine_history_list.append(MedicineHistory.from_alipay_dict(i))
    @property
    def pregnancy_history(self):
        return self._pregnancy_history

    @pregnancy_history.setter
    def pregnancy_history(self, value):
        if isinstance(value, PregnancyHistory):
            self._pregnancy_history = value
        else:
            self._pregnancy_history = PregnancyHistory.from_alipay_dict(value)
    @property
    def smoking_history(self):
        return self._smoking_history

    @smoking_history.setter
    def smoking_history(self, value):
        if isinstance(value, SmokingHistory):
            self._smoking_history = value
        else:
            self._smoking_history = SmokingHistory.from_alipay_dict(value)
    @property
    def surgical_history_list(self):
        return self._surgical_history_list

    @surgical_history_list.setter
    def surgical_history_list(self, value):
        if isinstance(value, list):
            self._surgical_history_list = list()
            for i in value:
                if isinstance(i, SurgicalHistory):
                    self._surgical_history_list.append(i)
                else:
                    self._surgical_history_list.append(SurgicalHistory.from_alipay_dict(i))
    @property
    def vaccination_history_list(self):
        return self._vaccination_history_list

    @vaccination_history_list.setter
    def vaccination_history_list(self, value):
        if isinstance(value, list):
            self._vaccination_history_list = list()
            for i in value:
                if isinstance(i, VaccinationHistory):
                    self._vaccination_history_list.append(i)
                else:
                    self._vaccination_history_list.append(VaccinationHistory.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.alcohol_history:
            if hasattr(self.alcohol_history, 'to_alipay_dict'):
                params['alcohol_history'] = self.alcohol_history.to_alipay_dict()
            else:
                params['alcohol_history'] = self.alcohol_history
        if self.allergy_history_list:
            if isinstance(self.allergy_history_list, list):
                for i in range(0, len(self.allergy_history_list)):
                    element = self.allergy_history_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.allergy_history_list[i] = element.to_alipay_dict()
            if hasattr(self.allergy_history_list, 'to_alipay_dict'):
                params['allergy_history_list'] = self.allergy_history_list.to_alipay_dict()
            else:
                params['allergy_history_list'] = self.allergy_history_list
        if self.disease_history_list:
            if isinstance(self.disease_history_list, list):
                for i in range(0, len(self.disease_history_list)):
                    element = self.disease_history_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.disease_history_list[i] = element.to_alipay_dict()
            if hasattr(self.disease_history_list, 'to_alipay_dict'):
                params['disease_history_list'] = self.disease_history_list.to_alipay_dict()
            else:
                params['disease_history_list'] = self.disease_history_list
        if self.family_history_list:
            if isinstance(self.family_history_list, list):
                for i in range(0, len(self.family_history_list)):
                    element = self.family_history_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.family_history_list[i] = element.to_alipay_dict()
            if hasattr(self.family_history_list, 'to_alipay_dict'):
                params['family_history_list'] = self.family_history_list.to_alipay_dict()
            else:
                params['family_history_list'] = self.family_history_list
        if self.medicine_history_list:
            if isinstance(self.medicine_history_list, list):
                for i in range(0, len(self.medicine_history_list)):
                    element = self.medicine_history_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medicine_history_list[i] = element.to_alipay_dict()
            if hasattr(self.medicine_history_list, 'to_alipay_dict'):
                params['medicine_history_list'] = self.medicine_history_list.to_alipay_dict()
            else:
                params['medicine_history_list'] = self.medicine_history_list
        if self.pregnancy_history:
            if hasattr(self.pregnancy_history, 'to_alipay_dict'):
                params['pregnancy_history'] = self.pregnancy_history.to_alipay_dict()
            else:
                params['pregnancy_history'] = self.pregnancy_history
        if self.smoking_history:
            if hasattr(self.smoking_history, 'to_alipay_dict'):
                params['smoking_history'] = self.smoking_history.to_alipay_dict()
            else:
                params['smoking_history'] = self.smoking_history
        if self.surgical_history_list:
            if isinstance(self.surgical_history_list, list):
                for i in range(0, len(self.surgical_history_list)):
                    element = self.surgical_history_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.surgical_history_list[i] = element.to_alipay_dict()
            if hasattr(self.surgical_history_list, 'to_alipay_dict'):
                params['surgical_history_list'] = self.surgical_history_list.to_alipay_dict()
            else:
                params['surgical_history_list'] = self.surgical_history_list
        if self.vaccination_history_list:
            if isinstance(self.vaccination_history_list, list):
                for i in range(0, len(self.vaccination_history_list)):
                    element = self.vaccination_history_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vaccination_history_list[i] = element.to_alipay_dict()
            if hasattr(self.vaccination_history_list, 'to_alipay_dict'):
                params['vaccination_history_list'] = self.vaccination_history_list.to_alipay_dict()
            else:
                params['vaccination_history_list'] = self.vaccination_history_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthHistory()
        if 'alcohol_history' in d:
            o.alcohol_history = d['alcohol_history']
        if 'allergy_history_list' in d:
            o.allergy_history_list = d['allergy_history_list']
        if 'disease_history_list' in d:
            o.disease_history_list = d['disease_history_list']
        if 'family_history_list' in d:
            o.family_history_list = d['family_history_list']
        if 'medicine_history_list' in d:
            o.medicine_history_list = d['medicine_history_list']
        if 'pregnancy_history' in d:
            o.pregnancy_history = d['pregnancy_history']
        if 'smoking_history' in d:
            o.smoking_history = d['smoking_history']
        if 'surgical_history_list' in d:
            o.surgical_history_list = d['surgical_history_list']
        if 'vaccination_history_list' in d:
            o.vaccination_history_list = d['vaccination_history_list']
        return o


