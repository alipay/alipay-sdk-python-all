#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCareerFollowupExecutionQueryModel(object):

    def __init__(self):
        self._execution_no = None
        self._out_biz_no = None

    @property
    def execution_no(self):
        return self._execution_no

    @execution_no.setter
    def execution_no(self, value):
        self._execution_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.execution_no:
            if hasattr(self.execution_no, 'to_alipay_dict'):
                params['execution_no'] = self.execution_no.to_alipay_dict()
            else:
                params['execution_no'] = self.execution_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCareerFollowupExecutionQueryModel()
        if 'execution_no' in d:
            o.execution_no = d['execution_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


