#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegisterMedicalCardVO(object):

    def __init__(self):
        self._card_no = None
        self._card_type = None
        self._icon_url = None
        self._medical_card_no = None
        self._medical_card_type = None
        self._platform_patient_id = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def medical_card_no(self):
        return self._medical_card_no

    @medical_card_no.setter
    def medical_card_no(self, value):
        self._medical_card_no = value
    @property
    def medical_card_type(self):
        return self._medical_card_type

    @medical_card_type.setter
    def medical_card_type(self, value):
        self._medical_card_type = value
    @property
    def platform_patient_id(self):
        return self._platform_patient_id

    @platform_patient_id.setter
    def platform_patient_id(self, value):
        self._platform_patient_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.icon_url:
            if hasattr(self.icon_url, 'to_alipay_dict'):
                params['icon_url'] = self.icon_url.to_alipay_dict()
            else:
                params['icon_url'] = self.icon_url
        if self.medical_card_no:
            if hasattr(self.medical_card_no, 'to_alipay_dict'):
                params['medical_card_no'] = self.medical_card_no.to_alipay_dict()
            else:
                params['medical_card_no'] = self.medical_card_no
        if self.medical_card_type:
            if hasattr(self.medical_card_type, 'to_alipay_dict'):
                params['medical_card_type'] = self.medical_card_type.to_alipay_dict()
            else:
                params['medical_card_type'] = self.medical_card_type
        if self.platform_patient_id:
            if hasattr(self.platform_patient_id, 'to_alipay_dict'):
                params['platform_patient_id'] = self.platform_patient_id.to_alipay_dict()
            else:
                params['platform_patient_id'] = self.platform_patient_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterMedicalCardVO()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'icon_url' in d:
            o.icon_url = d['icon_url']
        if 'medical_card_no' in d:
            o.medical_card_no = d['medical_card_no']
        if 'medical_card_type' in d:
            o.medical_card_type = d['medical_card_type']
        if 'platform_patient_id' in d:
            o.platform_patient_id = d['platform_patient_id']
        return o


