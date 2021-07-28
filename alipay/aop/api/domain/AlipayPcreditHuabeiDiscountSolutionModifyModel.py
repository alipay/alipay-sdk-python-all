#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubShopInfo import SubShopInfo


class AlipayPcreditHuabeiDiscountSolutionModifyModel(object):

    def __init__(self):
        self._activity_name = None
        self._amount_budget = None
        self._budget_warning_mail_list = None
        self._budget_warning_mobile_no_list = None
        self._budget_warning_money = None
        self._end_time = None
        self._install_num_str_list = None
        self._max_money_limit = None
        self._min_money_limit = None
        self._solution_id = None
        self._start_time = None
        self._sub_shop_info = None

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
        if isinstance(value, list):
            self._budget_warning_mail_list = list()
            for i in value:
                self._budget_warning_mail_list.append(i)
    @property
    def budget_warning_mobile_no_list(self):
        return self._budget_warning_mobile_no_list

    @budget_warning_mobile_no_list.setter
    def budget_warning_mobile_no_list(self, value):
        if isinstance(value, list):
            self._budget_warning_mobile_no_list = list()
            for i in value:
                self._budget_warning_mobile_no_list.append(i)
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
    def install_num_str_list(self):
        return self._install_num_str_list

    @install_num_str_list.setter
    def install_num_str_list(self, value):
        if isinstance(value, list):
            self._install_num_str_list = list()
            for i in value:
                self._install_num_str_list.append(i)
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
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_shop_info(self):
        return self._sub_shop_info

    @sub_shop_info.setter
    def sub_shop_info(self, value):
        if isinstance(value, SubShopInfo):
            self._sub_shop_info = value
        else:
            self._sub_shop_info = SubShopInfo.from_alipay_dict(value)


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
            if isinstance(self.budget_warning_mail_list, list):
                for i in range(0, len(self.budget_warning_mail_list)):
                    element = self.budget_warning_mail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.budget_warning_mail_list[i] = element.to_alipay_dict()
            if hasattr(self.budget_warning_mail_list, 'to_alipay_dict'):
                params['budget_warning_mail_list'] = self.budget_warning_mail_list.to_alipay_dict()
            else:
                params['budget_warning_mail_list'] = self.budget_warning_mail_list
        if self.budget_warning_mobile_no_list:
            if isinstance(self.budget_warning_mobile_no_list, list):
                for i in range(0, len(self.budget_warning_mobile_no_list)):
                    element = self.budget_warning_mobile_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.budget_warning_mobile_no_list[i] = element.to_alipay_dict()
            if hasattr(self.budget_warning_mobile_no_list, 'to_alipay_dict'):
                params['budget_warning_mobile_no_list'] = self.budget_warning_mobile_no_list.to_alipay_dict()
            else:
                params['budget_warning_mobile_no_list'] = self.budget_warning_mobile_no_list
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
        if self.install_num_str_list:
            if isinstance(self.install_num_str_list, list):
                for i in range(0, len(self.install_num_str_list)):
                    element = self.install_num_str_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.install_num_str_list[i] = element.to_alipay_dict()
            if hasattr(self.install_num_str_list, 'to_alipay_dict'):
                params['install_num_str_list'] = self.install_num_str_list.to_alipay_dict()
            else:
                params['install_num_str_list'] = self.install_num_str_list
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
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_shop_info:
            if hasattr(self.sub_shop_info, 'to_alipay_dict'):
                params['sub_shop_info'] = self.sub_shop_info.to_alipay_dict()
            else:
                params['sub_shop_info'] = self.sub_shop_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiDiscountSolutionModifyModel()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'amount_budget' in d:
            o.amount_budget = d['amount_budget']
        if 'budget_warning_mail_list' in d:
            o.budget_warning_mail_list = d['budget_warning_mail_list']
        if 'budget_warning_mobile_no_list' in d:
            o.budget_warning_mobile_no_list = d['budget_warning_mobile_no_list']
        if 'budget_warning_money' in d:
            o.budget_warning_money = d['budget_warning_money']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'install_num_str_list' in d:
            o.install_num_str_list = d['install_num_str_list']
        if 'max_money_limit' in d:
            o.max_money_limit = d['max_money_limit']
        if 'min_money_limit' in d:
            o.min_money_limit = d['min_money_limit']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_shop_info' in d:
            o.sub_shop_info = d['sub_shop_info']
        return o


