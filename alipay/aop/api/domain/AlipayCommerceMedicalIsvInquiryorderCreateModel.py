#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIsvInquiryorderCreateModel(object):

    def __init__(self):
        self._amount = None
        self._aq_patient_id = None
        self._business_type = None
        self._disease_desc = None
        self._inquiry_mode = None
        self._inquiry_type = None
        self._isv_code = None
        self._order_status = None
        self._out_chat_id = None
        self._out_doctor_id = None
        self._out_order_id = None
        self._patient_birthday = None
        self._patient_gender = None
        self._patient_name = None
        self._platform_code = None
        self._service_id = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def aq_patient_id(self):
        return self._aq_patient_id

    @aq_patient_id.setter
    def aq_patient_id(self, value):
        self._aq_patient_id = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def disease_desc(self):
        return self._disease_desc

    @disease_desc.setter
    def disease_desc(self, value):
        self._disease_desc = value
    @property
    def inquiry_mode(self):
        return self._inquiry_mode

    @inquiry_mode.setter
    def inquiry_mode(self, value):
        self._inquiry_mode = value
    @property
    def inquiry_type(self):
        return self._inquiry_type

    @inquiry_type.setter
    def inquiry_type(self, value):
        self._inquiry_type = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_chat_id(self):
        return self._out_chat_id

    @out_chat_id.setter
    def out_chat_id(self, value):
        self._out_chat_id = value
    @property
    def out_doctor_id(self):
        return self._out_doctor_id

    @out_doctor_id.setter
    def out_doctor_id(self, value):
        self._out_doctor_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def patient_birthday(self):
        return self._patient_birthday

    @patient_birthday.setter
    def patient_birthday(self, value):
        self._patient_birthday = value
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
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.aq_patient_id:
            if hasattr(self.aq_patient_id, 'to_alipay_dict'):
                params['aq_patient_id'] = self.aq_patient_id.to_alipay_dict()
            else:
                params['aq_patient_id'] = self.aq_patient_id
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.disease_desc:
            if hasattr(self.disease_desc, 'to_alipay_dict'):
                params['disease_desc'] = self.disease_desc.to_alipay_dict()
            else:
                params['disease_desc'] = self.disease_desc
        if self.inquiry_mode:
            if hasattr(self.inquiry_mode, 'to_alipay_dict'):
                params['inquiry_mode'] = self.inquiry_mode.to_alipay_dict()
            else:
                params['inquiry_mode'] = self.inquiry_mode
        if self.inquiry_type:
            if hasattr(self.inquiry_type, 'to_alipay_dict'):
                params['inquiry_type'] = self.inquiry_type.to_alipay_dict()
            else:
                params['inquiry_type'] = self.inquiry_type
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_chat_id:
            if hasattr(self.out_chat_id, 'to_alipay_dict'):
                params['out_chat_id'] = self.out_chat_id.to_alipay_dict()
            else:
                params['out_chat_id'] = self.out_chat_id
        if self.out_doctor_id:
            if hasattr(self.out_doctor_id, 'to_alipay_dict'):
                params['out_doctor_id'] = self.out_doctor_id.to_alipay_dict()
            else:
                params['out_doctor_id'] = self.out_doctor_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.patient_birthday:
            if hasattr(self.patient_birthday, 'to_alipay_dict'):
                params['patient_birthday'] = self.patient_birthday.to_alipay_dict()
            else:
                params['patient_birthday'] = self.patient_birthday
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
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
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
        o = AlipayCommerceMedicalIsvInquiryorderCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'aq_patient_id' in d:
            o.aq_patient_id = d['aq_patient_id']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'disease_desc' in d:
            o.disease_desc = d['disease_desc']
        if 'inquiry_mode' in d:
            o.inquiry_mode = d['inquiry_mode']
        if 'inquiry_type' in d:
            o.inquiry_type = d['inquiry_type']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_chat_id' in d:
            o.out_chat_id = d['out_chat_id']
        if 'out_doctor_id' in d:
            o.out_doctor_id = d['out_doctor_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'patient_birthday' in d:
            o.patient_birthday = d['patient_birthday']
        if 'patient_gender' in d:
            o.patient_gender = d['patient_gender']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


