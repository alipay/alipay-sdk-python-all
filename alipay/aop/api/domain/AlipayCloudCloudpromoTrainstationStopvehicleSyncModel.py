#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoTrainstationStopvehicleSyncModel(object):

    def __init__(self):
        self._car_image_url = None
        self._car_number = None
        self._departure_time = None
        self._enter_time = None
        self._floor = None
        self._latitude = None
        self._leave_parking_time = None
        self._longitude = None
        self._parking_lot_name = None
        self._parking_number = None
        self._place_name = None
        self._poi_id = None
        self._status = None
        self._stop_time = None

    @property
    def car_image_url(self):
        return self._car_image_url

    @car_image_url.setter
    def car_image_url(self, value):
        self._car_image_url = value
    @property
    def car_number(self):
        return self._car_number

    @car_number.setter
    def car_number(self, value):
        self._car_number = value
    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value):
        self._departure_time = value
    @property
    def enter_time(self):
        return self._enter_time

    @enter_time.setter
    def enter_time(self, value):
        self._enter_time = value
    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def leave_parking_time(self):
        return self._leave_parking_time

    @leave_parking_time.setter
    def leave_parking_time(self, value):
        self._leave_parking_time = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def parking_lot_name(self):
        return self._parking_lot_name

    @parking_lot_name.setter
    def parking_lot_name(self, value):
        self._parking_lot_name = value
    @property
    def parking_number(self):
        return self._parking_number

    @parking_number.setter
    def parking_number(self, value):
        self._parking_number = value
    @property
    def place_name(self):
        return self._place_name

    @place_name.setter
    def place_name(self, value):
        self._place_name = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def stop_time(self):
        return self._stop_time

    @stop_time.setter
    def stop_time(self, value):
        self._stop_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_image_url:
            if hasattr(self.car_image_url, 'to_alipay_dict'):
                params['car_image_url'] = self.car_image_url.to_alipay_dict()
            else:
                params['car_image_url'] = self.car_image_url
        if self.car_number:
            if hasattr(self.car_number, 'to_alipay_dict'):
                params['car_number'] = self.car_number.to_alipay_dict()
            else:
                params['car_number'] = self.car_number
        if self.departure_time:
            if hasattr(self.departure_time, 'to_alipay_dict'):
                params['departure_time'] = self.departure_time.to_alipay_dict()
            else:
                params['departure_time'] = self.departure_time
        if self.enter_time:
            if hasattr(self.enter_time, 'to_alipay_dict'):
                params['enter_time'] = self.enter_time.to_alipay_dict()
            else:
                params['enter_time'] = self.enter_time
        if self.floor:
            if hasattr(self.floor, 'to_alipay_dict'):
                params['floor'] = self.floor.to_alipay_dict()
            else:
                params['floor'] = self.floor
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.leave_parking_time:
            if hasattr(self.leave_parking_time, 'to_alipay_dict'):
                params['leave_parking_time'] = self.leave_parking_time.to_alipay_dict()
            else:
                params['leave_parking_time'] = self.leave_parking_time
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.parking_lot_name:
            if hasattr(self.parking_lot_name, 'to_alipay_dict'):
                params['parking_lot_name'] = self.parking_lot_name.to_alipay_dict()
            else:
                params['parking_lot_name'] = self.parking_lot_name
        if self.parking_number:
            if hasattr(self.parking_number, 'to_alipay_dict'):
                params['parking_number'] = self.parking_number.to_alipay_dict()
            else:
                params['parking_number'] = self.parking_number
        if self.place_name:
            if hasattr(self.place_name, 'to_alipay_dict'):
                params['place_name'] = self.place_name.to_alipay_dict()
            else:
                params['place_name'] = self.place_name
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.stop_time:
            if hasattr(self.stop_time, 'to_alipay_dict'):
                params['stop_time'] = self.stop_time.to_alipay_dict()
            else:
                params['stop_time'] = self.stop_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoTrainstationStopvehicleSyncModel()
        if 'car_image_url' in d:
            o.car_image_url = d['car_image_url']
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'departure_time' in d:
            o.departure_time = d['departure_time']
        if 'enter_time' in d:
            o.enter_time = d['enter_time']
        if 'floor' in d:
            o.floor = d['floor']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'leave_parking_time' in d:
            o.leave_parking_time = d['leave_parking_time']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'parking_lot_name' in d:
            o.parking_lot_name = d['parking_lot_name']
        if 'parking_number' in d:
            o.parking_number = d['parking_number']
        if 'place_name' in d:
            o.place_name = d['place_name']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        if 'status' in d:
            o.status = d['status']
        if 'stop_time' in d:
            o.stop_time = d['stop_time']
        return o


