#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneContentCommunitySegmentRealtimeSaveModel(object):

    def __init__(self):
        self._live_id = None
        self._request_time = None
        self._segment_info = None

    @property
    def live_id(self):
        return self._live_id

    @live_id.setter
    def live_id(self, value):
        self._live_id = value
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value
    @property
    def segment_info(self):
        return self._segment_info

    @segment_info.setter
    def segment_info(self, value):
        self._segment_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.live_id:
            if hasattr(self.live_id, 'to_alipay_dict'):
                params['live_id'] = self.live_id.to_alipay_dict()
            else:
                params['live_id'] = self.live_id
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
        if self.segment_info:
            if hasattr(self.segment_info, 'to_alipay_dict'):
                params['segment_info'] = self.segment_info.to_alipay_dict()
            else:
                params['segment_info'] = self.segment_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneContentCommunitySegmentRealtimeSaveModel()
        if 'live_id' in d:
            o.live_id = d['live_id']
        if 'request_time' in d:
            o.request_time = d['request_time']
        if 'segment_info' in d:
            o.segment_info = d['segment_info']
        return o


