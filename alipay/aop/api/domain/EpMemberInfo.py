#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpMemberInfo(object):

    def __init__(self):
        self._duty = None
        self._member = None

    @property
    def duty(self):
        return self._duty

    @duty.setter
    def duty(self, value):
        self._duty = value
    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, value):
        self._member = value


    def to_alipay_dict(self):
        params = dict()
        if self.duty:
            if hasattr(self.duty, 'to_alipay_dict'):
                params['duty'] = self.duty.to_alipay_dict()
            else:
                params['duty'] = self.duty
        if self.member:
            if hasattr(self.member, 'to_alipay_dict'):
                params['member'] = self.member.to_alipay_dict()
            else:
                params['member'] = self.member
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpMemberInfo()
        if 'duty' in d:
            o.duty = d['duty']
        if 'member' in d:
            o.member = d['member']
        return o


