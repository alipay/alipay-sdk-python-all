#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduDepartmentNode import EduDepartmentNode


class AlipayCommerceEducateRosterInfoSaveModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_no_tail = None
        self._cert_type = None
        self._department_info = None
        self._email = None
        self._employee_no = None
        self._expire_time = None
        self._gender = None
        self._inst_id = None
        self._inst_name = None
        self._mobile = None
        self._name = None
        self._node_id_list = None
        self._role_name = None
        self._role_name_list = None
        self._role_type = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_no_tail(self):
        return self._cert_no_tail

    @cert_no_tail.setter
    def cert_no_tail(self, value):
        self._cert_no_tail = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def department_info(self):
        return self._department_info

    @department_info.setter
    def department_info(self, value):
        if isinstance(value, list):
            self._department_info = list()
            for i in value:
                if isinstance(i, EduDepartmentNode):
                    self._department_info.append(i)
                else:
                    self._department_info.append(EduDepartmentNode.from_alipay_dict(i))
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def node_id_list(self):
        return self._node_id_list

    @node_id_list.setter
    def node_id_list(self, value):
        if isinstance(value, list):
            self._node_id_list = list()
            for i in value:
                self._node_id_list.append(i)
    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, value):
        self._role_name = value
    @property
    def role_name_list(self):
        return self._role_name_list

    @role_name_list.setter
    def role_name_list(self, value):
        if isinstance(value, list):
            self._role_name_list = list()
            for i in value:
                self._role_name_list.append(i)
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_no_tail:
            if hasattr(self.cert_no_tail, 'to_alipay_dict'):
                params['cert_no_tail'] = self.cert_no_tail.to_alipay_dict()
            else:
                params['cert_no_tail'] = self.cert_no_tail
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.department_info:
            if isinstance(self.department_info, list):
                for i in range(0, len(self.department_info)):
                    element = self.department_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.department_info[i] = element.to_alipay_dict()
            if hasattr(self.department_info, 'to_alipay_dict'):
                params['department_info'] = self.department_info.to_alipay_dict()
            else:
                params['department_info'] = self.department_info
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.employee_no:
            if hasattr(self.employee_no, 'to_alipay_dict'):
                params['employee_no'] = self.employee_no.to_alipay_dict()
            else:
                params['employee_no'] = self.employee_no
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.node_id_list:
            if isinstance(self.node_id_list, list):
                for i in range(0, len(self.node_id_list)):
                    element = self.node_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.node_id_list[i] = element.to_alipay_dict()
            if hasattr(self.node_id_list, 'to_alipay_dict'):
                params['node_id_list'] = self.node_id_list.to_alipay_dict()
            else:
                params['node_id_list'] = self.node_id_list
        if self.role_name:
            if hasattr(self.role_name, 'to_alipay_dict'):
                params['role_name'] = self.role_name.to_alipay_dict()
            else:
                params['role_name'] = self.role_name
        if self.role_name_list:
            if isinstance(self.role_name_list, list):
                for i in range(0, len(self.role_name_list)):
                    element = self.role_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_name_list[i] = element.to_alipay_dict()
            if hasattr(self.role_name_list, 'to_alipay_dict'):
                params['role_name_list'] = self.role_name_list.to_alipay_dict()
            else:
                params['role_name_list'] = self.role_name_list
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateRosterInfoSaveModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_no_tail' in d:
            o.cert_no_tail = d['cert_no_tail']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'department_info' in d:
            o.department_info = d['department_info']
        if 'email' in d:
            o.email = d['email']
        if 'employee_no' in d:
            o.employee_no = d['employee_no']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'gender' in d:
            o.gender = d['gender']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'node_id_list' in d:
            o.node_id_list = d['node_id_list']
        if 'role_name' in d:
            o.role_name = d['role_name']
        if 'role_name_list' in d:
            o.role_name_list = d['role_name_list']
        if 'role_type' in d:
            o.role_type = d['role_type']
        return o


