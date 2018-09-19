#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcoRenthouseRoomInfoList(object):

    def __init__(self):
        self._deposit_end_time = None
        self._ka_room_id = None
        self._room_code = None
        self._room_num = None

    @property
    def deposit_end_time(self):
        return self._deposit_end_time

    @deposit_end_time.setter
    def deposit_end_time(self, value):
        self._deposit_end_time = value
    @property
    def ka_room_id(self):
        return self._ka_room_id

    @ka_room_id.setter
    def ka_room_id(self, value):
        self._ka_room_id = value
    @property
    def room_code(self):
        return self._room_code

    @room_code.setter
    def room_code(self, value):
        self._room_code = value
    @property
    def room_num(self):
        return self._room_num

    @room_num.setter
    def room_num(self, value):
        self._room_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.deposit_end_time:
            if hasattr(self.deposit_end_time, 'to_alipay_dict'):
                params['deposit_end_time'] = self.deposit_end_time.to_alipay_dict()
            else:
                params['deposit_end_time'] = self.deposit_end_time
        if self.ka_room_id:
            if hasattr(self.ka_room_id, 'to_alipay_dict'):
                params['ka_room_id'] = self.ka_room_id.to_alipay_dict()
            else:
                params['ka_room_id'] = self.ka_room_id
        if self.room_code:
            if hasattr(self.room_code, 'to_alipay_dict'):
                params['room_code'] = self.room_code.to_alipay_dict()
            else:
                params['room_code'] = self.room_code
        if self.room_num:
            if hasattr(self.room_num, 'to_alipay_dict'):
                params['room_num'] = self.room_num.to_alipay_dict()
            else:
                params['room_num'] = self.room_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcoRenthouseRoomInfoList()
        if 'deposit_end_time' in d:
            o.deposit_end_time = d['deposit_end_time']
        if 'ka_room_id' in d:
            o.ka_room_id = d['ka_room_id']
        if 'room_code' in d:
            o.room_code = d['room_code']
        if 'room_num' in d:
            o.room_num = d['room_num']
        return o


