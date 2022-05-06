#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DepartmentData import DepartmentData


class AlipayCommerceMedicalIndustrydataDepartmentUploadModel(object):

    def __init__(self):
        self._department_list = None
        self._isv_pid = None
        self._request_id = None

    @property
    def department_list(self):
        return self._department_list

    @department_list.setter
    def department_list(self, value):
        if isinstance(value, list):
            self._department_list = list()
            for i in value:
                if isinstance(i, DepartmentData):
                    self._department_list.append(i)
                else:
                    self._department_list.append(DepartmentData.from_alipay_dict(i))
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataDepartmentUploadModel()
        if 'department_list' in d:
            o.department_list = d['department_list']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


