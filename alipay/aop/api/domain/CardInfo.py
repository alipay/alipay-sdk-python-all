#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardInfo(object):

    def __init__(self):
        self._taken_time = None
        self._user_name = None

    @property
    def taken_time(self):
        return self._taken_time

    @taken_time.setter
    def taken_time(self, value):
        self._taken_time = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.taken_time:
            if hasattr(self.taken_time, 'to_alipay_dict'):
                params['taken_time'] = self.taken_time.to_alipay_dict()
            else:
                params['taken_time'] = self.taken_time
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardInfo()
        if 'taken_time' in d:
            o.taken_time = d['taken_time']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


