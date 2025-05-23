#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MarketTargetConfiguration import MarketTargetConfiguration


class PlanPageListRes(object):

    def __init__(self):
        self._budget = None
        self._charge_type = None
        self._end_date = None
        self._gmt_modified = None
        self._market_target_code = None
        self._market_target_config = None
        self._market_target_name = None
        self._plan_id = None
        self._plan_name = None
        self._plan_status = None
        self._plan_unlimited_budget_switch = None
        self._principal_id = None
        self._scene_code = None
        self._sell_mode = None
        self._start_date = None
        self._time_schema = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        self._budget = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def market_target_code(self):
        return self._market_target_code

    @market_target_code.setter
    def market_target_code(self, value):
        self._market_target_code = value
    @property
    def market_target_config(self):
        return self._market_target_config

    @market_target_config.setter
    def market_target_config(self, value):
        if isinstance(value, MarketTargetConfiguration):
            self._market_target_config = value
        else:
            self._market_target_config = MarketTargetConfiguration.from_alipay_dict(value)
    @property
    def market_target_name(self):
        return self._market_target_name

    @market_target_name.setter
    def market_target_name(self, value):
        self._market_target_name = value
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
    def plan_status(self):
        return self._plan_status

    @plan_status.setter
    def plan_status(self, value):
        self._plan_status = value
    @property
    def plan_unlimited_budget_switch(self):
        return self._plan_unlimited_budget_switch

    @plan_unlimited_budget_switch.setter
    def plan_unlimited_budget_switch(self, value):
        self._plan_unlimited_budget_switch = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sell_mode(self):
        return self._sell_mode

    @sell_mode.setter
    def sell_mode(self, value):
        self._sell_mode = value
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
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.market_target_code:
            if hasattr(self.market_target_code, 'to_alipay_dict'):
                params['market_target_code'] = self.market_target_code.to_alipay_dict()
            else:
                params['market_target_code'] = self.market_target_code
        if self.market_target_config:
            if hasattr(self.market_target_config, 'to_alipay_dict'):
                params['market_target_config'] = self.market_target_config.to_alipay_dict()
            else:
                params['market_target_config'] = self.market_target_config
        if self.market_target_name:
            if hasattr(self.market_target_name, 'to_alipay_dict'):
                params['market_target_name'] = self.market_target_name.to_alipay_dict()
            else:
                params['market_target_name'] = self.market_target_name
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
        if self.plan_status:
            if hasattr(self.plan_status, 'to_alipay_dict'):
                params['plan_status'] = self.plan_status.to_alipay_dict()
            else:
                params['plan_status'] = self.plan_status
        if self.plan_unlimited_budget_switch:
            if hasattr(self.plan_unlimited_budget_switch, 'to_alipay_dict'):
                params['plan_unlimited_budget_switch'] = self.plan_unlimited_budget_switch.to_alipay_dict()
            else:
                params['plan_unlimited_budget_switch'] = self.plan_unlimited_budget_switch
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.sell_mode:
            if hasattr(self.sell_mode, 'to_alipay_dict'):
                params['sell_mode'] = self.sell_mode.to_alipay_dict()
            else:
                params['sell_mode'] = self.sell_mode
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
        o = PlanPageListRes()
        if 'budget' in d:
            o.budget = d['budget']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'market_target_code' in d:
            o.market_target_code = d['market_target_code']
        if 'market_target_config' in d:
            o.market_target_config = d['market_target_config']
        if 'market_target_name' in d:
            o.market_target_name = d['market_target_name']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'plan_status' in d:
            o.plan_status = d['plan_status']
        if 'plan_unlimited_budget_switch' in d:
            o.plan_unlimited_budget_switch = d['plan_unlimited_budget_switch']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sell_mode' in d:
            o.sell_mode = d['sell_mode']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'time_schema' in d:
            o.time_schema = d['time_schema']
        return o


