#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalInquiryOrderEvaluateInfo(object):

    def __init__(self):
        self._evaluate_content = None
        self._evaluate_label = None
        self._evaluate_score = None
        self._evaluate_time = None
        self._open_status = None

    @property
    def evaluate_content(self):
        return self._evaluate_content

    @evaluate_content.setter
    def evaluate_content(self, value):
        self._evaluate_content = value
    @property
    def evaluate_label(self):
        return self._evaluate_label

    @evaluate_label.setter
    def evaluate_label(self, value):
        self._evaluate_label = value
    @property
    def evaluate_score(self):
        return self._evaluate_score

    @evaluate_score.setter
    def evaluate_score(self, value):
        self._evaluate_score = value
    @property
    def evaluate_time(self):
        return self._evaluate_time

    @evaluate_time.setter
    def evaluate_time(self, value):
        self._evaluate_time = value
    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.evaluate_content:
            if hasattr(self.evaluate_content, 'to_alipay_dict'):
                params['evaluate_content'] = self.evaluate_content.to_alipay_dict()
            else:
                params['evaluate_content'] = self.evaluate_content
        if self.evaluate_label:
            if hasattr(self.evaluate_label, 'to_alipay_dict'):
                params['evaluate_label'] = self.evaluate_label.to_alipay_dict()
            else:
                params['evaluate_label'] = self.evaluate_label
        if self.evaluate_score:
            if hasattr(self.evaluate_score, 'to_alipay_dict'):
                params['evaluate_score'] = self.evaluate_score.to_alipay_dict()
            else:
                params['evaluate_score'] = self.evaluate_score
        if self.evaluate_time:
            if hasattr(self.evaluate_time, 'to_alipay_dict'):
                params['evaluate_time'] = self.evaluate_time.to_alipay_dict()
            else:
                params['evaluate_time'] = self.evaluate_time
        if self.open_status:
            if hasattr(self.open_status, 'to_alipay_dict'):
                params['open_status'] = self.open_status.to_alipay_dict()
            else:
                params['open_status'] = self.open_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalInquiryOrderEvaluateInfo()
        if 'evaluate_content' in d:
            o.evaluate_content = d['evaluate_content']
        if 'evaluate_label' in d:
            o.evaluate_label = d['evaluate_label']
        if 'evaluate_score' in d:
            o.evaluate_score = d['evaluate_score']
        if 'evaluate_time' in d:
            o.evaluate_time = d['evaluate_time']
        if 'open_status' in d:
            o.open_status = d['open_status']
        return o


