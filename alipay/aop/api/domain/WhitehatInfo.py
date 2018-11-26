#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WhitehatInfo(object):

    def __init__(self):
        self._coin = None
        self._history_coin = None
        self._level = None

    @property
    def coin(self):
        return self._coin

    @coin.setter
    def coin(self, value):
        self._coin = value
    @property
    def history_coin(self):
        return self._history_coin

    @history_coin.setter
    def history_coin(self, value):
        self._history_coin = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value


    def to_alipay_dict(self):
        params = dict()
        if self.coin:
            if hasattr(self.coin, 'to_alipay_dict'):
                params['coin'] = self.coin.to_alipay_dict()
            else:
                params['coin'] = self.coin
        if self.history_coin:
            if hasattr(self.history_coin, 'to_alipay_dict'):
                params['history_coin'] = self.history_coin.to_alipay_dict()
            else:
                params['history_coin'] = self.history_coin
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WhitehatInfo()
        if 'coin' in d:
            o.coin = d['coin']
        if 'history_coin' in d:
            o.history_coin = d['history_coin']
        if 'level' in d:
            o.level = d['level']
        return o


