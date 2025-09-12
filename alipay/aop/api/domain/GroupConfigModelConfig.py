#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupConfigModelConfig(object):

    def __init__(self):
        self._check_condition = None
        self._need_block_check = None
        self._user_relate_type = None

    @property
    def check_condition(self):
        return self._check_condition

    @check_condition.setter
    def check_condition(self, value):
        if isinstance(value, list):
            self._check_condition = list()
            for i in value:
                self._check_condition.append(i)
    @property
    def need_block_check(self):
        return self._need_block_check

    @need_block_check.setter
    def need_block_check(self, value):
        self._need_block_check = value
    @property
    def user_relate_type(self):
        return self._user_relate_type

    @user_relate_type.setter
    def user_relate_type(self, value):
        self._user_relate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_condition:
            if isinstance(self.check_condition, list):
                for i in range(0, len(self.check_condition)):
                    element = self.check_condition[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_condition[i] = element.to_alipay_dict()
            if hasattr(self.check_condition, 'to_alipay_dict'):
                params['check_condition'] = self.check_condition.to_alipay_dict()
            else:
                params['check_condition'] = self.check_condition
        if self.need_block_check:
            if hasattr(self.need_block_check, 'to_alipay_dict'):
                params['need_block_check'] = self.need_block_check.to_alipay_dict()
            else:
                params['need_block_check'] = self.need_block_check
        if self.user_relate_type:
            if hasattr(self.user_relate_type, 'to_alipay_dict'):
                params['user_relate_type'] = self.user_relate_type.to_alipay_dict()
            else:
                params['user_relate_type'] = self.user_relate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupConfigModelConfig()
        if 'check_condition' in d:
            o.check_condition = d['check_condition']
        if 'need_block_check' in d:
            o.need_block_check = d['need_block_check']
        if 'user_relate_type' in d:
            o.user_relate_type = d['user_relate_type']
        return o


