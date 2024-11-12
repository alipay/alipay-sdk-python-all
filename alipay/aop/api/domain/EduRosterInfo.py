#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduDepartmentNode import EduDepartmentNode
from alipay.aop.api.domain.EduDepartmentNode import EduDepartmentNode


class EduRosterInfo(object):

    def __init__(self):
        self._bind_status = None
        self._cert_no = None
        self._cert_type = None
        self._department_info = None
        self._department_info_list = None
        self._employee_no = None
        self._expire_time = None
        self._gender = None
        self._inst_id = None
        self._inst_name = None
        self._mobile = None
        self._name = None
        self._role_name = None
        self._role_type = None
        self._roster_id = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
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
    def department_info(self):
        return self._department_info

    @department_info.setter
    def department_info(self, value):
        if isinstance(value, EduDepartmentNode):
            self._department_info = value
        else:
            self._department_info = EduDepartmentNode.from_alipay_dict(value)
    @property
    def department_info_list(self):
        return self._department_info_list

    @department_info_list.setter
    def department_info_list(self, value):
        if isinstance(value, list):
            self._department_info_list = list()
            for i in value:
                if isinstance(i, EduDepartmentNode):
                    self._department_info_list.append(i)
                else:
                    self._department_info_list.append(EduDepartmentNode.from_alipay_dict(i))
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
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, value):
        self._role_name = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def roster_id(self):
        return self._roster_id

    @roster_id.setter
    def roster_id(self, value):
        self._roster_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_status:
            if hasattr(self.bind_status, 'to_alipay_dict'):
                params['bind_status'] = self.bind_status.to_alipay_dict()
            else:
                params['bind_status'] = self.bind_status
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
        if self.department_info:
            if hasattr(self.department_info, 'to_alipay_dict'):
                params['department_info'] = self.department_info.to_alipay_dict()
            else:
                params['department_info'] = self.department_info
        if self.department_info_list:
            if isinstance(self.department_info_list, list):
                for i in range(0, len(self.department_info_list)):
                    element = self.department_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.department_info_list[i] = element.to_alipay_dict()
            if hasattr(self.department_info_list, 'to_alipay_dict'):
                params['department_info_list'] = self.department_info_list.to_alipay_dict()
            else:
                params['department_info_list'] = self.department_info_list
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
        if self.role_name:
            if hasattr(self.role_name, 'to_alipay_dict'):
                params['role_name'] = self.role_name.to_alipay_dict()
            else:
                params['role_name'] = self.role_name
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        if self.roster_id:
            if hasattr(self.roster_id, 'to_alipay_dict'):
                params['roster_id'] = self.roster_id.to_alipay_dict()
            else:
                params['roster_id'] = self.roster_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduRosterInfo()
        if 'bind_status' in d:
            o.bind_status = d['bind_status']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'department_info' in d:
            o.department_info = d['department_info']
        if 'department_info_list' in d:
            o.department_info_list = d['department_info_list']
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
        if 'role_name' in d:
            o.role_name = d['role_name']
        if 'role_type' in d:
            o.role_type = d['role_type']
        if 'roster_id' in d:
            o.roster_id = d['roster_id']
        return o


