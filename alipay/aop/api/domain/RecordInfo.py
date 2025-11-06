#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecordInfo(object):

    def __init__(self):
        self._conf_duration = None
        self._duration = None
        self._file_size = None
        self._id = None
        self._record_title = None
        self._url = None

    @property
    def conf_duration(self):
        return self._conf_duration

    @conf_duration.setter
    def conf_duration(self, value):
        self._conf_duration = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def record_title(self):
        return self._record_title

    @record_title.setter
    def record_title(self, value):
        self._record_title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.conf_duration:
            if hasattr(self.conf_duration, 'to_alipay_dict'):
                params['conf_duration'] = self.conf_duration.to_alipay_dict()
            else:
                params['conf_duration'] = self.conf_duration
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.record_title:
            if hasattr(self.record_title, 'to_alipay_dict'):
                params['record_title'] = self.record_title.to_alipay_dict()
            else:
                params['record_title'] = self.record_title
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
        o = RecordInfo()
        if 'conf_duration' in d:
            o.conf_duration = d['conf_duration']
        if 'duration' in d:
            o.duration = d['duration']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'id' in d:
            o.id = d['id']
        if 'record_title' in d:
            o.record_title = d['record_title']
        if 'url' in d:
            o.url = d['url']
        return o


