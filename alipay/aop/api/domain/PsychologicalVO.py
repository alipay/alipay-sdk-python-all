#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PsychologicalVO(object):

    def __init__(self):
        self._fulfillment_no = None
        self._fulfillment_status = None
        self._fulfillment_status_desc = None
        self._fulfillment_type = None
        self._gender = None
        self._open_id = None
        self._patient_name = None
        self._patient_phone = None
        self._user_id = None

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
    def fulfillment_status_desc(self):
        return self._fulfillment_status_desc

    @fulfillment_status_desc.setter
    def fulfillment_status_desc(self, value):
        self._fulfillment_status_desc = value
    @property
    def fulfillment_type(self):
        return self._fulfillment_type

    @fulfillment_type.setter
    def fulfillment_type(self, value):
        self._fulfillment_type = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.fulfillment_status_desc:
            if hasattr(self.fulfillment_status_desc, 'to_alipay_dict'):
                params['fulfillment_status_desc'] = self.fulfillment_status_desc.to_alipay_dict()
            else:
                params['fulfillment_status_desc'] = self.fulfillment_status_desc
        if self.fulfillment_type:
            if hasattr(self.fulfillment_type, 'to_alipay_dict'):
                params['fulfillment_type'] = self.fulfillment_type.to_alipay_dict()
            else:
                params['fulfillment_type'] = self.fulfillment_type
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = PsychologicalVO()
        if 'fulfillment_no' in d:
            o.fulfillment_no = d['fulfillment_no']
        if 'fulfillment_status' in d:
            o.fulfillment_status = d['fulfillment_status']
        if 'fulfillment_status_desc' in d:
            o.fulfillment_status_desc = d['fulfillment_status_desc']
        if 'fulfillment_type' in d:
            o.fulfillment_type = d['fulfillment_type']
        if 'gender' in d:
            o.gender = d['gender']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_phone' in d:
            o.patient_phone = d['patient_phone']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


