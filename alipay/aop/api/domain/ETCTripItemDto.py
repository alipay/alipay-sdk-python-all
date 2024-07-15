#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ETCTripItemDto(object):

    def __init__(self):
        self._end_station_name = None
        self._end_time = None
        self._item_amount = None
        self._item_category = None
        self._out_trip_id = None
        self._start_station_name = None
        self._start_time = None

    @property
    def end_station_name(self):
        return self._end_station_name

    @end_station_name.setter
    def end_station_name(self, value):
        self._end_station_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def item_amount(self):
        return self._item_amount

    @item_amount.setter
    def item_amount(self, value):
        self._item_amount = value
    @property
    def item_category(self):
        return self._item_category

    @item_category.setter
    def item_category(self, value):
        self._item_category = value
    @property
    def out_trip_id(self):
        return self._out_trip_id

    @out_trip_id.setter
    def out_trip_id(self, value):
        self._out_trip_id = value
    @property
    def start_station_name(self):
        return self._start_station_name

    @start_station_name.setter
    def start_station_name(self, value):
        self._start_station_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_station_name:
            if hasattr(self.end_station_name, 'to_alipay_dict'):
                params['end_station_name'] = self.end_station_name.to_alipay_dict()
            else:
                params['end_station_name'] = self.end_station_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.item_amount:
            if hasattr(self.item_amount, 'to_alipay_dict'):
                params['item_amount'] = self.item_amount.to_alipay_dict()
            else:
                params['item_amount'] = self.item_amount
        if self.item_category:
            if hasattr(self.item_category, 'to_alipay_dict'):
                params['item_category'] = self.item_category.to_alipay_dict()
            else:
                params['item_category'] = self.item_category
        if self.out_trip_id:
            if hasattr(self.out_trip_id, 'to_alipay_dict'):
                params['out_trip_id'] = self.out_trip_id.to_alipay_dict()
            else:
                params['out_trip_id'] = self.out_trip_id
        if self.start_station_name:
            if hasattr(self.start_station_name, 'to_alipay_dict'):
                params['start_station_name'] = self.start_station_name.to_alipay_dict()
            else:
                params['start_station_name'] = self.start_station_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ETCTripItemDto()
        if 'end_station_name' in d:
            o.end_station_name = d['end_station_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'item_amount' in d:
            o.item_amount = d['item_amount']
        if 'item_category' in d:
            o.item_category = d['item_category']
        if 'out_trip_id' in d:
            o.out_trip_id = d['out_trip_id']
        if 'start_station_name' in d:
            o.start_station_name = d['start_station_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


