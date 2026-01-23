#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsuredInfo(object):

    def __init__(self):
        self._ext_info = None
        self._insured_birthday = None
        self._insured_cert_no = None
        self._insured_cert_type = None
        self._insured_name = None
        self._insured_status = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def insured_birthday(self):
        return self._insured_birthday

    @insured_birthday.setter
    def insured_birthday(self, value):
        self._insured_birthday = value
    @property
    def insured_cert_no(self):
        return self._insured_cert_no

    @insured_cert_no.setter
    def insured_cert_no(self, value):
        self._insured_cert_no = value
    @property
    def insured_cert_type(self):
        return self._insured_cert_type

    @insured_cert_type.setter
    def insured_cert_type(self, value):
        self._insured_cert_type = value
    @property
    def insured_name(self):
        return self._insured_name

    @insured_name.setter
    def insured_name(self, value):
        self._insured_name = value
    @property
    def insured_status(self):
        return self._insured_status

    @insured_status.setter
    def insured_status(self, value):
        self._insured_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.insured_birthday:
            if hasattr(self.insured_birthday, 'to_alipay_dict'):
                params['insured_birthday'] = self.insured_birthday.to_alipay_dict()
            else:
                params['insured_birthday'] = self.insured_birthday
        if self.insured_cert_no:
            if hasattr(self.insured_cert_no, 'to_alipay_dict'):
                params['insured_cert_no'] = self.insured_cert_no.to_alipay_dict()
            else:
                params['insured_cert_no'] = self.insured_cert_no
        if self.insured_cert_type:
            if hasattr(self.insured_cert_type, 'to_alipay_dict'):
                params['insured_cert_type'] = self.insured_cert_type.to_alipay_dict()
            else:
                params['insured_cert_type'] = self.insured_cert_type
        if self.insured_name:
            if hasattr(self.insured_name, 'to_alipay_dict'):
                params['insured_name'] = self.insured_name.to_alipay_dict()
            else:
                params['insured_name'] = self.insured_name
        if self.insured_status:
            if hasattr(self.insured_status, 'to_alipay_dict'):
                params['insured_status'] = self.insured_status.to_alipay_dict()
            else:
                params['insured_status'] = self.insured_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsuredInfo()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'insured_birthday' in d:
            o.insured_birthday = d['insured_birthday']
        if 'insured_cert_no' in d:
            o.insured_cert_no = d['insured_cert_no']
        if 'insured_cert_type' in d:
            o.insured_cert_type = d['insured_cert_type']
        if 'insured_name' in d:
            o.insured_name = d['insured_name']
        if 'insured_status' in d:
            o.insured_status = d['insured_status']
        return o


