#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CancelCommissionRoleInfo import CancelCommissionRoleInfo


class CancelCommissionInfo(object):

    def __init__(self):
        self._commission_role_list = None
        self._modify_isv_rule = None
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
                if isinstance(i, CancelCommissionRoleInfo):
                    self._commission_role_list.append(i)
                else:
                    self._commission_role_list.append(CancelCommissionRoleInfo.from_alipay_dict(i))
    @property
    def modify_isv_rule(self):
        return self._modify_isv_rule

    @modify_isv_rule.setter
    def modify_isv_rule(self, value):
        self._modify_isv_rule = value
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
        if self.modify_isv_rule:
            if hasattr(self.modify_isv_rule, 'to_alipay_dict'):
                params['modify_isv_rule'] = self.modify_isv_rule.to_alipay_dict()
            else:
                params['modify_isv_rule'] = self.modify_isv_rule
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
        o = CancelCommissionInfo()
        if 'commission_role_list' in d:
            o.commission_role_list = d['commission_role_list']
        if 'modify_isv_rule' in d:
            o.modify_isv_rule = d['modify_isv_rule']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        return o


