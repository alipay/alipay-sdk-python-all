#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitInfoDTO import BenefitInfoDTO


class AlipayCommerceOperationTaskbenefitcenterTaskCompleteModel(object):

    def __init__(self):
        self._benefit_list = None
        self._task_code = None
        self._task_template_code = None
        self._user_unique_code = None

    @property
    def benefit_list(self):
        return self._benefit_list

    @benefit_list.setter
    def benefit_list(self, value):
        if isinstance(value, list):
            self._benefit_list = list()
            for i in value:
                if isinstance(i, BenefitInfoDTO):
                    self._benefit_list.append(i)
                else:
                    self._benefit_list.append(BenefitInfoDTO.from_alipay_dict(i))
    @property
    def task_code(self):
        return self._task_code

    @task_code.setter
    def task_code(self, value):
        self._task_code = value
    @property
    def task_template_code(self):
        return self._task_template_code

    @task_template_code.setter
    def task_template_code(self, value):
        self._task_template_code = value
    @property
    def user_unique_code(self):
        return self._user_unique_code

    @user_unique_code.setter
    def user_unique_code(self, value):
        self._user_unique_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_list:
            if isinstance(self.benefit_list, list):
                for i in range(0, len(self.benefit_list)):
                    element = self.benefit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_list[i] = element.to_alipay_dict()
            if hasattr(self.benefit_list, 'to_alipay_dict'):
                params['benefit_list'] = self.benefit_list.to_alipay_dict()
            else:
                params['benefit_list'] = self.benefit_list
        if self.task_code:
            if hasattr(self.task_code, 'to_alipay_dict'):
                params['task_code'] = self.task_code.to_alipay_dict()
            else:
                params['task_code'] = self.task_code
        if self.task_template_code:
            if hasattr(self.task_template_code, 'to_alipay_dict'):
                params['task_template_code'] = self.task_template_code.to_alipay_dict()
            else:
                params['task_template_code'] = self.task_template_code
        if self.user_unique_code:
            if hasattr(self.user_unique_code, 'to_alipay_dict'):
                params['user_unique_code'] = self.user_unique_code.to_alipay_dict()
            else:
                params['user_unique_code'] = self.user_unique_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationTaskbenefitcenterTaskCompleteModel()
        if 'benefit_list' in d:
            o.benefit_list = d['benefit_list']
        if 'task_code' in d:
            o.task_code = d['task_code']
        if 'task_template_code' in d:
            o.task_template_code = d['task_template_code']
        if 'user_unique_code' in d:
            o.user_unique_code = d['user_unique_code']
        return o


