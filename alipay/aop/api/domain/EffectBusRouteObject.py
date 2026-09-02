#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EffectBusRouteObject(object):

    def __init__(self):
        self._change_ratio = None
        self._daily_passenger_flow = None
        self._down_direction = None
        self._down_passenger_drop_station = None
        self._passenger_delta = None
        self._rank = None
        self._route_information = None
        self._route_name = None
        self._route_repeat = None
        self._trend_type = None
        self._up_direction = None
        self._up_passenger_drop_station = None

    @property
    def change_ratio(self):
        return self._change_ratio

    @change_ratio.setter
    def change_ratio(self, value):
        self._change_ratio = value
    @property
    def daily_passenger_flow(self):
        return self._daily_passenger_flow

    @daily_passenger_flow.setter
    def daily_passenger_flow(self, value):
        self._daily_passenger_flow = value
    @property
    def down_direction(self):
        return self._down_direction

    @down_direction.setter
    def down_direction(self, value):
        self._down_direction = value
    @property
    def down_passenger_drop_station(self):
        return self._down_passenger_drop_station

    @down_passenger_drop_station.setter
    def down_passenger_drop_station(self, value):
        self._down_passenger_drop_station = value
    @property
    def passenger_delta(self):
        return self._passenger_delta

    @passenger_delta.setter
    def passenger_delta(self, value):
        self._passenger_delta = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def route_information(self):
        return self._route_information

    @route_information.setter
    def route_information(self, value):
        self._route_information = value
    @property
    def route_name(self):
        return self._route_name

    @route_name.setter
    def route_name(self, value):
        self._route_name = value
    @property
    def route_repeat(self):
        return self._route_repeat

    @route_repeat.setter
    def route_repeat(self, value):
        self._route_repeat = value
    @property
    def trend_type(self):
        return self._trend_type

    @trend_type.setter
    def trend_type(self, value):
        self._trend_type = value
    @property
    def up_direction(self):
        return self._up_direction

    @up_direction.setter
    def up_direction(self, value):
        self._up_direction = value
    @property
    def up_passenger_drop_station(self):
        return self._up_passenger_drop_station

    @up_passenger_drop_station.setter
    def up_passenger_drop_station(self, value):
        self._up_passenger_drop_station = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_ratio:
            if hasattr(self.change_ratio, 'to_alipay_dict'):
                params['change_ratio'] = self.change_ratio.to_alipay_dict()
            else:
                params['change_ratio'] = self.change_ratio
        if self.daily_passenger_flow:
            if hasattr(self.daily_passenger_flow, 'to_alipay_dict'):
                params['daily_passenger_flow'] = self.daily_passenger_flow.to_alipay_dict()
            else:
                params['daily_passenger_flow'] = self.daily_passenger_flow
        if self.down_direction:
            if hasattr(self.down_direction, 'to_alipay_dict'):
                params['down_direction'] = self.down_direction.to_alipay_dict()
            else:
                params['down_direction'] = self.down_direction
        if self.down_passenger_drop_station:
            if hasattr(self.down_passenger_drop_station, 'to_alipay_dict'):
                params['down_passenger_drop_station'] = self.down_passenger_drop_station.to_alipay_dict()
            else:
                params['down_passenger_drop_station'] = self.down_passenger_drop_station
        if self.passenger_delta:
            if hasattr(self.passenger_delta, 'to_alipay_dict'):
                params['passenger_delta'] = self.passenger_delta.to_alipay_dict()
            else:
                params['passenger_delta'] = self.passenger_delta
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.route_information:
            if hasattr(self.route_information, 'to_alipay_dict'):
                params['route_information'] = self.route_information.to_alipay_dict()
            else:
                params['route_information'] = self.route_information
        if self.route_name:
            if hasattr(self.route_name, 'to_alipay_dict'):
                params['route_name'] = self.route_name.to_alipay_dict()
            else:
                params['route_name'] = self.route_name
        if self.route_repeat:
            if hasattr(self.route_repeat, 'to_alipay_dict'):
                params['route_repeat'] = self.route_repeat.to_alipay_dict()
            else:
                params['route_repeat'] = self.route_repeat
        if self.trend_type:
            if hasattr(self.trend_type, 'to_alipay_dict'):
                params['trend_type'] = self.trend_type.to_alipay_dict()
            else:
                params['trend_type'] = self.trend_type
        if self.up_direction:
            if hasattr(self.up_direction, 'to_alipay_dict'):
                params['up_direction'] = self.up_direction.to_alipay_dict()
            else:
                params['up_direction'] = self.up_direction
        if self.up_passenger_drop_station:
            if hasattr(self.up_passenger_drop_station, 'to_alipay_dict'):
                params['up_passenger_drop_station'] = self.up_passenger_drop_station.to_alipay_dict()
            else:
                params['up_passenger_drop_station'] = self.up_passenger_drop_station
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EffectBusRouteObject()
        if 'change_ratio' in d:
            o.change_ratio = d['change_ratio']
        if 'daily_passenger_flow' in d:
            o.daily_passenger_flow = d['daily_passenger_flow']
        if 'down_direction' in d:
            o.down_direction = d['down_direction']
        if 'down_passenger_drop_station' in d:
            o.down_passenger_drop_station = d['down_passenger_drop_station']
        if 'passenger_delta' in d:
            o.passenger_delta = d['passenger_delta']
        if 'rank' in d:
            o.rank = d['rank']
        if 'route_information' in d:
            o.route_information = d['route_information']
        if 'route_name' in d:
            o.route_name = d['route_name']
        if 'route_repeat' in d:
            o.route_repeat = d['route_repeat']
        if 'trend_type' in d:
            o.trend_type = d['trend_type']
        if 'up_direction' in d:
            o.up_direction = d['up_direction']
        if 'up_passenger_drop_station' in d:
            o.up_passenger_drop_station = d['up_passenger_drop_station']
        return o


