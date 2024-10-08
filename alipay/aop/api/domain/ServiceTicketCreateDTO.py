#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceTicketCreateDTO(object):

    def __init__(self):
        self._event_action = None
        self._event_content = None
        self._event_time = None
        self._seat_id = None
        self._seat_type = None

    @property
    def event_action(self):
        return self._event_action

    @event_action.setter
    def event_action(self, value):
        self._event_action = value
    @property
    def event_content(self):
        return self._event_content

    @event_content.setter
    def event_content(self, value):
        self._event_content = value
    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def seat_id(self):
        return self._seat_id

    @seat_id.setter
    def seat_id(self, value):
        self._seat_id = value
    @property
    def seat_type(self):
        return self._seat_type

    @seat_type.setter
    def seat_type(self, value):
        self._seat_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_action:
            if hasattr(self.event_action, 'to_alipay_dict'):
                params['event_action'] = self.event_action.to_alipay_dict()
            else:
                params['event_action'] = self.event_action
        if self.event_content:
            if hasattr(self.event_content, 'to_alipay_dict'):
                params['event_content'] = self.event_content.to_alipay_dict()
            else:
                params['event_content'] = self.event_content
        if self.event_time:
            if hasattr(self.event_time, 'to_alipay_dict'):
                params['event_time'] = self.event_time.to_alipay_dict()
            else:
                params['event_time'] = self.event_time
        if self.seat_id:
            if hasattr(self.seat_id, 'to_alipay_dict'):
                params['seat_id'] = self.seat_id.to_alipay_dict()
            else:
                params['seat_id'] = self.seat_id
        if self.seat_type:
            if hasattr(self.seat_type, 'to_alipay_dict'):
                params['seat_type'] = self.seat_type.to_alipay_dict()
            else:
                params['seat_type'] = self.seat_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceTicketCreateDTO()
        if 'event_action' in d:
            o.event_action = d['event_action']
        if 'event_content' in d:
            o.event_content = d['event_content']
        if 'event_time' in d:
            o.event_time = d['event_time']
        if 'seat_id' in d:
            o.seat_id = d['seat_id']
        if 'seat_type' in d:
            o.seat_type = d['seat_type']
        return o


