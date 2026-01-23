#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailBenefitwhiteSetModel(object):

    def __init__(self):
        self._activity_id = None
        self._activity_type = None
        self._operator = None
        self._verify_tester_list = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def verify_tester_list(self):
        return self._verify_tester_list

    @verify_tester_list.setter
    def verify_tester_list(self, value):
        if isinstance(value, list):
            self._verify_tester_list = list()
            for i in value:
                self._verify_tester_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.verify_tester_list:
            if isinstance(self.verify_tester_list, list):
                for i in range(0, len(self.verify_tester_list)):
                    element = self.verify_tester_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.verify_tester_list[i] = element.to_alipay_dict()
            if hasattr(self.verify_tester_list, 'to_alipay_dict'):
                params['verify_tester_list'] = self.verify_tester_list.to_alipay_dict()
            else:
                params['verify_tester_list'] = self.verify_tester_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailBenefitwhiteSetModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'operator' in d:
            o.operator = d['operator']
        if 'verify_tester_list' in d:
            o.verify_tester_list = d['verify_tester_list']
        return o


