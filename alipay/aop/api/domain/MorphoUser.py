#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MorphoUser(object):

    def __init__(self):
        self._id = None
        self._nick = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.nick:
            if hasattr(self.nick, 'to_alipay_dict'):
                params['nick'] = self.nick.to_alipay_dict()
            else:
                params['nick'] = self.nick
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MorphoUser()
        if 'id' in d:
            o.id = d['id']
        if 'nick' in d:
            o.nick = d['nick']
        return o


