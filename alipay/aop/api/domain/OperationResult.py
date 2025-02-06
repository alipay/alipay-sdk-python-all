#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperationResult(object):

    def __init__(self):
        self._failure_count = None
        self._failure_ids = None
        self._success_count = None
        self._success_ids = None

    @property
    def failure_count(self):
        return self._failure_count

    @failure_count.setter
    def failure_count(self, value):
        self._failure_count = value
    @property
    def failure_ids(self):
        return self._failure_ids

    @failure_ids.setter
    def failure_ids(self, value):
        if isinstance(value, list):
            self._failure_ids = list()
            for i in value:
                self._failure_ids.append(i)
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value
    @property
    def success_ids(self):
        return self._success_ids

    @success_ids.setter
    def success_ids(self, value):
        if isinstance(value, list):
            self._success_ids = list()
            for i in value:
                self._success_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.failure_count:
            if hasattr(self.failure_count, 'to_alipay_dict'):
                params['failure_count'] = self.failure_count.to_alipay_dict()
            else:
                params['failure_count'] = self.failure_count
        if self.failure_ids:
            if isinstance(self.failure_ids, list):
                for i in range(0, len(self.failure_ids)):
                    element = self.failure_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.failure_ids[i] = element.to_alipay_dict()
            if hasattr(self.failure_ids, 'to_alipay_dict'):
                params['failure_ids'] = self.failure_ids.to_alipay_dict()
            else:
                params['failure_ids'] = self.failure_ids
        if self.success_count:
            if hasattr(self.success_count, 'to_alipay_dict'):
                params['success_count'] = self.success_count.to_alipay_dict()
            else:
                params['success_count'] = self.success_count
        if self.success_ids:
            if isinstance(self.success_ids, list):
                for i in range(0, len(self.success_ids)):
                    element = self.success_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.success_ids[i] = element.to_alipay_dict()
            if hasattr(self.success_ids, 'to_alipay_dict'):
                params['success_ids'] = self.success_ids.to_alipay_dict()
            else:
                params['success_ids'] = self.success_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperationResult()
        if 'failure_count' in d:
            o.failure_count = d['failure_count']
        if 'failure_ids' in d:
            o.failure_ids = d['failure_ids']
        if 'success_count' in d:
            o.success_count = d['success_count']
        if 'success_ids' in d:
            o.success_ids = d['success_ids']
        return o


