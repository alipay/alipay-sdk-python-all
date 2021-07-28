#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HomeAwayInfo(object):

    def __init__(self):
        self._away = None
        self._home = None

    @property
    def away(self):
        return self._away

    @away.setter
    def away(self, value):
        self._away = value
    @property
    def home(self):
        return self._home

    @home.setter
    def home(self, value):
        self._home = value


    def to_alipay_dict(self):
        params = dict()
        if self.away:
            if hasattr(self.away, 'to_alipay_dict'):
                params['away'] = self.away.to_alipay_dict()
            else:
                params['away'] = self.away
        if self.home:
            if hasattr(self.home, 'to_alipay_dict'):
                params['home'] = self.home.to_alipay_dict()
            else:
                params['home'] = self.home
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HomeAwayInfo()
        if 'away' in d:
            o.away = d['away']
        if 'home' in d:
            o.home = d['home']
        return o


