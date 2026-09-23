#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CheckItem(object):

    def __init__(self):
        self._department = None
        self._doctor_remark = None
        self._id = None
        self._name = None
        self._notice = None
        self._purposes = None
        self._type = None

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def doctor_remark(self):
        return self._doctor_remark

    @doctor_remark.setter
    def doctor_remark(self, value):
        self._doctor_remark = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def purposes(self):
        return self._purposes

    @purposes.setter
    def purposes(self, value):
        self._purposes = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.doctor_remark:
            if hasattr(self.doctor_remark, 'to_alipay_dict'):
                params['doctor_remark'] = self.doctor_remark.to_alipay_dict()
            else:
                params['doctor_remark'] = self.doctor_remark
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        if self.purposes:
            if hasattr(self.purposes, 'to_alipay_dict'):
                params['purposes'] = self.purposes.to_alipay_dict()
            else:
                params['purposes'] = self.purposes
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CheckItem()
        if 'department' in d:
            o.department = d['department']
        if 'doctor_remark' in d:
            o.doctor_remark = d['doctor_remark']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'notice' in d:
            o.notice = d['notice']
        if 'purposes' in d:
            o.purposes = d['purposes']
        if 'type' in d:
            o.type = d['type']
        return o


