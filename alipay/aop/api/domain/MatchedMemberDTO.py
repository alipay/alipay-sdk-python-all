#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MatchedMemberDTO(object):

    def __init__(self):
        self._member_id = None
        self._member_name = None
        self._member_role = None

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def member_name(self):
        return self._member_name

    @member_name.setter
    def member_name(self, value):
        self._member_name = value
    @property
    def member_role(self):
        return self._member_role

    @member_role.setter
    def member_role(self, value):
        self._member_role = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.member_name:
            if hasattr(self.member_name, 'to_alipay_dict'):
                params['member_name'] = self.member_name.to_alipay_dict()
            else:
                params['member_name'] = self.member_name
        if self.member_role:
            if hasattr(self.member_role, 'to_alipay_dict'):
                params['member_role'] = self.member_role.to_alipay_dict()
            else:
                params['member_role'] = self.member_role
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MatchedMemberDTO()
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'member_name' in d:
            o.member_name = d['member_name']
        if 'member_role' in d:
            o.member_role = d['member_role']
        return o


