#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YpzSdkPhoneQualityStatDTOOne(object):

    def __init__(self):
        self._event_name = None
        self._event_occur_time = None
        self._event_type = None
        self._medical_institution_name = None
        self._pass_rate = None
        self._problem_count = None
        self._problem_rate = None
        self._total_count = None
        self._uscc = None

    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value
    @property
    def event_occur_time(self):
        return self._event_occur_time

    @event_occur_time.setter
    def event_occur_time(self, value):
        self._event_occur_time = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def medical_institution_name(self):
        return self._medical_institution_name

    @medical_institution_name.setter
    def medical_institution_name(self, value):
        self._medical_institution_name = value
    @property
    def pass_rate(self):
        return self._pass_rate

    @pass_rate.setter
    def pass_rate(self, value):
        self._pass_rate = value
    @property
    def problem_count(self):
        return self._problem_count

    @problem_count.setter
    def problem_count(self, value):
        self._problem_count = value
    @property
    def problem_rate(self):
        return self._problem_rate

    @problem_rate.setter
    def problem_rate(self, value):
        self._problem_rate = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_name:
            if hasattr(self.event_name, 'to_alipay_dict'):
                params['event_name'] = self.event_name.to_alipay_dict()
            else:
                params['event_name'] = self.event_name
        if self.event_occur_time:
            if hasattr(self.event_occur_time, 'to_alipay_dict'):
                params['event_occur_time'] = self.event_occur_time.to_alipay_dict()
            else:
                params['event_occur_time'] = self.event_occur_time
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.medical_institution_name:
            if hasattr(self.medical_institution_name, 'to_alipay_dict'):
                params['medical_institution_name'] = self.medical_institution_name.to_alipay_dict()
            else:
                params['medical_institution_name'] = self.medical_institution_name
        if self.pass_rate:
            if hasattr(self.pass_rate, 'to_alipay_dict'):
                params['pass_rate'] = self.pass_rate.to_alipay_dict()
            else:
                params['pass_rate'] = self.pass_rate
        if self.problem_count:
            if hasattr(self.problem_count, 'to_alipay_dict'):
                params['problem_count'] = self.problem_count.to_alipay_dict()
            else:
                params['problem_count'] = self.problem_count
        if self.problem_rate:
            if hasattr(self.problem_rate, 'to_alipay_dict'):
                params['problem_rate'] = self.problem_rate.to_alipay_dict()
            else:
                params['problem_rate'] = self.problem_rate
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YpzSdkPhoneQualityStatDTOOne()
        if 'event_name' in d:
            o.event_name = d['event_name']
        if 'event_occur_time' in d:
            o.event_occur_time = d['event_occur_time']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'medical_institution_name' in d:
            o.medical_institution_name = d['medical_institution_name']
        if 'pass_rate' in d:
            o.pass_rate = d['pass_rate']
        if 'problem_count' in d:
            o.problem_count = d['problem_count']
        if 'problem_rate' in d:
            o.problem_rate = d['problem_rate']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


