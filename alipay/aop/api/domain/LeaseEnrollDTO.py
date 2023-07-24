#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LeaseEnrollDTO(object):

    def __init__(self):
        self._brand_pid = None
        self._create_time = None
        self._name = None
        self._plan_id = None
        self._status = None

    @property
    def brand_pid(self):
        return self._brand_pid

    @brand_pid.setter
    def brand_pid(self, value):
        self._brand_pid = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_pid:
            if hasattr(self.brand_pid, 'to_alipay_dict'):
                params['brand_pid'] = self.brand_pid.to_alipay_dict()
            else:
                params['brand_pid'] = self.brand_pid
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LeaseEnrollDTO()
        if 'brand_pid' in d:
            o.brand_pid = d['brand_pid']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'name' in d:
            o.name = d['name']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'status' in d:
            o.status = d['status']
        return o


