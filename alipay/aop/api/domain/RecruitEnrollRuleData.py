#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitVoucherRule import RecruitVoucherRule


class RecruitEnrollRuleData(object):

    def __init__(self):
        self._recruit_voucher_rules = None
        self._schema = None

    @property
    def recruit_voucher_rules(self):
        return self._recruit_voucher_rules

    @recruit_voucher_rules.setter
    def recruit_voucher_rules(self, value):
        if isinstance(value, list):
            self._recruit_voucher_rules = list()
            for i in value:
                if isinstance(i, RecruitVoucherRule):
                    self._recruit_voucher_rules.append(i)
                else:
                    self._recruit_voucher_rules.append(RecruitVoucherRule.from_alipay_dict(i))
    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, value):
        self._schema = value


    def to_alipay_dict(self):
        params = dict()
        if self.recruit_voucher_rules:
            if isinstance(self.recruit_voucher_rules, list):
                for i in range(0, len(self.recruit_voucher_rules)):
                    element = self.recruit_voucher_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.recruit_voucher_rules[i] = element.to_alipay_dict()
            if hasattr(self.recruit_voucher_rules, 'to_alipay_dict'):
                params['recruit_voucher_rules'] = self.recruit_voucher_rules.to_alipay_dict()
            else:
                params['recruit_voucher_rules'] = self.recruit_voucher_rules
        if self.schema:
            if hasattr(self.schema, 'to_alipay_dict'):
                params['schema'] = self.schema.to_alipay_dict()
            else:
                params['schema'] = self.schema
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitEnrollRuleData()
        if 'recruit_voucher_rules' in d:
            o.recruit_voucher_rules = d['recruit_voucher_rules']
        if 'schema' in d:
            o.schema = d['schema']
        return o


