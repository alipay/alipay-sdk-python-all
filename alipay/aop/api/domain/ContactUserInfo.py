#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContactUserInfo(object):

    def __init__(self):
        self._auth_file = None
        self._cert_image = None
        self._cert_image_back = None
        self._cert_no = None
        self._cert_type = None
        self._name = None
        self._phone = None

    @property
    def auth_file(self):
        return self._auth_file

    @auth_file.setter
    def auth_file(self, value):
        self._auth_file = value
    @property
    def cert_image(self):
        return self._cert_image

    @cert_image.setter
    def cert_image(self, value):
        self._cert_image = value
    @property
    def cert_image_back(self):
        return self._cert_image_back

    @cert_image_back.setter
    def cert_image_back(self, value):
        self._cert_image_back = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_file:
            if hasattr(self.auth_file, 'to_alipay_dict'):
                params['auth_file'] = self.auth_file.to_alipay_dict()
            else:
                params['auth_file'] = self.auth_file
        if self.cert_image:
            if hasattr(self.cert_image, 'to_alipay_dict'):
                params['cert_image'] = self.cert_image.to_alipay_dict()
            else:
                params['cert_image'] = self.cert_image
        if self.cert_image_back:
            if hasattr(self.cert_image_back, 'to_alipay_dict'):
                params['cert_image_back'] = self.cert_image_back.to_alipay_dict()
            else:
                params['cert_image_back'] = self.cert_image_back
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContactUserInfo()
        if 'auth_file' in d:
            o.auth_file = d['auth_file']
        if 'cert_image' in d:
            o.cert_image = d['cert_image']
        if 'cert_image_back' in d:
            o.cert_image_back = d['cert_image_back']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        return o


