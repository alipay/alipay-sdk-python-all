#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceTicketUpdateDTO(object):

    def __init__(self):
        self._action_time = None
        self._event_action = None
        self._event_content = None
        self._event_time = None

    @property
    def action_time(self):
        return self._action_time

    @action_time.setter
    def action_time(self, value):
        self._action_time = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.action_time:
            if hasattr(self.action_time, 'to_alipay_dict'):
                params['action_time'] = self.action_time.to_alipay_dict()
            else:
                params['action_time'] = self.action_time
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceTicketUpdateDTO()
        if 'action_time' in d:
            o.action_time = d['action_time']
        if 'event_action' in d:
            o.event_action = d['event_action']
        if 'event_content' in d:
            o.event_content = d['event_content']
        if 'event_time' in d:
            o.event_time = d['event_time']
        return o


