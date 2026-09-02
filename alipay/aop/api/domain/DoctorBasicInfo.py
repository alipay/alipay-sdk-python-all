#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceButtonInfo import ServiceButtonInfo
from alipay.aop.api.domain.TreatExperienceInfo import TreatExperienceInfo


class DoctorBasicInfo(object):

    def __init__(self):
        self._brief_intro = None
        self._doctor_inner_id = None
        self._doctor_name = None
        self._doctor_online_flag = None
        self._hdf_doctor_id = None
        self._hospital_name = None
        self._hot_rank = None
        self._medical_record_cnt = None
        self._service_button_info_list = None
        self._skilled_desc = None
        self._title = None
        self._treatment_experience_list = None

    @property
    def brief_intro(self):
        return self._brief_intro

    @brief_intro.setter
    def brief_intro(self, value):
        self._brief_intro = value
    @property
    def doctor_inner_id(self):
        return self._doctor_inner_id

    @doctor_inner_id.setter
    def doctor_inner_id(self, value):
        self._doctor_inner_id = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def doctor_online_flag(self):
        return self._doctor_online_flag

    @doctor_online_flag.setter
    def doctor_online_flag(self, value):
        self._doctor_online_flag = value
    @property
    def hdf_doctor_id(self):
        return self._hdf_doctor_id

    @hdf_doctor_id.setter
    def hdf_doctor_id(self, value):
        self._hdf_doctor_id = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def hot_rank(self):
        return self._hot_rank

    @hot_rank.setter
    def hot_rank(self, value):
        self._hot_rank = value
    @property
    def medical_record_cnt(self):
        return self._medical_record_cnt

    @medical_record_cnt.setter
    def medical_record_cnt(self, value):
        self._medical_record_cnt = value
    @property
    def service_button_info_list(self):
        return self._service_button_info_list

    @service_button_info_list.setter
    def service_button_info_list(self, value):
        if isinstance(value, list):
            self._service_button_info_list = list()
            for i in value:
                if isinstance(i, ServiceButtonInfo):
                    self._service_button_info_list.append(i)
                else:
                    self._service_button_info_list.append(ServiceButtonInfo.from_alipay_dict(i))
    @property
    def skilled_desc(self):
        return self._skilled_desc

    @skilled_desc.setter
    def skilled_desc(self, value):
        self._skilled_desc = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def treatment_experience_list(self):
        return self._treatment_experience_list

    @treatment_experience_list.setter
    def treatment_experience_list(self, value):
        if isinstance(value, list):
            self._treatment_experience_list = list()
            for i in value:
                if isinstance(i, TreatExperienceInfo):
                    self._treatment_experience_list.append(i)
                else:
                    self._treatment_experience_list.append(TreatExperienceInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.brief_intro:
            if hasattr(self.brief_intro, 'to_alipay_dict'):
                params['brief_intro'] = self.brief_intro.to_alipay_dict()
            else:
                params['brief_intro'] = self.brief_intro
        if self.doctor_inner_id:
            if hasattr(self.doctor_inner_id, 'to_alipay_dict'):
                params['doctor_inner_id'] = self.doctor_inner_id.to_alipay_dict()
            else:
                params['doctor_inner_id'] = self.doctor_inner_id
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.doctor_online_flag:
            if hasattr(self.doctor_online_flag, 'to_alipay_dict'):
                params['doctor_online_flag'] = self.doctor_online_flag.to_alipay_dict()
            else:
                params['doctor_online_flag'] = self.doctor_online_flag
        if self.hdf_doctor_id:
            if hasattr(self.hdf_doctor_id, 'to_alipay_dict'):
                params['hdf_doctor_id'] = self.hdf_doctor_id.to_alipay_dict()
            else:
                params['hdf_doctor_id'] = self.hdf_doctor_id
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.hot_rank:
            if hasattr(self.hot_rank, 'to_alipay_dict'):
                params['hot_rank'] = self.hot_rank.to_alipay_dict()
            else:
                params['hot_rank'] = self.hot_rank
        if self.medical_record_cnt:
            if hasattr(self.medical_record_cnt, 'to_alipay_dict'):
                params['medical_record_cnt'] = self.medical_record_cnt.to_alipay_dict()
            else:
                params['medical_record_cnt'] = self.medical_record_cnt
        if self.service_button_info_list:
            if isinstance(self.service_button_info_list, list):
                for i in range(0, len(self.service_button_info_list)):
                    element = self.service_button_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_button_info_list[i] = element.to_alipay_dict()
            if hasattr(self.service_button_info_list, 'to_alipay_dict'):
                params['service_button_info_list'] = self.service_button_info_list.to_alipay_dict()
            else:
                params['service_button_info_list'] = self.service_button_info_list
        if self.skilled_desc:
            if hasattr(self.skilled_desc, 'to_alipay_dict'):
                params['skilled_desc'] = self.skilled_desc.to_alipay_dict()
            else:
                params['skilled_desc'] = self.skilled_desc
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.treatment_experience_list:
            if isinstance(self.treatment_experience_list, list):
                for i in range(0, len(self.treatment_experience_list)):
                    element = self.treatment_experience_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.treatment_experience_list[i] = element.to_alipay_dict()
            if hasattr(self.treatment_experience_list, 'to_alipay_dict'):
                params['treatment_experience_list'] = self.treatment_experience_list.to_alipay_dict()
            else:
                params['treatment_experience_list'] = self.treatment_experience_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorBasicInfo()
        if 'brief_intro' in d:
            o.brief_intro = d['brief_intro']
        if 'doctor_inner_id' in d:
            o.doctor_inner_id = d['doctor_inner_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'doctor_online_flag' in d:
            o.doctor_online_flag = d['doctor_online_flag']
        if 'hdf_doctor_id' in d:
            o.hdf_doctor_id = d['hdf_doctor_id']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'hot_rank' in d:
            o.hot_rank = d['hot_rank']
        if 'medical_record_cnt' in d:
            o.medical_record_cnt = d['medical_record_cnt']
        if 'service_button_info_list' in d:
            o.service_button_info_list = d['service_button_info_list']
        if 'skilled_desc' in d:
            o.skilled_desc = d['skilled_desc']
        if 'title' in d:
            o.title = d['title']
        if 'treatment_experience_list' in d:
            o.treatment_experience_list = d['treatment_experience_list']
        return o


