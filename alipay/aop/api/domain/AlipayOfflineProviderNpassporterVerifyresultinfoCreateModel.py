#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VerifyResultConfig import VerifyResultConfig


class AlipayOfflineProviderNpassporterVerifyresultinfoCreateModel(object):

    def __init__(self):
        self._activity_code = None
        self._solution_code = None
        self._verify_issue_config_list = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value
    @property
    def verify_issue_config_list(self):
        return self._verify_issue_config_list

    @verify_issue_config_list.setter
    def verify_issue_config_list(self, value):
        if isinstance(value, list):
            self._verify_issue_config_list = list()
            for i in value:
                if isinstance(i, VerifyResultConfig):
                    self._verify_issue_config_list.append(i)
                else:
                    self._verify_issue_config_list.append(VerifyResultConfig.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        if self.verify_issue_config_list:
            if isinstance(self.verify_issue_config_list, list):
                for i in range(0, len(self.verify_issue_config_list)):
                    element = self.verify_issue_config_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.verify_issue_config_list[i] = element.to_alipay_dict()
            if hasattr(self.verify_issue_config_list, 'to_alipay_dict'):
                params['verify_issue_config_list'] = self.verify_issue_config_list.to_alipay_dict()
            else:
                params['verify_issue_config_list'] = self.verify_issue_config_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNpassporterVerifyresultinfoCreateModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        if 'verify_issue_config_list' in d:
            o.verify_issue_config_list = d['verify_issue_config_list']
        return o


