#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitGradePoint import BenefitGradePoint


class UserInfoAndBenefitQueryResult(object):

    def __init__(self):
        self._balance = None
        self._benefit_info_list = None
        self._grade = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def benefit_info_list(self):
        return self._benefit_info_list

    @benefit_info_list.setter
    def benefit_info_list(self, value):
        if isinstance(value, list):
            self._benefit_info_list = list()
            for i in value:
                if isinstance(i, BenefitGradePoint):
                    self._benefit_info_list.append(i)
                else:
                    self._benefit_info_list.append(BenefitGradePoint.from_alipay_dict(i))
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value


    def to_alipay_dict(self):
        params = dict()
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.benefit_info_list:
            if isinstance(self.benefit_info_list, list):
                for i in range(0, len(self.benefit_info_list)):
                    element = self.benefit_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_info_list[i] = element.to_alipay_dict()
            if hasattr(self.benefit_info_list, 'to_alipay_dict'):
                params['benefit_info_list'] = self.benefit_info_list.to_alipay_dict()
            else:
                params['benefit_info_list'] = self.benefit_info_list
        if self.grade:
            if hasattr(self.grade, 'to_alipay_dict'):
                params['grade'] = self.grade.to_alipay_dict()
            else:
                params['grade'] = self.grade
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserInfoAndBenefitQueryResult()
        if 'balance' in d:
            o.balance = d['balance']
        if 'benefit_info_list' in d:
            o.benefit_info_list = d['benefit_info_list']
        if 'grade' in d:
            o.grade = d['grade']
        return o


