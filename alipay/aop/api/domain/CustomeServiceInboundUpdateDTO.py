#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomeServiceInboundUpdateDTO(object):

    def __init__(self):
        self._action_time = None
        self._channel_id = None
        self._channel_type = None
        self._event_action = None
        self._event_content = None
        self._event_time = None
        self._seat_id = None
        self._seat_type = None
        self._skill_group_id = None
        self._skill_group_type = None
        self._visitor_id = None
        self._visitor_type = None

    @property
    def action_time(self):
        return self._action_time

    @action_time.setter
    def action_time(self, value):
        self._action_time = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
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
    @property
    def skill_group_id(self):
        return self._skill_group_id

    @skill_group_id.setter
    def skill_group_id(self, value):
        self._skill_group_id = value
    @property
    def skill_group_type(self):
        return self._skill_group_type

    @skill_group_type.setter
    def skill_group_type(self, value):
        self._skill_group_type = value
    @property
    def visitor_id(self):
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, value):
        self._visitor_id = value
    @property
    def visitor_type(self):
        return self._visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        self._visitor_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_time:
            if hasattr(self.action_time, 'to_alipay_dict'):
                params['action_time'] = self.action_time.to_alipay_dict()
            else:
                params['action_time'] = self.action_time
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
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
        if self.skill_group_id:
            if hasattr(self.skill_group_id, 'to_alipay_dict'):
                params['skill_group_id'] = self.skill_group_id.to_alipay_dict()
            else:
                params['skill_group_id'] = self.skill_group_id
        if self.skill_group_type:
            if hasattr(self.skill_group_type, 'to_alipay_dict'):
                params['skill_group_type'] = self.skill_group_type.to_alipay_dict()
            else:
                params['skill_group_type'] = self.skill_group_type
        if self.visitor_id:
            if hasattr(self.visitor_id, 'to_alipay_dict'):
                params['visitor_id'] = self.visitor_id.to_alipay_dict()
            else:
                params['visitor_id'] = self.visitor_id
        if self.visitor_type:
            if hasattr(self.visitor_type, 'to_alipay_dict'):
                params['visitor_type'] = self.visitor_type.to_alipay_dict()
            else:
                params['visitor_type'] = self.visitor_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomeServiceInboundUpdateDTO()
        if 'action_time' in d:
            o.action_time = d['action_time']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
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
        if 'skill_group_id' in d:
            o.skill_group_id = d['skill_group_id']
        if 'skill_group_type' in d:
            o.skill_group_type = d['skill_group_type']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        if 'visitor_type' in d:
            o.visitor_type = d['visitor_type']
        return o


