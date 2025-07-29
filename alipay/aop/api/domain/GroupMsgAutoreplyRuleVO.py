#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupMsgAutoreplyActionConfigVO import GroupMsgAutoreplyActionConfigVO
from alipay.aop.api.domain.GroupMsgAutoreplyTriggerRuleVO import GroupMsgAutoreplyTriggerRuleVO


class GroupMsgAutoreplyRuleVO(object):

    def __init__(self):
        self._action_config = None
        self._trigger_rule = None

    @property
    def action_config(self):
        return self._action_config

    @action_config.setter
    def action_config(self, value):
        if isinstance(value, GroupMsgAutoreplyActionConfigVO):
            self._action_config = value
        else:
            self._action_config = GroupMsgAutoreplyActionConfigVO.from_alipay_dict(value)
    @property
    def trigger_rule(self):
        return self._trigger_rule

    @trigger_rule.setter
    def trigger_rule(self, value):
        if isinstance(value, GroupMsgAutoreplyTriggerRuleVO):
            self._trigger_rule = value
        else:
            self._trigger_rule = GroupMsgAutoreplyTriggerRuleVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.action_config:
            if hasattr(self.action_config, 'to_alipay_dict'):
                params['action_config'] = self.action_config.to_alipay_dict()
            else:
                params['action_config'] = self.action_config
        if self.trigger_rule:
            if hasattr(self.trigger_rule, 'to_alipay_dict'):
                params['trigger_rule'] = self.trigger_rule.to_alipay_dict()
            else:
                params['trigger_rule'] = self.trigger_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupMsgAutoreplyRuleVO()
        if 'action_config' in d:
            o.action_config = d['action_config']
        if 'trigger_rule' in d:
            o.trigger_rule = d['trigger_rule']
        return o


