#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReserveCustomer(object):

    def __init__(self):
        self._customer_birthday = None
        self._customer_gender = None
        self._customer_identity_no = None
        self._customer_identity_type = None
        self._customer_medical_status = None
        self._customer_mobile_phone = None
        self._customer_name = None
        self._prepare_pregnancy = None

    @property
    def customer_birthday(self):
        return self._customer_birthday

    @customer_birthday.setter
    def customer_birthday(self, value):
        self._customer_birthday = value
    @property
    def customer_gender(self):
        return self._customer_gender

    @customer_gender.setter
    def customer_gender(self, value):
        self._customer_gender = value
    @property
    def customer_identity_no(self):
        return self._customer_identity_no

    @customer_identity_no.setter
    def customer_identity_no(self, value):
        self._customer_identity_no = value
    @property
    def customer_identity_type(self):
        return self._customer_identity_type

    @customer_identity_type.setter
    def customer_identity_type(self, value):
        self._customer_identity_type = value
    @property
    def customer_medical_status(self):
        return self._customer_medical_status

    @customer_medical_status.setter
    def customer_medical_status(self, value):
        self._customer_medical_status = value
    @property
    def customer_mobile_phone(self):
        return self._customer_mobile_phone

    @customer_mobile_phone.setter
    def customer_mobile_phone(self, value):
        self._customer_mobile_phone = value
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def prepare_pregnancy(self):
        return self._prepare_pregnancy

    @prepare_pregnancy.setter
    def prepare_pregnancy(self, value):
        self._prepare_pregnancy = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_birthday:
            if hasattr(self.customer_birthday, 'to_alipay_dict'):
                params['customer_birthday'] = self.customer_birthday.to_alipay_dict()
            else:
                params['customer_birthday'] = self.customer_birthday
        if self.customer_gender:
            if hasattr(self.customer_gender, 'to_alipay_dict'):
                params['customer_gender'] = self.customer_gender.to_alipay_dict()
            else:
                params['customer_gender'] = self.customer_gender
        if self.customer_identity_no:
            if hasattr(self.customer_identity_no, 'to_alipay_dict'):
                params['customer_identity_no'] = self.customer_identity_no.to_alipay_dict()
            else:
                params['customer_identity_no'] = self.customer_identity_no
        if self.customer_identity_type:
            if hasattr(self.customer_identity_type, 'to_alipay_dict'):
                params['customer_identity_type'] = self.customer_identity_type.to_alipay_dict()
            else:
                params['customer_identity_type'] = self.customer_identity_type
        if self.customer_medical_status:
            if hasattr(self.customer_medical_status, 'to_alipay_dict'):
                params['customer_medical_status'] = self.customer_medical_status.to_alipay_dict()
            else:
                params['customer_medical_status'] = self.customer_medical_status
        if self.customer_mobile_phone:
            if hasattr(self.customer_mobile_phone, 'to_alipay_dict'):
                params['customer_mobile_phone'] = self.customer_mobile_phone.to_alipay_dict()
            else:
                params['customer_mobile_phone'] = self.customer_mobile_phone
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.prepare_pregnancy:
            if hasattr(self.prepare_pregnancy, 'to_alipay_dict'):
                params['prepare_pregnancy'] = self.prepare_pregnancy.to_alipay_dict()
            else:
                params['prepare_pregnancy'] = self.prepare_pregnancy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReserveCustomer()
        if 'customer_birthday' in d:
            o.customer_birthday = d['customer_birthday']
        if 'customer_gender' in d:
            o.customer_gender = d['customer_gender']
        if 'customer_identity_no' in d:
            o.customer_identity_no = d['customer_identity_no']
        if 'customer_identity_type' in d:
            o.customer_identity_type = d['customer_identity_type']
        if 'customer_medical_status' in d:
            o.customer_medical_status = d['customer_medical_status']
        if 'customer_mobile_phone' in d:
            o.customer_mobile_phone = d['customer_mobile_phone']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'prepare_pregnancy' in d:
            o.prepare_pregnancy = d['prepare_pregnancy']
        return o


