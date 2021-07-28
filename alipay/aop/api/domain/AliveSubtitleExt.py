#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AliveSubtitleExt(object):

    def __init__(self):
        self._action_type = None
        self._action_url = None
        self._confidence = None
        self._end_time = None
        self._index = None
        self._info_sec_result = None
        self._start_time = None
        self._sub_index = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def confidence(self):
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        self._confidence = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def info_sec_result(self):
        return self._info_sec_result

    @info_sec_result.setter
    def info_sec_result(self, value):
        self._info_sec_result = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_index(self):
        return self._sub_index

    @sub_index.setter
    def sub_index(self, value):
        self._sub_index = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.confidence:
            if hasattr(self.confidence, 'to_alipay_dict'):
                params['confidence'] = self.confidence.to_alipay_dict()
            else:
                params['confidence'] = self.confidence
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.info_sec_result:
            if hasattr(self.info_sec_result, 'to_alipay_dict'):
                params['info_sec_result'] = self.info_sec_result.to_alipay_dict()
            else:
                params['info_sec_result'] = self.info_sec_result
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_index:
            if hasattr(self.sub_index, 'to_alipay_dict'):
                params['sub_index'] = self.sub_index.to_alipay_dict()
            else:
                params['sub_index'] = self.sub_index
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AliveSubtitleExt()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'confidence' in d:
            o.confidence = d['confidence']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'index' in d:
            o.index = d['index']
        if 'info_sec_result' in d:
            o.info_sec_result = d['info_sec_result']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_index' in d:
            o.sub_index = d['sub_index']
        return o


