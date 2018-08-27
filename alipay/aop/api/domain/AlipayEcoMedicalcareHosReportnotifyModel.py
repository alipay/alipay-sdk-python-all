#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalHospitalDeptInfo import MedicalHospitalDeptInfo
from alipay.aop.api.domain.MedicalHospitalDoctorInfo import MedicalHospitalDoctorInfo
from alipay.aop.api.domain.MedicalHospitalInfo import MedicalHospitalInfo
from alipay.aop.api.domain.MedicalHospitalReportList import MedicalHospitalReportList


class AlipayEcoMedicalcareHosReportnotifyModel(object):

    def __init__(self):
        self._dept_info = None
        self._doctor_info = None
        self._extend_params = None
        self._hos_info = None
        self._notify_time = None
        self._operate = None
        self._patient_card_no = None
        self._patient_card_type = None
        self._patient_name = None
        self._reg_out_trade_no = None
        self._report_list = None
        self._third_no = None
        self._treat_out_trade_no = None
        self._user_id = None

    @property
    def dept_info(self):
        return self._dept_info

    @dept_info.setter
    def dept_info(self, value):
        if isinstance(value, MedicalHospitalDeptInfo):
            self._dept_info = value
        else:
            self._dept_info = MedicalHospitalDeptInfo.from_alipay_dict(value)
    @property
    def doctor_info(self):
        return self._doctor_info

    @doctor_info.setter
    def doctor_info(self, value):
        if isinstance(value, MedicalHospitalDoctorInfo):
            self._doctor_info = value
        else:
            self._doctor_info = MedicalHospitalDoctorInfo.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def hos_info(self):
        return self._hos_info

    @hos_info.setter
    def hos_info(self, value):
        if isinstance(value, MedicalHospitalInfo):
            self._hos_info = value
        else:
            self._hos_info = MedicalHospitalInfo.from_alipay_dict(value)
    @property
    def notify_time(self):
        return self._notify_time

    @notify_time.setter
    def notify_time(self, value):
        self._notify_time = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def patient_card_no(self):
        return self._patient_card_no

    @patient_card_no.setter
    def patient_card_no(self, value):
        self._patient_card_no = value
    @property
    def patient_card_type(self):
        return self._patient_card_type

    @patient_card_type.setter
    def patient_card_type(self, value):
        self._patient_card_type = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def reg_out_trade_no(self):
        return self._reg_out_trade_no

    @reg_out_trade_no.setter
    def reg_out_trade_no(self, value):
        self._reg_out_trade_no = value
    @property
    def report_list(self):
        return self._report_list

    @report_list.setter
    def report_list(self, value):
        if isinstance(value, list):
            self._report_list = list()
            for i in value:
                if isinstance(i, MedicalHospitalReportList):
                    self._report_list.append(i)
                else:
                    self._report_list.append(MedicalHospitalReportList.from_alipay_dict(i))
    @property
    def third_no(self):
        return self._third_no

    @third_no.setter
    def third_no(self, value):
        self._third_no = value
    @property
    def treat_out_trade_no(self):
        return self._treat_out_trade_no

    @treat_out_trade_no.setter
    def treat_out_trade_no(self, value):
        self._treat_out_trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dept_info:
            if hasattr(self.dept_info, 'to_alipay_dict'):
                params['dept_info'] = self.dept_info.to_alipay_dict()
            else:
                params['dept_info'] = self.dept_info
        if self.doctor_info:
            if hasattr(self.doctor_info, 'to_alipay_dict'):
                params['doctor_info'] = self.doctor_info.to_alipay_dict()
            else:
                params['doctor_info'] = self.doctor_info
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.hos_info:
            if hasattr(self.hos_info, 'to_alipay_dict'):
                params['hos_info'] = self.hos_info.to_alipay_dict()
            else:
                params['hos_info'] = self.hos_info
        if self.notify_time:
            if hasattr(self.notify_time, 'to_alipay_dict'):
                params['notify_time'] = self.notify_time.to_alipay_dict()
            else:
                params['notify_time'] = self.notify_time
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.patient_card_no:
            if hasattr(self.patient_card_no, 'to_alipay_dict'):
                params['patient_card_no'] = self.patient_card_no.to_alipay_dict()
            else:
                params['patient_card_no'] = self.patient_card_no
        if self.patient_card_type:
            if hasattr(self.patient_card_type, 'to_alipay_dict'):
                params['patient_card_type'] = self.patient_card_type.to_alipay_dict()
            else:
                params['patient_card_type'] = self.patient_card_type
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.reg_out_trade_no:
            if hasattr(self.reg_out_trade_no, 'to_alipay_dict'):
                params['reg_out_trade_no'] = self.reg_out_trade_no.to_alipay_dict()
            else:
                params['reg_out_trade_no'] = self.reg_out_trade_no
        if self.report_list:
            if isinstance(self.report_list, list):
                for i in range(0, len(self.report_list)):
                    element = self.report_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.report_list[i] = element.to_alipay_dict()
            if hasattr(self.report_list, 'to_alipay_dict'):
                params['report_list'] = self.report_list.to_alipay_dict()
            else:
                params['report_list'] = self.report_list
        if self.third_no:
            if hasattr(self.third_no, 'to_alipay_dict'):
                params['third_no'] = self.third_no.to_alipay_dict()
            else:
                params['third_no'] = self.third_no
        if self.treat_out_trade_no:
            if hasattr(self.treat_out_trade_no, 'to_alipay_dict'):
                params['treat_out_trade_no'] = self.treat_out_trade_no.to_alipay_dict()
            else:
                params['treat_out_trade_no'] = self.treat_out_trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMedicalcareHosReportnotifyModel()
        if 'dept_info' in d:
            o.dept_info = d['dept_info']
        if 'doctor_info' in d:
            o.doctor_info = d['doctor_info']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'hos_info' in d:
            o.hos_info = d['hos_info']
        if 'notify_time' in d:
            o.notify_time = d['notify_time']
        if 'operate' in d:
            o.operate = d['operate']
        if 'patient_card_no' in d:
            o.patient_card_no = d['patient_card_no']
        if 'patient_card_type' in d:
            o.patient_card_type = d['patient_card_type']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'reg_out_trade_no' in d:
            o.reg_out_trade_no = d['reg_out_trade_no']
        if 'report_list' in d:
            o.report_list = d['report_list']
        if 'third_no' in d:
            o.third_no = d['third_no']
        if 'treat_out_trade_no' in d:
            o.treat_out_trade_no = d['treat_out_trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


