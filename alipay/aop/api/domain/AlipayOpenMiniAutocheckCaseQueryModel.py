#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAutocheckCaseQueryModel(object):

    def __init__(self):
        self._case_id = None
        self._case_name = None

    @property
    def case_id(self):
        return self._case_id

    @case_id.setter
    def case_id(self, value):
        self._case_id = value
    @property
    def case_name(self):
        return self._case_name

    @case_name.setter
    def case_name(self, value):
        self._case_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_id:
            if hasattr(self.case_id, 'to_alipay_dict'):
                params['case_id'] = self.case_id.to_alipay_dict()
            else:
                params['case_id'] = self.case_id
        if self.case_name:
            if hasattr(self.case_name, 'to_alipay_dict'):
                params['case_name'] = self.case_name.to_alipay_dict()
            else:
                params['case_name'] = self.case_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAutocheckCaseQueryModel()
        if 'case_id' in d:
            o.case_id = d['case_id']
        if 'case_name' in d:
            o.case_name = d['case_name']
        return o


