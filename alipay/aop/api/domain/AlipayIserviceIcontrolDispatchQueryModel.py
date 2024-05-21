#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIcontrolDispatchQueryModel(object):

    def __init__(self):
        self._business_type = None
        self._job_id = None
        self._question_level = None
        self._session_label = None

    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def question_level(self):
        return self._question_level

    @question_level.setter
    def question_level(self, value):
        self._question_level = value
    @property
    def session_label(self):
        return self._session_label

    @session_label.setter
    def session_label(self, value):
        self._session_label = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.question_level:
            if hasattr(self.question_level, 'to_alipay_dict'):
                params['question_level'] = self.question_level.to_alipay_dict()
            else:
                params['question_level'] = self.question_level
        if self.session_label:
            if hasattr(self.session_label, 'to_alipay_dict'):
                params['session_label'] = self.session_label.to_alipay_dict()
            else:
                params['session_label'] = self.session_label
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIcontrolDispatchQueryModel()
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'question_level' in d:
            o.question_level = d['question_level']
        if 'session_label' in d:
            o.session_label = d['session_label']
        return o


