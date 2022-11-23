#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskFinishLabel import RiskFinishLabel


class RiskFinishInfo(object):

    def __init__(self):
        self._finish_label = None
        self._finish_type = None
        self._task_id = None

    @property
    def finish_label(self):
        return self._finish_label

    @finish_label.setter
    def finish_label(self, value):
        if isinstance(value, list):
            self._finish_label = list()
            for i in value:
                if isinstance(i, RiskFinishLabel):
                    self._finish_label.append(i)
                else:
                    self._finish_label.append(RiskFinishLabel.from_alipay_dict(i))
    @property
    def finish_type(self):
        return self._finish_type

    @finish_type.setter
    def finish_type(self, value):
        self._finish_type = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.finish_label:
            if isinstance(self.finish_label, list):
                for i in range(0, len(self.finish_label)):
                    element = self.finish_label[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.finish_label[i] = element.to_alipay_dict()
            if hasattr(self.finish_label, 'to_alipay_dict'):
                params['finish_label'] = self.finish_label.to_alipay_dict()
            else:
                params['finish_label'] = self.finish_label
        if self.finish_type:
            if hasattr(self.finish_type, 'to_alipay_dict'):
                params['finish_type'] = self.finish_type.to_alipay_dict()
            else:
                params['finish_type'] = self.finish_type
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
        o = RiskFinishInfo()
        if 'finish_label' in d:
            o.finish_label = d['finish_label']
        if 'finish_type' in d:
            o.finish_type = d['finish_type']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


