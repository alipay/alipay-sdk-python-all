#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsOnlinegameUsergamedataSyncModel(object):

    def __init__(self):
        self._end_time = None
        self._open_id = None
        self._out_user_game_no = None
        self._start_time = None
        self._user_game_id = None
        self._user_id = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def user_game_id(self):
        return self._user_game_id

    @user_game_id.setter
    def user_game_id(self, value):
        self._user_game_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if self.user_game_id:
            if hasattr(self.user_game_id, 'to_alipay_dict'):
                params['user_game_id'] = self.user_game_id.to_alipay_dict()
            else:
                params['user_game_id'] = self.user_game_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsOnlinegameUsergamedataSyncModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_user_game_no' in d:
            o.out_user_game_no = d['out_user_game_no']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_game_id' in d:
            o.user_game_id = d['user_game_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


