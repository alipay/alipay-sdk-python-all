#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DepartmentData(object):

    def __init__(self):
        self._department_disease_info = None
        self._department_id = None
        self._department_name = None
        self._department_tag = None
        self._department_type = None
        self._department_url = None
        self._hospital_name = None
        self._parent_department_id = None
        self._parent_department_name = None

    @property
    def department_disease_info(self):
        return self._department_disease_info

    @department_disease_info.setter
    def department_disease_info(self, value):
        self._department_disease_info = value
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def department_tag(self):
        return self._department_tag

    @department_tag.setter
    def department_tag(self, value):
        self._department_tag = value
    @property
    def department_type(self):
        return self._department_type

    @department_type.setter
    def department_type(self, value):
        self._department_type = value
    @property
    def department_url(self):
        return self._department_url

    @department_url.setter
    def department_url(self, value):
        self._department_url = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def parent_department_id(self):
        return self._parent_department_id

    @parent_department_id.setter
    def parent_department_id(self, value):
        self._parent_department_id = value
    @property
    def parent_department_name(self):
        return self._parent_department_name

    @parent_department_name.setter
    def parent_department_name(self, value):
        self._parent_department_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.department_disease_info:
            if hasattr(self.department_disease_info, 'to_alipay_dict'):
                params['department_disease_info'] = self.department_disease_info.to_alipay_dict()
            else:
                params['department_disease_info'] = self.department_disease_info
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.department_tag:
            if hasattr(self.department_tag, 'to_alipay_dict'):
                params['department_tag'] = self.department_tag.to_alipay_dict()
            else:
                params['department_tag'] = self.department_tag
        if self.department_type:
            if hasattr(self.department_type, 'to_alipay_dict'):
                params['department_type'] = self.department_type.to_alipay_dict()
            else:
                params['department_type'] = self.department_type
        if self.department_url:
            if hasattr(self.department_url, 'to_alipay_dict'):
                params['department_url'] = self.department_url.to_alipay_dict()
            else:
                params['department_url'] = self.department_url
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.parent_department_id:
            if hasattr(self.parent_department_id, 'to_alipay_dict'):
                params['parent_department_id'] = self.parent_department_id.to_alipay_dict()
            else:
                params['parent_department_id'] = self.parent_department_id
        if self.parent_department_name:
            if hasattr(self.parent_department_name, 'to_alipay_dict'):
                params['parent_department_name'] = self.parent_department_name.to_alipay_dict()
            else:
                params['parent_department_name'] = self.parent_department_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DepartmentData()
        if 'department_disease_info' in d:
            o.department_disease_info = d['department_disease_info']
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'department_tag' in d:
            o.department_tag = d['department_tag']
        if 'department_type' in d:
            o.department_type = d['department_type']
        if 'department_url' in d:
            o.department_url = d['department_url']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'parent_department_id' in d:
            o.parent_department_id = d['parent_department_id']
        if 'parent_department_name' in d:
            o.parent_department_name = d['parent_department_name']
        return o


