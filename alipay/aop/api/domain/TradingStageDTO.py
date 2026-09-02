#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradingStageDTO(object):

    def __init__(self):
        self._begin = None
        self._begin_included = None
        self._end = None
        self._end_included = None
        self._state = None
        self._state_desc = None

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        self._begin = value
    @property
    def begin_included(self):
        return self._begin_included

    @begin_included.setter
    def begin_included(self, value):
        self._begin_included = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def end_included(self):
        return self._end_included

    @end_included.setter
    def end_included(self, value):
        self._end_included = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def state_desc(self):
        return self._state_desc

    @state_desc.setter
    def state_desc(self, value):
        self._state_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin:
            if hasattr(self.begin, 'to_alipay_dict'):
                params['begin'] = self.begin.to_alipay_dict()
            else:
                params['begin'] = self.begin
        if self.begin_included:
            if hasattr(self.begin_included, 'to_alipay_dict'):
                params['begin_included'] = self.begin_included.to_alipay_dict()
            else:
                params['begin_included'] = self.begin_included
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        if self.end_included:
            if hasattr(self.end_included, 'to_alipay_dict'):
                params['end_included'] = self.end_included.to_alipay_dict()
            else:
                params['end_included'] = self.end_included
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.state_desc:
            if hasattr(self.state_desc, 'to_alipay_dict'):
                params['state_desc'] = self.state_desc.to_alipay_dict()
            else:
                params['state_desc'] = self.state_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradingStageDTO()
        if 'begin' in d:
            o.begin = d['begin']
        if 'begin_included' in d:
            o.begin_included = d['begin_included']
        if 'end' in d:
            o.end = d['end']
        if 'end_included' in d:
            o.end_included = d['end_included']
        if 'state' in d:
            o.state = d['state']
        if 'state_desc' in d:
            o.state_desc = d['state_desc']
        return o


