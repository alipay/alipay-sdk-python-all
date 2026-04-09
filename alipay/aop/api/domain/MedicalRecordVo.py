#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalRecordVo(object):

    def __init__(self):
        self._avatar = None
        self._doctor_id = None
        self._doctor_name = None
        self._hospital_name = None
        self._medical_content = None
        self._medical_record_id = None
        self._medical_title = None
        self._third_class = None
        self._title = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
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
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def medical_content(self):
        return self._medical_content

    @medical_content.setter
    def medical_content(self, value):
        self._medical_content = value
    @property
    def medical_record_id(self):
        return self._medical_record_id

    @medical_record_id.setter
    def medical_record_id(self, value):
        self._medical_record_id = value
    @property
    def medical_title(self):
        return self._medical_title

    @medical_title.setter
    def medical_title(self, value):
        self._medical_title = value
    @property
    def third_class(self):
        return self._third_class

    @third_class.setter
    def third_class(self, value):
        self._third_class = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
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
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.medical_content:
            if hasattr(self.medical_content, 'to_alipay_dict'):
                params['medical_content'] = self.medical_content.to_alipay_dict()
            else:
                params['medical_content'] = self.medical_content
        if self.medical_record_id:
            if hasattr(self.medical_record_id, 'to_alipay_dict'):
                params['medical_record_id'] = self.medical_record_id.to_alipay_dict()
            else:
                params['medical_record_id'] = self.medical_record_id
        if self.medical_title:
            if hasattr(self.medical_title, 'to_alipay_dict'):
                params['medical_title'] = self.medical_title.to_alipay_dict()
            else:
                params['medical_title'] = self.medical_title
        if self.third_class:
            if hasattr(self.third_class, 'to_alipay_dict'):
                params['third_class'] = self.third_class.to_alipay_dict()
            else:
                params['third_class'] = self.third_class
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalRecordVo()
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'medical_content' in d:
            o.medical_content = d['medical_content']
        if 'medical_record_id' in d:
            o.medical_record_id = d['medical_record_id']
        if 'medical_title' in d:
            o.medical_title = d['medical_title']
        if 'third_class' in d:
            o.third_class = d['third_class']
        if 'title' in d:
            o.title = d['title']
        return o


