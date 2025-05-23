#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdcampaignPlanCreateormodifyModel(object):

    def __init__(self):
        self._budget = None
        self._end_date = None
        self._market_target_code = None
        self._plan_id = None
        self._plan_name = None
        self._plan_unlimited_budget_switch = None
        self._principal_tag = None
        self._start_date = None
        self._time_schema = None

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
    def market_target_code(self):
        return self._market_target_code

    @market_target_code.setter
    def market_target_code(self, value):
        self._market_target_code = value
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
    def plan_unlimited_budget_switch(self):
        return self._plan_unlimited_budget_switch

    @plan_unlimited_budget_switch.setter
    def plan_unlimited_budget_switch(self, value):
        self._plan_unlimited_budget_switch = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def time_schema(self):
        return self._time_schema

    @time_schema.setter
    def time_schema(self, value):
        self._time_schema = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.market_target_code:
            if hasattr(self.market_target_code, 'to_alipay_dict'):
                params['market_target_code'] = self.market_target_code.to_alipay_dict()
            else:
                params['market_target_code'] = self.market_target_code
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
        if self.plan_unlimited_budget_switch:
            if hasattr(self.plan_unlimited_budget_switch, 'to_alipay_dict'):
                params['plan_unlimited_budget_switch'] = self.plan_unlimited_budget_switch.to_alipay_dict()
            else:
                params['plan_unlimited_budget_switch'] = self.plan_unlimited_budget_switch
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.time_schema:
            if hasattr(self.time_schema, 'to_alipay_dict'):
                params['time_schema'] = self.time_schema.to_alipay_dict()
            else:
                params['time_schema'] = self.time_schema
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdcampaignPlanCreateormodifyModel()
        if 'budget' in d:
            o.budget = d['budget']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'market_target_code' in d:
            o.market_target_code = d['market_target_code']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'plan_unlimited_budget_switch' in d:
            o.plan_unlimited_budget_switch = d['plan_unlimited_budget_switch']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'time_schema' in d:
            o.time_schema = d['time_schema']
        return o


