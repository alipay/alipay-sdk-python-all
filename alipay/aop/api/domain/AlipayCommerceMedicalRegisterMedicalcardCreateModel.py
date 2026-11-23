#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalRegisterMedicalcardCreateModel(object):

    def __init__(self):
        self._area = None
        self._birth_day = None
        self._card_no = None
        self._card_type = None
        self._channel = None
        self._gender = None
        self._hospital_id = None
        self._isv_code = None
        self._medical_card_no = None
        self._medical_card_type = None
        self._open_id = None
        self._patient_create_prop = None
        self._patient_id = None
        self._patient_name = None
        self._phone = None
        self._platform_code = None
        self._scene_code = None
        self._user_id = None

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def birth_day(self):
        return self._birth_day

    @birth_day.setter
    def birth_day(self, value):
        self._birth_day = value
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
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def patient_create_prop(self):
        return self._patient_create_prop

    @patient_create_prop.setter
    def patient_create_prop(self, value):
        self._patient_create_prop = value
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
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.area:
            if hasattr(self.area, 'to_alipay_dict'):
                params['area'] = self.area.to_alipay_dict()
            else:
                params['area'] = self.area
        if self.birth_day:
            if hasattr(self.birth_day, 'to_alipay_dict'):
                params['birth_day'] = self.birth_day.to_alipay_dict()
            else:
                params['birth_day'] = self.birth_day
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
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
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
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.patient_create_prop:
            if hasattr(self.patient_create_prop, 'to_alipay_dict'):
                params['patient_create_prop'] = self.patient_create_prop.to_alipay_dict()
            else:
                params['patient_create_prop'] = self.patient_create_prop
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
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
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
        o = AlipayCommerceMedicalRegisterMedicalcardCreateModel()
        if 'area' in d:
            o.area = d['area']
        if 'birth_day' in d:
            o.birth_day = d['birth_day']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'gender' in d:
            o.gender = d['gender']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'medical_card_no' in d:
            o.medical_card_no = d['medical_card_no']
        if 'medical_card_type' in d:
            o.medical_card_type = d['medical_card_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'patient_create_prop' in d:
            o.patient_create_prop = d['patient_create_prop']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


