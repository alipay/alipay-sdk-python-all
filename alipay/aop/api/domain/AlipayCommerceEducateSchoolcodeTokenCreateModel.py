#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSchoolcodeTokenCreateModel(object):

    def __init__(self):
        self._cert_no = None
        self._school_std_code = None
        self._student_cert_no = None
        self._student_cert_type = None
        self._student_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def school_std_code(self):
        return self._school_std_code

    @school_std_code.setter
    def school_std_code(self, value):
        self._school_std_code = value
    @property
    def student_cert_no(self):
        return self._student_cert_no

    @student_cert_no.setter
    def student_cert_no(self, value):
        self._student_cert_no = value
    @property
    def student_cert_type(self):
        return self._student_cert_type

    @student_cert_type.setter
    def student_cert_type(self, value):
        self._student_cert_type = value
    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, value):
        self._student_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.school_std_code:
            if hasattr(self.school_std_code, 'to_alipay_dict'):
                params['school_std_code'] = self.school_std_code.to_alipay_dict()
            else:
                params['school_std_code'] = self.school_std_code
        if self.student_cert_no:
            if hasattr(self.student_cert_no, 'to_alipay_dict'):
                params['student_cert_no'] = self.student_cert_no.to_alipay_dict()
            else:
                params['student_cert_no'] = self.student_cert_no
        if self.student_cert_type:
            if hasattr(self.student_cert_type, 'to_alipay_dict'):
                params['student_cert_type'] = self.student_cert_type.to_alipay_dict()
            else:
                params['student_cert_type'] = self.student_cert_type
        if self.student_name:
            if hasattr(self.student_name, 'to_alipay_dict'):
                params['student_name'] = self.student_name.to_alipay_dict()
            else:
                params['student_name'] = self.student_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSchoolcodeTokenCreateModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'school_std_code' in d:
            o.school_std_code = d['school_std_code']
        if 'student_cert_no' in d:
            o.student_cert_no = d['student_cert_no']
        if 'student_cert_type' in d:
            o.student_cert_type = d['student_cert_type']
        if 'student_name' in d:
            o.student_name = d['student_name']
        return o


