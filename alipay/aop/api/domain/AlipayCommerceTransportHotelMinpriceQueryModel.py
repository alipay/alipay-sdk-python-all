#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportHotelMinpriceQueryModel(object):

    def __init__(self):
        self._arrival_date = None
        self._departure_date = None
        self._hotel_id = None
        self._open_id = None
        self._options = None
        self._room_id = None
        self._user_id = None

    @property
    def arrival_date(self):
        return self._arrival_date

    @arrival_date.setter
    def arrival_date(self, value):
        self._arrival_date = value
    @property
    def departure_date(self):
        return self._departure_date

    @departure_date.setter
    def departure_date(self, value):
        self._departure_date = value
    @property
    def hotel_id(self):
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, value):
        self._hotel_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrival_date:
            if hasattr(self.arrival_date, 'to_alipay_dict'):
                params['arrival_date'] = self.arrival_date.to_alipay_dict()
            else:
                params['arrival_date'] = self.arrival_date
        if self.departure_date:
            if hasattr(self.departure_date, 'to_alipay_dict'):
                params['departure_date'] = self.departure_date.to_alipay_dict()
            else:
                params['departure_date'] = self.departure_date
        if self.hotel_id:
            if hasattr(self.hotel_id, 'to_alipay_dict'):
                params['hotel_id'] = self.hotel_id.to_alipay_dict()
            else:
                params['hotel_id'] = self.hotel_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.options:
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
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
        o = AlipayCommerceTransportHotelMinpriceQueryModel()
        if 'arrival_date' in d:
            o.arrival_date = d['arrival_date']
        if 'departure_date' in d:
            o.departure_date = d['departure_date']
        if 'hotel_id' in d:
            o.hotel_id = d['hotel_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'options' in d:
            o.options = d['options']
        if 'room_id' in d:
            o.room_id = d['room_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


