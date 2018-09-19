#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditUserRoleQueryModel(object):

    def __init__(self):
        self._member = None

    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, value):
        if isinstance(value, Member):
            self._member = value
        else:
            self._member = Member.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
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
        o = MybankCreditUserRoleQueryModel()
        if 'member' in d:
            o.member = d['member']
        return o


