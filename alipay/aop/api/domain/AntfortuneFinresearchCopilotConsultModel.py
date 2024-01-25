#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchCopilotConsultModel(object):

    def __init__(self):
        self._consult_param = None
        self._consult_type = None
        self._end_date = None
        self._question = None
        self._start_date = None

    @property
    def consult_param(self):
        return self._consult_param

    @consult_param.setter
    def consult_param(self, value):
        self._consult_param = value
    @property
    def consult_type(self):
        return self._consult_type

    @consult_type.setter
    def consult_type(self, value):
        self._consult_type = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_param:
            if hasattr(self.consult_param, 'to_alipay_dict'):
                params['consult_param'] = self.consult_param.to_alipay_dict()
            else:
                params['consult_param'] = self.consult_param
        if self.consult_type:
            if hasattr(self.consult_type, 'to_alipay_dict'):
                params['consult_type'] = self.consult_type.to_alipay_dict()
            else:
                params['consult_type'] = self.consult_type
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchCopilotConsultModel()
        if 'consult_param' in d:
            o.consult_param = d['consult_param']
        if 'consult_type' in d:
            o.consult_type = d['consult_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'question' in d:
            o.question = d['question']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


