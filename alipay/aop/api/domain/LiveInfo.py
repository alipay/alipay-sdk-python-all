#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LiveContentInfo import LiveContentInfo


class LiveInfo(object):

    def __init__(self):
        self._content_info_list = None
        self._live_end_time = None
        self._live_id = None
        self._live_start_time = None
        self._summary = None
        self._title = None

    @property
    def content_info_list(self):
        return self._content_info_list

    @content_info_list.setter
    def content_info_list(self, value):
        if isinstance(value, list):
            self._content_info_list = list()
            for i in value:
                if isinstance(i, LiveContentInfo):
                    self._content_info_list.append(i)
                else:
                    self._content_info_list.append(LiveContentInfo.from_alipay_dict(i))
    @property
    def live_end_time(self):
        return self._live_end_time

    @live_end_time.setter
    def live_end_time(self, value):
        self._live_end_time = value
    @property
    def live_id(self):
        return self._live_id

    @live_id.setter
    def live_id(self, value):
        self._live_id = value
    @property
    def live_start_time(self):
        return self._live_start_time

    @live_start_time.setter
    def live_start_time(self, value):
        self._live_start_time = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_info_list:
            if isinstance(self.content_info_list, list):
                for i in range(0, len(self.content_info_list)):
                    element = self.content_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_info_list[i] = element.to_alipay_dict()
            if hasattr(self.content_info_list, 'to_alipay_dict'):
                params['content_info_list'] = self.content_info_list.to_alipay_dict()
            else:
                params['content_info_list'] = self.content_info_list
        if self.live_end_time:
            if hasattr(self.live_end_time, 'to_alipay_dict'):
                params['live_end_time'] = self.live_end_time.to_alipay_dict()
            else:
                params['live_end_time'] = self.live_end_time
        if self.live_id:
            if hasattr(self.live_id, 'to_alipay_dict'):
                params['live_id'] = self.live_id.to_alipay_dict()
            else:
                params['live_id'] = self.live_id
        if self.live_start_time:
            if hasattr(self.live_start_time, 'to_alipay_dict'):
                params['live_start_time'] = self.live_start_time.to_alipay_dict()
            else:
                params['live_start_time'] = self.live_start_time
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LiveInfo()
        if 'content_info_list' in d:
            o.content_info_list = d['content_info_list']
        if 'live_end_time' in d:
            o.live_end_time = d['live_end_time']
        if 'live_id' in d:
            o.live_id = d['live_id']
        if 'live_start_time' in d:
            o.live_start_time = d['live_start_time']
        if 'summary' in d:
            o.summary = d['summary']
        if 'title' in d:
            o.title = d['title']
        return o


