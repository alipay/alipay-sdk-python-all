#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VehicleLocationInfo import VehicleLocationInfo


class AlipayCommerceTransportOnlinerideOrderFreezeModel(object):

    def __init__(self):
        self._docking_circle = None
        self._estimated_pickup_time = None
        self._exist_driver = None
        self._order_no = None
        self._pick_up_route_id = None
        self._schedule_id = None
        self._upgrade_status = None
        self._vehicle_distance = None
        self._vehicle_info = None

    @property
    def docking_circle(self):
        return self._docking_circle

    @docking_circle.setter
    def docking_circle(self, value):
        self._docking_circle = value
    @property
    def estimated_pickup_time(self):
        return self._estimated_pickup_time

    @estimated_pickup_time.setter
    def estimated_pickup_time(self, value):
        self._estimated_pickup_time = value
    @property
    def exist_driver(self):
        return self._exist_driver

    @exist_driver.setter
    def exist_driver(self, value):
        self._exist_driver = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pick_up_route_id(self):
        return self._pick_up_route_id

    @pick_up_route_id.setter
    def pick_up_route_id(self, value):
        self._pick_up_route_id = value
    @property
    def schedule_id(self):
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, value):
        self._schedule_id = value
    @property
    def upgrade_status(self):
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, value):
        self._upgrade_status = value
    @property
    def vehicle_distance(self):
        return self._vehicle_distance

    @vehicle_distance.setter
    def vehicle_distance(self, value):
        self._vehicle_distance = value
    @property
    def vehicle_info(self):
        return self._vehicle_info

    @vehicle_info.setter
    def vehicle_info(self, value):
        if isinstance(value, VehicleLocationInfo):
            self._vehicle_info = value
        else:
            self._vehicle_info = VehicleLocationInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.docking_circle:
            if hasattr(self.docking_circle, 'to_alipay_dict'):
                params['docking_circle'] = self.docking_circle.to_alipay_dict()
            else:
                params['docking_circle'] = self.docking_circle
        if self.estimated_pickup_time:
            if hasattr(self.estimated_pickup_time, 'to_alipay_dict'):
                params['estimated_pickup_time'] = self.estimated_pickup_time.to_alipay_dict()
            else:
                params['estimated_pickup_time'] = self.estimated_pickup_time
        if self.exist_driver:
            if hasattr(self.exist_driver, 'to_alipay_dict'):
                params['exist_driver'] = self.exist_driver.to_alipay_dict()
            else:
                params['exist_driver'] = self.exist_driver
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.pick_up_route_id:
            if hasattr(self.pick_up_route_id, 'to_alipay_dict'):
                params['pick_up_route_id'] = self.pick_up_route_id.to_alipay_dict()
            else:
                params['pick_up_route_id'] = self.pick_up_route_id
        if self.schedule_id:
            if hasattr(self.schedule_id, 'to_alipay_dict'):
                params['schedule_id'] = self.schedule_id.to_alipay_dict()
            else:
                params['schedule_id'] = self.schedule_id
        if self.upgrade_status:
            if hasattr(self.upgrade_status, 'to_alipay_dict'):
                params['upgrade_status'] = self.upgrade_status.to_alipay_dict()
            else:
                params['upgrade_status'] = self.upgrade_status
        if self.vehicle_distance:
            if hasattr(self.vehicle_distance, 'to_alipay_dict'):
                params['vehicle_distance'] = self.vehicle_distance.to_alipay_dict()
            else:
                params['vehicle_distance'] = self.vehicle_distance
        if self.vehicle_info:
            if hasattr(self.vehicle_info, 'to_alipay_dict'):
                params['vehicle_info'] = self.vehicle_info.to_alipay_dict()
            else:
                params['vehicle_info'] = self.vehicle_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportOnlinerideOrderFreezeModel()
        if 'docking_circle' in d:
            o.docking_circle = d['docking_circle']
        if 'estimated_pickup_time' in d:
            o.estimated_pickup_time = d['estimated_pickup_time']
        if 'exist_driver' in d:
            o.exist_driver = d['exist_driver']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pick_up_route_id' in d:
            o.pick_up_route_id = d['pick_up_route_id']
        if 'schedule_id' in d:
            o.schedule_id = d['schedule_id']
        if 'upgrade_status' in d:
            o.upgrade_status = d['upgrade_status']
        if 'vehicle_distance' in d:
            o.vehicle_distance = d['vehicle_distance']
        if 'vehicle_info' in d:
            o.vehicle_info = d['vehicle_info']
        return o


