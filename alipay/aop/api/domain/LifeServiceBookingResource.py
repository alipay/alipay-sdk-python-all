#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LifeServiceBookingResource(object):

    def __init__(self):
        self._booking_end_time = None
        self._booking_start_time = None
        self._out_resource_id = None
        self._resource_id = None
        self._resource_index = None
        self._resource_name = None
        self._resource_type = None

    @property
    def booking_end_time(self):
        return self._booking_end_time

    @booking_end_time.setter
    def booking_end_time(self, value):
        self._booking_end_time = value
    @property
    def booking_start_time(self):
        return self._booking_start_time

    @booking_start_time.setter
    def booking_start_time(self, value):
        self._booking_start_time = value
    @property
    def out_resource_id(self):
        return self._out_resource_id

    @out_resource_id.setter
    def out_resource_id(self, value):
        self._out_resource_id = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def resource_index(self):
        return self._resource_index

    @resource_index.setter
    def resource_index(self, value):
        self._resource_index = value
    @property
    def resource_name(self):
        return self._resource_name

    @resource_name.setter
    def resource_name(self, value):
        self._resource_name = value
    @property
    def resource_type(self):
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value):
        self._resource_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.booking_end_time:
            if hasattr(self.booking_end_time, 'to_alipay_dict'):
                params['booking_end_time'] = self.booking_end_time.to_alipay_dict()
            else:
                params['booking_end_time'] = self.booking_end_time
        if self.booking_start_time:
            if hasattr(self.booking_start_time, 'to_alipay_dict'):
                params['booking_start_time'] = self.booking_start_time.to_alipay_dict()
            else:
                params['booking_start_time'] = self.booking_start_time
        if self.out_resource_id:
            if hasattr(self.out_resource_id, 'to_alipay_dict'):
                params['out_resource_id'] = self.out_resource_id.to_alipay_dict()
            else:
                params['out_resource_id'] = self.out_resource_id
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.resource_index:
            if hasattr(self.resource_index, 'to_alipay_dict'):
                params['resource_index'] = self.resource_index.to_alipay_dict()
            else:
                params['resource_index'] = self.resource_index
        if self.resource_name:
            if hasattr(self.resource_name, 'to_alipay_dict'):
                params['resource_name'] = self.resource_name.to_alipay_dict()
            else:
                params['resource_name'] = self.resource_name
        if self.resource_type:
            if hasattr(self.resource_type, 'to_alipay_dict'):
                params['resource_type'] = self.resource_type.to_alipay_dict()
            else:
                params['resource_type'] = self.resource_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeServiceBookingResource()
        if 'booking_end_time' in d:
            o.booking_end_time = d['booking_end_time']
        if 'booking_start_time' in d:
            o.booking_start_time = d['booking_start_time']
        if 'out_resource_id' in d:
            o.out_resource_id = d['out_resource_id']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'resource_index' in d:
            o.resource_index = d['resource_index']
        if 'resource_name' in d:
            o.resource_name = d['resource_name']
        if 'resource_type' in d:
            o.resource_type = d['resource_type']
        return o


