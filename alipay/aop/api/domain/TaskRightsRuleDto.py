#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TaskRightsRuleDynamicAwardConfigDto import TaskRightsRuleDynamicAwardConfigDto


class TaskRightsRuleDto(object):

    def __init__(self):
        self._base_award_count = None
        self._dynamic_award_config = None
        self._rights_id = None
        self._rights_name = None
        self._rule_desc = None
        self._rule_name = None
        self._rule_type = None

    @property
    def base_award_count(self):
        return self._base_award_count

    @base_award_count.setter
    def base_award_count(self, value):
        self._base_award_count = value
    @property
    def dynamic_award_config(self):
        return self._dynamic_award_config

    @dynamic_award_config.setter
    def dynamic_award_config(self, value):
        if isinstance(value, TaskRightsRuleDynamicAwardConfigDto):
            self._dynamic_award_config = value
        else:
            self._dynamic_award_config = TaskRightsRuleDynamicAwardConfigDto.from_alipay_dict(value)
    @property
    def rights_id(self):
        return self._rights_id

    @rights_id.setter
    def rights_id(self, value):
        self._rights_id = value
    @property
    def rights_name(self):
        return self._rights_name

    @rights_name.setter
    def rights_name(self, value):
        self._rights_name = value
    @property
    def rule_desc(self):
        return self._rule_desc

    @rule_desc.setter
    def rule_desc(self, value):
        self._rule_desc = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_award_count:
            if hasattr(self.base_award_count, 'to_alipay_dict'):
                params['base_award_count'] = self.base_award_count.to_alipay_dict()
            else:
                params['base_award_count'] = self.base_award_count
        if self.dynamic_award_config:
            if hasattr(self.dynamic_award_config, 'to_alipay_dict'):
                params['dynamic_award_config'] = self.dynamic_award_config.to_alipay_dict()
            else:
                params['dynamic_award_config'] = self.dynamic_award_config
        if self.rights_id:
            if hasattr(self.rights_id, 'to_alipay_dict'):
                params['rights_id'] = self.rights_id.to_alipay_dict()
            else:
                params['rights_id'] = self.rights_id
        if self.rights_name:
            if hasattr(self.rights_name, 'to_alipay_dict'):
                params['rights_name'] = self.rights_name.to_alipay_dict()
            else:
                params['rights_name'] = self.rights_name
        if self.rule_desc:
            if hasattr(self.rule_desc, 'to_alipay_dict'):
                params['rule_desc'] = self.rule_desc.to_alipay_dict()
            else:
                params['rule_desc'] = self.rule_desc
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskRightsRuleDto()
        if 'base_award_count' in d:
            o.base_award_count = d['base_award_count']
        if 'dynamic_award_config' in d:
            o.dynamic_award_config = d['dynamic_award_config']
        if 'rights_id' in d:
            o.rights_id = d['rights_id']
        if 'rights_name' in d:
            o.rights_name = d['rights_name']
        if 'rule_desc' in d:
            o.rule_desc = d['rule_desc']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        return o


