#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApiContractGoal(object):

    def __init__(self):
        self._complete_date = None
        self._create_date = None
        self._goal_current_value = None
        self._goal_key = None
        self._goal_status = None
        self._goal_type = None
        self._goal_value = None
        self._item_no = None
        self._last_complete_date = None

    @property
    def complete_date(self):
        return self._complete_date

    @complete_date.setter
    def complete_date(self, value):
        self._complete_date = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def goal_current_value(self):
        return self._goal_current_value

    @goal_current_value.setter
    def goal_current_value(self, value):
        self._goal_current_value = value
    @property
    def goal_key(self):
        return self._goal_key

    @goal_key.setter
    def goal_key(self, value):
        self._goal_key = value
    @property
    def goal_status(self):
        return self._goal_status

    @goal_status.setter
    def goal_status(self, value):
        self._goal_status = value
    @property
    def goal_type(self):
        return self._goal_type

    @goal_type.setter
    def goal_type(self, value):
        self._goal_type = value
    @property
    def goal_value(self):
        return self._goal_value

    @goal_value.setter
    def goal_value(self, value):
        self._goal_value = value
    @property
    def item_no(self):
        return self._item_no

    @item_no.setter
    def item_no(self, value):
        self._item_no = value
    @property
    def last_complete_date(self):
        return self._last_complete_date

    @last_complete_date.setter
    def last_complete_date(self, value):
        self._last_complete_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.complete_date:
            if hasattr(self.complete_date, 'to_alipay_dict'):
                params['complete_date'] = self.complete_date.to_alipay_dict()
            else:
                params['complete_date'] = self.complete_date
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.goal_current_value:
            if hasattr(self.goal_current_value, 'to_alipay_dict'):
                params['goal_current_value'] = self.goal_current_value.to_alipay_dict()
            else:
                params['goal_current_value'] = self.goal_current_value
        if self.goal_key:
            if hasattr(self.goal_key, 'to_alipay_dict'):
                params['goal_key'] = self.goal_key.to_alipay_dict()
            else:
                params['goal_key'] = self.goal_key
        if self.goal_status:
            if hasattr(self.goal_status, 'to_alipay_dict'):
                params['goal_status'] = self.goal_status.to_alipay_dict()
            else:
                params['goal_status'] = self.goal_status
        if self.goal_type:
            if hasattr(self.goal_type, 'to_alipay_dict'):
                params['goal_type'] = self.goal_type.to_alipay_dict()
            else:
                params['goal_type'] = self.goal_type
        if self.goal_value:
            if hasattr(self.goal_value, 'to_alipay_dict'):
                params['goal_value'] = self.goal_value.to_alipay_dict()
            else:
                params['goal_value'] = self.goal_value
        if self.item_no:
            if hasattr(self.item_no, 'to_alipay_dict'):
                params['item_no'] = self.item_no.to_alipay_dict()
            else:
                params['item_no'] = self.item_no
        if self.last_complete_date:
            if hasattr(self.last_complete_date, 'to_alipay_dict'):
                params['last_complete_date'] = self.last_complete_date.to_alipay_dict()
            else:
                params['last_complete_date'] = self.last_complete_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApiContractGoal()
        if 'complete_date' in d:
            o.complete_date = d['complete_date']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'goal_current_value' in d:
            o.goal_current_value = d['goal_current_value']
        if 'goal_key' in d:
            o.goal_key = d['goal_key']
        if 'goal_status' in d:
            o.goal_status = d['goal_status']
        if 'goal_type' in d:
            o.goal_type = d['goal_type']
        if 'goal_value' in d:
            o.goal_value = d['goal_value']
        if 'item_no' in d:
            o.item_no = d['item_no']
        if 'last_complete_date' in d:
            o.last_complete_date = d['last_complete_date']
        return o


