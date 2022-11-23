#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdRisktaskCreateModel(object):

    def __init__(self):
        self._out_biz_id = None
        self._risk_info = None
        self._risk_task_memo = None
        self._task_source = None
        self._task_type = None
        self._tenant = None

    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        self._risk_info = value
    @property
    def risk_task_memo(self):
        return self._risk_task_memo

    @risk_task_memo.setter
    def risk_task_memo(self, value):
        self._risk_task_memo = value
    @property
    def task_source(self):
        return self._task_source

    @task_source.setter
    def task_source(self, value):
        self._task_source = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.risk_info:
            if hasattr(self.risk_info, 'to_alipay_dict'):
                params['risk_info'] = self.risk_info.to_alipay_dict()
            else:
                params['risk_info'] = self.risk_info
        if self.risk_task_memo:
            if hasattr(self.risk_task_memo, 'to_alipay_dict'):
                params['risk_task_memo'] = self.risk_task_memo.to_alipay_dict()
            else:
                params['risk_task_memo'] = self.risk_task_memo
        if self.task_source:
            if hasattr(self.task_source, 'to_alipay_dict'):
                params['task_source'] = self.task_source.to_alipay_dict()
            else:
                params['task_source'] = self.task_source
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdRisktaskCreateModel()
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'risk_info' in d:
            o.risk_info = d['risk_info']
        if 'risk_task_memo' in d:
            o.risk_task_memo = d['risk_task_memo']
        if 'task_source' in d:
            o.task_source = d['task_source']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


