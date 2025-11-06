#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardPurchaseNotice(object):

    def __init__(self):
        self._max_users_options = None
        self._max_users_value = None
        self._reserve_rules_options = None
        self._reserve_rules_value = None
        self._target_users_options = None

    @property
    def max_users_options(self):
        return self._max_users_options

    @max_users_options.setter
    def max_users_options(self, value):
        self._max_users_options = value
    @property
    def max_users_value(self):
        return self._max_users_value

    @max_users_value.setter
    def max_users_value(self, value):
        self._max_users_value = value
    @property
    def reserve_rules_options(self):
        return self._reserve_rules_options

    @reserve_rules_options.setter
    def reserve_rules_options(self, value):
        self._reserve_rules_options = value
    @property
    def reserve_rules_value(self):
        return self._reserve_rules_value

    @reserve_rules_value.setter
    def reserve_rules_value(self, value):
        self._reserve_rules_value = value
    @property
    def target_users_options(self):
        return self._target_users_options

    @target_users_options.setter
    def target_users_options(self, value):
        self._target_users_options = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_users_options:
            if hasattr(self.max_users_options, 'to_alipay_dict'):
                params['max_users_options'] = self.max_users_options.to_alipay_dict()
            else:
                params['max_users_options'] = self.max_users_options
        if self.max_users_value:
            if hasattr(self.max_users_value, 'to_alipay_dict'):
                params['max_users_value'] = self.max_users_value.to_alipay_dict()
            else:
                params['max_users_value'] = self.max_users_value
        if self.reserve_rules_options:
            if hasattr(self.reserve_rules_options, 'to_alipay_dict'):
                params['reserve_rules_options'] = self.reserve_rules_options.to_alipay_dict()
            else:
                params['reserve_rules_options'] = self.reserve_rules_options
        if self.reserve_rules_value:
            if hasattr(self.reserve_rules_value, 'to_alipay_dict'):
                params['reserve_rules_value'] = self.reserve_rules_value.to_alipay_dict()
            else:
                params['reserve_rules_value'] = self.reserve_rules_value
        if self.target_users_options:
            if hasattr(self.target_users_options, 'to_alipay_dict'):
                params['target_users_options'] = self.target_users_options.to_alipay_dict()
            else:
                params['target_users_options'] = self.target_users_options
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardPurchaseNotice()
        if 'max_users_options' in d:
            o.max_users_options = d['max_users_options']
        if 'max_users_value' in d:
            o.max_users_value = d['max_users_value']
        if 'reserve_rules_options' in d:
            o.reserve_rules_options = d['reserve_rules_options']
        if 'reserve_rules_value' in d:
            o.reserve_rules_value = d['reserve_rules_value']
        if 'target_users_options' in d:
            o.target_users_options = d['target_users_options']
        return o


