#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalAppointmentOrderUploadExtInfo(object):

    def __init__(self):
        self._call_num_url = None
        self._department = None
        self._dept_loc = None
        self._dept_num = None
        self._doctor = None
        self._doctor_id = None
        self._doctor_rank = None
        self._hospital = None
        self._hospital_id_type = None
        self._hospital_register_id = None
        self._medical_num = None
        self._merchant_order_link_page = None
        self._navigation = None
        self._patient = None
        self._scheduled_time = None
        self._scheduled_time_period = None
        self._take_num_url = None

    @property
    def call_num_url(self):
        return self._call_num_url

    @call_num_url.setter
    def call_num_url(self, value):
        self._call_num_url = value
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def dept_loc(self):
        return self._dept_loc

    @dept_loc.setter
    def dept_loc(self, value):
        self._dept_loc = value
    @property
    def dept_num(self):
        return self._dept_num

    @dept_num.setter
    def dept_num(self, value):
        self._dept_num = value
    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, value):
        self._doctor = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_rank(self):
        return self._doctor_rank

    @doctor_rank.setter
    def doctor_rank(self, value):
        self._doctor_rank = value
    @property
    def hospital(self):
        return self._hospital

    @hospital.setter
    def hospital(self, value):
        self._hospital = value
    @property
    def hospital_id_type(self):
        return self._hospital_id_type

    @hospital_id_type.setter
    def hospital_id_type(self, value):
        self._hospital_id_type = value
    @property
    def hospital_register_id(self):
        return self._hospital_register_id

    @hospital_register_id.setter
    def hospital_register_id(self, value):
        self._hospital_register_id = value
    @property
    def medical_num(self):
        return self._medical_num

    @medical_num.setter
    def medical_num(self, value):
        self._medical_num = value
    @property
    def merchant_order_link_page(self):
        return self._merchant_order_link_page

    @merchant_order_link_page.setter
    def merchant_order_link_page(self, value):
        self._merchant_order_link_page = value
    @property
    def navigation(self):
        return self._navigation

    @navigation.setter
    def navigation(self, value):
        self._navigation = value
    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, value):
        self._patient = value
    @property
    def scheduled_time(self):
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, value):
        self._scheduled_time = value
    @property
    def scheduled_time_period(self):
        return self._scheduled_time_period

    @scheduled_time_period.setter
    def scheduled_time_period(self, value):
        self._scheduled_time_period = value
    @property
    def take_num_url(self):
        return self._take_num_url

    @take_num_url.setter
    def take_num_url(self, value):
        self._take_num_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.call_num_url:
            if hasattr(self.call_num_url, 'to_alipay_dict'):
                params['call_num_url'] = self.call_num_url.to_alipay_dict()
            else:
                params['call_num_url'] = self.call_num_url
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.dept_loc:
            if hasattr(self.dept_loc, 'to_alipay_dict'):
                params['dept_loc'] = self.dept_loc.to_alipay_dict()
            else:
                params['dept_loc'] = self.dept_loc
        if self.dept_num:
            if hasattr(self.dept_num, 'to_alipay_dict'):
                params['dept_num'] = self.dept_num.to_alipay_dict()
            else:
                params['dept_num'] = self.dept_num
        if self.doctor:
            if hasattr(self.doctor, 'to_alipay_dict'):
                params['doctor'] = self.doctor.to_alipay_dict()
            else:
                params['doctor'] = self.doctor
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_rank:
            if hasattr(self.doctor_rank, 'to_alipay_dict'):
                params['doctor_rank'] = self.doctor_rank.to_alipay_dict()
            else:
                params['doctor_rank'] = self.doctor_rank
        if self.hospital:
            if hasattr(self.hospital, 'to_alipay_dict'):
                params['hospital'] = self.hospital.to_alipay_dict()
            else:
                params['hospital'] = self.hospital
        if self.hospital_id_type:
            if hasattr(self.hospital_id_type, 'to_alipay_dict'):
                params['hospital_id_type'] = self.hospital_id_type.to_alipay_dict()
            else:
                params['hospital_id_type'] = self.hospital_id_type
        if self.hospital_register_id:
            if hasattr(self.hospital_register_id, 'to_alipay_dict'):
                params['hospital_register_id'] = self.hospital_register_id.to_alipay_dict()
            else:
                params['hospital_register_id'] = self.hospital_register_id
        if self.medical_num:
            if hasattr(self.medical_num, 'to_alipay_dict'):
                params['medical_num'] = self.medical_num.to_alipay_dict()
            else:
                params['medical_num'] = self.medical_num
        if self.merchant_order_link_page:
            if hasattr(self.merchant_order_link_page, 'to_alipay_dict'):
                params['merchant_order_link_page'] = self.merchant_order_link_page.to_alipay_dict()
            else:
                params['merchant_order_link_page'] = self.merchant_order_link_page
        if self.navigation:
            if hasattr(self.navigation, 'to_alipay_dict'):
                params['navigation'] = self.navigation.to_alipay_dict()
            else:
                params['navigation'] = self.navigation
        if self.patient:
            if hasattr(self.patient, 'to_alipay_dict'):
                params['patient'] = self.patient.to_alipay_dict()
            else:
                params['patient'] = self.patient
        if self.scheduled_time:
            if hasattr(self.scheduled_time, 'to_alipay_dict'):
                params['scheduled_time'] = self.scheduled_time.to_alipay_dict()
            else:
                params['scheduled_time'] = self.scheduled_time
        if self.scheduled_time_period:
            if hasattr(self.scheduled_time_period, 'to_alipay_dict'):
                params['scheduled_time_period'] = self.scheduled_time_period.to_alipay_dict()
            else:
                params['scheduled_time_period'] = self.scheduled_time_period
        if self.take_num_url:
            if hasattr(self.take_num_url, 'to_alipay_dict'):
                params['take_num_url'] = self.take_num_url.to_alipay_dict()
            else:
                params['take_num_url'] = self.take_num_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalAppointmentOrderUploadExtInfo()
        if 'call_num_url' in d:
            o.call_num_url = d['call_num_url']
        if 'department' in d:
            o.department = d['department']
        if 'dept_loc' in d:
            o.dept_loc = d['dept_loc']
        if 'dept_num' in d:
            o.dept_num = d['dept_num']
        if 'doctor' in d:
            o.doctor = d['doctor']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_rank' in d:
            o.doctor_rank = d['doctor_rank']
        if 'hospital' in d:
            o.hospital = d['hospital']
        if 'hospital_id_type' in d:
            o.hospital_id_type = d['hospital_id_type']
        if 'hospital_register_id' in d:
            o.hospital_register_id = d['hospital_register_id']
        if 'medical_num' in d:
            o.medical_num = d['medical_num']
        if 'merchant_order_link_page' in d:
            o.merchant_order_link_page = d['merchant_order_link_page']
        if 'navigation' in d:
            o.navigation = d['navigation']
        if 'patient' in d:
            o.patient = d['patient']
        if 'scheduled_time' in d:
            o.scheduled_time = d['scheduled_time']
        if 'scheduled_time_period' in d:
            o.scheduled_time_period = d['scheduled_time_period']
        if 'take_num_url' in d:
            o.take_num_url = d['take_num_url']
        return o


