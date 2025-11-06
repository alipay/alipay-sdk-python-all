#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReferralFormPageVO(object):

    def __init__(self):
        self._age = None
        self._area = None
        self._doctor_cert_no = None
        self._gmt_create = None
        self._real_name = None
        self._referral_form_id = None
        self._sex = None
        self._status = None
        self._user_description = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def doctor_cert_no(self):
        return self._doctor_cert_no

    @doctor_cert_no.setter
    def doctor_cert_no(self, value):
        self._doctor_cert_no = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def referral_form_id(self):
        return self._referral_form_id

    @referral_form_id.setter
    def referral_form_id(self, value):
        self._referral_form_id = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_description(self):
        return self._user_description

    @user_description.setter
    def user_description(self, value):
        self._user_description = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.doctor_cert_no:
            if hasattr(self.doctor_cert_no, 'to_alipay_dict'):
                params['doctor_cert_no'] = self.doctor_cert_no.to_alipay_dict()
            else:
                params['doctor_cert_no'] = self.doctor_cert_no
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.referral_form_id:
            if hasattr(self.referral_form_id, 'to_alipay_dict'):
                params['referral_form_id'] = self.referral_form_id.to_alipay_dict()
            else:
                params['referral_form_id'] = self.referral_form_id
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_description:
            if hasattr(self.user_description, 'to_alipay_dict'):
                params['user_description'] = self.user_description.to_alipay_dict()
            else:
                params['user_description'] = self.user_description
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReferralFormPageVO()
        if 'age' in d:
            o.age = d['age']
        if 'area' in d:
            o.area = d['area']
        if 'doctor_cert_no' in d:
            o.doctor_cert_no = d['doctor_cert_no']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'referral_form_id' in d:
            o.referral_form_id = d['referral_form_id']
        if 'sex' in d:
            o.sex = d['sex']
        if 'status' in d:
            o.status = d['status']
        if 'user_description' in d:
            o.user_description = d['user_description']
        return o


