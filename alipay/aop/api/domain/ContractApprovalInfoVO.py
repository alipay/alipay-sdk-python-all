#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractApprovalInfoVO(object):

    def __init__(self):
        self._file_urls = None
        self._node = None
        self._operate_time = None
        self._operator = None
        self._remark = None
        self._result = None

    @property
    def file_urls(self):
        return self._file_urls

    @file_urls.setter
    def file_urls(self, value):
        if isinstance(value, list):
            self._file_urls = list()
            for i in value:
                self._file_urls.append(i)
    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, value):
        self._node = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_urls:
            if isinstance(self.file_urls, list):
                for i in range(0, len(self.file_urls)):
                    element = self.file_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_urls[i] = element.to_alipay_dict()
            if hasattr(self.file_urls, 'to_alipay_dict'):
                params['file_urls'] = self.file_urls.to_alipay_dict()
            else:
                params['file_urls'] = self.file_urls
        if self.node:
            if hasattr(self.node, 'to_alipay_dict'):
                params['node'] = self.node.to_alipay_dict()
            else:
                params['node'] = self.node
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractApprovalInfoVO()
        if 'file_urls' in d:
            o.file_urls = d['file_urls']
        if 'node' in d:
            o.node = d['node']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'operator' in d:
            o.operator = d['operator']
        if 'remark' in d:
            o.remark = d['remark']
        if 'result' in d:
            o.result = d['result']
        return o


