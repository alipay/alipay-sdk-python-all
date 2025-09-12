#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ThirdActivityInfo(object):

    def __init__(self):
        self._aggr_id = None
        self._end_time = None
        self._fund_type = None
        self._install_num_list = None
        self._max_money_limit = None
        self._min_money_limit = None
        self._name = None
        self._start_time = None
        self._status = None
        self._subsidy_scope = None

    @property
    def aggr_id(self):
        return self._aggr_id

    @aggr_id.setter
    def aggr_id(self, value):
        self._aggr_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def install_num_list(self):
        return self._install_num_list

    @install_num_list.setter
    def install_num_list(self, value):
        if isinstance(value, list):
            self._install_num_list = list()
            for i in value:
                self._install_num_list.append(i)
    @property
    def max_money_limit(self):
        return self._max_money_limit

    @max_money_limit.setter
    def max_money_limit(self, value):
        self._max_money_limit = value
    @property
    def min_money_limit(self):
        return self._min_money_limit

    @min_money_limit.setter
    def min_money_limit(self, value):
        self._min_money_limit = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subsidy_scope(self):
        return self._subsidy_scope

    @subsidy_scope.setter
    def subsidy_scope(self, value):
        self._subsidy_scope = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggr_id:
            if hasattr(self.aggr_id, 'to_alipay_dict'):
                params['aggr_id'] = self.aggr_id.to_alipay_dict()
            else:
                params['aggr_id'] = self.aggr_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.install_num_list:
            if isinstance(self.install_num_list, list):
                for i in range(0, len(self.install_num_list)):
                    element = self.install_num_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.install_num_list[i] = element.to_alipay_dict()
            if hasattr(self.install_num_list, 'to_alipay_dict'):
                params['install_num_list'] = self.install_num_list.to_alipay_dict()
            else:
                params['install_num_list'] = self.install_num_list
        if self.max_money_limit:
            if hasattr(self.max_money_limit, 'to_alipay_dict'):
                params['max_money_limit'] = self.max_money_limit.to_alipay_dict()
            else:
                params['max_money_limit'] = self.max_money_limit
        if self.min_money_limit:
            if hasattr(self.min_money_limit, 'to_alipay_dict'):
                params['min_money_limit'] = self.min_money_limit.to_alipay_dict()
            else:
                params['min_money_limit'] = self.min_money_limit
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.subsidy_scope:
            if hasattr(self.subsidy_scope, 'to_alipay_dict'):
                params['subsidy_scope'] = self.subsidy_scope.to_alipay_dict()
            else:
                params['subsidy_scope'] = self.subsidy_scope
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ThirdActivityInfo()
        if 'aggr_id' in d:
            o.aggr_id = d['aggr_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'install_num_list' in d:
            o.install_num_list = d['install_num_list']
        if 'max_money_limit' in d:
            o.max_money_limit = d['max_money_limit']
        if 'min_money_limit' in d:
            o.min_money_limit = d['min_money_limit']
        if 'name' in d:
            o.name = d['name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'subsidy_scope' in d:
            o.subsidy_scope = d['subsidy_scope']
        return o


