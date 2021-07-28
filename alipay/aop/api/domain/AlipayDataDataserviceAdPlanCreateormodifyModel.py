#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdPlanCreateormodifyModel(object):

    def __init__(self):
        self._biz_token = None
        self._budget = None
        self._charge_type = None
        self._end_date = None
        self._extend_info = None
        self._plan_name = None
        self._plan_outer_id = None
        self._plan_status = None
        self._principal_id = None
        self._sell_mode = None
        self._start_date = None
        self._time_schema = None
        self._user_id = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
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
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def plan_outer_id(self):
        return self._plan_outer_id

    @plan_outer_id.setter
    def plan_outer_id(self, value):
        self._plan_outer_id = value
    @property
    def plan_status(self):
        return self._plan_status

    @plan_status.setter
    def plan_status(self, value):
        self._plan_status = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
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
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
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
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.plan_outer_id:
            if hasattr(self.plan_outer_id, 'to_alipay_dict'):
                params['plan_outer_id'] = self.plan_outer_id.to_alipay_dict()
            else:
                params['plan_outer_id'] = self.plan_outer_id
        if self.plan_status:
            if hasattr(self.plan_status, 'to_alipay_dict'):
                params['plan_status'] = self.plan_status.to_alipay_dict()
            else:
                params['plan_status'] = self.plan_status
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
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
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdPlanCreateormodifyModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'budget' in d:
            o.budget = d['budget']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'plan_outer_id' in d:
            o.plan_outer_id = d['plan_outer_id']
        if 'plan_status' in d:
            o.plan_status = d['plan_status']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'sell_mode' in d:
            o.sell_mode = d['sell_mode']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'time_schema' in d:
            o.time_schema = d['time_schema']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


