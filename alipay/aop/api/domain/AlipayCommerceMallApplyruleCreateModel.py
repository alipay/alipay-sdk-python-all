#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RuleExpireTime import RuleExpireTime
from alipay.aop.api.domain.RuleLimitCreateParams import RuleLimitCreateParams


class AlipayCommerceMallApplyruleCreateModel(object):

    def __init__(self):
        self._mall_id = None
        self._rule_expire_time = None
        self._rule_limit_params = None
        self._rule_name = None
        self._rule_scene = None

    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def rule_expire_time(self):
        return self._rule_expire_time

    @rule_expire_time.setter
    def rule_expire_time(self, value):
        if isinstance(value, RuleExpireTime):
            self._rule_expire_time = value
        else:
            self._rule_expire_time = RuleExpireTime.from_alipay_dict(value)
    @property
    def rule_limit_params(self):
        return self._rule_limit_params

    @rule_limit_params.setter
    def rule_limit_params(self, value):
        if isinstance(value, RuleLimitCreateParams):
            self._rule_limit_params = value
        else:
            self._rule_limit_params = RuleLimitCreateParams.from_alipay_dict(value)
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def rule_scene(self):
        return self._rule_scene

    @rule_scene.setter
    def rule_scene(self, value):
        self._rule_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.rule_expire_time:
            if hasattr(self.rule_expire_time, 'to_alipay_dict'):
                params['rule_expire_time'] = self.rule_expire_time.to_alipay_dict()
            else:
                params['rule_expire_time'] = self.rule_expire_time
        if self.rule_limit_params:
            if hasattr(self.rule_limit_params, 'to_alipay_dict'):
                params['rule_limit_params'] = self.rule_limit_params.to_alipay_dict()
            else:
                params['rule_limit_params'] = self.rule_limit_params
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.rule_scene:
            if hasattr(self.rule_scene, 'to_alipay_dict'):
                params['rule_scene'] = self.rule_scene.to_alipay_dict()
            else:
                params['rule_scene'] = self.rule_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMallApplyruleCreateModel()
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'rule_expire_time' in d:
            o.rule_expire_time = d['rule_expire_time']
        if 'rule_limit_params' in d:
            o.rule_limit_params = d['rule_limit_params']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'rule_scene' in d:
            o.rule_scene = d['rule_scene']
        return o


