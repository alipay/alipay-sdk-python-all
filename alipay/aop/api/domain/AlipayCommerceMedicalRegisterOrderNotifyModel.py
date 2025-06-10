#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalRegisterOrderNotifyModel(object):

    def __init__(self):
        self._action = None
        self._alipay_open_id = None
        self._alipay_user_id = None
        self._appoint_part = None
        self._cancel_reason = None
        self._cancel_time = None
        self._channle = None
        self._clinic_end_time = None
        self._clinic_start_time = None
        self._clinic_time = None
        self._department_id = None
        self._doctor_id = None
        self._doctor_name = None
        self._fee = None
        self._hospital_code = None
        self._hospital_number_no = None
        self._isv_code = None
        self._isv_hos_dept_name = None
        self._isv_hos_name = None
        self._isv_user_id = None
        self._number_id = None
        self._number_seq_no = None
        self._order_no = None
        self._order_status = None
        self._order_time = None
        self._out_order_id = None
        self._patient_id = None
        self._pay_time = None
        self._pay_type = None
        self._platform_code = None
        self._register_date = None
        self._register_id = None
        self._shift_type = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def appoint_part(self):
        return self._appoint_part

    @appoint_part.setter
    def appoint_part(self, value):
        self._appoint_part = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def channle(self):
        return self._channle

    @channle.setter
    def channle(self, value):
        self._channle = value
    @property
    def clinic_end_time(self):
        return self._clinic_end_time

    @clinic_end_time.setter
    def clinic_end_time(self, value):
        self._clinic_end_time = value
    @property
    def clinic_start_time(self):
        return self._clinic_start_time

    @clinic_start_time.setter
    def clinic_start_time(self, value):
        self._clinic_start_time = value
    @property
    def clinic_time(self):
        return self._clinic_time

    @clinic_time.setter
    def clinic_time(self, value):
        self._clinic_time = value
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
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
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def hospital_code(self):
        return self._hospital_code

    @hospital_code.setter
    def hospital_code(self, value):
        self._hospital_code = value
    @property
    def hospital_number_no(self):
        return self._hospital_number_no

    @hospital_number_no.setter
    def hospital_number_no(self, value):
        self._hospital_number_no = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def isv_hos_dept_name(self):
        return self._isv_hos_dept_name

    @isv_hos_dept_name.setter
    def isv_hos_dept_name(self, value):
        self._isv_hos_dept_name = value
    @property
    def isv_hos_name(self):
        return self._isv_hos_name

    @isv_hos_name.setter
    def isv_hos_name(self, value):
        self._isv_hos_name = value
    @property
    def isv_user_id(self):
        return self._isv_user_id

    @isv_user_id.setter
    def isv_user_id(self, value):
        self._isv_user_id = value
    @property
    def number_id(self):
        return self._number_id

    @number_id.setter
    def number_id(self, value):
        self._number_id = value
    @property
    def number_seq_no(self):
        return self._number_seq_no

    @number_seq_no.setter
    def number_seq_no(self, value):
        self._number_seq_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value
    @property
    def shift_type(self):
        return self._shift_type

    @shift_type.setter
    def shift_type(self, value):
        self._shift_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.appoint_part:
            if hasattr(self.appoint_part, 'to_alipay_dict'):
                params['appoint_part'] = self.appoint_part.to_alipay_dict()
            else:
                params['appoint_part'] = self.appoint_part
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.channle:
            if hasattr(self.channle, 'to_alipay_dict'):
                params['channle'] = self.channle.to_alipay_dict()
            else:
                params['channle'] = self.channle
        if self.clinic_end_time:
            if hasattr(self.clinic_end_time, 'to_alipay_dict'):
                params['clinic_end_time'] = self.clinic_end_time.to_alipay_dict()
            else:
                params['clinic_end_time'] = self.clinic_end_time
        if self.clinic_start_time:
            if hasattr(self.clinic_start_time, 'to_alipay_dict'):
                params['clinic_start_time'] = self.clinic_start_time.to_alipay_dict()
            else:
                params['clinic_start_time'] = self.clinic_start_time
        if self.clinic_time:
            if hasattr(self.clinic_time, 'to_alipay_dict'):
                params['clinic_time'] = self.clinic_time.to_alipay_dict()
            else:
                params['clinic_time'] = self.clinic_time
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
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
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.hospital_code:
            if hasattr(self.hospital_code, 'to_alipay_dict'):
                params['hospital_code'] = self.hospital_code.to_alipay_dict()
            else:
                params['hospital_code'] = self.hospital_code
        if self.hospital_number_no:
            if hasattr(self.hospital_number_no, 'to_alipay_dict'):
                params['hospital_number_no'] = self.hospital_number_no.to_alipay_dict()
            else:
                params['hospital_number_no'] = self.hospital_number_no
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.isv_hos_dept_name:
            if hasattr(self.isv_hos_dept_name, 'to_alipay_dict'):
                params['isv_hos_dept_name'] = self.isv_hos_dept_name.to_alipay_dict()
            else:
                params['isv_hos_dept_name'] = self.isv_hos_dept_name
        if self.isv_hos_name:
            if hasattr(self.isv_hos_name, 'to_alipay_dict'):
                params['isv_hos_name'] = self.isv_hos_name.to_alipay_dict()
            else:
                params['isv_hos_name'] = self.isv_hos_name
        if self.isv_user_id:
            if hasattr(self.isv_user_id, 'to_alipay_dict'):
                params['isv_user_id'] = self.isv_user_id.to_alipay_dict()
            else:
                params['isv_user_id'] = self.isv_user_id
        if self.number_id:
            if hasattr(self.number_id, 'to_alipay_dict'):
                params['number_id'] = self.number_id.to_alipay_dict()
            else:
                params['number_id'] = self.number_id
        if self.number_seq_no:
            if hasattr(self.number_seq_no, 'to_alipay_dict'):
                params['number_seq_no'] = self.number_seq_no.to_alipay_dict()
            else:
                params['number_seq_no'] = self.number_seq_no
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.register_id:
            if hasattr(self.register_id, 'to_alipay_dict'):
                params['register_id'] = self.register_id.to_alipay_dict()
            else:
                params['register_id'] = self.register_id
        if self.shift_type:
            if hasattr(self.shift_type, 'to_alipay_dict'):
                params['shift_type'] = self.shift_type.to_alipay_dict()
            else:
                params['shift_type'] = self.shift_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalRegisterOrderNotifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'appoint_part' in d:
            o.appoint_part = d['appoint_part']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'channle' in d:
            o.channle = d['channle']
        if 'clinic_end_time' in d:
            o.clinic_end_time = d['clinic_end_time']
        if 'clinic_start_time' in d:
            o.clinic_start_time = d['clinic_start_time']
        if 'clinic_time' in d:
            o.clinic_time = d['clinic_time']
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'fee' in d:
            o.fee = d['fee']
        if 'hospital_code' in d:
            o.hospital_code = d['hospital_code']
        if 'hospital_number_no' in d:
            o.hospital_number_no = d['hospital_number_no']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'isv_hos_dept_name' in d:
            o.isv_hos_dept_name = d['isv_hos_dept_name']
        if 'isv_hos_name' in d:
            o.isv_hos_name = d['isv_hos_name']
        if 'isv_user_id' in d:
            o.isv_user_id = d['isv_user_id']
        if 'number_id' in d:
            o.number_id = d['number_id']
        if 'number_seq_no' in d:
            o.number_seq_no = d['number_seq_no']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'register_id' in d:
            o.register_id = d['register_id']
        if 'shift_type' in d:
            o.shift_type = d['shift_type']
        return o


