#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommercializationCustomizeRuleReq(object):

    def __init__(self):
        self._attention_level = None
        self._black_list = None
        self._request_id = None
        self._required_list = None
        self._risk_level = None
        self._risk_tips = None
        self._rule_code = None
        self._rule_desc = None
        self._rule_name = None
        self._scene_code = None
        self._white_list = None

    @property
    def attention_level(self):
        return self._attention_level

    @attention_level.setter
    def attention_level(self, value):
        self._attention_level = value
    @property
    def black_list(self):
        return self._black_list

    @black_list.setter
    def black_list(self, value):
        if isinstance(value, list):
            self._black_list = list()
            for i in value:
                self._black_list.append(i)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def required_list(self):
        return self._required_list

    @required_list.setter
    def required_list(self, value):
        if isinstance(value, list):
            self._required_list = list()
            for i in value:
                self._required_list.append(i)
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_tips(self):
        return self._risk_tips

    @risk_tips.setter
    def risk_tips(self, value):
        self._risk_tips = value
    @property
    def rule_code(self):
        return self._rule_code

    @rule_code.setter
    def rule_code(self, value):
        self._rule_code = value
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
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def white_list(self):
        return self._white_list

    @white_list.setter
    def white_list(self, value):
        if isinstance(value, list):
            self._white_list = list()
            for i in value:
                self._white_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.attention_level:
            if hasattr(self.attention_level, 'to_alipay_dict'):
                params['attention_level'] = self.attention_level.to_alipay_dict()
            else:
                params['attention_level'] = self.attention_level
        if self.black_list:
            if isinstance(self.black_list, list):
                for i in range(0, len(self.black_list)):
                    element = self.black_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.black_list[i] = element.to_alipay_dict()
            if hasattr(self.black_list, 'to_alipay_dict'):
                params['black_list'] = self.black_list.to_alipay_dict()
            else:
                params['black_list'] = self.black_list
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.required_list:
            if isinstance(self.required_list, list):
                for i in range(0, len(self.required_list)):
                    element = self.required_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.required_list[i] = element.to_alipay_dict()
            if hasattr(self.required_list, 'to_alipay_dict'):
                params['required_list'] = self.required_list.to_alipay_dict()
            else:
                params['required_list'] = self.required_list
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_tips:
            if hasattr(self.risk_tips, 'to_alipay_dict'):
                params['risk_tips'] = self.risk_tips.to_alipay_dict()
            else:
                params['risk_tips'] = self.risk_tips
        if self.rule_code:
            if hasattr(self.rule_code, 'to_alipay_dict'):
                params['rule_code'] = self.rule_code.to_alipay_dict()
            else:
                params['rule_code'] = self.rule_code
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
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.white_list:
            if isinstance(self.white_list, list):
                for i in range(0, len(self.white_list)):
                    element = self.white_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.white_list[i] = element.to_alipay_dict()
            if hasattr(self.white_list, 'to_alipay_dict'):
                params['white_list'] = self.white_list.to_alipay_dict()
            else:
                params['white_list'] = self.white_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommercializationCustomizeRuleReq()
        if 'attention_level' in d:
            o.attention_level = d['attention_level']
        if 'black_list' in d:
            o.black_list = d['black_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'required_list' in d:
            o.required_list = d['required_list']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_tips' in d:
            o.risk_tips = d['risk_tips']
        if 'rule_code' in d:
            o.rule_code = d['rule_code']
        if 'rule_desc' in d:
            o.rule_desc = d['rule_desc']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'white_list' in d:
            o.white_list = d['white_list']
        return o


