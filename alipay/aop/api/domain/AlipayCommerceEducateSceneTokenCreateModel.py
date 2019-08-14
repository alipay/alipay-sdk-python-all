#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSceneTokenCreateModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._operator_user_id = None
        self._parent_phone = None
        self._school_std_code = None
        self._student_name = None
        self._sub_code = None

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
    def operator_user_id(self):
        return self._operator_user_id

    @operator_user_id.setter
    def operator_user_id(self, value):
        self._operator_user_id = value
    @property
    def parent_phone(self):
        return self._parent_phone

    @parent_phone.setter
    def parent_phone(self, value):
        self._parent_phone = value
    @property
    def school_std_code(self):
        return self._school_std_code

    @school_std_code.setter
    def school_std_code(self, value):
        self._school_std_code = value
    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, value):
        self._student_name = value
    @property
    def sub_code(self):
        return self._sub_code

    @sub_code.setter
    def sub_code(self, value):
        self._sub_code = value


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
        if self.operator_user_id:
            if hasattr(self.operator_user_id, 'to_alipay_dict'):
                params['operator_user_id'] = self.operator_user_id.to_alipay_dict()
            else:
                params['operator_user_id'] = self.operator_user_id
        if self.parent_phone:
            if hasattr(self.parent_phone, 'to_alipay_dict'):
                params['parent_phone'] = self.parent_phone.to_alipay_dict()
            else:
                params['parent_phone'] = self.parent_phone
        if self.school_std_code:
            if hasattr(self.school_std_code, 'to_alipay_dict'):
                params['school_std_code'] = self.school_std_code.to_alipay_dict()
            else:
                params['school_std_code'] = self.school_std_code
        if self.student_name:
            if hasattr(self.student_name, 'to_alipay_dict'):
                params['student_name'] = self.student_name.to_alipay_dict()
            else:
                params['student_name'] = self.student_name
        if self.sub_code:
            if hasattr(self.sub_code, 'to_alipay_dict'):
                params['sub_code'] = self.sub_code.to_alipay_dict()
            else:
                params['sub_code'] = self.sub_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSceneTokenCreateModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'operator_user_id' in d:
            o.operator_user_id = d['operator_user_id']
        if 'parent_phone' in d:
            o.parent_phone = d['parent_phone']
        if 'school_std_code' in d:
            o.school_std_code = d['school_std_code']
        if 'student_name' in d:
            o.student_name = d['student_name']
        if 'sub_code' in d:
            o.sub_code = d['sub_code']
        return o


