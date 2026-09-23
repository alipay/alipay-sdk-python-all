#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Doctors(object):

    def __init__(self):
        self._authority = None
        self._department = None
        self._doctor_user_name = None
        self._hospital = None
        self._name = None
        self._phone_price = None
        self._phone_reply_time = None
        self._professional = None
        self._service = None
        self._text_price = None
        self._text_reply_time = None
        self._yellow_page_url = None

    @property
    def authority(self):
        return self._authority

    @authority.setter
    def authority(self, value):
        self._authority = value
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def doctor_user_name(self):
        return self._doctor_user_name

    @doctor_user_name.setter
    def doctor_user_name(self, value):
        self._doctor_user_name = value
    @property
    def hospital(self):
        return self._hospital

    @hospital.setter
    def hospital(self, value):
        self._hospital = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone_price(self):
        return self._phone_price

    @phone_price.setter
    def phone_price(self, value):
        self._phone_price = value
    @property
    def phone_reply_time(self):
        return self._phone_reply_time

    @phone_reply_time.setter
    def phone_reply_time(self, value):
        self._phone_reply_time = value
    @property
    def professional(self):
        return self._professional

    @professional.setter
    def professional(self, value):
        self._professional = value
    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value
    @property
    def text_price(self):
        return self._text_price

    @text_price.setter
    def text_price(self, value):
        self._text_price = value
    @property
    def text_reply_time(self):
        return self._text_reply_time

    @text_reply_time.setter
    def text_reply_time(self, value):
        self._text_reply_time = value
    @property
    def yellow_page_url(self):
        return self._yellow_page_url

    @yellow_page_url.setter
    def yellow_page_url(self, value):
        self._yellow_page_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.authority:
            if hasattr(self.authority, 'to_alipay_dict'):
                params['authority'] = self.authority.to_alipay_dict()
            else:
                params['authority'] = self.authority
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.doctor_user_name:
            if hasattr(self.doctor_user_name, 'to_alipay_dict'):
                params['doctor_user_name'] = self.doctor_user_name.to_alipay_dict()
            else:
                params['doctor_user_name'] = self.doctor_user_name
        if self.hospital:
            if hasattr(self.hospital, 'to_alipay_dict'):
                params['hospital'] = self.hospital.to_alipay_dict()
            else:
                params['hospital'] = self.hospital
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone_price:
            if hasattr(self.phone_price, 'to_alipay_dict'):
                params['phone_price'] = self.phone_price.to_alipay_dict()
            else:
                params['phone_price'] = self.phone_price
        if self.phone_reply_time:
            if hasattr(self.phone_reply_time, 'to_alipay_dict'):
                params['phone_reply_time'] = self.phone_reply_time.to_alipay_dict()
            else:
                params['phone_reply_time'] = self.phone_reply_time
        if self.professional:
            if hasattr(self.professional, 'to_alipay_dict'):
                params['professional'] = self.professional.to_alipay_dict()
            else:
                params['professional'] = self.professional
        if self.service:
            if hasattr(self.service, 'to_alipay_dict'):
                params['service'] = self.service.to_alipay_dict()
            else:
                params['service'] = self.service
        if self.text_price:
            if hasattr(self.text_price, 'to_alipay_dict'):
                params['text_price'] = self.text_price.to_alipay_dict()
            else:
                params['text_price'] = self.text_price
        if self.text_reply_time:
            if hasattr(self.text_reply_time, 'to_alipay_dict'):
                params['text_reply_time'] = self.text_reply_time.to_alipay_dict()
            else:
                params['text_reply_time'] = self.text_reply_time
        if self.yellow_page_url:
            if hasattr(self.yellow_page_url, 'to_alipay_dict'):
                params['yellow_page_url'] = self.yellow_page_url.to_alipay_dict()
            else:
                params['yellow_page_url'] = self.yellow_page_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Doctors()
        if 'authority' in d:
            o.authority = d['authority']
        if 'department' in d:
            o.department = d['department']
        if 'doctor_user_name' in d:
            o.doctor_user_name = d['doctor_user_name']
        if 'hospital' in d:
            o.hospital = d['hospital']
        if 'name' in d:
            o.name = d['name']
        if 'phone_price' in d:
            o.phone_price = d['phone_price']
        if 'phone_reply_time' in d:
            o.phone_reply_time = d['phone_reply_time']
        if 'professional' in d:
            o.professional = d['professional']
        if 'service' in d:
            o.service = d['service']
        if 'text_price' in d:
            o.text_price = d['text_price']
        if 'text_reply_time' in d:
            o.text_reply_time = d['text_reply_time']
        if 'yellow_page_url' in d:
            o.yellow_page_url = d['yellow_page_url']
        return o


