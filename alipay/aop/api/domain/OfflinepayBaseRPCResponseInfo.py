#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OfflinepayErrorIndicator import OfflinepayErrorIndicator


class OfflinepayBaseRPCResponseInfo(object):

    def __init__(self):
        self._error_indicator = None
        self._ext_info = None
        self._success = None
        self._time = None

    @property
    def error_indicator(self):
        return self._error_indicator

    @error_indicator.setter
    def error_indicator(self, value):
        if isinstance(value, OfflinepayErrorIndicator):
            self._error_indicator = value
        else:
            self._error_indicator = OfflinepayErrorIndicator.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_indicator:
            if hasattr(self.error_indicator, 'to_alipay_dict'):
                params['error_indicator'] = self.error_indicator.to_alipay_dict()
            else:
                params['error_indicator'] = self.error_indicator
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OfflinepayBaseRPCResponseInfo()
        if 'error_indicator' in d:
            o.error_indicator = d['error_indicator']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'success' in d:
            o.success = d['success']
        if 'time' in d:
            o.time = d['time']
        return o


