#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScopeInfo import ScopeInfo
from alipay.aop.api.domain.ScopeInfo import ScopeInfo
from alipay.aop.api.domain.TakeAwayScopeInfo import TakeAwayScopeInfo


class CateringServiceScopeInfo(object):

    def __init__(self):
        self._pick_up_scope_info = None
        self._queue_scope_info = None
        self._take_away_scope_info = None

    @property
    def pick_up_scope_info(self):
        return self._pick_up_scope_info

    @pick_up_scope_info.setter
    def pick_up_scope_info(self, value):
        if isinstance(value, ScopeInfo):
            self._pick_up_scope_info = value
        else:
            self._pick_up_scope_info = ScopeInfo.from_alipay_dict(value)
    @property
    def queue_scope_info(self):
        return self._queue_scope_info

    @queue_scope_info.setter
    def queue_scope_info(self, value):
        if isinstance(value, ScopeInfo):
            self._queue_scope_info = value
        else:
            self._queue_scope_info = ScopeInfo.from_alipay_dict(value)
    @property
    def take_away_scope_info(self):
        return self._take_away_scope_info

    @take_away_scope_info.setter
    def take_away_scope_info(self, value):
        if isinstance(value, list):
            self._take_away_scope_info = list()
            for i in value:
                if isinstance(i, TakeAwayScopeInfo):
                    self._take_away_scope_info.append(i)
                else:
                    self._take_away_scope_info.append(TakeAwayScopeInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.pick_up_scope_info:
            if hasattr(self.pick_up_scope_info, 'to_alipay_dict'):
                params['pick_up_scope_info'] = self.pick_up_scope_info.to_alipay_dict()
            else:
                params['pick_up_scope_info'] = self.pick_up_scope_info
        if self.queue_scope_info:
            if hasattr(self.queue_scope_info, 'to_alipay_dict'):
                params['queue_scope_info'] = self.queue_scope_info.to_alipay_dict()
            else:
                params['queue_scope_info'] = self.queue_scope_info
        if self.take_away_scope_info:
            if isinstance(self.take_away_scope_info, list):
                for i in range(0, len(self.take_away_scope_info)):
                    element = self.take_away_scope_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.take_away_scope_info[i] = element.to_alipay_dict()
            if hasattr(self.take_away_scope_info, 'to_alipay_dict'):
                params['take_away_scope_info'] = self.take_away_scope_info.to_alipay_dict()
            else:
                params['take_away_scope_info'] = self.take_away_scope_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CateringServiceScopeInfo()
        if 'pick_up_scope_info' in d:
            o.pick_up_scope_info = d['pick_up_scope_info']
        if 'queue_scope_info' in d:
            o.queue_scope_info = d['queue_scope_info']
        if 'take_away_scope_info' in d:
            o.take_away_scope_info = d['take_away_scope_info']
        return o


