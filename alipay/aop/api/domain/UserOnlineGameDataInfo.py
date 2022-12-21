#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserOnlineGameDataInfo(object):

    def __init__(self):
        self._end_time = None
        self._out_user_game_no = None
        self._start_time = None
        self._user_data_calory = None
        self._user_data_seconds = None
        self._user_data_speed = None
        self._user_data_sports_type = None
        self._user_data_unit = None
        self._user_data_value = None
        self._user_game_data_id = None
        self._user_game_id = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def out_user_game_no(self):
        return self._out_user_game_no

    @out_user_game_no.setter
    def out_user_game_no(self, value):
        self._out_user_game_no = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def user_data_calory(self):
        return self._user_data_calory

    @user_data_calory.setter
    def user_data_calory(self, value):
        self._user_data_calory = value
    @property
    def user_data_seconds(self):
        return self._user_data_seconds

    @user_data_seconds.setter
    def user_data_seconds(self, value):
        self._user_data_seconds = value
    @property
    def user_data_speed(self):
        return self._user_data_speed

    @user_data_speed.setter
    def user_data_speed(self, value):
        self._user_data_speed = value
    @property
    def user_data_sports_type(self):
        return self._user_data_sports_type

    @user_data_sports_type.setter
    def user_data_sports_type(self, value):
        self._user_data_sports_type = value
    @property
    def user_data_unit(self):
        return self._user_data_unit

    @user_data_unit.setter
    def user_data_unit(self, value):
        self._user_data_unit = value
    @property
    def user_data_value(self):
        return self._user_data_value

    @user_data_value.setter
    def user_data_value(self, value):
        self._user_data_value = value
    @property
    def user_game_data_id(self):
        return self._user_game_data_id

    @user_game_data_id.setter
    def user_game_data_id(self, value):
        self._user_game_data_id = value
    @property
    def user_game_id(self):
        return self._user_game_id

    @user_game_id.setter
    def user_game_id(self, value):
        self._user_game_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.out_user_game_no:
            if hasattr(self.out_user_game_no, 'to_alipay_dict'):
                params['out_user_game_no'] = self.out_user_game_no.to_alipay_dict()
            else:
                params['out_user_game_no'] = self.out_user_game_no
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.user_data_calory:
            if hasattr(self.user_data_calory, 'to_alipay_dict'):
                params['user_data_calory'] = self.user_data_calory.to_alipay_dict()
            else:
                params['user_data_calory'] = self.user_data_calory
        if self.user_data_seconds:
            if hasattr(self.user_data_seconds, 'to_alipay_dict'):
                params['user_data_seconds'] = self.user_data_seconds.to_alipay_dict()
            else:
                params['user_data_seconds'] = self.user_data_seconds
        if self.user_data_speed:
            if hasattr(self.user_data_speed, 'to_alipay_dict'):
                params['user_data_speed'] = self.user_data_speed.to_alipay_dict()
            else:
                params['user_data_speed'] = self.user_data_speed
        if self.user_data_sports_type:
            if hasattr(self.user_data_sports_type, 'to_alipay_dict'):
                params['user_data_sports_type'] = self.user_data_sports_type.to_alipay_dict()
            else:
                params['user_data_sports_type'] = self.user_data_sports_type
        if self.user_data_unit:
            if hasattr(self.user_data_unit, 'to_alipay_dict'):
                params['user_data_unit'] = self.user_data_unit.to_alipay_dict()
            else:
                params['user_data_unit'] = self.user_data_unit
        if self.user_data_value:
            if hasattr(self.user_data_value, 'to_alipay_dict'):
                params['user_data_value'] = self.user_data_value.to_alipay_dict()
            else:
                params['user_data_value'] = self.user_data_value
        if self.user_game_data_id:
            if hasattr(self.user_game_data_id, 'to_alipay_dict'):
                params['user_game_data_id'] = self.user_game_data_id.to_alipay_dict()
            else:
                params['user_game_data_id'] = self.user_game_data_id
        if self.user_game_id:
            if hasattr(self.user_game_id, 'to_alipay_dict'):
                params['user_game_id'] = self.user_game_id.to_alipay_dict()
            else:
                params['user_game_id'] = self.user_game_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserOnlineGameDataInfo()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'out_user_game_no' in d:
            o.out_user_game_no = d['out_user_game_no']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_data_calory' in d:
            o.user_data_calory = d['user_data_calory']
        if 'user_data_seconds' in d:
            o.user_data_seconds = d['user_data_seconds']
        if 'user_data_speed' in d:
            o.user_data_speed = d['user_data_speed']
        if 'user_data_sports_type' in d:
            o.user_data_sports_type = d['user_data_sports_type']
        if 'user_data_unit' in d:
            o.user_data_unit = d['user_data_unit']
        if 'user_data_value' in d:
            o.user_data_value = d['user_data_value']
        if 'user_game_data_id' in d:
            o.user_game_data_id = d['user_game_data_id']
        if 'user_game_id' in d:
            o.user_game_id = d['user_game_id']
        return o


