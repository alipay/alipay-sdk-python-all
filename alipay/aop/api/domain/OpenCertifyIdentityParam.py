#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenCertifyIdentityParam(object):

    def __init__(self):
        self._cert_digest = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._facial_picture_front = None
        self._identity_type = None
        self._open_id = None
        self._phone_no = None
        self._user_id = None

    @property
    def cert_digest(self):
        return self._cert_digest

    @cert_digest.setter
    def cert_digest(self, value):
        self._cert_digest = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
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
    def facial_picture_front(self):
        return self._facial_picture_front

    @facial_picture_front.setter
    def facial_picture_front(self, value):
        self._facial_picture_front = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_digest:
            if hasattr(self.cert_digest, 'to_alipay_dict'):
                params['cert_digest'] = self.cert_digest.to_alipay_dict()
            else:
                params['cert_digest'] = self.cert_digest
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
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
        if self.facial_picture_front:
            if hasattr(self.facial_picture_front, 'to_alipay_dict'):
                params['facial_picture_front'] = self.facial_picture_front.to_alipay_dict()
            else:
                params['facial_picture_front'] = self.facial_picture_front
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
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
        o = OpenCertifyIdentityParam()
        if 'cert_digest' in d:
            o.cert_digest = d['cert_digest']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'facial_picture_front' in d:
            o.facial_picture_front = d['facial_picture_front']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


