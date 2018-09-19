#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalHospitalDeptInfo import MedicalHospitalDeptInfo
from alipay.aop.api.domain.MedicalHospitalDoctorInfo import MedicalHospitalDoctorInfo
from alipay.aop.api.domain.MedicalHospitalInfo import MedicalHospitalInfo


class AlipayEcoMedicalcareHosRegnotifyModel(object):

    def __init__(self):
        self._biz_type = None
        self._cancel_desc = None
        self._cancel_reason = None
        self._dept_info = None
        self._doctor_info = None
        self._extend_params = None
        self._hos_info = None
        self._line_no = None
        self._notify_time = None
        self._operate = None
        self._order_link = None
        self._patient_card_no = None
        self._patient_card_type = None
        self._patient_name = None
        self._reg_link = None
        self._third_no = None
        self._treat_date = None
        self._treat_date_ext = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cancel_desc(self):
        return self._cancel_desc

    @cancel_desc.setter
    def cancel_desc(self, value):
        self._cancel_desc = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
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
    def line_no(self):
        return self._line_no

    @line_no.setter
    def line_no(self, value):
        self._line_no = value
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
    def order_link(self):
        return self._order_link

    @order_link.setter
    def order_link(self, value):
        self._order_link = value
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
    def reg_link(self):
        return self._reg_link

    @reg_link.setter
    def reg_link(self, value):
        self._reg_link = value
    @property
    def third_no(self):
        return self._third_no

    @third_no.setter
    def third_no(self, value):
        self._third_no = value
    @property
    def treat_date(self):
        return self._treat_date

    @treat_date.setter
    def treat_date(self, value):
        self._treat_date = value
    @property
    def treat_date_ext(self):
        return self._treat_date_ext

    @treat_date_ext.setter
    def treat_date_ext(self, value):
        self._treat_date_ext = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cancel_desc:
            if hasattr(self.cancel_desc, 'to_alipay_dict'):
                params['cancel_desc'] = self.cancel_desc.to_alipay_dict()
            else:
                params['cancel_desc'] = self.cancel_desc
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
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
        if self.line_no:
            if hasattr(self.line_no, 'to_alipay_dict'):
                params['line_no'] = self.line_no.to_alipay_dict()
            else:
                params['line_no'] = self.line_no
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
        if self.order_link:
            if hasattr(self.order_link, 'to_alipay_dict'):
                params['order_link'] = self.order_link.to_alipay_dict()
            else:
                params['order_link'] = self.order_link
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
        if self.reg_link:
            if hasattr(self.reg_link, 'to_alipay_dict'):
                params['reg_link'] = self.reg_link.to_alipay_dict()
            else:
                params['reg_link'] = self.reg_link
        if self.third_no:
            if hasattr(self.third_no, 'to_alipay_dict'):
                params['third_no'] = self.third_no.to_alipay_dict()
            else:
                params['third_no'] = self.third_no
        if self.treat_date:
            if hasattr(self.treat_date, 'to_alipay_dict'):
                params['treat_date'] = self.treat_date.to_alipay_dict()
            else:
                params['treat_date'] = self.treat_date
        if self.treat_date_ext:
            if hasattr(self.treat_date_ext, 'to_alipay_dict'):
                params['treat_date_ext'] = self.treat_date_ext.to_alipay_dict()
            else:
                params['treat_date_ext'] = self.treat_date_ext
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
        o = AlipayEcoMedicalcareHosRegnotifyModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cancel_desc' in d:
            o.cancel_desc = d['cancel_desc']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'dept_info' in d:
            o.dept_info = d['dept_info']
        if 'doctor_info' in d:
            o.doctor_info = d['doctor_info']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'hos_info' in d:
            o.hos_info = d['hos_info']
        if 'line_no' in d:
            o.line_no = d['line_no']
        if 'notify_time' in d:
            o.notify_time = d['notify_time']
        if 'operate' in d:
            o.operate = d['operate']
        if 'order_link' in d:
            o.order_link = d['order_link']
        if 'patient_card_no' in d:
            o.patient_card_no = d['patient_card_no']
        if 'patient_card_type' in d:
            o.patient_card_type = d['patient_card_type']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'reg_link' in d:
            o.reg_link = d['reg_link']
        if 'third_no' in d:
            o.third_no = d['third_no']
        if 'treat_date' in d:
            o.treat_date = d['treat_date']
        if 'treat_date_ext' in d:
            o.treat_date_ext = d['treat_date_ext']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


