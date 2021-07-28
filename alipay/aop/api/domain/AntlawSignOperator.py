#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntlawSignOperator(object):

    def __init__(self):
        self._cert_type = None
        self._operator_cert_no = None
        self._operator_name = None
        self._operator_uid = None
        self._sign_operator_type = None

    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def operator_cert_no(self):
        return self._operator_cert_no

    @operator_cert_no.setter
    def operator_cert_no(self, value):
        self._operator_cert_no = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def operator_uid(self):
        return self._operator_uid

    @operator_uid.setter
    def operator_uid(self, value):
        self._operator_uid = value
    @property
    def sign_operator_type(self):
        return self._sign_operator_type

    @sign_operator_type.setter
    def sign_operator_type(self, value):
        self._sign_operator_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.operator_cert_no:
            if hasattr(self.operator_cert_no, 'to_alipay_dict'):
                params['operator_cert_no'] = self.operator_cert_no.to_alipay_dict()
            else:
                params['operator_cert_no'] = self.operator_cert_no
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.operator_uid:
            if hasattr(self.operator_uid, 'to_alipay_dict'):
                params['operator_uid'] = self.operator_uid.to_alipay_dict()
            else:
                params['operator_uid'] = self.operator_uid
        if self.sign_operator_type:
            if hasattr(self.sign_operator_type, 'to_alipay_dict'):
                params['sign_operator_type'] = self.sign_operator_type.to_alipay_dict()
            else:
                params['sign_operator_type'] = self.sign_operator_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntlawSignOperator()
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'operator_cert_no' in d:
            o.operator_cert_no = d['operator_cert_no']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'operator_uid' in d:
            o.operator_uid = d['operator_uid']
        if 'sign_operator_type' in d:
            o.sign_operator_type = d['sign_operator_type']
        return o


