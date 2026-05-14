#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailTaskSaveModel(object):

    def __init__(self):
        self._base_info = None
        self._benefit = None
        self._bonus_rule = None
        self._completed_rule = None
        self._delivery_rule = None
        self._limit_rule = None
        self._operate_type = None
        self._show_rule = None
        self._task_action = None

    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        self._base_info = value
    @property
    def benefit(self):
        return self._benefit

    @benefit.setter
    def benefit(self, value):
        self._benefit = value
    @property
    def bonus_rule(self):
        return self._bonus_rule

    @bonus_rule.setter
    def bonus_rule(self, value):
        self._bonus_rule = value
    @property
    def completed_rule(self):
        return self._completed_rule

    @completed_rule.setter
    def completed_rule(self, value):
        self._completed_rule = value
    @property
    def delivery_rule(self):
        return self._delivery_rule

    @delivery_rule.setter
    def delivery_rule(self, value):
        self._delivery_rule = value
    @property
    def limit_rule(self):
        return self._limit_rule

    @limit_rule.setter
    def limit_rule(self, value):
        self._limit_rule = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def show_rule(self):
        return self._show_rule

    @show_rule.setter
    def show_rule(self, value):
        self._show_rule = value
    @property
    def task_action(self):
        return self._task_action

    @task_action.setter
    def task_action(self, value):
        self._task_action = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        if self.benefit:
            if hasattr(self.benefit, 'to_alipay_dict'):
                params['benefit'] = self.benefit.to_alipay_dict()
            else:
                params['benefit'] = self.benefit
        if self.bonus_rule:
            if hasattr(self.bonus_rule, 'to_alipay_dict'):
                params['bonus_rule'] = self.bonus_rule.to_alipay_dict()
            else:
                params['bonus_rule'] = self.bonus_rule
        if self.completed_rule:
            if hasattr(self.completed_rule, 'to_alipay_dict'):
                params['completed_rule'] = self.completed_rule.to_alipay_dict()
            else:
                params['completed_rule'] = self.completed_rule
        if self.delivery_rule:
            if hasattr(self.delivery_rule, 'to_alipay_dict'):
                params['delivery_rule'] = self.delivery_rule.to_alipay_dict()
            else:
                params['delivery_rule'] = self.delivery_rule
        if self.limit_rule:
            if hasattr(self.limit_rule, 'to_alipay_dict'):
                params['limit_rule'] = self.limit_rule.to_alipay_dict()
            else:
                params['limit_rule'] = self.limit_rule
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.show_rule:
            if hasattr(self.show_rule, 'to_alipay_dict'):
                params['show_rule'] = self.show_rule.to_alipay_dict()
            else:
                params['show_rule'] = self.show_rule
        if self.task_action:
            if hasattr(self.task_action, 'to_alipay_dict'):
                params['task_action'] = self.task_action.to_alipay_dict()
            else:
                params['task_action'] = self.task_action
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailTaskSaveModel()
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'benefit' in d:
            o.benefit = d['benefit']
        if 'bonus_rule' in d:
            o.bonus_rule = d['bonus_rule']
        if 'completed_rule' in d:
            o.completed_rule = d['completed_rule']
        if 'delivery_rule' in d:
            o.delivery_rule = d['delivery_rule']
        if 'limit_rule' in d:
            o.limit_rule = d['limit_rule']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'show_rule' in d:
            o.show_rule = d['show_rule']
        if 'task_action' in d:
            o.task_action = d['task_action']
        return o


