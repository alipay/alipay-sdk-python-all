#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DetailCommissionRoleInfo import DetailCommissionRoleInfo
from alipay.aop.api.domain.LatestCommissionInfo import LatestCommissionInfo


class DetailCommissionInfo(object):

    def __init__(self):
        self._alloc_invalid_time = None
        self._alloc_valid_time = None
        self._commission_role_list = None
        self._commission_status = None
        self._isv_rate = None
        self._latest_commission = None
        self._real_invalid_time = None
        self._real_valid_time = None
        self._target_id = None
        self._target_type = None

    @property
    def alloc_invalid_time(self):
        return self._alloc_invalid_time

    @alloc_invalid_time.setter
    def alloc_invalid_time(self, value):
        self._alloc_invalid_time = value
    @property
    def alloc_valid_time(self):
        return self._alloc_valid_time

    @alloc_valid_time.setter
    def alloc_valid_time(self, value):
        self._alloc_valid_time = value
    @property
    def commission_role_list(self):
        return self._commission_role_list

    @commission_role_list.setter
    def commission_role_list(self, value):
        if isinstance(value, list):
            self._commission_role_list = list()
            for i in value:
                if isinstance(i, DetailCommissionRoleInfo):
                    self._commission_role_list.append(i)
                else:
                    self._commission_role_list.append(DetailCommissionRoleInfo.from_alipay_dict(i))
    @property
    def commission_status(self):
        return self._commission_status

    @commission_status.setter
    def commission_status(self, value):
        self._commission_status = value
    @property
    def isv_rate(self):
        return self._isv_rate

    @isv_rate.setter
    def isv_rate(self, value):
        self._isv_rate = value
    @property
    def latest_commission(self):
        return self._latest_commission

    @latest_commission.setter
    def latest_commission(self, value):
        if isinstance(value, LatestCommissionInfo):
            self._latest_commission = value
        else:
            self._latest_commission = LatestCommissionInfo.from_alipay_dict(value)
    @property
    def real_invalid_time(self):
        return self._real_invalid_time

    @real_invalid_time.setter
    def real_invalid_time(self, value):
        self._real_invalid_time = value
    @property
    def real_valid_time(self):
        return self._real_valid_time

    @real_valid_time.setter
    def real_valid_time(self, value):
        self._real_valid_time = value
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
        if self.alloc_invalid_time:
            if hasattr(self.alloc_invalid_time, 'to_alipay_dict'):
                params['alloc_invalid_time'] = self.alloc_invalid_time.to_alipay_dict()
            else:
                params['alloc_invalid_time'] = self.alloc_invalid_time
        if self.alloc_valid_time:
            if hasattr(self.alloc_valid_time, 'to_alipay_dict'):
                params['alloc_valid_time'] = self.alloc_valid_time.to_alipay_dict()
            else:
                params['alloc_valid_time'] = self.alloc_valid_time
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
        if self.commission_status:
            if hasattr(self.commission_status, 'to_alipay_dict'):
                params['commission_status'] = self.commission_status.to_alipay_dict()
            else:
                params['commission_status'] = self.commission_status
        if self.isv_rate:
            if hasattr(self.isv_rate, 'to_alipay_dict'):
                params['isv_rate'] = self.isv_rate.to_alipay_dict()
            else:
                params['isv_rate'] = self.isv_rate
        if self.latest_commission:
            if hasattr(self.latest_commission, 'to_alipay_dict'):
                params['latest_commission'] = self.latest_commission.to_alipay_dict()
            else:
                params['latest_commission'] = self.latest_commission
        if self.real_invalid_time:
            if hasattr(self.real_invalid_time, 'to_alipay_dict'):
                params['real_invalid_time'] = self.real_invalid_time.to_alipay_dict()
            else:
                params['real_invalid_time'] = self.real_invalid_time
        if self.real_valid_time:
            if hasattr(self.real_valid_time, 'to_alipay_dict'):
                params['real_valid_time'] = self.real_valid_time.to_alipay_dict()
            else:
                params['real_valid_time'] = self.real_valid_time
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
        o = DetailCommissionInfo()
        if 'alloc_invalid_time' in d:
            o.alloc_invalid_time = d['alloc_invalid_time']
        if 'alloc_valid_time' in d:
            o.alloc_valid_time = d['alloc_valid_time']
        if 'commission_role_list' in d:
            o.commission_role_list = d['commission_role_list']
        if 'commission_status' in d:
            o.commission_status = d['commission_status']
        if 'isv_rate' in d:
            o.isv_rate = d['isv_rate']
        if 'latest_commission' in d:
            o.latest_commission = d['latest_commission']
        if 'real_invalid_time' in d:
            o.real_invalid_time = d['real_invalid_time']
        if 'real_valid_time' in d:
            o.real_valid_time = d['real_valid_time']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        return o


