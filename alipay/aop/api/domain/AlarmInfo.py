#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlarmInfo(object):

    def __init__(self):
        self._ad_code = None
        self._ad_code_list = None
        self._alarm_publish_unit = None
        self._content = None
        self._end_time = None
        self._level = None
        self._out_id = None
        self._target_url = None
        self._time = None
        self._title = None
        self._type = None

    @property
    def ad_code(self):
        return self._ad_code

    @ad_code.setter
    def ad_code(self, value):
        self._ad_code = value
    @property
    def ad_code_list(self):
        return self._ad_code_list

    @ad_code_list.setter
    def ad_code_list(self, value):
        if isinstance(value, list):
            self._ad_code_list = list()
            for i in value:
                self._ad_code_list.append(i)
    @property
    def alarm_publish_unit(self):
        return self._alarm_publish_unit

    @alarm_publish_unit.setter
    def alarm_publish_unit(self, value):
        self._alarm_publish_unit = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def target_url(self):
        return self._target_url

    @target_url.setter
    def target_url(self, value):
        self._target_url = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_code:
            if hasattr(self.ad_code, 'to_alipay_dict'):
                params['ad_code'] = self.ad_code.to_alipay_dict()
            else:
                params['ad_code'] = self.ad_code
        if self.ad_code_list:
            if isinstance(self.ad_code_list, list):
                for i in range(0, len(self.ad_code_list)):
                    element = self.ad_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ad_code_list[i] = element.to_alipay_dict()
            if hasattr(self.ad_code_list, 'to_alipay_dict'):
                params['ad_code_list'] = self.ad_code_list.to_alipay_dict()
            else:
                params['ad_code_list'] = self.ad_code_list
        if self.alarm_publish_unit:
            if hasattr(self.alarm_publish_unit, 'to_alipay_dict'):
                params['alarm_publish_unit'] = self.alarm_publish_unit.to_alipay_dict()
            else:
                params['alarm_publish_unit'] = self.alarm_publish_unit
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.target_url:
            if hasattr(self.target_url, 'to_alipay_dict'):
                params['target_url'] = self.target_url.to_alipay_dict()
            else:
                params['target_url'] = self.target_url
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlarmInfo()
        if 'ad_code' in d:
            o.ad_code = d['ad_code']
        if 'ad_code_list' in d:
            o.ad_code_list = d['ad_code_list']
        if 'alarm_publish_unit' in d:
            o.alarm_publish_unit = d['alarm_publish_unit']
        if 'content' in d:
            o.content = d['content']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'level' in d:
            o.level = d['level']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'target_url' in d:
            o.target_url = d['target_url']
        if 'time' in d:
            o.time = d['time']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o


