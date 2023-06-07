#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessInfoRequest(object):

    def __init__(self):
        self._end_time = None
        self._place_name = None
        self._place_type = None
        self._sn = None
        self._start_time = None
        self._url = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def place_name(self):
        return self._place_name

    @place_name.setter
    def place_name(self, value):
        self._place_name = value
    @property
    def place_type(self):
        return self._place_type

    @place_type.setter
    def place_type(self, value):
        self._place_type = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.place_name:
            if hasattr(self.place_name, 'to_alipay_dict'):
                params['place_name'] = self.place_name.to_alipay_dict()
            else:
                params['place_name'] = self.place_name
        if self.place_type:
            if hasattr(self.place_type, 'to_alipay_dict'):
                params['place_type'] = self.place_type.to_alipay_dict()
            else:
                params['place_type'] = self.place_type
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessInfoRequest()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'place_name' in d:
            o.place_name = d['place_name']
        if 'place_type' in d:
            o.place_type = d['place_type']
        if 'sn' in d:
            o.sn = d['sn']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'url' in d:
            o.url = d['url']
        return o


