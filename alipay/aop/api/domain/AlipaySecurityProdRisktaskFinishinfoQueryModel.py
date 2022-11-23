#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdRisktaskFinishinfoQueryModel(object):

    def __init__(self):
        self._task_id_list = None

    @property
    def task_id_list(self):
        return self._task_id_list

    @task_id_list.setter
    def task_id_list(self, value):
        if isinstance(value, list):
            self._task_id_list = list()
            for i in value:
                self._task_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.task_id_list:
            if isinstance(self.task_id_list, list):
                for i in range(0, len(self.task_id_list)):
                    element = self.task_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_id_list[i] = element.to_alipay_dict()
            if hasattr(self.task_id_list, 'to_alipay_dict'):
                params['task_id_list'] = self.task_id_list.to_alipay_dict()
            else:
                params['task_id_list'] = self.task_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdRisktaskFinishinfoQueryModel()
        if 'task_id_list' in d:
            o.task_id_list = d['task_id_list']
        return o


