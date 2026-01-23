#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceTpaappointmentstatusNotifyModel(object):

    def __init__(self):
        self._appointment_no = None
        self._appointment_status = None
        self._appointment_status_msg = None
        self._fail_reason = None
        self._open_id = None
        self._user_id = None
        self._visit_department = None
        self._visit_hospital = None
        self._visit_hospital_address = None
        self._visit_hospital_code = None
        self._visit_store_code = None
        self._visit_time = None

    @property
    def appointment_no(self):
        return self._appointment_no

    @appointment_no.setter
    def appointment_no(self, value):
        self._appointment_no = value
    @property
    def appointment_status(self):
        return self._appointment_status

    @appointment_status.setter
    def appointment_status(self, value):
        self._appointment_status = value
    @property
    def appointment_status_msg(self):
        return self._appointment_status_msg

    @appointment_status_msg.setter
    def appointment_status_msg(self, value):
        self._appointment_status_msg = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def visit_department(self):
        return self._visit_department

    @visit_department.setter
    def visit_department(self, value):
        self._visit_department = value
    @property
    def visit_hospital(self):
        return self._visit_hospital

    @visit_hospital.setter
    def visit_hospital(self, value):
        self._visit_hospital = value
    @property
    def visit_hospital_address(self):
        return self._visit_hospital_address

    @visit_hospital_address.setter
    def visit_hospital_address(self, value):
        self._visit_hospital_address = value
    @property
    def visit_hospital_code(self):
        return self._visit_hospital_code

    @visit_hospital_code.setter
    def visit_hospital_code(self, value):
        self._visit_hospital_code = value
    @property
    def visit_store_code(self):
        return self._visit_store_code

    @visit_store_code.setter
    def visit_store_code(self, value):
        self._visit_store_code = value
    @property
    def visit_time(self):
        return self._visit_time

    @visit_time.setter
    def visit_time(self, value):
        self._visit_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.appointment_no:
            if hasattr(self.appointment_no, 'to_alipay_dict'):
                params['appointment_no'] = self.appointment_no.to_alipay_dict()
            else:
                params['appointment_no'] = self.appointment_no
        if self.appointment_status:
            if hasattr(self.appointment_status, 'to_alipay_dict'):
                params['appointment_status'] = self.appointment_status.to_alipay_dict()
            else:
                params['appointment_status'] = self.appointment_status
        if self.appointment_status_msg:
            if hasattr(self.appointment_status_msg, 'to_alipay_dict'):
                params['appointment_status_msg'] = self.appointment_status_msg.to_alipay_dict()
            else:
                params['appointment_status_msg'] = self.appointment_status_msg
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.visit_department:
            if hasattr(self.visit_department, 'to_alipay_dict'):
                params['visit_department'] = self.visit_department.to_alipay_dict()
            else:
                params['visit_department'] = self.visit_department
        if self.visit_hospital:
            if hasattr(self.visit_hospital, 'to_alipay_dict'):
                params['visit_hospital'] = self.visit_hospital.to_alipay_dict()
            else:
                params['visit_hospital'] = self.visit_hospital
        if self.visit_hospital_address:
            if hasattr(self.visit_hospital_address, 'to_alipay_dict'):
                params['visit_hospital_address'] = self.visit_hospital_address.to_alipay_dict()
            else:
                params['visit_hospital_address'] = self.visit_hospital_address
        if self.visit_hospital_code:
            if hasattr(self.visit_hospital_code, 'to_alipay_dict'):
                params['visit_hospital_code'] = self.visit_hospital_code.to_alipay_dict()
            else:
                params['visit_hospital_code'] = self.visit_hospital_code
        if self.visit_store_code:
            if hasattr(self.visit_store_code, 'to_alipay_dict'):
                params['visit_store_code'] = self.visit_store_code.to_alipay_dict()
            else:
                params['visit_store_code'] = self.visit_store_code
        if self.visit_time:
            if hasattr(self.visit_time, 'to_alipay_dict'):
                params['visit_time'] = self.visit_time.to_alipay_dict()
            else:
                params['visit_time'] = self.visit_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceTpaappointmentstatusNotifyModel()
        if 'appointment_no' in d:
            o.appointment_no = d['appointment_no']
        if 'appointment_status' in d:
            o.appointment_status = d['appointment_status']
        if 'appointment_status_msg' in d:
            o.appointment_status_msg = d['appointment_status_msg']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'visit_department' in d:
            o.visit_department = d['visit_department']
        if 'visit_hospital' in d:
            o.visit_hospital = d['visit_hospital']
        if 'visit_hospital_address' in d:
            o.visit_hospital_address = d['visit_hospital_address']
        if 'visit_hospital_code' in d:
            o.visit_hospital_code = d['visit_hospital_code']
        if 'visit_store_code' in d:
            o.visit_store_code = d['visit_store_code']
        if 'visit_time' in d:
            o.visit_time = d['visit_time']
        return o


