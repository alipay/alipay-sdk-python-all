#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityPeriodInfo(object):

    def __init__(self):
        self._activity_code = None
        self._round_end_time = None
        self._round_id = None
        self._round_name = None
        self._round_start_time = None
        self._sign_up_end_time = None
        self._sign_up_start_time = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def round_end_time(self):
        return self._round_end_time

    @round_end_time.setter
    def round_end_time(self, value):
        self._round_end_time = value
    @property
    def round_id(self):
        return self._round_id

    @round_id.setter
    def round_id(self, value):
        self._round_id = value
    @property
    def round_name(self):
        return self._round_name

    @round_name.setter
    def round_name(self, value):
        self._round_name = value
    @property
    def round_start_time(self):
        return self._round_start_time

    @round_start_time.setter
    def round_start_time(self, value):
        self._round_start_time = value
    @property
    def sign_up_end_time(self):
        return self._sign_up_end_time

    @sign_up_end_time.setter
    def sign_up_end_time(self, value):
        self._sign_up_end_time = value
    @property
    def sign_up_start_time(self):
        return self._sign_up_start_time

    @sign_up_start_time.setter
    def sign_up_start_time(self, value):
        self._sign_up_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.round_end_time:
            if hasattr(self.round_end_time, 'to_alipay_dict'):
                params['round_end_time'] = self.round_end_time.to_alipay_dict()
            else:
                params['round_end_time'] = self.round_end_time
        if self.round_id:
            if hasattr(self.round_id, 'to_alipay_dict'):
                params['round_id'] = self.round_id.to_alipay_dict()
            else:
                params['round_id'] = self.round_id
        if self.round_name:
            if hasattr(self.round_name, 'to_alipay_dict'):
                params['round_name'] = self.round_name.to_alipay_dict()
            else:
                params['round_name'] = self.round_name
        if self.round_start_time:
            if hasattr(self.round_start_time, 'to_alipay_dict'):
                params['round_start_time'] = self.round_start_time.to_alipay_dict()
            else:
                params['round_start_time'] = self.round_start_time
        if self.sign_up_end_time:
            if hasattr(self.sign_up_end_time, 'to_alipay_dict'):
                params['sign_up_end_time'] = self.sign_up_end_time.to_alipay_dict()
            else:
                params['sign_up_end_time'] = self.sign_up_end_time
        if self.sign_up_start_time:
            if hasattr(self.sign_up_start_time, 'to_alipay_dict'):
                params['sign_up_start_time'] = self.sign_up_start_time.to_alipay_dict()
            else:
                params['sign_up_start_time'] = self.sign_up_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityPeriodInfo()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'round_end_time' in d:
            o.round_end_time = d['round_end_time']
        if 'round_id' in d:
            o.round_id = d['round_id']
        if 'round_name' in d:
            o.round_name = d['round_name']
        if 'round_start_time' in d:
            o.round_start_time = d['round_start_time']
        if 'sign_up_end_time' in d:
            o.sign_up_end_time = d['sign_up_end_time']
        if 'sign_up_start_time' in d:
            o.sign_up_start_time = d['sign_up_start_time']
        return o


