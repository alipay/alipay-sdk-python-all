#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotAdvertiserAdCreateModel(object):

    def __init__(self):
        self._device_sn_list = None
        self._device_type = None
        self._end_time = None
        self._event = None
        self._material_id = None
        self._plan_name = None
        self._start_time = None

    @property
    def device_sn_list(self):
        return self._device_sn_list

    @device_sn_list.setter
    def device_sn_list(self, value):
        if isinstance(value, list):
            self._device_sn_list = list()
            for i in value:
                self._device_sn_list.append(i)
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value
    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn_list:
            if isinstance(self.device_sn_list, list):
                for i in range(0, len(self.device_sn_list)):
                    element = self.device_sn_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_sn_list[i] = element.to_alipay_dict()
            if hasattr(self.device_sn_list, 'to_alipay_dict'):
                params['device_sn_list'] = self.device_sn_list.to_alipay_dict()
            else:
                params['device_sn_list'] = self.device_sn_list
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.event:
            if hasattr(self.event, 'to_alipay_dict'):
                params['event'] = self.event.to_alipay_dict()
            else:
                params['event'] = self.event
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
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
        o = AlipayCommerceIotAdvertiserAdCreateModel()
        if 'device_sn_list' in d:
            o.device_sn_list = d['device_sn_list']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'event' in d:
            o.event = d['event']
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


