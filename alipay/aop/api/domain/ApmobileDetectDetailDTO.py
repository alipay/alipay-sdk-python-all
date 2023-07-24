#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileDetectItemDTO import ApmobileDetectItemDTO


class ApmobileDetectDetailDTO(object):

    def __init__(self):
        self._detect_item_list = None
        self._detect_item_problem_num = None
        self._detect_item_sum = None
        self._detect_item_type = None

    @property
    def detect_item_list(self):
        return self._detect_item_list

    @detect_item_list.setter
    def detect_item_list(self, value):
        if isinstance(value, list):
            self._detect_item_list = list()
            for i in value:
                if isinstance(i, ApmobileDetectItemDTO):
                    self._detect_item_list.append(i)
                else:
                    self._detect_item_list.append(ApmobileDetectItemDTO.from_alipay_dict(i))
    @property
    def detect_item_problem_num(self):
        return self._detect_item_problem_num

    @detect_item_problem_num.setter
    def detect_item_problem_num(self, value):
        self._detect_item_problem_num = value
    @property
    def detect_item_sum(self):
        return self._detect_item_sum

    @detect_item_sum.setter
    def detect_item_sum(self, value):
        self._detect_item_sum = value
    @property
    def detect_item_type(self):
        return self._detect_item_type

    @detect_item_type.setter
    def detect_item_type(self, value):
        self._detect_item_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.detect_item_list:
            if isinstance(self.detect_item_list, list):
                for i in range(0, len(self.detect_item_list)):
                    element = self.detect_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detect_item_list[i] = element.to_alipay_dict()
            if hasattr(self.detect_item_list, 'to_alipay_dict'):
                params['detect_item_list'] = self.detect_item_list.to_alipay_dict()
            else:
                params['detect_item_list'] = self.detect_item_list
        if self.detect_item_problem_num:
            if hasattr(self.detect_item_problem_num, 'to_alipay_dict'):
                params['detect_item_problem_num'] = self.detect_item_problem_num.to_alipay_dict()
            else:
                params['detect_item_problem_num'] = self.detect_item_problem_num
        if self.detect_item_sum:
            if hasattr(self.detect_item_sum, 'to_alipay_dict'):
                params['detect_item_sum'] = self.detect_item_sum.to_alipay_dict()
            else:
                params['detect_item_sum'] = self.detect_item_sum
        if self.detect_item_type:
            if hasattr(self.detect_item_type, 'to_alipay_dict'):
                params['detect_item_type'] = self.detect_item_type.to_alipay_dict()
            else:
                params['detect_item_type'] = self.detect_item_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileDetectDetailDTO()
        if 'detect_item_list' in d:
            o.detect_item_list = d['detect_item_list']
        if 'detect_item_problem_num' in d:
            o.detect_item_problem_num = d['detect_item_problem_num']
        if 'detect_item_sum' in d:
            o.detect_item_sum = d['detect_item_sum']
        if 'detect_item_type' in d:
            o.detect_item_type = d['detect_item_type']
        return o


