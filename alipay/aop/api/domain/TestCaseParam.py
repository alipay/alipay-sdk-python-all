#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TestCaseParam(object):

    def __init__(self):
        self._case_id = None
        self._case_type = None
        self._test_suite_id = None
        self._test_suite_name = None

    @property
    def case_id(self):
        return self._case_id

    @case_id.setter
    def case_id(self, value):
        self._case_id = value
    @property
    def case_type(self):
        return self._case_type

    @case_type.setter
    def case_type(self, value):
        self._case_type = value
    @property
    def test_suite_id(self):
        return self._test_suite_id

    @test_suite_id.setter
    def test_suite_id(self, value):
        self._test_suite_id = value
    @property
    def test_suite_name(self):
        return self._test_suite_name

    @test_suite_name.setter
    def test_suite_name(self, value):
        self._test_suite_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_id:
            if hasattr(self.case_id, 'to_alipay_dict'):
                params['case_id'] = self.case_id.to_alipay_dict()
            else:
                params['case_id'] = self.case_id
        if self.case_type:
            if hasattr(self.case_type, 'to_alipay_dict'):
                params['case_type'] = self.case_type.to_alipay_dict()
            else:
                params['case_type'] = self.case_type
        if self.test_suite_id:
            if hasattr(self.test_suite_id, 'to_alipay_dict'):
                params['test_suite_id'] = self.test_suite_id.to_alipay_dict()
            else:
                params['test_suite_id'] = self.test_suite_id
        if self.test_suite_name:
            if hasattr(self.test_suite_name, 'to_alipay_dict'):
                params['test_suite_name'] = self.test_suite_name.to_alipay_dict()
            else:
                params['test_suite_name'] = self.test_suite_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TestCaseParam()
        if 'case_id' in d:
            o.case_id = d['case_id']
        if 'case_type' in d:
            o.case_type = d['case_type']
        if 'test_suite_id' in d:
            o.test_suite_id = d['test_suite_id']
        if 'test_suite_name' in d:
            o.test_suite_name = d['test_suite_name']
        return o


