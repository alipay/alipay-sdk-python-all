#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EscortVO(object):

    def __init__(self):
        self._fulfillment_no = None
        self._fulfillment_status = None
        self._fulfillment_status_desc = None
        self._fulfillment_type = None
        self._item_code = None
        self._patient_age = None
        self._patient_gender = None
        self._patient_id = None
        self._patient_name = None
        self._patient_phone = None
        self._service_package_id = None
        self._service_package_name = None

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
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def patient_age(self):
        return self._patient_age

    @patient_age.setter
    def patient_age(self, value):
        self._patient_age = value
    @property
    def patient_gender(self):
        return self._patient_gender

    @patient_gender.setter
    def patient_gender(self, value):
        self._patient_gender = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
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
    def service_package_id(self):
        return self._service_package_id

    @service_package_id.setter
    def service_package_id(self, value):
        self._service_package_id = value
    @property
    def service_package_name(self):
        return self._service_package_name

    @service_package_name.setter
    def service_package_name(self, value):
        self._service_package_name = value


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
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.patient_age:
            if hasattr(self.patient_age, 'to_alipay_dict'):
                params['patient_age'] = self.patient_age.to_alipay_dict()
            else:
                params['patient_age'] = self.patient_age
        if self.patient_gender:
            if hasattr(self.patient_gender, 'to_alipay_dict'):
                params['patient_gender'] = self.patient_gender.to_alipay_dict()
            else:
                params['patient_gender'] = self.patient_gender
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
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
        if self.service_package_id:
            if hasattr(self.service_package_id, 'to_alipay_dict'):
                params['service_package_id'] = self.service_package_id.to_alipay_dict()
            else:
                params['service_package_id'] = self.service_package_id
        if self.service_package_name:
            if hasattr(self.service_package_name, 'to_alipay_dict'):
                params['service_package_name'] = self.service_package_name.to_alipay_dict()
            else:
                params['service_package_name'] = self.service_package_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EscortVO()
        if 'fulfillment_no' in d:
            o.fulfillment_no = d['fulfillment_no']
        if 'fulfillment_status' in d:
            o.fulfillment_status = d['fulfillment_status']
        if 'fulfillment_status_desc' in d:
            o.fulfillment_status_desc = d['fulfillment_status_desc']
        if 'fulfillment_type' in d:
            o.fulfillment_type = d['fulfillment_type']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'patient_age' in d:
            o.patient_age = d['patient_age']
        if 'patient_gender' in d:
            o.patient_gender = d['patient_gender']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_phone' in d:
            o.patient_phone = d['patient_phone']
        if 'service_package_id' in d:
            o.service_package_id = d['service_package_id']
        if 'service_package_name' in d:
            o.service_package_name = d['service_package_name']
        return o


