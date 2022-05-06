#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalHospitalOrderUploadExtInfo(object):

    def __init__(self):
        self._call_num_url = None
        self._check_item = None
        self._check_loc = None
        self._check_num = None
        self._check_precautions = None
        self._check_time = None
        self._current_num = None
        self._department = None
        self._dept_loc = None
        self._dept_num = None
        self._doctor = None
        self._doctor_avatar = None
        self._doctor_id = None
        self._doctor_rank = None
        self._expected_waiting_time = None
        self._hospital = None
        self._hospital_id_type = None
        self._hospital_register_id = None
        self._medical_num = None
        self._medical_order_id = None
        self._merchant_order_link_page = None
        self._navigation = None
        self._patient = None
        self._report_url = None
        self._scheduled_time = None
        self._take_medicine_loc = None
        self._take_medicine_url = None
        self._take_num_password = None
        self._take_num_url = None
        self._user_card_no = None
        self._user_card_type = None
        self._waiting_num = None

    @property
    def call_num_url(self):
        return self._call_num_url

    @call_num_url.setter
    def call_num_url(self, value):
        self._call_num_url = value
    @property
    def check_item(self):
        return self._check_item

    @check_item.setter
    def check_item(self, value):
        self._check_item = value
    @property
    def check_loc(self):
        return self._check_loc

    @check_loc.setter
    def check_loc(self, value):
        self._check_loc = value
    @property
    def check_num(self):
        return self._check_num

    @check_num.setter
    def check_num(self, value):
        self._check_num = value
    @property
    def check_precautions(self):
        return self._check_precautions

    @check_precautions.setter
    def check_precautions(self, value):
        self._check_precautions = value
    @property
    def check_time(self):
        return self._check_time

    @check_time.setter
    def check_time(self, value):
        self._check_time = value
    @property
    def current_num(self):
        return self._current_num

    @current_num.setter
    def current_num(self, value):
        self._current_num = value
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
    def doctor_avatar(self):
        return self._doctor_avatar

    @doctor_avatar.setter
    def doctor_avatar(self, value):
        self._doctor_avatar = value
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
    def expected_waiting_time(self):
        return self._expected_waiting_time

    @expected_waiting_time.setter
    def expected_waiting_time(self, value):
        self._expected_waiting_time = value
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
    def medical_order_id(self):
        return self._medical_order_id

    @medical_order_id.setter
    def medical_order_id(self, value):
        self._medical_order_id = value
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
    def report_url(self):
        return self._report_url

    @report_url.setter
    def report_url(self, value):
        self._report_url = value
    @property
    def scheduled_time(self):
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, value):
        self._scheduled_time = value
    @property
    def take_medicine_loc(self):
        return self._take_medicine_loc

    @take_medicine_loc.setter
    def take_medicine_loc(self, value):
        self._take_medicine_loc = value
    @property
    def take_medicine_url(self):
        return self._take_medicine_url

    @take_medicine_url.setter
    def take_medicine_url(self, value):
        self._take_medicine_url = value
    @property
    def take_num_password(self):
        return self._take_num_password

    @take_num_password.setter
    def take_num_password(self, value):
        self._take_num_password = value
    @property
    def take_num_url(self):
        return self._take_num_url

    @take_num_url.setter
    def take_num_url(self, value):
        self._take_num_url = value
    @property
    def user_card_no(self):
        return self._user_card_no

    @user_card_no.setter
    def user_card_no(self, value):
        self._user_card_no = value
    @property
    def user_card_type(self):
        return self._user_card_type

    @user_card_type.setter
    def user_card_type(self, value):
        self._user_card_type = value
    @property
    def waiting_num(self):
        return self._waiting_num

    @waiting_num.setter
    def waiting_num(self, value):
        self._waiting_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.call_num_url:
            if hasattr(self.call_num_url, 'to_alipay_dict'):
                params['call_num_url'] = self.call_num_url.to_alipay_dict()
            else:
                params['call_num_url'] = self.call_num_url
        if self.check_item:
            if hasattr(self.check_item, 'to_alipay_dict'):
                params['check_item'] = self.check_item.to_alipay_dict()
            else:
                params['check_item'] = self.check_item
        if self.check_loc:
            if hasattr(self.check_loc, 'to_alipay_dict'):
                params['check_loc'] = self.check_loc.to_alipay_dict()
            else:
                params['check_loc'] = self.check_loc
        if self.check_num:
            if hasattr(self.check_num, 'to_alipay_dict'):
                params['check_num'] = self.check_num.to_alipay_dict()
            else:
                params['check_num'] = self.check_num
        if self.check_precautions:
            if hasattr(self.check_precautions, 'to_alipay_dict'):
                params['check_precautions'] = self.check_precautions.to_alipay_dict()
            else:
                params['check_precautions'] = self.check_precautions
        if self.check_time:
            if hasattr(self.check_time, 'to_alipay_dict'):
                params['check_time'] = self.check_time.to_alipay_dict()
            else:
                params['check_time'] = self.check_time
        if self.current_num:
            if hasattr(self.current_num, 'to_alipay_dict'):
                params['current_num'] = self.current_num.to_alipay_dict()
            else:
                params['current_num'] = self.current_num
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
        if self.doctor_avatar:
            if hasattr(self.doctor_avatar, 'to_alipay_dict'):
                params['doctor_avatar'] = self.doctor_avatar.to_alipay_dict()
            else:
                params['doctor_avatar'] = self.doctor_avatar
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
        if self.expected_waiting_time:
            if hasattr(self.expected_waiting_time, 'to_alipay_dict'):
                params['expected_waiting_time'] = self.expected_waiting_time.to_alipay_dict()
            else:
                params['expected_waiting_time'] = self.expected_waiting_time
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
        if self.medical_order_id:
            if hasattr(self.medical_order_id, 'to_alipay_dict'):
                params['medical_order_id'] = self.medical_order_id.to_alipay_dict()
            else:
                params['medical_order_id'] = self.medical_order_id
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
        if self.report_url:
            if hasattr(self.report_url, 'to_alipay_dict'):
                params['report_url'] = self.report_url.to_alipay_dict()
            else:
                params['report_url'] = self.report_url
        if self.scheduled_time:
            if hasattr(self.scheduled_time, 'to_alipay_dict'):
                params['scheduled_time'] = self.scheduled_time.to_alipay_dict()
            else:
                params['scheduled_time'] = self.scheduled_time
        if self.take_medicine_loc:
            if hasattr(self.take_medicine_loc, 'to_alipay_dict'):
                params['take_medicine_loc'] = self.take_medicine_loc.to_alipay_dict()
            else:
                params['take_medicine_loc'] = self.take_medicine_loc
        if self.take_medicine_url:
            if hasattr(self.take_medicine_url, 'to_alipay_dict'):
                params['take_medicine_url'] = self.take_medicine_url.to_alipay_dict()
            else:
                params['take_medicine_url'] = self.take_medicine_url
        if self.take_num_password:
            if hasattr(self.take_num_password, 'to_alipay_dict'):
                params['take_num_password'] = self.take_num_password.to_alipay_dict()
            else:
                params['take_num_password'] = self.take_num_password
        if self.take_num_url:
            if hasattr(self.take_num_url, 'to_alipay_dict'):
                params['take_num_url'] = self.take_num_url.to_alipay_dict()
            else:
                params['take_num_url'] = self.take_num_url
        if self.user_card_no:
            if hasattr(self.user_card_no, 'to_alipay_dict'):
                params['user_card_no'] = self.user_card_no.to_alipay_dict()
            else:
                params['user_card_no'] = self.user_card_no
        if self.user_card_type:
            if hasattr(self.user_card_type, 'to_alipay_dict'):
                params['user_card_type'] = self.user_card_type.to_alipay_dict()
            else:
                params['user_card_type'] = self.user_card_type
        if self.waiting_num:
            if hasattr(self.waiting_num, 'to_alipay_dict'):
                params['waiting_num'] = self.waiting_num.to_alipay_dict()
            else:
                params['waiting_num'] = self.waiting_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalHospitalOrderUploadExtInfo()
        if 'call_num_url' in d:
            o.call_num_url = d['call_num_url']
        if 'check_item' in d:
            o.check_item = d['check_item']
        if 'check_loc' in d:
            o.check_loc = d['check_loc']
        if 'check_num' in d:
            o.check_num = d['check_num']
        if 'check_precautions' in d:
            o.check_precautions = d['check_precautions']
        if 'check_time' in d:
            o.check_time = d['check_time']
        if 'current_num' in d:
            o.current_num = d['current_num']
        if 'department' in d:
            o.department = d['department']
        if 'dept_loc' in d:
            o.dept_loc = d['dept_loc']
        if 'dept_num' in d:
            o.dept_num = d['dept_num']
        if 'doctor' in d:
            o.doctor = d['doctor']
        if 'doctor_avatar' in d:
            o.doctor_avatar = d['doctor_avatar']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_rank' in d:
            o.doctor_rank = d['doctor_rank']
        if 'expected_waiting_time' in d:
            o.expected_waiting_time = d['expected_waiting_time']
        if 'hospital' in d:
            o.hospital = d['hospital']
        if 'hospital_id_type' in d:
            o.hospital_id_type = d['hospital_id_type']
        if 'hospital_register_id' in d:
            o.hospital_register_id = d['hospital_register_id']
        if 'medical_num' in d:
            o.medical_num = d['medical_num']
        if 'medical_order_id' in d:
            o.medical_order_id = d['medical_order_id']
        if 'merchant_order_link_page' in d:
            o.merchant_order_link_page = d['merchant_order_link_page']
        if 'navigation' in d:
            o.navigation = d['navigation']
        if 'patient' in d:
            o.patient = d['patient']
        if 'report_url' in d:
            o.report_url = d['report_url']
        if 'scheduled_time' in d:
            o.scheduled_time = d['scheduled_time']
        if 'take_medicine_loc' in d:
            o.take_medicine_loc = d['take_medicine_loc']
        if 'take_medicine_url' in d:
            o.take_medicine_url = d['take_medicine_url']
        if 'take_num_password' in d:
            o.take_num_password = d['take_num_password']
        if 'take_num_url' in d:
            o.take_num_url = d['take_num_url']
        if 'user_card_no' in d:
            o.user_card_no = d['user_card_no']
        if 'user_card_type' in d:
            o.user_card_type = d['user_card_type']
        if 'waiting_num' in d:
            o.waiting_num = d['waiting_num']
        return o


