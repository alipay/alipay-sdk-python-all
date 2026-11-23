#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CaCertApplyUser(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._legal_person_id_no = None
        self._legal_person_name = None
        self._user_name = None
        self._user_no = None
        self._user_type = None

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
    def legal_person_id_no(self):
        return self._legal_person_id_no

    @legal_person_id_no.setter
    def legal_person_id_no(self, value):
        self._legal_person_id_no = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_no(self):
        return self._user_no

    @user_no.setter
    def user_no(self, value):
        self._user_no = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.legal_person_id_no:
            if hasattr(self.legal_person_id_no, 'to_alipay_dict'):
                params['legal_person_id_no'] = self.legal_person_id_no.to_alipay_dict()
            else:
                params['legal_person_id_no'] = self.legal_person_id_no
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_no:
            if hasattr(self.user_no, 'to_alipay_dict'):
                params['user_no'] = self.user_no.to_alipay_dict()
            else:
                params['user_no'] = self.user_no
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaCertApplyUser()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'legal_person_id_no' in d:
            o.legal_person_id_no = d['legal_person_id_no']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_no' in d:
            o.user_no = d['user_no']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


