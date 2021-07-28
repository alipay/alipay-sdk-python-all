#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceDmpserviceCreateModel(object):

    def __init__(self):
        self._conversion_id = None
        self._conversion_time = None
        self._conversion_type = None
        self._device_id = None
        self._device_type = None
        self._event_type = None
        self._ext_info = None
        self._is_conversion = None
        self._request_id = None
        self._source = None
        self._track_url = None
        self._user_id = None

    @property
    def conversion_id(self):
        return self._conversion_id

    @conversion_id.setter
    def conversion_id(self, value):
        self._conversion_id = value
    @property
    def conversion_time(self):
        return self._conversion_time

    @conversion_time.setter
    def conversion_time(self, value):
        self._conversion_time = value
    @property
    def conversion_type(self):
        return self._conversion_type

    @conversion_type.setter
    def conversion_type(self, value):
        self._conversion_type = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def is_conversion(self):
        return self._is_conversion

    @is_conversion.setter
    def is_conversion(self, value):
        self._is_conversion = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def track_url(self):
        return self._track_url

    @track_url.setter
    def track_url(self, value):
        self._track_url = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.conversion_id:
            if hasattr(self.conversion_id, 'to_alipay_dict'):
                params['conversion_id'] = self.conversion_id.to_alipay_dict()
            else:
                params['conversion_id'] = self.conversion_id
        if self.conversion_time:
            if hasattr(self.conversion_time, 'to_alipay_dict'):
                params['conversion_time'] = self.conversion_time.to_alipay_dict()
            else:
                params['conversion_time'] = self.conversion_time
        if self.conversion_type:
            if hasattr(self.conversion_type, 'to_alipay_dict'):
                params['conversion_type'] = self.conversion_type.to_alipay_dict()
            else:
                params['conversion_type'] = self.conversion_type
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.is_conversion:
            if hasattr(self.is_conversion, 'to_alipay_dict'):
                params['is_conversion'] = self.is_conversion.to_alipay_dict()
            else:
                params['is_conversion'] = self.is_conversion
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.track_url:
            if hasattr(self.track_url, 'to_alipay_dict'):
                params['track_url'] = self.track_url.to_alipay_dict()
            else:
                params['track_url'] = self.track_url
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDmpserviceCreateModel()
        if 'conversion_id' in d:
            o.conversion_id = d['conversion_id']
        if 'conversion_time' in d:
            o.conversion_time = d['conversion_time']
        if 'conversion_type' in d:
            o.conversion_type = d['conversion_type']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'is_conversion' in d:
            o.is_conversion = d['is_conversion']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'source' in d:
            o.source = d['source']
        if 'track_url' in d:
            o.track_url = d['track_url']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


