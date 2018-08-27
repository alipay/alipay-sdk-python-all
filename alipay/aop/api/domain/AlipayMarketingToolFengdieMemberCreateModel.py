#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingToolFengdieMemberCreateModel(object):

    def __init__(self):
        self._nick = None
        self._operator = None
        self._origin_user_id = None
        self._space_id = None

    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def origin_user_id(self):
        return self._origin_user_id

    @origin_user_id.setter
    def origin_user_id(self, value):
        self._origin_user_id = value
    @property
    def space_id(self):
        return self._space_id

    @space_id.setter
    def space_id(self, value):
        self._space_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.nick:
            if hasattr(self.nick, 'to_alipay_dict'):
                params['nick'] = self.nick.to_alipay_dict()
            else:
                params['nick'] = self.nick
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.origin_user_id:
            if hasattr(self.origin_user_id, 'to_alipay_dict'):
                params['origin_user_id'] = self.origin_user_id.to_alipay_dict()
            else:
                params['origin_user_id'] = self.origin_user_id
        if self.space_id:
            if hasattr(self.space_id, 'to_alipay_dict'):
                params['space_id'] = self.space_id.to_alipay_dict()
            else:
                params['space_id'] = self.space_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingToolFengdieMemberCreateModel()
        if 'nick' in d:
            o.nick = d['nick']
        if 'operator' in d:
            o.operator = d['operator']
        if 'origin_user_id' in d:
            o.origin_user_id = d['origin_user_id']
        if 'space_id' in d:
            o.space_id = d['space_id']
        return o


