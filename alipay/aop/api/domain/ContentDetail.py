#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContentDetail(object):

    def __init__(self):
        self._rtc_time_difference = None
        self._unique_id = None

    @property
    def rtc_time_difference(self):
        return self._rtc_time_difference

    @rtc_time_difference.setter
    def rtc_time_difference(self, value):
        self._rtc_time_difference = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.rtc_time_difference:
            if hasattr(self.rtc_time_difference, 'to_alipay_dict'):
                params['rtc_time_difference'] = self.rtc_time_difference.to_alipay_dict()
            else:
                params['rtc_time_difference'] = self.rtc_time_difference
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentDetail()
        if 'rtc_time_difference' in d:
            o.rtc_time_difference = d['rtc_time_difference']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


