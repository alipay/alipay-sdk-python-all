#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LifeServiceRoomInfo(object):

    def __init__(self):
        self._book_end_time = None
        self._book_start_time = None
        self._room_id = None
        self._room_name = None

    @property
    def book_end_time(self):
        return self._book_end_time

    @book_end_time.setter
    def book_end_time(self, value):
        self._book_end_time = value
    @property
    def book_start_time(self):
        return self._book_start_time

    @book_start_time.setter
    def book_start_time(self, value):
        self._book_start_time = value
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
        if self.book_end_time:
            if hasattr(self.book_end_time, 'to_alipay_dict'):
                params['book_end_time'] = self.book_end_time.to_alipay_dict()
            else:
                params['book_end_time'] = self.book_end_time
        if self.book_start_time:
            if hasattr(self.book_start_time, 'to_alipay_dict'):
                params['book_start_time'] = self.book_start_time.to_alipay_dict()
            else:
                params['book_start_time'] = self.book_start_time
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
        o = LifeServiceRoomInfo()
        if 'book_end_time' in d:
            o.book_end_time = d['book_end_time']
        if 'book_start_time' in d:
            o.book_start_time = d['book_start_time']
        if 'room_id' in d:
            o.room_id = d['room_id']
        if 'room_name' in d:
            o.room_name = d['room_name']
        return o


