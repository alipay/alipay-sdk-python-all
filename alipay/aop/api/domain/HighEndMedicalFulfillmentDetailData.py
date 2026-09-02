#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HighEndMedicalFulfillmentDetailData(object):

    def __init__(self):
        self._alternative_time = None
        self._appointment_time = None
        self._bill_amount = None
        self._birth_day = None
        self._confirm_time = None
        self._department = None
        self._fulfillment_no = None
        self._fulfillment_status = None
        self._hospital_name = None
        self._out_order_no = None
        self._patient_cert_no = None
        self._patient_cert_type = None
        self._patient_gender = None
        self._patient_name = None
        self._patient_phone = None
        self._product_type = None
        self._remark = None
        self._symptom = None
        self._total_times = None
        self._type = None
        self._used_times = None

    @property
    def alternative_time(self):
        return self._alternative_time

    @alternative_time.setter
    def alternative_time(self, value):
        self._alternative_time = value
    @property
    def appointment_time(self):
        return self._appointment_time

    @appointment_time.setter
    def appointment_time(self, value):
        self._appointment_time = value
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def birth_day(self):
        return self._birth_day

    @birth_day.setter
    def birth_day(self, value):
        self._birth_day = value
    @property
    def confirm_time(self):
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, value):
        self._confirm_time = value
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def fulfillment_no(self):
        return self._fulfillment_no

    @fulfillment_no.setter
    def fulfillment_no(self, value):
        self._fulfillment_no = value
    @property
    def fulfillment_status(self):
        return self._fulfillment_status

    @fulfillment_status.setter
    def fulfillment_status(self, value):
        self._fulfillment_status = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def patient_cert_no(self):
        return self._patient_cert_no

    @patient_cert_no.setter
    def patient_cert_no(self, value):
        self._patient_cert_no = value
    @property
    def patient_cert_type(self):
        return self._patient_cert_type

    @patient_cert_type.setter
    def patient_cert_type(self, value):
        self._patient_cert_type = value
    @property
    def patient_gender(self):
        return self._patient_gender

    @patient_gender.setter
    def patient_gender(self, value):
        self._patient_gender = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def patient_phone(self):
        return self._patient_phone

    @patient_phone.setter
    def patient_phone(self, value):
        self._patient_phone = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def symptom(self):
        return self._symptom

    @symptom.setter
    def symptom(self, value):
        self._symptom = value
    @property
    def total_times(self):
        return self._total_times

    @total_times.setter
    def total_times(self, value):
        self._total_times = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def used_times(self):
        return self._used_times

    @used_times.setter
    def used_times(self, value):
        self._used_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.alternative_time:
            if hasattr(self.alternative_time, 'to_alipay_dict'):
                params['alternative_time'] = self.alternative_time.to_alipay_dict()
            else:
                params['alternative_time'] = self.alternative_time
        if self.appointment_time:
            if hasattr(self.appointment_time, 'to_alipay_dict'):
                params['appointment_time'] = self.appointment_time.to_alipay_dict()
            else:
                params['appointment_time'] = self.appointment_time
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.birth_day:
            if hasattr(self.birth_day, 'to_alipay_dict'):
                params['birth_day'] = self.birth_day.to_alipay_dict()
            else:
                params['birth_day'] = self.birth_day
        if self.confirm_time:
            if hasattr(self.confirm_time, 'to_alipay_dict'):
                params['confirm_time'] = self.confirm_time.to_alipay_dict()
            else:
                params['confirm_time'] = self.confirm_time
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.fulfillment_no:
            if hasattr(self.fulfillment_no, 'to_alipay_dict'):
                params['fulfillment_no'] = self.fulfillment_no.to_alipay_dict()
            else:
                params['fulfillment_no'] = self.fulfillment_no
        if self.fulfillment_status:
            if hasattr(self.fulfillment_status, 'to_alipay_dict'):
                params['fulfillment_status'] = self.fulfillment_status.to_alipay_dict()
            else:
                params['fulfillment_status'] = self.fulfillment_status
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.patient_cert_no:
            if hasattr(self.patient_cert_no, 'to_alipay_dict'):
                params['patient_cert_no'] = self.patient_cert_no.to_alipay_dict()
            else:
                params['patient_cert_no'] = self.patient_cert_no
        if self.patient_cert_type:
            if hasattr(self.patient_cert_type, 'to_alipay_dict'):
                params['patient_cert_type'] = self.patient_cert_type.to_alipay_dict()
            else:
                params['patient_cert_type'] = self.patient_cert_type
        if self.patient_gender:
            if hasattr(self.patient_gender, 'to_alipay_dict'):
                params['patient_gender'] = self.patient_gender.to_alipay_dict()
            else:
                params['patient_gender'] = self.patient_gender
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.patient_phone:
            if hasattr(self.patient_phone, 'to_alipay_dict'):
                params['patient_phone'] = self.patient_phone.to_alipay_dict()
            else:
                params['patient_phone'] = self.patient_phone
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.symptom:
            if hasattr(self.symptom, 'to_alipay_dict'):
                params['symptom'] = self.symptom.to_alipay_dict()
            else:
                params['symptom'] = self.symptom
        if self.total_times:
            if hasattr(self.total_times, 'to_alipay_dict'):
                params['total_times'] = self.total_times.to_alipay_dict()
            else:
                params['total_times'] = self.total_times
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.used_times:
            if hasattr(self.used_times, 'to_alipay_dict'):
                params['used_times'] = self.used_times.to_alipay_dict()
            else:
                params['used_times'] = self.used_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HighEndMedicalFulfillmentDetailData()
        if 'alternative_time' in d:
            o.alternative_time = d['alternative_time']
        if 'appointment_time' in d:
            o.appointment_time = d['appointment_time']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'birth_day' in d:
            o.birth_day = d['birth_day']
        if 'confirm_time' in d:
            o.confirm_time = d['confirm_time']
        if 'department' in d:
            o.department = d['department']
        if 'fulfillment_no' in d:
            o.fulfillment_no = d['fulfillment_no']
        if 'fulfillment_status' in d:
            o.fulfillment_status = d['fulfillment_status']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'patient_cert_no' in d:
            o.patient_cert_no = d['patient_cert_no']
        if 'patient_cert_type' in d:
            o.patient_cert_type = d['patient_cert_type']
        if 'patient_gender' in d:
            o.patient_gender = d['patient_gender']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_phone' in d:
            o.patient_phone = d['patient_phone']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'remark' in d:
            o.remark = d['remark']
        if 'symptom' in d:
            o.symptom = d['symptom']
        if 'total_times' in d:
            o.total_times = d['total_times']
        if 'type' in d:
            o.type = d['type']
        if 'used_times' in d:
            o.used_times = d['used_times']
        return o


