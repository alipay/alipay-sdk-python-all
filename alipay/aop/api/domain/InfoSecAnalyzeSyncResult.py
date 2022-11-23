#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DetectCheckLabel import DetectCheckLabel


class InfoSecAnalyzeSyncResult(object):

    def __init__(self):
        self._data_id = None
        self._detect_check_labels = None
        self._suggestion = None
        self._task_id = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def detect_check_labels(self):
        return self._detect_check_labels

    @detect_check_labels.setter
    def detect_check_labels(self, value):
        if isinstance(value, list):
            self._detect_check_labels = list()
            for i in value:
                if isinstance(i, DetectCheckLabel):
                    self._detect_check_labels.append(i)
                else:
                    self._detect_check_labels.append(DetectCheckLabel.from_alipay_dict(i))
    @property
    def suggestion(self):
        return self._suggestion

    @suggestion.setter
    def suggestion(self, value):
        self._suggestion = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.detect_check_labels:
            if isinstance(self.detect_check_labels, list):
                for i in range(0, len(self.detect_check_labels)):
                    element = self.detect_check_labels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detect_check_labels[i] = element.to_alipay_dict()
            if hasattr(self.detect_check_labels, 'to_alipay_dict'):
                params['detect_check_labels'] = self.detect_check_labels.to_alipay_dict()
            else:
                params['detect_check_labels'] = self.detect_check_labels
        if self.suggestion:
            if hasattr(self.suggestion, 'to_alipay_dict'):
                params['suggestion'] = self.suggestion.to_alipay_dict()
            else:
                params['suggestion'] = self.suggestion
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
        o = InfoSecAnalyzeSyncResult()
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'detect_check_labels' in d:
            o.detect_check_labels = d['detect_check_labels']
        if 'suggestion' in d:
            o.suggestion = d['suggestion']
        if 'task_id' in d:
            o.task_id = d['task_id']
        return o


