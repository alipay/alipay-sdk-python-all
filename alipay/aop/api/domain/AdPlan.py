#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdGroup import AdGroup


class AdPlan(object):

    def __init__(self):
        self._ad_user_id = None
        self._budget = None
        self._end_date = None
        self._group_list = None
        self._plan_id = None
        self._plan_name = None
        self._quantity = None
        self._start_date = None

    @property
    def ad_user_id(self):
        return self._ad_user_id

    @ad_user_id.setter
    def ad_user_id(self, value):
        self._ad_user_id = value
    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        self._budget = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def group_list(self):
        return self._group_list

    @group_list.setter
    def group_list(self, value):
        if isinstance(value, AdGroup):
            self._group_list = value
        else:
            self._group_list = AdGroup.from_alipay_dict(value)
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_user_id:
            if hasattr(self.ad_user_id, 'to_alipay_dict'):
                params['ad_user_id'] = self.ad_user_id.to_alipay_dict()
            else:
                params['ad_user_id'] = self.ad_user_id
        if self.budget:
            if hasattr(self.budget, 'to_alipay_dict'):
                params['budget'] = self.budget.to_alipay_dict()
            else:
                params['budget'] = self.budget
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.group_list:
            if hasattr(self.group_list, 'to_alipay_dict'):
                params['group_list'] = self.group_list.to_alipay_dict()
            else:
                params['group_list'] = self.group_list
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
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
        o = AdPlan()
        if 'ad_user_id' in d:
            o.ad_user_id = d['ad_user_id']
        if 'budget' in d:
            o.budget = d['budget']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'group_list' in d:
            o.group_list = d['group_list']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


