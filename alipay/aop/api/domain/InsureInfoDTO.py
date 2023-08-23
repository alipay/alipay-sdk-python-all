#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsureInfoDTO(object):

    def __init__(self):
        self._channel = None
        self._event_type = None
        self._job = None
        self._job_level = None
        self._out_employee_id = None
        self._product_plan_id = None
        self._scene_code = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value
    @property
    def job_level(self):
        return self._job_level

    @job_level.setter
    def job_level(self, value):
        self._job_level = value
    @property
    def out_employee_id(self):
        return self._out_employee_id

    @out_employee_id.setter
    def out_employee_id(self, value):
        self._out_employee_id = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.job:
            if hasattr(self.job, 'to_alipay_dict'):
                params['job'] = self.job.to_alipay_dict()
            else:
                params['job'] = self.job
        if self.job_level:
            if hasattr(self.job_level, 'to_alipay_dict'):
                params['job_level'] = self.job_level.to_alipay_dict()
            else:
                params['job_level'] = self.job_level
        if self.out_employee_id:
            if hasattr(self.out_employee_id, 'to_alipay_dict'):
                params['out_employee_id'] = self.out_employee_id.to_alipay_dict()
            else:
                params['out_employee_id'] = self.out_employee_id
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsureInfoDTO()
        if 'channel' in d:
            o.channel = d['channel']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'job' in d:
            o.job = d['job']
        if 'job_level' in d:
            o.job_level = d['job_level']
        if 'out_employee_id' in d:
            o.out_employee_id = d['out_employee_id']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


