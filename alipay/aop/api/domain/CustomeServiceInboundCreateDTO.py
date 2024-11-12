#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomeServiceInboundCreateDTO(object):

    def __init__(self):
        self._biz_package_code = None
        self._channel_id = None
        self._channel_type = None
        self._event_action = None
        self._event_content = None
        self._event_time = None
        self._origin_seat_id = None
        self._origin_service_uniq_code = None
        self._phone_number = None
        self._seat_id = None
        self._seat_type = None
        self._service_uniq_code = None
        self._skill_group_id = None
        self._skill_group_type = None
        self._visitor_id = None
        self._visitor_mode = None
        self._visitor_type = None

    @property
    def biz_package_code(self):
        return self._biz_package_code

    @biz_package_code.setter
    def biz_package_code(self, value):
        self._biz_package_code = value
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
    def origin_seat_id(self):
        return self._origin_seat_id

    @origin_seat_id.setter
    def origin_seat_id(self, value):
        self._origin_seat_id = value
    @property
    def origin_service_uniq_code(self):
        return self._origin_service_uniq_code

    @origin_service_uniq_code.setter
    def origin_service_uniq_code(self, value):
        self._origin_service_uniq_code = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
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
    def service_uniq_code(self):
        return self._service_uniq_code

    @service_uniq_code.setter
    def service_uniq_code(self, value):
        self._service_uniq_code = value
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
    def visitor_mode(self):
        return self._visitor_mode

    @visitor_mode.setter
    def visitor_mode(self, value):
        self._visitor_mode = value
    @property
    def visitor_type(self):
        return self._visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        self._visitor_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_package_code:
            if hasattr(self.biz_package_code, 'to_alipay_dict'):
                params['biz_package_code'] = self.biz_package_code.to_alipay_dict()
            else:
                params['biz_package_code'] = self.biz_package_code
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
        if self.origin_seat_id:
            if hasattr(self.origin_seat_id, 'to_alipay_dict'):
                params['origin_seat_id'] = self.origin_seat_id.to_alipay_dict()
            else:
                params['origin_seat_id'] = self.origin_seat_id
        if self.origin_service_uniq_code:
            if hasattr(self.origin_service_uniq_code, 'to_alipay_dict'):
                params['origin_service_uniq_code'] = self.origin_service_uniq_code.to_alipay_dict()
            else:
                params['origin_service_uniq_code'] = self.origin_service_uniq_code
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
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
        if self.service_uniq_code:
            if hasattr(self.service_uniq_code, 'to_alipay_dict'):
                params['service_uniq_code'] = self.service_uniq_code.to_alipay_dict()
            else:
                params['service_uniq_code'] = self.service_uniq_code
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
        if self.visitor_mode:
            if hasattr(self.visitor_mode, 'to_alipay_dict'):
                params['visitor_mode'] = self.visitor_mode.to_alipay_dict()
            else:
                params['visitor_mode'] = self.visitor_mode
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
        o = CustomeServiceInboundCreateDTO()
        if 'biz_package_code' in d:
            o.biz_package_code = d['biz_package_code']
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
        if 'origin_seat_id' in d:
            o.origin_seat_id = d['origin_seat_id']
        if 'origin_service_uniq_code' in d:
            o.origin_service_uniq_code = d['origin_service_uniq_code']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'seat_id' in d:
            o.seat_id = d['seat_id']
        if 'seat_type' in d:
            o.seat_type = d['seat_type']
        if 'service_uniq_code' in d:
            o.service_uniq_code = d['service_uniq_code']
        if 'skill_group_id' in d:
            o.skill_group_id = d['skill_group_id']
        if 'skill_group_type' in d:
            o.skill_group_type = d['skill_group_type']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        if 'visitor_mode' in d:
            o.visitor_mode = d['visitor_mode']
        if 'visitor_type' in d:
            o.visitor_type = d['visitor_type']
        return o


