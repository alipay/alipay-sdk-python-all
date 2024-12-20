#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskDetectionResultOnSubRuleDTO(object):

    def __init__(self):
        self._detection_result_memo = None
        self._need_break = None
        self._risk_judge_sub_rule_id = None
        self._risk_judge_sub_rule_name = None
        self._risk_level = None
        self._risk_rule_id = None
        self._sub_rule_content = None
        self._sub_rule_match_sucess = None

    @property
    def detection_result_memo(self):
        return self._detection_result_memo

    @detection_result_memo.setter
    def detection_result_memo(self, value):
        self._detection_result_memo = value
    @property
    def need_break(self):
        return self._need_break

    @need_break.setter
    def need_break(self, value):
        self._need_break = value
    @property
    def risk_judge_sub_rule_id(self):
        return self._risk_judge_sub_rule_id

    @risk_judge_sub_rule_id.setter
    def risk_judge_sub_rule_id(self, value):
        self._risk_judge_sub_rule_id = value
    @property
    def risk_judge_sub_rule_name(self):
        return self._risk_judge_sub_rule_name

    @risk_judge_sub_rule_name.setter
    def risk_judge_sub_rule_name(self, value):
        self._risk_judge_sub_rule_name = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_rule_id(self):
        return self._risk_rule_id

    @risk_rule_id.setter
    def risk_rule_id(self, value):
        self._risk_rule_id = value
    @property
    def sub_rule_content(self):
        return self._sub_rule_content

    @sub_rule_content.setter
    def sub_rule_content(self, value):
        self._sub_rule_content = value
    @property
    def sub_rule_match_sucess(self):
        return self._sub_rule_match_sucess

    @sub_rule_match_sucess.setter
    def sub_rule_match_sucess(self, value):
        self._sub_rule_match_sucess = value


    def to_alipay_dict(self):
        params = dict()
        if self.detection_result_memo:
            if hasattr(self.detection_result_memo, 'to_alipay_dict'):
                params['detection_result_memo'] = self.detection_result_memo.to_alipay_dict()
            else:
                params['detection_result_memo'] = self.detection_result_memo
        if self.need_break:
            if hasattr(self.need_break, 'to_alipay_dict'):
                params['need_break'] = self.need_break.to_alipay_dict()
            else:
                params['need_break'] = self.need_break
        if self.risk_judge_sub_rule_id:
            if hasattr(self.risk_judge_sub_rule_id, 'to_alipay_dict'):
                params['risk_judge_sub_rule_id'] = self.risk_judge_sub_rule_id.to_alipay_dict()
            else:
                params['risk_judge_sub_rule_id'] = self.risk_judge_sub_rule_id
        if self.risk_judge_sub_rule_name:
            if hasattr(self.risk_judge_sub_rule_name, 'to_alipay_dict'):
                params['risk_judge_sub_rule_name'] = self.risk_judge_sub_rule_name.to_alipay_dict()
            else:
                params['risk_judge_sub_rule_name'] = self.risk_judge_sub_rule_name
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_rule_id:
            if hasattr(self.risk_rule_id, 'to_alipay_dict'):
                params['risk_rule_id'] = self.risk_rule_id.to_alipay_dict()
            else:
                params['risk_rule_id'] = self.risk_rule_id
        if self.sub_rule_content:
            if hasattr(self.sub_rule_content, 'to_alipay_dict'):
                params['sub_rule_content'] = self.sub_rule_content.to_alipay_dict()
            else:
                params['sub_rule_content'] = self.sub_rule_content
        if self.sub_rule_match_sucess:
            if hasattr(self.sub_rule_match_sucess, 'to_alipay_dict'):
                params['sub_rule_match_sucess'] = self.sub_rule_match_sucess.to_alipay_dict()
            else:
                params['sub_rule_match_sucess'] = self.sub_rule_match_sucess
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskDetectionResultOnSubRuleDTO()
        if 'detection_result_memo' in d:
            o.detection_result_memo = d['detection_result_memo']
        if 'need_break' in d:
            o.need_break = d['need_break']
        if 'risk_judge_sub_rule_id' in d:
            o.risk_judge_sub_rule_id = d['risk_judge_sub_rule_id']
        if 'risk_judge_sub_rule_name' in d:
            o.risk_judge_sub_rule_name = d['risk_judge_sub_rule_name']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_rule_id' in d:
            o.risk_rule_id = d['risk_rule_id']
        if 'sub_rule_content' in d:
            o.sub_rule_content = d['sub_rule_content']
        if 'sub_rule_match_sucess' in d:
            o.sub_rule_match_sucess = d['sub_rule_match_sucess']
        return o


