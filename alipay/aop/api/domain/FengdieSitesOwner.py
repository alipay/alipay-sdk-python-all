#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FengdieSitesOwner(object):

    def __init__(self):
        self._nick = None
        self._origin_user_id = None

    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value
    @property
    def origin_user_id(self):
        return self._origin_user_id

    @origin_user_id.setter
    def origin_user_id(self, value):
        self._origin_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.nick:
            if hasattr(self.nick, 'to_alipay_dict'):
                params['nick'] = self.nick.to_alipay_dict()
            else:
                params['nick'] = self.nick
        if self.origin_user_id:
            if hasattr(self.origin_user_id, 'to_alipay_dict'):
                params['origin_user_id'] = self.origin_user_id.to_alipay_dict()
            else:
                params['origin_user_id'] = self.origin_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdieSitesOwner()
        if 'nick' in d:
            o.nick = d['nick']
        if 'origin_user_id' in d:
            o.origin_user_id = d['origin_user_id']
        return o


