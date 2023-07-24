#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApmobileDetectItemProblemDTO import ApmobileDetectItemProblemDTO


class ApmobileAppPermissionReportSummaryDTO(object):

    def __init__(self):
        self._detect_item_evaluate_num = None
        self._detect_item_fail_num = None
        self._detect_item_pass_num = None
        self._detect_item_problem_dtos = None
        self._detect_item_sum = None
        self._detect_item_type_problem_sum = None
        self._detect_item_type_sum = None
        self._task_id = None

    @property
    def detect_item_evaluate_num(self):
        return self._detect_item_evaluate_num

    @detect_item_evaluate_num.setter
    def detect_item_evaluate_num(self, value):
        self._detect_item_evaluate_num = value
    @property
    def detect_item_fail_num(self):
        return self._detect_item_fail_num

    @detect_item_fail_num.setter
    def detect_item_fail_num(self, value):
        self._detect_item_fail_num = value
    @property
    def detect_item_pass_num(self):
        return self._detect_item_pass_num

    @detect_item_pass_num.setter
    def detect_item_pass_num(self, value):
        self._detect_item_pass_num = value
    @property
    def detect_item_problem_dtos(self):
        return self._detect_item_problem_dtos

    @detect_item_problem_dtos.setter
    def detect_item_problem_dtos(self, value):
        if isinstance(value, list):
            self._detect_item_problem_dtos = list()
            for i in value:
                if isinstance(i, ApmobileDetectItemProblemDTO):
                    self._detect_item_problem_dtos.append(i)
                else:
                    self._detect_item_problem_dtos.append(ApmobileDetectItemProblemDTO.from_alipay_dict(i))
    @property
    def detect_item_sum(self):
        return self._detect_item_sum

    @detect_item_sum.setter
    def detect_item_sum(self, value):
        self._detect_item_sum = value
    @property
    def detect_item_type_problem_sum(self):
        return self._detect_item_type_problem_sum

    @detect_item_type_problem_sum.setter
    def detect_item_type_problem_sum(self, value):
        self._detect_item_type_problem_sum = value
    @property
    def detect_item_type_sum(self):
        return self._detect_item_type_sum

    @detect_item_type_sum.setter
    def detect_item_type_sum(self, value):
        self._detect_item_type_sum = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.detect_item_evaluate_num:
            if hasattr(self.detect_item_evaluate_num, 'to_alipay_dict'):
                params['detect_item_evaluate_num'] = self.detect_item_evaluate_num.to_alipay_dict()
            else:
                params['detect_item_evaluate_num'] = self.detect_item_evaluate_num
        if self.detect_item_fail_num:
            if hasattr(self.detect_item_fail_num, 'to_alipay_dict'):
                params['detect_item_fail_num'] = self.detect_item_fail_num.to_alipay_dict()
            else:
                params['detect_item_fail_num'] = self.detect_item_fail_num
        if self.detect_item_pass_num:
            if hasattr(self.detect_item_pass_num, 'to_alipay_dict'):
                params['detect_item_pass_num'] = self.detect_item_pass_num.to_alipay_dict()
            else:
                params['detect_item_pass_num'] = self.detect_item_pass_num
        if self.detect_item_problem_dtos:
            if isinstance(self.detect_item_problem_dtos, list):
                for i in range(0, len(self.detect_item_problem_dtos)):
                    element = self.detect_item_problem_dtos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detect_item_problem_dtos[i] = element.to_alipay_dict()
            if hasattr(self.detect_item_problem_dtos, 'to_alipay_dict'):
                params['detect_item_problem_dtos'] = self.detect_item_problem_dtos.to_alipay_dict()
            else:
                params['detect_item_problem_dtos'] = self.detect_item_problem_dtos
        if self.detect_item_sum:
            if hasattr(self.detect_item_sum, 'to_alipay_dict'):
                params['detect_item_sum'] = self.detect_item_sum.to_alipay_dict()
            else:
                params['detect_item_sum'] = self.detect_item_sum
        if self.detect_item_type_problem_sum:
            if hasattr(self.detect_item_type_problem_sum, 'to_alipay_dict'):
                params['detect_item_type_problem_sum'] = self.detect_item_type_problem_sum.to_alipay_dict()
            else:
                params['detect_item_type_problem_sum'] = self.detect_item_type_problem_sum
        if self.detect_item_type_sum:
            if hasattr(self.detect_item_type_sum, 'to_alipay_dict'):
                params['detect_item_type_sum'] = self.detect_item_type_sum.to_alipay_dict()
            else:
                params['detect_item_type_sum'] = self.detect_item_type_sum
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppPermissionReportSummaryDTO()
        if 'detect_item_evaluate_num' in d:
            o.detect_item_evaluate_num = d['detect_item_evaluate_num']
        if 'detect_item_fail_num' in d:
            o.detect_item_fail_num = d['detect_item_fail_num']
        if 'detect_item_pass_num' in d:
            o.detect_item_pass_num = d['detect_item_pass_num']
        if 'detect_item_problem_dtos' in d:
            o.detect_item_problem_dtos = d['detect_item_problem_dtos']
        if 'detect_item_sum' in d:
            o.detect_item_sum = d['detect_item_sum']
        if 'detect_item_type_problem_sum' in d:
            o.detect_item_type_problem_sum = d['detect_item_type_problem_sum']
        if 'detect_item_type_sum' in d:
            o.detect_item_type_sum = d['detect_item_type_sum']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


