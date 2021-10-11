#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitMaterial(object):

    def __init__(self):
        self._data = None
        self._description = None
        self._material_audit_info = None
        self._name = None
        self._subject_id = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def material_audit_info(self):
        return self._material_audit_info

    @material_audit_info.setter
    def material_audit_info(self, value):
        self._material_audit_info = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value):
        self._subject_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.material_audit_info:
            if hasattr(self.material_audit_info, 'to_alipay_dict'):
                params['material_audit_info'] = self.material_audit_info.to_alipay_dict()
            else:
                params['material_audit_info'] = self.material_audit_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.subject_id:
            if hasattr(self.subject_id, 'to_alipay_dict'):
                params['subject_id'] = self.subject_id.to_alipay_dict()
            else:
                params['subject_id'] = self.subject_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitMaterial()
        if 'data' in d:
            o.data = d['data']
        if 'description' in d:
            o.description = d['description']
        if 'material_audit_info' in d:
            o.material_audit_info = d['material_audit_info']
        if 'name' in d:
            o.name = d['name']
        if 'subject_id' in d:
            o.subject_id = d['subject_id']
        return o


