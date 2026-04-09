#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubDepartmentInfoVO import SubDepartmentInfoVO


class DepartmentInfoVO(object):

    def __init__(self):
        self._child_department_list = None
        self._depart_doctor_num = None
        self._depart_id = None
        self._depart_logo = None
        self._depart_name = None
        self._parent_depart_id = None

    @property
    def child_department_list(self):
        return self._child_department_list

    @child_department_list.setter
    def child_department_list(self, value):
        if isinstance(value, list):
            self._child_department_list = list()
            for i in value:
                if isinstance(i, SubDepartmentInfoVO):
                    self._child_department_list.append(i)
                else:
                    self._child_department_list.append(SubDepartmentInfoVO.from_alipay_dict(i))
    @property
    def depart_doctor_num(self):
        return self._depart_doctor_num

    @depart_doctor_num.setter
    def depart_doctor_num(self, value):
        self._depart_doctor_num = value
    @property
    def depart_id(self):
        return self._depart_id

    @depart_id.setter
    def depart_id(self, value):
        self._depart_id = value
    @property
    def depart_logo(self):
        return self._depart_logo

    @depart_logo.setter
    def depart_logo(self, value):
        self._depart_logo = value
    @property
    def depart_name(self):
        return self._depart_name

    @depart_name.setter
    def depart_name(self, value):
        self._depart_name = value
    @property
    def parent_depart_id(self):
        return self._parent_depart_id

    @parent_depart_id.setter
    def parent_depart_id(self, value):
        self._parent_depart_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.child_department_list:
            if isinstance(self.child_department_list, list):
                for i in range(0, len(self.child_department_list)):
                    element = self.child_department_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.child_department_list[i] = element.to_alipay_dict()
            if hasattr(self.child_department_list, 'to_alipay_dict'):
                params['child_department_list'] = self.child_department_list.to_alipay_dict()
            else:
                params['child_department_list'] = self.child_department_list
        if self.depart_doctor_num:
            if hasattr(self.depart_doctor_num, 'to_alipay_dict'):
                params['depart_doctor_num'] = self.depart_doctor_num.to_alipay_dict()
            else:
                params['depart_doctor_num'] = self.depart_doctor_num
        if self.depart_id:
            if hasattr(self.depart_id, 'to_alipay_dict'):
                params['depart_id'] = self.depart_id.to_alipay_dict()
            else:
                params['depart_id'] = self.depart_id
        if self.depart_logo:
            if hasattr(self.depart_logo, 'to_alipay_dict'):
                params['depart_logo'] = self.depart_logo.to_alipay_dict()
            else:
                params['depart_logo'] = self.depart_logo
        if self.depart_name:
            if hasattr(self.depart_name, 'to_alipay_dict'):
                params['depart_name'] = self.depart_name.to_alipay_dict()
            else:
                params['depart_name'] = self.depart_name
        if self.parent_depart_id:
            if hasattr(self.parent_depart_id, 'to_alipay_dict'):
                params['parent_depart_id'] = self.parent_depart_id.to_alipay_dict()
            else:
                params['parent_depart_id'] = self.parent_depart_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DepartmentInfoVO()
        if 'child_department_list' in d:
            o.child_department_list = d['child_department_list']
        if 'depart_doctor_num' in d:
            o.depart_doctor_num = d['depart_doctor_num']
        if 'depart_id' in d:
            o.depart_id = d['depart_id']
        if 'depart_logo' in d:
            o.depart_logo = d['depart_logo']
        if 'depart_name' in d:
            o.depart_name = d['depart_name']
        if 'parent_depart_id' in d:
            o.parent_depart_id = d['parent_depart_id']
        return o


