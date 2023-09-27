#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEmployeeAddModel(object):

    def __init__(self):
        self._department_ids = None
        self._employee_cert_no = None
        self._employee_cert_type = None
        self._employee_email = None
        self._employee_mobile = None
        self._employee_name = None
        self._employee_no = None
        self._encrypt_cert_no = None
        self._encrypt_mobile = None
        self._enterprise_id = None
        self._identity = None
        self._identity_open_id = None
        self._identity_type = None
        self._iot_check_type = None
        self._iot_vid = None
        self._role_list = None
        self._sign_return_url = None
        self._sign_url_carry_info = None

    @property
    def department_ids(self):
        return self._department_ids

    @department_ids.setter
    def department_ids(self, value):
        if isinstance(value, list):
            self._department_ids = list()
            for i in value:
                self._department_ids.append(i)
    @property
    def employee_cert_no(self):
        return self._employee_cert_no

    @employee_cert_no.setter
    def employee_cert_no(self, value):
        self._employee_cert_no = value
    @property
    def employee_cert_type(self):
        return self._employee_cert_type

    @employee_cert_type.setter
    def employee_cert_type(self, value):
        self._employee_cert_type = value
    @property
    def employee_email(self):
        return self._employee_email

    @employee_email.setter
    def employee_email(self, value):
        self._employee_email = value
    @property
    def employee_mobile(self):
        return self._employee_mobile

    @employee_mobile.setter
    def employee_mobile(self, value):
        self._employee_mobile = value
    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self, value):
        self._employee_name = value
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def encrypt_cert_no(self):
        return self._encrypt_cert_no

    @encrypt_cert_no.setter
    def encrypt_cert_no(self, value):
        self._encrypt_cert_no = value
    @property
    def encrypt_mobile(self):
        return self._encrypt_mobile

    @encrypt_mobile.setter
    def encrypt_mobile(self, value):
        self._encrypt_mobile = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_open_id(self):
        return self._identity_open_id

    @identity_open_id.setter
    def identity_open_id(self, value):
        self._identity_open_id = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def iot_check_type(self):
        return self._iot_check_type

    @iot_check_type.setter
    def iot_check_type(self, value):
        self._iot_check_type = value
    @property
    def iot_vid(self):
        return self._iot_vid

    @iot_vid.setter
    def iot_vid(self, value):
        self._iot_vid = value
    @property
    def role_list(self):
        return self._role_list

    @role_list.setter
    def role_list(self, value):
        if isinstance(value, list):
            self._role_list = list()
            for i in value:
                self._role_list.append(i)
    @property
    def sign_return_url(self):
        return self._sign_return_url

    @sign_return_url.setter
    def sign_return_url(self, value):
        self._sign_return_url = value
    @property
    def sign_url_carry_info(self):
        return self._sign_url_carry_info

    @sign_url_carry_info.setter
    def sign_url_carry_info(self, value):
        self._sign_url_carry_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_ids:
            if isinstance(self.department_ids, list):
                for i in range(0, len(self.department_ids)):
                    element = self.department_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.department_ids[i] = element.to_alipay_dict()
            if hasattr(self.department_ids, 'to_alipay_dict'):
                params['department_ids'] = self.department_ids.to_alipay_dict()
            else:
                params['department_ids'] = self.department_ids
        if self.employee_cert_no:
            if hasattr(self.employee_cert_no, 'to_alipay_dict'):
                params['employee_cert_no'] = self.employee_cert_no.to_alipay_dict()
            else:
                params['employee_cert_no'] = self.employee_cert_no
        if self.employee_cert_type:
            if hasattr(self.employee_cert_type, 'to_alipay_dict'):
                params['employee_cert_type'] = self.employee_cert_type.to_alipay_dict()
            else:
                params['employee_cert_type'] = self.employee_cert_type
        if self.employee_email:
            if hasattr(self.employee_email, 'to_alipay_dict'):
                params['employee_email'] = self.employee_email.to_alipay_dict()
            else:
                params['employee_email'] = self.employee_email
        if self.employee_mobile:
            if hasattr(self.employee_mobile, 'to_alipay_dict'):
                params['employee_mobile'] = self.employee_mobile.to_alipay_dict()
            else:
                params['employee_mobile'] = self.employee_mobile
        if self.employee_name:
            if hasattr(self.employee_name, 'to_alipay_dict'):
                params['employee_name'] = self.employee_name.to_alipay_dict()
            else:
                params['employee_name'] = self.employee_name
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.encrypt_cert_no:
            if hasattr(self.encrypt_cert_no, 'to_alipay_dict'):
                params['encrypt_cert_no'] = self.encrypt_cert_no.to_alipay_dict()
            else:
                params['encrypt_cert_no'] = self.encrypt_cert_no
        if self.encrypt_mobile:
            if hasattr(self.encrypt_mobile, 'to_alipay_dict'):
                params['encrypt_mobile'] = self.encrypt_mobile.to_alipay_dict()
            else:
                params['encrypt_mobile'] = self.encrypt_mobile
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_open_id:
            if hasattr(self.identity_open_id, 'to_alipay_dict'):
                params['identity_open_id'] = self.identity_open_id.to_alipay_dict()
            else:
                params['identity_open_id'] = self.identity_open_id
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.iot_check_type:
            if hasattr(self.iot_check_type, 'to_alipay_dict'):
                params['iot_check_type'] = self.iot_check_type.to_alipay_dict()
            else:
                params['iot_check_type'] = self.iot_check_type
        if self.iot_vid:
            if hasattr(self.iot_vid, 'to_alipay_dict'):
                params['iot_vid'] = self.iot_vid.to_alipay_dict()
            else:
                params['iot_vid'] = self.iot_vid
        if self.role_list:
            if isinstance(self.role_list, list):
                for i in range(0, len(self.role_list)):
                    element = self.role_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_list[i] = element.to_alipay_dict()
            if hasattr(self.role_list, 'to_alipay_dict'):
                params['role_list'] = self.role_list.to_alipay_dict()
            else:
                params['role_list'] = self.role_list
        if self.sign_return_url:
            if hasattr(self.sign_return_url, 'to_alipay_dict'):
                params['sign_return_url'] = self.sign_return_url.to_alipay_dict()
            else:
                params['sign_return_url'] = self.sign_return_url
        if self.sign_url_carry_info:
            if hasattr(self.sign_url_carry_info, 'to_alipay_dict'):
                params['sign_url_carry_info'] = self.sign_url_carry_info.to_alipay_dict()
            else:
                params['sign_url_carry_info'] = self.sign_url_carry_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEmployeeAddModel()
        if 'department_ids' in d:
            o.department_ids = d['department_ids']
        if 'employee_cert_no' in d:
            o.employee_cert_no = d['employee_cert_no']
        if 'employee_cert_type' in d:
            o.employee_cert_type = d['employee_cert_type']
        if 'employee_email' in d:
            o.employee_email = d['employee_email']
        if 'employee_mobile' in d:
            o.employee_mobile = d['employee_mobile']
        if 'employee_name' in d:
            o.employee_name = d['employee_name']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'encrypt_cert_no' in d:
            o.encrypt_cert_no = d['encrypt_cert_no']
        if 'encrypt_mobile' in d:
            o.encrypt_mobile = d['encrypt_mobile']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_open_id' in d:
            o.identity_open_id = d['identity_open_id']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'iot_check_type' in d:
            o.iot_check_type = d['iot_check_type']
        if 'iot_vid' in d:
            o.iot_vid = d['iot_vid']
        if 'role_list' in d:
            o.role_list = d['role_list']
        if 'sign_return_url' in d:
            o.sign_return_url = d['sign_return_url']
        if 'sign_url_carry_info' in d:
            o.sign_url_carry_info = d['sign_url_carry_info']
        return o


