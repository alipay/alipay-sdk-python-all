#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SnsTradeDataResult(object):

    def __init__(self):
        self._ch_info = None
        self._trd_count = None

    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def trd_count(self):
        return self._trd_count

    @trd_count.setter
    def trd_count(self, value):
        self._trd_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.trd_count:
            if hasattr(self.trd_count, 'to_alipay_dict'):
                params['trd_count'] = self.trd_count.to_alipay_dict()
            else:
                params['trd_count'] = self.trd_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SnsTradeDataResult()
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'trd_count' in d:
            o.trd_count = d['trd_count']
        return o


