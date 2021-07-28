#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RestTime(object):

    def __init__(self):
        self._ext_param = None
        self._rest_end_time = None
        self._rest_spot = None
        self._rest_start_time = None
        self._rest_time = None

    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def rest_end_time(self):
        return self._rest_end_time

    @rest_end_time.setter
    def rest_end_time(self, value):
        self._rest_end_time = value
    @property
    def rest_spot(self):
        return self._rest_spot

    @rest_spot.setter
    def rest_spot(self, value):
        self._rest_spot = value
    @property
    def rest_start_time(self):
        return self._rest_start_time

    @rest_start_time.setter
    def rest_start_time(self, value):
        self._rest_start_time = value
    @property
    def rest_time(self):
        return self._rest_time

    @rest_time.setter
    def rest_time(self, value):
        self._rest_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.rest_end_time:
            if hasattr(self.rest_end_time, 'to_alipay_dict'):
                params['rest_end_time'] = self.rest_end_time.to_alipay_dict()
            else:
                params['rest_end_time'] = self.rest_end_time
        if self.rest_spot:
            if hasattr(self.rest_spot, 'to_alipay_dict'):
                params['rest_spot'] = self.rest_spot.to_alipay_dict()
            else:
                params['rest_spot'] = self.rest_spot
        if self.rest_start_time:
            if hasattr(self.rest_start_time, 'to_alipay_dict'):
                params['rest_start_time'] = self.rest_start_time.to_alipay_dict()
            else:
                params['rest_start_time'] = self.rest_start_time
        if self.rest_time:
            if hasattr(self.rest_time, 'to_alipay_dict'):
                params['rest_time'] = self.rest_time.to_alipay_dict()
            else:
                params['rest_time'] = self.rest_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RestTime()
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'rest_end_time' in d:
            o.rest_end_time = d['rest_end_time']
        if 'rest_spot' in d:
            o.rest_spot = d['rest_spot']
        if 'rest_start_time' in d:
            o.rest_start_time = d['rest_start_time']
        if 'rest_time' in d:
            o.rest_time = d['rest_time']
        return o


