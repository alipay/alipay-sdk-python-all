#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DoctorDetails(object):

    def __init__(self):
        self._has_enter_room = None
        self._rtc_user_id = None
        self._space_id = None

    @property
    def has_enter_room(self):
        return self._has_enter_room

    @has_enter_room.setter
    def has_enter_room(self, value):
        self._has_enter_room = value
    @property
    def rtc_user_id(self):
        return self._rtc_user_id

    @rtc_user_id.setter
    def rtc_user_id(self, value):
        self._rtc_user_id = value
    @property
    def space_id(self):
        return self._space_id

    @space_id.setter
    def space_id(self, value):
        self._space_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_enter_room:
            if hasattr(self.has_enter_room, 'to_alipay_dict'):
                params['has_enter_room'] = self.has_enter_room.to_alipay_dict()
            else:
                params['has_enter_room'] = self.has_enter_room
        if self.rtc_user_id:
            if hasattr(self.rtc_user_id, 'to_alipay_dict'):
                params['rtc_user_id'] = self.rtc_user_id.to_alipay_dict()
            else:
                params['rtc_user_id'] = self.rtc_user_id
        if self.space_id:
            if hasattr(self.space_id, 'to_alipay_dict'):
                params['space_id'] = self.space_id.to_alipay_dict()
            else:
                params['space_id'] = self.space_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorDetails()
        if 'has_enter_room' in d:
            o.has_enter_room = d['has_enter_room']
        if 'rtc_user_id' in d:
            o.rtc_user_id = d['rtc_user_id']
        if 'space_id' in d:
            o.space_id = d['space_id']
        return o


