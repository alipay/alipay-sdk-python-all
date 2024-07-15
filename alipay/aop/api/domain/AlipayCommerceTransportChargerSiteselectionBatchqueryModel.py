#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportChargerSiteselectionBatchqueryModel(object):

    def __init__(self):
        self._task_ids = None

    @property
    def task_ids(self):
        return self._task_ids

    @task_ids.setter
    def task_ids(self, value):
        if isinstance(value, list):
            self._task_ids = list()
            for i in value:
                self._task_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.task_ids:
            if isinstance(self.task_ids, list):
                for i in range(0, len(self.task_ids)):
                    element = self.task_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_ids[i] = element.to_alipay_dict()
            if hasattr(self.task_ids, 'to_alipay_dict'):
                params['task_ids'] = self.task_ids.to_alipay_dict()
            else:
                params['task_ids'] = self.task_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportChargerSiteselectionBatchqueryModel()
        if 'task_ids' in d:
            o.task_ids = d['task_ids']
        return o


