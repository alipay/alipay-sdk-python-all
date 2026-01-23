#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoomDetailInfo import RoomDetailInfo


class RoomInfo(object):

    def __init__(self):
        self._room_detail = None
        self._room_id = None
        self._room_name = None

    @property
    def room_detail(self):
        return self._room_detail

    @room_detail.setter
    def room_detail(self, value):
        if isinstance(value, RoomDetailInfo):
            self._room_detail = value
        else:
            self._room_detail = RoomDetailInfo.from_alipay_dict(value)
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value
    @property
    def room_name(self):
        return self._room_name

    @room_name.setter
    def room_name(self, value):
        self._room_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.room_detail:
            if hasattr(self.room_detail, 'to_alipay_dict'):
                params['room_detail'] = self.room_detail.to_alipay_dict()
            else:
                params['room_detail'] = self.room_detail
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        if self.room_name:
            if hasattr(self.room_name, 'to_alipay_dict'):
                params['room_name'] = self.room_name.to_alipay_dict()
            else:
                params['room_name'] = self.room_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoomInfo()
        if 'room_detail' in d:
            o.room_detail = d['room_detail']
        if 'room_id' in d:
            o.room_id = d['room_id']
        if 'room_name' in d:
            o.room_name = d['room_name']
        return o


