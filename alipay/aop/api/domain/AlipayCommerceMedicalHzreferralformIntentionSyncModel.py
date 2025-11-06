#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHzreferralformIntentionSyncModel(object):

    def __init__(self):
        self._doctor_remark = None
        self._process_time = None
        self._referral_form_id = None
        self._status = None
        self._visit_department = None
        self._visit_doctor = None
        self._visit_hospital = None
        self._visit_time = None

    @property
    def doctor_remark(self):
        return self._doctor_remark

    @doctor_remark.setter
    def doctor_remark(self, value):
        self._doctor_remark = value
    @property
    def process_time(self):
        return self._process_time

    @process_time.setter
    def process_time(self, value):
        self._process_time = value
    @property
    def referral_form_id(self):
        return self._referral_form_id

    @referral_form_id.setter
    def referral_form_id(self, value):
        self._referral_form_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def visit_department(self):
        return self._visit_department

    @visit_department.setter
    def visit_department(self, value):
        self._visit_department = value
    @property
    def visit_doctor(self):
        return self._visit_doctor

    @visit_doctor.setter
    def visit_doctor(self, value):
        self._visit_doctor = value
    @property
    def visit_hospital(self):
        return self._visit_hospital

    @visit_hospital.setter
    def visit_hospital(self, value):
        self._visit_hospital = value
    @property
    def visit_time(self):
        return self._visit_time

    @visit_time.setter
    def visit_time(self, value):
        self._visit_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_remark:
            if hasattr(self.doctor_remark, 'to_alipay_dict'):
                params['doctor_remark'] = self.doctor_remark.to_alipay_dict()
            else:
                params['doctor_remark'] = self.doctor_remark
        if self.process_time:
            if hasattr(self.process_time, 'to_alipay_dict'):
                params['process_time'] = self.process_time.to_alipay_dict()
            else:
                params['process_time'] = self.process_time
        if self.referral_form_id:
            if hasattr(self.referral_form_id, 'to_alipay_dict'):
                params['referral_form_id'] = self.referral_form_id.to_alipay_dict()
            else:
                params['referral_form_id'] = self.referral_form_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.visit_department:
            if hasattr(self.visit_department, 'to_alipay_dict'):
                params['visit_department'] = self.visit_department.to_alipay_dict()
            else:
                params['visit_department'] = self.visit_department
        if self.visit_doctor:
            if hasattr(self.visit_doctor, 'to_alipay_dict'):
                params['visit_doctor'] = self.visit_doctor.to_alipay_dict()
            else:
                params['visit_doctor'] = self.visit_doctor
        if self.visit_hospital:
            if hasattr(self.visit_hospital, 'to_alipay_dict'):
                params['visit_hospital'] = self.visit_hospital.to_alipay_dict()
            else:
                params['visit_hospital'] = self.visit_hospital
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
        o = AlipayCommerceMedicalHzreferralformIntentionSyncModel()
        if 'doctor_remark' in d:
            o.doctor_remark = d['doctor_remark']
        if 'process_time' in d:
            o.process_time = d['process_time']
        if 'referral_form_id' in d:
            o.referral_form_id = d['referral_form_id']
        if 'status' in d:
            o.status = d['status']
        if 'visit_department' in d:
            o.visit_department = d['visit_department']
        if 'visit_doctor' in d:
            o.visit_doctor = d['visit_doctor']
        if 'visit_hospital' in d:
            o.visit_hospital = d['visit_hospital']
        if 'visit_time' in d:
            o.visit_time = d['visit_time']
        return o


