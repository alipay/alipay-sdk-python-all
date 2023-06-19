#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContactRecord(object):

    def __init__(self):
        self._call_duration = None
        self._call_time = None
        self._callee_mobile = None
        self._caller_mobile = None
        self._pick_up_time = None
        self._status = None

    @property
    def call_duration(self):
        return self._call_duration

    @call_duration.setter
    def call_duration(self, value):
        self._call_duration = value
    @property
    def call_time(self):
        return self._call_time

    @call_time.setter
    def call_time(self, value):
        self._call_time = value
    @property
    def callee_mobile(self):
        return self._callee_mobile

    @callee_mobile.setter
    def callee_mobile(self, value):
        self._callee_mobile = value
    @property
    def caller_mobile(self):
        return self._caller_mobile

    @caller_mobile.setter
    def caller_mobile(self, value):
        self._caller_mobile = value
    @property
    def pick_up_time(self):
        return self._pick_up_time

    @pick_up_time.setter
    def pick_up_time(self, value):
        self._pick_up_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.call_duration:
            if hasattr(self.call_duration, 'to_alipay_dict'):
                params['call_duration'] = self.call_duration.to_alipay_dict()
            else:
                params['call_duration'] = self.call_duration
        if self.call_time:
            if hasattr(self.call_time, 'to_alipay_dict'):
                params['call_time'] = self.call_time.to_alipay_dict()
            else:
                params['call_time'] = self.call_time
        if self.callee_mobile:
            if hasattr(self.callee_mobile, 'to_alipay_dict'):
                params['callee_mobile'] = self.callee_mobile.to_alipay_dict()
            else:
                params['callee_mobile'] = self.callee_mobile
        if self.caller_mobile:
            if hasattr(self.caller_mobile, 'to_alipay_dict'):
                params['caller_mobile'] = self.caller_mobile.to_alipay_dict()
            else:
                params['caller_mobile'] = self.caller_mobile
        if self.pick_up_time:
            if hasattr(self.pick_up_time, 'to_alipay_dict'):
                params['pick_up_time'] = self.pick_up_time.to_alipay_dict()
            else:
                params['pick_up_time'] = self.pick_up_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContactRecord()
        if 'call_duration' in d:
            o.call_duration = d['call_duration']
        if 'call_time' in d:
            o.call_time = d['call_time']
        if 'callee_mobile' in d:
            o.callee_mobile = d['callee_mobile']
        if 'caller_mobile' in d:
            o.caller_mobile = d['caller_mobile']
        if 'pick_up_time' in d:
            o.pick_up_time = d['pick_up_time']
        if 'status' in d:
            o.status = d['status']
        return o


