#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataBillEreceiptagentApplyModel(object):

    def __init__(self):
        self._agreement_no = None
        self._agreement_type = None
        self._end_time = None
        self._key = None
        self._start_time = None
        self._type = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_type(self):
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, value):
        self._agreement_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.agreement_type:
            if hasattr(self.agreement_type, 'to_alipay_dict'):
                params['agreement_type'] = self.agreement_type.to_alipay_dict()
            else:
                params['agreement_type'] = self.agreement_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataBillEreceiptagentApplyModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_type' in d:
            o.agreement_type = d['agreement_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'key' in d:
            o.key = d['key']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'type' in d:
            o.type = d['type']
        return o


