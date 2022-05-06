#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiseaseData import DiseaseData
from alipay.aop.api.domain.DoctorWorkInfo import DoctorWorkInfo


class DoctorData(object):

    def __init__(self):
        self._academic_title = None
        self._doctor_id = None
        self._doctor_introduction = None
        self._doctor_name = None
        self._doctor_photo = None
        self._doctor_tag = None
        self._doctor_url = None
        self._medical_practice_years = None
        self._skilled_disease = None
        self._skilled_disease_desc = None
        self._work_info = None
        self._work_time = None

    @property
    def academic_title(self):
        return self._academic_title

    @academic_title.setter
    def academic_title(self, value):
        self._academic_title = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_introduction(self):
        return self._doctor_introduction

    @doctor_introduction.setter
    def doctor_introduction(self, value):
        self._doctor_introduction = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def doctor_photo(self):
        return self._doctor_photo

    @doctor_photo.setter
    def doctor_photo(self, value):
        self._doctor_photo = value
    @property
    def doctor_tag(self):
        return self._doctor_tag

    @doctor_tag.setter
    def doctor_tag(self, value):
        self._doctor_tag = value
    @property
    def doctor_url(self):
        return self._doctor_url

    @doctor_url.setter
    def doctor_url(self, value):
        self._doctor_url = value
    @property
    def medical_practice_years(self):
        return self._medical_practice_years

    @medical_practice_years.setter
    def medical_practice_years(self, value):
        self._medical_practice_years = value
    @property
    def skilled_disease(self):
        return self._skilled_disease

    @skilled_disease.setter
    def skilled_disease(self, value):
        if isinstance(value, list):
            self._skilled_disease = list()
            for i in value:
                if isinstance(i, DiseaseData):
                    self._skilled_disease.append(i)
                else:
                    self._skilled_disease.append(DiseaseData.from_alipay_dict(i))
    @property
    def skilled_disease_desc(self):
        return self._skilled_disease_desc

    @skilled_disease_desc.setter
    def skilled_disease_desc(self, value):
        self._skilled_disease_desc = value
    @property
    def work_info(self):
        return self._work_info

    @work_info.setter
    def work_info(self, value):
        if isinstance(value, list):
            self._work_info = list()
            for i in value:
                if isinstance(i, DoctorWorkInfo):
                    self._work_info.append(i)
                else:
                    self._work_info.append(DoctorWorkInfo.from_alipay_dict(i))
    @property
    def work_time(self):
        return self._work_time

    @work_time.setter
    def work_time(self, value):
        self._work_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.academic_title:
            if hasattr(self.academic_title, 'to_alipay_dict'):
                params['academic_title'] = self.academic_title.to_alipay_dict()
            else:
                params['academic_title'] = self.academic_title
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_introduction:
            if hasattr(self.doctor_introduction, 'to_alipay_dict'):
                params['doctor_introduction'] = self.doctor_introduction.to_alipay_dict()
            else:
                params['doctor_introduction'] = self.doctor_introduction
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.doctor_photo:
            if hasattr(self.doctor_photo, 'to_alipay_dict'):
                params['doctor_photo'] = self.doctor_photo.to_alipay_dict()
            else:
                params['doctor_photo'] = self.doctor_photo
        if self.doctor_tag:
            if hasattr(self.doctor_tag, 'to_alipay_dict'):
                params['doctor_tag'] = self.doctor_tag.to_alipay_dict()
            else:
                params['doctor_tag'] = self.doctor_tag
        if self.doctor_url:
            if hasattr(self.doctor_url, 'to_alipay_dict'):
                params['doctor_url'] = self.doctor_url.to_alipay_dict()
            else:
                params['doctor_url'] = self.doctor_url
        if self.medical_practice_years:
            if hasattr(self.medical_practice_years, 'to_alipay_dict'):
                params['medical_practice_years'] = self.medical_practice_years.to_alipay_dict()
            else:
                params['medical_practice_years'] = self.medical_practice_years
        if self.skilled_disease:
            if isinstance(self.skilled_disease, list):
                for i in range(0, len(self.skilled_disease)):
                    element = self.skilled_disease[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skilled_disease[i] = element.to_alipay_dict()
            if hasattr(self.skilled_disease, 'to_alipay_dict'):
                params['skilled_disease'] = self.skilled_disease.to_alipay_dict()
            else:
                params['skilled_disease'] = self.skilled_disease
        if self.skilled_disease_desc:
            if hasattr(self.skilled_disease_desc, 'to_alipay_dict'):
                params['skilled_disease_desc'] = self.skilled_disease_desc.to_alipay_dict()
            else:
                params['skilled_disease_desc'] = self.skilled_disease_desc
        if self.work_info:
            if isinstance(self.work_info, list):
                for i in range(0, len(self.work_info)):
                    element = self.work_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_info[i] = element.to_alipay_dict()
            if hasattr(self.work_info, 'to_alipay_dict'):
                params['work_info'] = self.work_info.to_alipay_dict()
            else:
                params['work_info'] = self.work_info
        if self.work_time:
            if hasattr(self.work_time, 'to_alipay_dict'):
                params['work_time'] = self.work_time.to_alipay_dict()
            else:
                params['work_time'] = self.work_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorData()
        if 'academic_title' in d:
            o.academic_title = d['academic_title']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_introduction' in d:
            o.doctor_introduction = d['doctor_introduction']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'doctor_photo' in d:
            o.doctor_photo = d['doctor_photo']
        if 'doctor_tag' in d:
            o.doctor_tag = d['doctor_tag']
        if 'doctor_url' in d:
            o.doctor_url = d['doctor_url']
        if 'medical_practice_years' in d:
            o.medical_practice_years = d['medical_practice_years']
        if 'skilled_disease' in d:
            o.skilled_disease = d['skilled_disease']
        if 'skilled_disease_desc' in d:
            o.skilled_disease_desc = d['skilled_disease_desc']
        if 'work_info' in d:
            o.work_info = d['work_info']
        if 'work_time' in d:
            o.work_time = d['work_time']
        return o


