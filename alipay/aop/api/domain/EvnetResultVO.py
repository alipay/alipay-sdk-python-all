#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EventBacktrackingVO import EventBacktrackingVO


class EvnetResultVO(object):

    def __init__(self):
        self._backtrackings = None
        self._create_time = None
        self._event_code = None
        self._event_id = None
        self._remarks = None

    @property
    def backtrackings(self):
        return self._backtrackings

    @backtrackings.setter
    def backtrackings(self, value):
        if isinstance(value, EventBacktrackingVO):
            self._backtrackings = value
        else:
            self._backtrackings = EventBacktrackingVO.from_alipay_dict(value)
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value


    def to_alipay_dict(self):
        params = dict()
        if self.backtrackings:
            if hasattr(self.backtrackings, 'to_alipay_dict'):
                params['backtrackings'] = self.backtrackings.to_alipay_dict()
            else:
                params['backtrackings'] = self.backtrackings
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.event_id:
            if hasattr(self.event_id, 'to_alipay_dict'):
                params['event_id'] = self.event_id.to_alipay_dict()
            else:
                params['event_id'] = self.event_id
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EvnetResultVO()
        if 'backtrackings' in d:
            o.backtrackings = d['backtrackings']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'event_id' in d:
            o.event_id = d['event_id']
        if 'remarks' in d:
            o.remarks = d['remarks']
        return o


