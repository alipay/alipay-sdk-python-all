#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommissionRelationDTO import CommissionRelationDTO
from alipay.aop.api.domain.CommissionRelationDTO import CommissionRelationDTO


class CommissionRuleDTO(object):

    def __init__(self):
        self._charged_account_login_id = None
        self._charged_account_name = None
        self._commission_ratio = None
        self._commission_relation_info_list = None
        self._commission_relation_list = None
        self._create_time = None
        self._end_date = None
        self._rule_id = None
        self._start_date = None

    @property
    def charged_account_login_id(self):
        return self._charged_account_login_id

    @charged_account_login_id.setter
    def charged_account_login_id(self, value):
        self._charged_account_login_id = value
    @property
    def charged_account_name(self):
        return self._charged_account_name

    @charged_account_name.setter
    def charged_account_name(self, value):
        self._charged_account_name = value
    @property
    def commission_ratio(self):
        return self._commission_ratio

    @commission_ratio.setter
    def commission_ratio(self, value):
        self._commission_ratio = value
    @property
    def commission_relation_info_list(self):
        return self._commission_relation_info_list

    @commission_relation_info_list.setter
    def commission_relation_info_list(self, value):
        if isinstance(value, list):
            self._commission_relation_info_list = list()
            for i in value:
                if isinstance(i, CommissionRelationDTO):
                    self._commission_relation_info_list.append(i)
                else:
                    self._commission_relation_info_list.append(CommissionRelationDTO.from_alipay_dict(i))
    @property
    def commission_relation_list(self):
        return self._commission_relation_list

    @commission_relation_list.setter
    def commission_relation_list(self, value):
        if isinstance(value, CommissionRelationDTO):
            self._commission_relation_list = value
        else:
            self._commission_relation_list = CommissionRelationDTO.from_alipay_dict(value)
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.charged_account_login_id:
            if hasattr(self.charged_account_login_id, 'to_alipay_dict'):
                params['charged_account_login_id'] = self.charged_account_login_id.to_alipay_dict()
            else:
                params['charged_account_login_id'] = self.charged_account_login_id
        if self.charged_account_name:
            if hasattr(self.charged_account_name, 'to_alipay_dict'):
                params['charged_account_name'] = self.charged_account_name.to_alipay_dict()
            else:
                params['charged_account_name'] = self.charged_account_name
        if self.commission_ratio:
            if hasattr(self.commission_ratio, 'to_alipay_dict'):
                params['commission_ratio'] = self.commission_ratio.to_alipay_dict()
            else:
                params['commission_ratio'] = self.commission_ratio
        if self.commission_relation_info_list:
            if isinstance(self.commission_relation_info_list, list):
                for i in range(0, len(self.commission_relation_info_list)):
                    element = self.commission_relation_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commission_relation_info_list[i] = element.to_alipay_dict()
            if hasattr(self.commission_relation_info_list, 'to_alipay_dict'):
                params['commission_relation_info_list'] = self.commission_relation_info_list.to_alipay_dict()
            else:
                params['commission_relation_info_list'] = self.commission_relation_info_list
        if self.commission_relation_list:
            if hasattr(self.commission_relation_list, 'to_alipay_dict'):
                params['commission_relation_list'] = self.commission_relation_list.to_alipay_dict()
            else:
                params['commission_relation_list'] = self.commission_relation_list
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommissionRuleDTO()
        if 'charged_account_login_id' in d:
            o.charged_account_login_id = d['charged_account_login_id']
        if 'charged_account_name' in d:
            o.charged_account_name = d['charged_account_name']
        if 'commission_ratio' in d:
            o.commission_ratio = d['commission_ratio']
        if 'commission_relation_info_list' in d:
            o.commission_relation_info_list = d['commission_relation_info_list']
        if 'commission_relation_list' in d:
            o.commission_relation_list = d['commission_relation_list']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


