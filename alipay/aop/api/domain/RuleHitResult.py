#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HitDialogue import HitDialogue


class RuleHitResult(object):

    def __init__(self):
        self._hit_dialogues = None
        self._notice = None
        self._risk_level = None
        self._rule_code = None

    @property
    def hit_dialogues(self):
        return self._hit_dialogues

    @hit_dialogues.setter
    def hit_dialogues(self, value):
        if isinstance(value, list):
            self._hit_dialogues = list()
            for i in value:
                if isinstance(i, HitDialogue):
                    self._hit_dialogues.append(i)
                else:
                    self._hit_dialogues.append(HitDialogue.from_alipay_dict(i))
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def rule_code(self):
        return self._rule_code

    @rule_code.setter
    def rule_code(self, value):
        self._rule_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.hit_dialogues:
            if isinstance(self.hit_dialogues, list):
                for i in range(0, len(self.hit_dialogues)):
                    element = self.hit_dialogues[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hit_dialogues[i] = element.to_alipay_dict()
            if hasattr(self.hit_dialogues, 'to_alipay_dict'):
                params['hit_dialogues'] = self.hit_dialogues.to_alipay_dict()
            else:
                params['hit_dialogues'] = self.hit_dialogues
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.rule_code:
            if hasattr(self.rule_code, 'to_alipay_dict'):
                params['rule_code'] = self.rule_code.to_alipay_dict()
            else:
                params['rule_code'] = self.rule_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuleHitResult()
        if 'hit_dialogues' in d:
            o.hit_dialogues = d['hit_dialogues']
        if 'notice' in d:
            o.notice = d['notice']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'rule_code' in d:
            o.rule_code = d['rule_code']
        return o


