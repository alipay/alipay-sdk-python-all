#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StaffInfo import StaffInfo


class KoubeiMarketingDataEnterpriseStaffinfoUploadModel(object):

    def __init__(self):
        self._batch_id = None
        self._enterprise_name = None
        self._operator_type = None
        self._staff_info = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def staff_info(self):
        return self._staff_info

    @staff_info.setter
    def staff_info(self, value):
        if isinstance(value, list):
            self._staff_info = list()
            for i in value:
                if isinstance(i, StaffInfo):
                    self._staff_info.append(i)
                else:
                    self._staff_info.append(StaffInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.staff_info:
            if isinstance(self.staff_info, list):
                for i in range(0, len(self.staff_info)):
                    element = self.staff_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.staff_info[i] = element.to_alipay_dict()
            if hasattr(self.staff_info, 'to_alipay_dict'):
                params['staff_info'] = self.staff_info.to_alipay_dict()
            else:
                params['staff_info'] = self.staff_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataEnterpriseStaffinfoUploadModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'staff_info' in d:
            o.staff_info = d['staff_info']
        return o


