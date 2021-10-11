#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HbMerchantInfo import HbMerchantInfo


class AlipayPcreditHuabeiMerchantActivityCreateModel(object):

    def __init__(self):
        self._activity_name = None
        self._amount_budget = None
        self._budget_warning_mail_list = None
        self._budget_warning_mobile_list = None
        self._budget_warning_money = None
        self._end_time = None
        self._fund_type = None
        self._install_num_list = None
        self._isv_id = None
        self._max_money_limit = None
        self._merchant_info = None
        self._min_money_limit = None
        self._out_request_no = None
        self._start_time = None
        self._subsidy_scope = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def amount_budget(self):
        return self._amount_budget

    @amount_budget.setter
    def amount_budget(self, value):
        self._amount_budget = value
    @property
    def budget_warning_mail_list(self):
        return self._budget_warning_mail_list

    @budget_warning_mail_list.setter
    def budget_warning_mail_list(self, value):
        self._budget_warning_mail_list = value
    @property
    def budget_warning_mobile_list(self):
        return self._budget_warning_mobile_list

    @budget_warning_mobile_list.setter
    def budget_warning_mobile_list(self, value):
        self._budget_warning_mobile_list = value
    @property
    def budget_warning_money(self):
        return self._budget_warning_money

    @budget_warning_money.setter
    def budget_warning_money(self, value):
        self._budget_warning_money = value
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
    def isv_id(self):
        return self._isv_id

    @isv_id.setter
    def isv_id(self, value):
        self._isv_id = value
    @property
    def max_money_limit(self):
        return self._max_money_limit

    @max_money_limit.setter
    def max_money_limit(self, value):
        self._max_money_limit = value
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, list):
            self._merchant_info = list()
            for i in value:
                if isinstance(i, HbMerchantInfo):
                    self._merchant_info.append(i)
                else:
                    self._merchant_info.append(HbMerchantInfo.from_alipay_dict(i))
    @property
    def min_money_limit(self):
        return self._min_money_limit

    @min_money_limit.setter
    def min_money_limit(self, value):
        self._min_money_limit = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def subsidy_scope(self):
        return self._subsidy_scope

    @subsidy_scope.setter
    def subsidy_scope(self, value):
        self._subsidy_scope = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.amount_budget:
            if hasattr(self.amount_budget, 'to_alipay_dict'):
                params['amount_budget'] = self.amount_budget.to_alipay_dict()
            else:
                params['amount_budget'] = self.amount_budget
        if self.budget_warning_mail_list:
            if hasattr(self.budget_warning_mail_list, 'to_alipay_dict'):
                params['budget_warning_mail_list'] = self.budget_warning_mail_list.to_alipay_dict()
            else:
                params['budget_warning_mail_list'] = self.budget_warning_mail_list
        if self.budget_warning_mobile_list:
            if hasattr(self.budget_warning_mobile_list, 'to_alipay_dict'):
                params['budget_warning_mobile_list'] = self.budget_warning_mobile_list.to_alipay_dict()
            else:
                params['budget_warning_mobile_list'] = self.budget_warning_mobile_list
        if self.budget_warning_money:
            if hasattr(self.budget_warning_money, 'to_alipay_dict'):
                params['budget_warning_money'] = self.budget_warning_money.to_alipay_dict()
            else:
                params['budget_warning_money'] = self.budget_warning_money
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
        if self.isv_id:
            if hasattr(self.isv_id, 'to_alipay_dict'):
                params['isv_id'] = self.isv_id.to_alipay_dict()
            else:
                params['isv_id'] = self.isv_id
        if self.max_money_limit:
            if hasattr(self.max_money_limit, 'to_alipay_dict'):
                params['max_money_limit'] = self.max_money_limit.to_alipay_dict()
            else:
                params['max_money_limit'] = self.max_money_limit
        if self.merchant_info:
            if isinstance(self.merchant_info, list):
                for i in range(0, len(self.merchant_info)):
                    element = self.merchant_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_info[i] = element.to_alipay_dict()
            if hasattr(self.merchant_info, 'to_alipay_dict'):
                params['merchant_info'] = self.merchant_info.to_alipay_dict()
            else:
                params['merchant_info'] = self.merchant_info
        if self.min_money_limit:
            if hasattr(self.min_money_limit, 'to_alipay_dict'):
                params['min_money_limit'] = self.min_money_limit.to_alipay_dict()
            else:
                params['min_money_limit'] = self.min_money_limit
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = AlipayPcreditHuabeiMerchantActivityCreateModel()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'amount_budget' in d:
            o.amount_budget = d['amount_budget']
        if 'budget_warning_mail_list' in d:
            o.budget_warning_mail_list = d['budget_warning_mail_list']
        if 'budget_warning_mobile_list' in d:
            o.budget_warning_mobile_list = d['budget_warning_mobile_list']
        if 'budget_warning_money' in d:
            o.budget_warning_money = d['budget_warning_money']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'install_num_list' in d:
            o.install_num_list = d['install_num_list']
        if 'isv_id' in d:
            o.isv_id = d['isv_id']
        if 'max_money_limit' in d:
            o.max_money_limit = d['max_money_limit']
        if 'merchant_info' in d:
            o.merchant_info = d['merchant_info']
        if 'min_money_limit' in d:
            o.min_money_limit = d['min_money_limit']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'subsidy_scope' in d:
            o.subsidy_scope = d['subsidy_scope']
        return o


