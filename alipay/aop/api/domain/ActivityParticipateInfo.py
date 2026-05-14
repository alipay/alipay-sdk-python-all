#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityParticipateInfo(object):

    def __init__(self):
        self._activity_code = None
        self._activity_name = None
        self._admited = None
        self._has_sign_up = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def admited(self):
        return self._admited

    @admited.setter
    def admited(self, value):
        self._admited = value
    @property
    def has_sign_up(self):
        return self._has_sign_up

    @has_sign_up.setter
    def has_sign_up(self, value):
        self._has_sign_up = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.admited:
            if hasattr(self.admited, 'to_alipay_dict'):
                params['admited'] = self.admited.to_alipay_dict()
            else:
                params['admited'] = self.admited
        if self.has_sign_up:
            if hasattr(self.has_sign_up, 'to_alipay_dict'):
                params['has_sign_up'] = self.has_sign_up.to_alipay_dict()
            else:
                params['has_sign_up'] = self.has_sign_up
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityParticipateInfo()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'admited' in d:
            o.admited = d['admited']
        if 'has_sign_up' in d:
            o.has_sign_up = d['has_sign_up']
        return o


