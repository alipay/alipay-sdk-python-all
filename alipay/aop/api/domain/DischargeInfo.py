#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DischargeInfo(object):

    def __init__(self):
        self._complaint = None
        self._discharge_treatment_advice = None
        self._illness_history = None
        self._medicine_diagnosis = None
        self._physical_exam = None
        self._tcm_four_diagnosis = None
        self._traditional_chinese_medicine_diagnosis = None
        self._treatment_advice = None

    @property
    def complaint(self):
        return self._complaint

    @complaint.setter
    def complaint(self, value):
        self._complaint = value
    @property
    def discharge_treatment_advice(self):
        return self._discharge_treatment_advice

    @discharge_treatment_advice.setter
    def discharge_treatment_advice(self, value):
        self._discharge_treatment_advice = value
    @property
    def illness_history(self):
        return self._illness_history

    @illness_history.setter
    def illness_history(self, value):
        self._illness_history = value
    @property
    def medicine_diagnosis(self):
        return self._medicine_diagnosis

    @medicine_diagnosis.setter
    def medicine_diagnosis(self, value):
        self._medicine_diagnosis = value
    @property
    def physical_exam(self):
        return self._physical_exam

    @physical_exam.setter
    def physical_exam(self, value):
        self._physical_exam = value
    @property
    def tcm_four_diagnosis(self):
        return self._tcm_four_diagnosis

    @tcm_four_diagnosis.setter
    def tcm_four_diagnosis(self, value):
        self._tcm_four_diagnosis = value
    @property
    def traditional_chinese_medicine_diagnosis(self):
        return self._traditional_chinese_medicine_diagnosis

    @traditional_chinese_medicine_diagnosis.setter
    def traditional_chinese_medicine_diagnosis(self, value):
        self._traditional_chinese_medicine_diagnosis = value
    @property
    def treatment_advice(self):
        return self._treatment_advice

    @treatment_advice.setter
    def treatment_advice(self, value):
        self._treatment_advice = value


    def to_alipay_dict(self):
        params = dict()
        if self.complaint:
            if hasattr(self.complaint, 'to_alipay_dict'):
                params['complaint'] = self.complaint.to_alipay_dict()
            else:
                params['complaint'] = self.complaint
        if self.discharge_treatment_advice:
            if hasattr(self.discharge_treatment_advice, 'to_alipay_dict'):
                params['discharge_treatment_advice'] = self.discharge_treatment_advice.to_alipay_dict()
            else:
                params['discharge_treatment_advice'] = self.discharge_treatment_advice
        if self.illness_history:
            if hasattr(self.illness_history, 'to_alipay_dict'):
                params['illness_history'] = self.illness_history.to_alipay_dict()
            else:
                params['illness_history'] = self.illness_history
        if self.medicine_diagnosis:
            if hasattr(self.medicine_diagnosis, 'to_alipay_dict'):
                params['medicine_diagnosis'] = self.medicine_diagnosis.to_alipay_dict()
            else:
                params['medicine_diagnosis'] = self.medicine_diagnosis
        if self.physical_exam:
            if hasattr(self.physical_exam, 'to_alipay_dict'):
                params['physical_exam'] = self.physical_exam.to_alipay_dict()
            else:
                params['physical_exam'] = self.physical_exam
        if self.tcm_four_diagnosis:
            if hasattr(self.tcm_four_diagnosis, 'to_alipay_dict'):
                params['tcm_four_diagnosis'] = self.tcm_four_diagnosis.to_alipay_dict()
            else:
                params['tcm_four_diagnosis'] = self.tcm_four_diagnosis
        if self.traditional_chinese_medicine_diagnosis:
            if hasattr(self.traditional_chinese_medicine_diagnosis, 'to_alipay_dict'):
                params['traditional_chinese_medicine_diagnosis'] = self.traditional_chinese_medicine_diagnosis.to_alipay_dict()
            else:
                params['traditional_chinese_medicine_diagnosis'] = self.traditional_chinese_medicine_diagnosis
        if self.treatment_advice:
            if hasattr(self.treatment_advice, 'to_alipay_dict'):
                params['treatment_advice'] = self.treatment_advice.to_alipay_dict()
            else:
                params['treatment_advice'] = self.treatment_advice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DischargeInfo()
        if 'complaint' in d:
            o.complaint = d['complaint']
        if 'discharge_treatment_advice' in d:
            o.discharge_treatment_advice = d['discharge_treatment_advice']
        if 'illness_history' in d:
            o.illness_history = d['illness_history']
        if 'medicine_diagnosis' in d:
            o.medicine_diagnosis = d['medicine_diagnosis']
        if 'physical_exam' in d:
            o.physical_exam = d['physical_exam']
        if 'tcm_four_diagnosis' in d:
            o.tcm_four_diagnosis = d['tcm_four_diagnosis']
        if 'traditional_chinese_medicine_diagnosis' in d:
            o.traditional_chinese_medicine_diagnosis = d['traditional_chinese_medicine_diagnosis']
        if 'treatment_advice' in d:
            o.treatment_advice = d['treatment_advice']
        return o


