#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CplifeRoomInfoResp(object):

    def __init__(self):
        self._out_room_id = None
        self._room_id = None

    @property
    def out_room_id(self):
        return self._out_room_id

    @out_room_id.setter
    def out_room_id(self, value):
        self._out_room_id = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_room_id:
            if hasattr(self.out_room_id, 'to_alipay_dict'):
                params['out_room_id'] = self.out_room_id.to_alipay_dict()
            else:
                params['out_room_id'] = self.out_room_id
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CplifeRoomInfoResp()
        if 'out_room_id' in d:
            o.out_room_id = d['out_room_id']
        if 'room_id' in d:
            o.room_id = d['room_id']
        return o


