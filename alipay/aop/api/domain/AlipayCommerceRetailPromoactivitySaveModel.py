#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailPromoactivitySaveModel(object):

    def __init__(self):
        self._activity_type = None
        self._base_info = None
        self._benefit = None
        self._delivery_rule = None
        self._grant_rule = None
        self._limit_rule = None
        self._operate_type = None
        self._show_rule = None

    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
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
    def delivery_rule(self):
        return self._delivery_rule

    @delivery_rule.setter
    def delivery_rule(self, value):
        self._delivery_rule = value
    @property
    def grant_rule(self):
        return self._grant_rule

    @grant_rule.setter
    def grant_rule(self, value):
        self._grant_rule = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
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
        if self.delivery_rule:
            if hasattr(self.delivery_rule, 'to_alipay_dict'):
                params['delivery_rule'] = self.delivery_rule.to_alipay_dict()
            else:
                params['delivery_rule'] = self.delivery_rule
        if self.grant_rule:
            if hasattr(self.grant_rule, 'to_alipay_dict'):
                params['grant_rule'] = self.grant_rule.to_alipay_dict()
            else:
                params['grant_rule'] = self.grant_rule
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailPromoactivitySaveModel()
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'benefit' in d:
            o.benefit = d['benefit']
        if 'delivery_rule' in d:
            o.delivery_rule = d['delivery_rule']
        if 'grant_rule' in d:
            o.grant_rule = d['grant_rule']
        if 'limit_rule' in d:
            o.limit_rule = d['limit_rule']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'show_rule' in d:
            o.show_rule = d['show_rule']
        return o


