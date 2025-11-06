#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HDFChronicDisease import HDFChronicDisease
from alipay.aop.api.domain.HDFConditiondesc import HDFConditiondesc
from alipay.aop.api.domain.HDFDisease import HDFDisease
from alipay.aop.api.domain.HDFDrugAllergy import HDFDrugAllergy
from alipay.aop.api.domain.HDFGestationStr import HDFGestationStr
from alipay.aop.api.domain.HdfHospital import HdfHospital
from alipay.aop.api.domain.HDFIllnessHistory import HDFIllnessHistory
from alipay.aop.api.domain.HDFMedicineCondition import HDFMedicineCondition
from alipay.aop.api.domain.HDFPatientCourseTime import HDFPatientCourseTime
from alipay.aop.api.domain.HDFRecordBase import HDFRecordBase
from alipay.aop.api.domain.HDFHDFTreatmentProcess import HDFHDFTreatmentProcess


class HDFMedicalContent(object):

    def __init__(self):
        self._chronic_disease = None
        self._condition_desc = None
        self._disease = None
        self._drug_allergy = None
        self._gestation_str = None
        self._hostpital = None
        self._illness_history = None
        self._medicine_condition = None
        self._patient_course_time = None
        self._record_base = None
        self._treatment_process = None

    @property
    def chronic_disease(self):
        return self._chronic_disease

    @chronic_disease.setter
    def chronic_disease(self, value):
        if isinstance(value, HDFChronicDisease):
            self._chronic_disease = value
        else:
            self._chronic_disease = HDFChronicDisease.from_alipay_dict(value)
    @property
    def condition_desc(self):
        return self._condition_desc

    @condition_desc.setter
    def condition_desc(self, value):
        if isinstance(value, HDFConditiondesc):
            self._condition_desc = value
        else:
            self._condition_desc = HDFConditiondesc.from_alipay_dict(value)
    @property
    def disease(self):
        return self._disease

    @disease.setter
    def disease(self, value):
        if isinstance(value, HDFDisease):
            self._disease = value
        else:
            self._disease = HDFDisease.from_alipay_dict(value)
    @property
    def drug_allergy(self):
        return self._drug_allergy

    @drug_allergy.setter
    def drug_allergy(self, value):
        if isinstance(value, list):
            self._drug_allergy = list()
            for i in value:
                if isinstance(i, HDFDrugAllergy):
                    self._drug_allergy.append(i)
                else:
                    self._drug_allergy.append(HDFDrugAllergy.from_alipay_dict(i))
    @property
    def gestation_str(self):
        return self._gestation_str

    @gestation_str.setter
    def gestation_str(self, value):
        if isinstance(value, list):
            self._gestation_str = list()
            for i in value:
                if isinstance(i, HDFGestationStr):
                    self._gestation_str.append(i)
                else:
                    self._gestation_str.append(HDFGestationStr.from_alipay_dict(i))
    @property
    def hostpital(self):
        return self._hostpital

    @hostpital.setter
    def hostpital(self, value):
        if isinstance(value, HdfHospital):
            self._hostpital = value
        else:
            self._hostpital = HdfHospital.from_alipay_dict(value)
    @property
    def illness_history(self):
        return self._illness_history

    @illness_history.setter
    def illness_history(self, value):
        if isinstance(value, list):
            self._illness_history = list()
            for i in value:
                if isinstance(i, HDFIllnessHistory):
                    self._illness_history.append(i)
                else:
                    self._illness_history.append(HDFIllnessHistory.from_alipay_dict(i))
    @property
    def medicine_condition(self):
        return self._medicine_condition

    @medicine_condition.setter
    def medicine_condition(self, value):
        if isinstance(value, list):
            self._medicine_condition = list()
            for i in value:
                if isinstance(i, HDFMedicineCondition):
                    self._medicine_condition.append(i)
                else:
                    self._medicine_condition.append(HDFMedicineCondition.from_alipay_dict(i))
    @property
    def patient_course_time(self):
        return self._patient_course_time

    @patient_course_time.setter
    def patient_course_time(self, value):
        if isinstance(value, HDFPatientCourseTime):
            self._patient_course_time = value
        else:
            self._patient_course_time = HDFPatientCourseTime.from_alipay_dict(value)
    @property
    def record_base(self):
        return self._record_base

    @record_base.setter
    def record_base(self, value):
        if isinstance(value, HDFRecordBase):
            self._record_base = value
        else:
            self._record_base = HDFRecordBase.from_alipay_dict(value)
    @property
    def treatment_process(self):
        return self._treatment_process

    @treatment_process.setter
    def treatment_process(self, value):
        if isinstance(value, HDFHDFTreatmentProcess):
            self._treatment_process = value
        else:
            self._treatment_process = HDFHDFTreatmentProcess.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.chronic_disease:
            if hasattr(self.chronic_disease, 'to_alipay_dict'):
                params['chronic_disease'] = self.chronic_disease.to_alipay_dict()
            else:
                params['chronic_disease'] = self.chronic_disease
        if self.condition_desc:
            if hasattr(self.condition_desc, 'to_alipay_dict'):
                params['condition_desc'] = self.condition_desc.to_alipay_dict()
            else:
                params['condition_desc'] = self.condition_desc
        if self.disease:
            if hasattr(self.disease, 'to_alipay_dict'):
                params['disease'] = self.disease.to_alipay_dict()
            else:
                params['disease'] = self.disease
        if self.drug_allergy:
            if isinstance(self.drug_allergy, list):
                for i in range(0, len(self.drug_allergy)):
                    element = self.drug_allergy[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.drug_allergy[i] = element.to_alipay_dict()
            if hasattr(self.drug_allergy, 'to_alipay_dict'):
                params['drug_allergy'] = self.drug_allergy.to_alipay_dict()
            else:
                params['drug_allergy'] = self.drug_allergy
        if self.gestation_str:
            if isinstance(self.gestation_str, list):
                for i in range(0, len(self.gestation_str)):
                    element = self.gestation_str[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gestation_str[i] = element.to_alipay_dict()
            if hasattr(self.gestation_str, 'to_alipay_dict'):
                params['gestation_str'] = self.gestation_str.to_alipay_dict()
            else:
                params['gestation_str'] = self.gestation_str
        if self.hostpital:
            if hasattr(self.hostpital, 'to_alipay_dict'):
                params['hostpital'] = self.hostpital.to_alipay_dict()
            else:
                params['hostpital'] = self.hostpital
        if self.illness_history:
            if isinstance(self.illness_history, list):
                for i in range(0, len(self.illness_history)):
                    element = self.illness_history[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.illness_history[i] = element.to_alipay_dict()
            if hasattr(self.illness_history, 'to_alipay_dict'):
                params['illness_history'] = self.illness_history.to_alipay_dict()
            else:
                params['illness_history'] = self.illness_history
        if self.medicine_condition:
            if isinstance(self.medicine_condition, list):
                for i in range(0, len(self.medicine_condition)):
                    element = self.medicine_condition[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medicine_condition[i] = element.to_alipay_dict()
            if hasattr(self.medicine_condition, 'to_alipay_dict'):
                params['medicine_condition'] = self.medicine_condition.to_alipay_dict()
            else:
                params['medicine_condition'] = self.medicine_condition
        if self.patient_course_time:
            if hasattr(self.patient_course_time, 'to_alipay_dict'):
                params['patient_course_time'] = self.patient_course_time.to_alipay_dict()
            else:
                params['patient_course_time'] = self.patient_course_time
        if self.record_base:
            if hasattr(self.record_base, 'to_alipay_dict'):
                params['record_base'] = self.record_base.to_alipay_dict()
            else:
                params['record_base'] = self.record_base
        if self.treatment_process:
            if hasattr(self.treatment_process, 'to_alipay_dict'):
                params['treatment_process'] = self.treatment_process.to_alipay_dict()
            else:
                params['treatment_process'] = self.treatment_process
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFMedicalContent()
        if 'chronic_disease' in d:
            o.chronic_disease = d['chronic_disease']
        if 'condition_desc' in d:
            o.condition_desc = d['condition_desc']
        if 'disease' in d:
            o.disease = d['disease']
        if 'drug_allergy' in d:
            o.drug_allergy = d['drug_allergy']
        if 'gestation_str' in d:
            o.gestation_str = d['gestation_str']
        if 'hostpital' in d:
            o.hostpital = d['hostpital']
        if 'illness_history' in d:
            o.illness_history = d['illness_history']
        if 'medicine_condition' in d:
            o.medicine_condition = d['medicine_condition']
        if 'patient_course_time' in d:
            o.patient_course_time = d['patient_course_time']
        if 'record_base' in d:
            o.record_base = d['record_base']
        if 'treatment_process' in d:
            o.treatment_process = d['treatment_process']
        return o


