#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DoctorRecordDisease import DoctorRecordDisease
from alipay.aop.api.domain.DoctorServiceInfo import DoctorServiceInfo


class SimpleDoctorInfo(object):

    def __init__(self):
        self._doctor_id = None
        self._doctor_name = None
        self._doctor_online_flag = None
        self._hot_rank = None
        self._medical_record_cnt = None
        self._medical_record_disease_list = None
        self._service_info = None

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
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
    def medical_record_disease_list(self):
        return self._medical_record_disease_list

    @medical_record_disease_list.setter
    def medical_record_disease_list(self, value):
        if isinstance(value, list):
            self._medical_record_disease_list = list()
            for i in value:
                if isinstance(i, DoctorRecordDisease):
                    self._medical_record_disease_list.append(i)
                else:
                    self._medical_record_disease_list.append(DoctorRecordDisease.from_alipay_dict(i))
    @property
    def service_info(self):
        return self._service_info

    @service_info.setter
    def service_info(self, value):
        if isinstance(value, list):
            self._service_info = list()
            for i in value:
                if isinstance(i, DoctorServiceInfo):
                    self._service_info.append(i)
                else:
                    self._service_info.append(DoctorServiceInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
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
        if self.medical_record_disease_list:
            if isinstance(self.medical_record_disease_list, list):
                for i in range(0, len(self.medical_record_disease_list)):
                    element = self.medical_record_disease_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medical_record_disease_list[i] = element.to_alipay_dict()
            if hasattr(self.medical_record_disease_list, 'to_alipay_dict'):
                params['medical_record_disease_list'] = self.medical_record_disease_list.to_alipay_dict()
            else:
                params['medical_record_disease_list'] = self.medical_record_disease_list
        if self.service_info:
            if isinstance(self.service_info, list):
                for i in range(0, len(self.service_info)):
                    element = self.service_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_info[i] = element.to_alipay_dict()
            if hasattr(self.service_info, 'to_alipay_dict'):
                params['service_info'] = self.service_info.to_alipay_dict()
            else:
                params['service_info'] = self.service_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SimpleDoctorInfo()
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'doctor_online_flag' in d:
            o.doctor_online_flag = d['doctor_online_flag']
        if 'hot_rank' in d:
            o.hot_rank = d['hot_rank']
        if 'medical_record_cnt' in d:
            o.medical_record_cnt = d['medical_record_cnt']
        if 'medical_record_disease_list' in d:
            o.medical_record_disease_list = d['medical_record_disease_list']
        if 'service_info' in d:
            o.service_info = d['service_info']
        return o


