#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommissionRoleInfo import CommissionRoleInfo


class CommissionInfo(object):

    def __init__(self):
        self._commission_role_list = None
        self._isv_rate = None
        self._target_id = None
        self._target_type = None

    @property
    def commission_role_list(self):
        return self._commission_role_list

    @commission_role_list.setter
    def commission_role_list(self, value):
        if isinstance(value, list):
            self._commission_role_list = list()
            for i in value:
                if isinstance(i, CommissionRoleInfo):
                    self._commission_role_list.append(i)
                else:
                    self._commission_role_list.append(CommissionRoleInfo.from_alipay_dict(i))
    @property
    def isv_rate(self):
        return self._isv_rate

    @isv_rate.setter
    def isv_rate(self, value):
        self._isv_rate = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_role_list:
            if isinstance(self.commission_role_list, list):
                for i in range(0, len(self.commission_role_list)):
                    element = self.commission_role_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commission_role_list[i] = element.to_alipay_dict()
            if hasattr(self.commission_role_list, 'to_alipay_dict'):
                params['commission_role_list'] = self.commission_role_list.to_alipay_dict()
            else:
                params['commission_role_list'] = self.commission_role_list
        if self.isv_rate:
            if hasattr(self.isv_rate, 'to_alipay_dict'):
                params['isv_rate'] = self.isv_rate.to_alipay_dict()
            else:
                params['isv_rate'] = self.isv_rate
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_type:
            if hasattr(self.target_type, 'to_alipay_dict'):
                params['target_type'] = self.target_type.to_alipay_dict()
            else:
                params['target_type'] = self.target_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommissionInfo()
        if 'commission_role_list' in d:
            o.commission_role_list = d['commission_role_list']
        if 'isv_rate' in d:
            o.isv_rate = d['isv_rate']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        return o


