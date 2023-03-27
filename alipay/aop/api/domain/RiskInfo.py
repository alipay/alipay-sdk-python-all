#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskInfoDetail import RiskInfoDetail


class RiskInfo(object):

    def __init__(self):
        self._biz_rule = None
        self._notice = None
        self._risk_info_detail_list = None
        self._risk_level = None
        self._rule_code = None
        self._rule_name = None
        self._rule_robot_status = None

    @property
    def biz_rule(self):
        return self._biz_rule

    @biz_rule.setter
    def biz_rule(self, value):
        self._biz_rule = value
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def risk_info_detail_list(self):
        return self._risk_info_detail_list

    @risk_info_detail_list.setter
    def risk_info_detail_list(self, value):
        if isinstance(value, list):
            self._risk_info_detail_list = list()
            for i in value:
                if isinstance(i, RiskInfoDetail):
                    self._risk_info_detail_list.append(i)
                else:
                    self._risk_info_detail_list.append(RiskInfoDetail.from_alipay_dict(i))
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
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def rule_robot_status(self):
        return self._rule_robot_status

    @rule_robot_status.setter
    def rule_robot_status(self, value):
        self._rule_robot_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_rule:
            if hasattr(self.biz_rule, 'to_alipay_dict'):
                params['biz_rule'] = self.biz_rule.to_alipay_dict()
            else:
                params['biz_rule'] = self.biz_rule
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        if self.risk_info_detail_list:
            if isinstance(self.risk_info_detail_list, list):
                for i in range(0, len(self.risk_info_detail_list)):
                    element = self.risk_info_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_info_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.risk_info_detail_list, 'to_alipay_dict'):
                params['risk_info_detail_list'] = self.risk_info_detail_list.to_alipay_dict()
            else:
                params['risk_info_detail_list'] = self.risk_info_detail_list
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
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.rule_robot_status:
            if hasattr(self.rule_robot_status, 'to_alipay_dict'):
                params['rule_robot_status'] = self.rule_robot_status.to_alipay_dict()
            else:
                params['rule_robot_status'] = self.rule_robot_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskInfo()
        if 'biz_rule' in d:
            o.biz_rule = d['biz_rule']
        if 'notice' in d:
            o.notice = d['notice']
        if 'risk_info_detail_list' in d:
            o.risk_info_detail_list = d['risk_info_detail_list']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'rule_code' in d:
            o.rule_code = d['rule_code']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'rule_robot_status' in d:
            o.rule_robot_status = d['rule_robot_status']
        return o


