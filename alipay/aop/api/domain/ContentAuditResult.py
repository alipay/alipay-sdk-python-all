#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentRiskInfo import ContentRiskInfo


class ContentAuditResult(object):

    def __init__(self):
        self._content_risk_info_list = None
        self._robot_check_finished = None
        self._robot_status = None
        self._rule_counts = None

    @property
    def content_risk_info_list(self):
        return self._content_risk_info_list

    @content_risk_info_list.setter
    def content_risk_info_list(self, value):
        if isinstance(value, list):
            self._content_risk_info_list = list()
            for i in value:
                if isinstance(i, ContentRiskInfo):
                    self._content_risk_info_list.append(i)
                else:
                    self._content_risk_info_list.append(ContentRiskInfo.from_alipay_dict(i))
    @property
    def robot_check_finished(self):
        return self._robot_check_finished

    @robot_check_finished.setter
    def robot_check_finished(self, value):
        self._robot_check_finished = value
    @property
    def robot_status(self):
        return self._robot_status

    @robot_status.setter
    def robot_status(self, value):
        self._robot_status = value
    @property
    def rule_counts(self):
        return self._rule_counts

    @rule_counts.setter
    def rule_counts(self, value):
        self._rule_counts = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_risk_info_list:
            if isinstance(self.content_risk_info_list, list):
                for i in range(0, len(self.content_risk_info_list)):
                    element = self.content_risk_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_risk_info_list[i] = element.to_alipay_dict()
            if hasattr(self.content_risk_info_list, 'to_alipay_dict'):
                params['content_risk_info_list'] = self.content_risk_info_list.to_alipay_dict()
            else:
                params['content_risk_info_list'] = self.content_risk_info_list
        if self.robot_check_finished:
            if hasattr(self.robot_check_finished, 'to_alipay_dict'):
                params['robot_check_finished'] = self.robot_check_finished.to_alipay_dict()
            else:
                params['robot_check_finished'] = self.robot_check_finished
        if self.robot_status:
            if hasattr(self.robot_status, 'to_alipay_dict'):
                params['robot_status'] = self.robot_status.to_alipay_dict()
            else:
                params['robot_status'] = self.robot_status
        if self.rule_counts:
            if hasattr(self.rule_counts, 'to_alipay_dict'):
                params['rule_counts'] = self.rule_counts.to_alipay_dict()
            else:
                params['rule_counts'] = self.rule_counts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentAuditResult()
        if 'content_risk_info_list' in d:
            o.content_risk_info_list = d['content_risk_info_list']
        if 'robot_check_finished' in d:
            o.robot_check_finished = d['robot_check_finished']
        if 'robot_status' in d:
            o.robot_status = d['robot_status']
        if 'rule_counts' in d:
            o.rule_counts = d['rule_counts']
        return o


