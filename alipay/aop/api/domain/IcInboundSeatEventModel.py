#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IcInboundSeatEventModel(object):

    def __init__(self):
        self._event_time = None
        self._seat_biz_action = None
        self._seat_current_load = None
        self._seat_id = None
        self._seat_id_type = None
        self._seat_max_load = None
        self._seat_service_status = None
        self._seat_sign_channel = None
        self._service_channel = None
        self._skill_group_id_type = None
        self._skill_group_ids = None
        self._tnt_inst_id = None

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def seat_biz_action(self):
        return self._seat_biz_action

    @seat_biz_action.setter
    def seat_biz_action(self, value):
        self._seat_biz_action = value
    @property
    def seat_current_load(self):
        return self._seat_current_load

    @seat_current_load.setter
    def seat_current_load(self, value):
        self._seat_current_load = value
    @property
    def seat_id(self):
        return self._seat_id

    @seat_id.setter
    def seat_id(self, value):
        self._seat_id = value
    @property
    def seat_id_type(self):
        return self._seat_id_type

    @seat_id_type.setter
    def seat_id_type(self, value):
        self._seat_id_type = value
    @property
    def seat_max_load(self):
        return self._seat_max_load

    @seat_max_load.setter
    def seat_max_load(self, value):
        self._seat_max_load = value
    @property
    def seat_service_status(self):
        return self._seat_service_status

    @seat_service_status.setter
    def seat_service_status(self, value):
        self._seat_service_status = value
    @property
    def seat_sign_channel(self):
        return self._seat_sign_channel

    @seat_sign_channel.setter
    def seat_sign_channel(self, value):
        self._seat_sign_channel = value
    @property
    def service_channel(self):
        return self._service_channel

    @service_channel.setter
    def service_channel(self, value):
        self._service_channel = value
    @property
    def skill_group_id_type(self):
        return self._skill_group_id_type

    @skill_group_id_type.setter
    def skill_group_id_type(self, value):
        self._skill_group_id_type = value
    @property
    def skill_group_ids(self):
        return self._skill_group_ids

    @skill_group_ids.setter
    def skill_group_ids(self, value):
        if isinstance(value, list):
            self._skill_group_ids = list()
            for i in value:
                self._skill_group_ids.append(i)
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_time:
            if hasattr(self.event_time, 'to_alipay_dict'):
                params['event_time'] = self.event_time.to_alipay_dict()
            else:
                params['event_time'] = self.event_time
        if self.seat_biz_action:
            if hasattr(self.seat_biz_action, 'to_alipay_dict'):
                params['seat_biz_action'] = self.seat_biz_action.to_alipay_dict()
            else:
                params['seat_biz_action'] = self.seat_biz_action
        if self.seat_current_load:
            if hasattr(self.seat_current_load, 'to_alipay_dict'):
                params['seat_current_load'] = self.seat_current_load.to_alipay_dict()
            else:
                params['seat_current_load'] = self.seat_current_load
        if self.seat_id:
            if hasattr(self.seat_id, 'to_alipay_dict'):
                params['seat_id'] = self.seat_id.to_alipay_dict()
            else:
                params['seat_id'] = self.seat_id
        if self.seat_id_type:
            if hasattr(self.seat_id_type, 'to_alipay_dict'):
                params['seat_id_type'] = self.seat_id_type.to_alipay_dict()
            else:
                params['seat_id_type'] = self.seat_id_type
        if self.seat_max_load:
            if hasattr(self.seat_max_load, 'to_alipay_dict'):
                params['seat_max_load'] = self.seat_max_load.to_alipay_dict()
            else:
                params['seat_max_load'] = self.seat_max_load
        if self.seat_service_status:
            if hasattr(self.seat_service_status, 'to_alipay_dict'):
                params['seat_service_status'] = self.seat_service_status.to_alipay_dict()
            else:
                params['seat_service_status'] = self.seat_service_status
        if self.seat_sign_channel:
            if hasattr(self.seat_sign_channel, 'to_alipay_dict'):
                params['seat_sign_channel'] = self.seat_sign_channel.to_alipay_dict()
            else:
                params['seat_sign_channel'] = self.seat_sign_channel
        if self.service_channel:
            if hasattr(self.service_channel, 'to_alipay_dict'):
                params['service_channel'] = self.service_channel.to_alipay_dict()
            else:
                params['service_channel'] = self.service_channel
        if self.skill_group_id_type:
            if hasattr(self.skill_group_id_type, 'to_alipay_dict'):
                params['skill_group_id_type'] = self.skill_group_id_type.to_alipay_dict()
            else:
                params['skill_group_id_type'] = self.skill_group_id_type
        if self.skill_group_ids:
            if isinstance(self.skill_group_ids, list):
                for i in range(0, len(self.skill_group_ids)):
                    element = self.skill_group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skill_group_ids[i] = element.to_alipay_dict()
            if hasattr(self.skill_group_ids, 'to_alipay_dict'):
                params['skill_group_ids'] = self.skill_group_ids.to_alipay_dict()
            else:
                params['skill_group_ids'] = self.skill_group_ids
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcInboundSeatEventModel()
        if 'event_time' in d:
            o.event_time = d['event_time']
        if 'seat_biz_action' in d:
            o.seat_biz_action = d['seat_biz_action']
        if 'seat_current_load' in d:
            o.seat_current_load = d['seat_current_load']
        if 'seat_id' in d:
            o.seat_id = d['seat_id']
        if 'seat_id_type' in d:
            o.seat_id_type = d['seat_id_type']
        if 'seat_max_load' in d:
            o.seat_max_load = d['seat_max_load']
        if 'seat_service_status' in d:
            o.seat_service_status = d['seat_service_status']
        if 'seat_sign_channel' in d:
            o.seat_sign_channel = d['seat_sign_channel']
        if 'service_channel' in d:
            o.service_channel = d['service_channel']
        if 'skill_group_id_type' in d:
            o.skill_group_id_type = d['skill_group_id_type']
        if 'skill_group_ids' in d:
            o.skill_group_ids = d['skill_group_ids']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


