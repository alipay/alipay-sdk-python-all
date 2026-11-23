#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEmployeePaydeductauthUnsignModel(object):

    def __init__(self):
        self._employee_id = None
        self._enterprise_id = None
        self._receiver_pids = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def receiver_pids(self):
        return self._receiver_pids

    @receiver_pids.setter
    def receiver_pids(self, value):
        if isinstance(value, list):
            self._receiver_pids = list()
            for i in value:
                self._receiver_pids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.receiver_pids:
            if isinstance(self.receiver_pids, list):
                for i in range(0, len(self.receiver_pids)):
                    element = self.receiver_pids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.receiver_pids[i] = element.to_alipay_dict()
            if hasattr(self.receiver_pids, 'to_alipay_dict'):
                params['receiver_pids'] = self.receiver_pids.to_alipay_dict()
            else:
                params['receiver_pids'] = self.receiver_pids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcEmployeePaydeductauthUnsignModel()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'receiver_pids' in d:
            o.receiver_pids = d['receiver_pids']
        return o


