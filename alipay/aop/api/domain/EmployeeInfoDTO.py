#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EmployeeDepartmentDTO import EmployeeDepartmentDTO


class EmployeeInfoDTO(object):

    def __init__(self):
        self._activate = None
        self._department_list = None
        self._email = None
        self._employee_cert_no = None
        self._employee_cert_type = None
        self._employee_id = None
        self._employee_name = None
        self._employee_no = None
        self._encrypt_cert_no = None
        self._encrypt_mobile = None
        self._gmt_create = None
        self._gmt_modified = None
        self._iot_face_status = None
        self._iot_vid = None
        self._mobile = None
        self._open_id = None
        self._role_list = None
        self._user_id = None

    @property
    def activate(self):
        return self._activate

    @activate.setter
    def activate(self, value):
        self._activate = value
    @property
    def department_list(self):
        return self._department_list

    @department_list.setter
    def department_list(self, value):
        if isinstance(value, list):
            self._department_list = list()
            for i in value:
                if isinstance(i, EmployeeDepartmentDTO):
                    self._department_list.append(i)
                else:
                    self._department_list.append(EmployeeDepartmentDTO.from_alipay_dict(i))
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
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
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
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
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def iot_face_status(self):
        return self._iot_face_status

    @iot_face_status.setter
    def iot_face_status(self, value):
        self._iot_face_status = value
    @property
    def iot_vid(self):
        return self._iot_vid

    @iot_vid.setter
    def iot_vid(self, value):
        self._iot_vid = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activate:
            if hasattr(self.activate, 'to_alipay_dict'):
                params['activate'] = self.activate.to_alipay_dict()
            else:
                params['activate'] = self.activate
        if self.department_list:
            if isinstance(self.department_list, list):
                for i in range(0, len(self.department_list)):
                    element = self.department_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.department_list[i] = element.to_alipay_dict()
            if hasattr(self.department_list, 'to_alipay_dict'):
                params['department_list'] = self.department_list.to_alipay_dict()
            else:
                params['department_list'] = self.department_list
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
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
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
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
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.iot_face_status:
            if hasattr(self.iot_face_status, 'to_alipay_dict'):
                params['iot_face_status'] = self.iot_face_status.to_alipay_dict()
            else:
                params['iot_face_status'] = self.iot_face_status
        if self.iot_vid:
            if hasattr(self.iot_vid, 'to_alipay_dict'):
                params['iot_vid'] = self.iot_vid.to_alipay_dict()
            else:
                params['iot_vid'] = self.iot_vid
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = EmployeeInfoDTO()
        if 'activate' in d:
            o.activate = d['activate']
        if 'department_list' in d:
            o.department_list = d['department_list']
        if 'email' in d:
            o.email = d['email']
        if 'employee_cert_no' in d:
            o.employee_cert_no = d['employee_cert_no']
        if 'employee_cert_type' in d:
            o.employee_cert_type = d['employee_cert_type']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'employee_name' in d:
            o.employee_name = d['employee_name']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'encrypt_cert_no' in d:
            o.encrypt_cert_no = d['encrypt_cert_no']
        if 'encrypt_mobile' in d:
            o.encrypt_mobile = d['encrypt_mobile']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'iot_face_status' in d:
            o.iot_face_status = d['iot_face_status']
        if 'iot_vid' in d:
            o.iot_vid = d['iot_vid']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'role_list' in d:
            o.role_list = d['role_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


