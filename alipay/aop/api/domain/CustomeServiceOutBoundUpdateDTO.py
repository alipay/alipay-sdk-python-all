#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomeServiceOutBoundUpdateDTO(object):

    def __init__(self):
        self._callee = None
        self._callee_name = None
        self._channel_type = None
        self._event_action = None
        self._event_content = None
        self._event_time = None
        self._seat_id = None
        self._seat_type = None

    @property
    def callee(self):
        return self._callee

    @callee.setter
    def callee(self, value):
        self._callee = value
    @property
    def callee_name(self):
        return self._callee_name

    @callee_name.setter
    def callee_name(self, value):
        self._callee_name = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
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
        if self.callee:
            if hasattr(self.callee, 'to_alipay_dict'):
                params['callee'] = self.callee.to_alipay_dict()
            else:
                params['callee'] = self.callee
        if self.callee_name:
            if hasattr(self.callee_name, 'to_alipay_dict'):
                params['callee_name'] = self.callee_name.to_alipay_dict()
            else:
                params['callee_name'] = self.callee_name
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
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
        o = CustomeServiceOutBoundUpdateDTO()
        if 'callee' in d:
            o.callee = d['callee']
        if 'callee_name' in d:
            o.callee_name = d['callee_name']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
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


