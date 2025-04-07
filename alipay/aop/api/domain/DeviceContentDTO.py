#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DetectResult import DetectResult


class DeviceContentDTO(object):

    def __init__(self):
        self._content_id = None
        self._content_time = None
        self._content_type = None
        self._content_upload_time = None
        self._detect_results = None
        self._file_url = None
        self._out_content_id = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def content_time(self):
        return self._content_time

    @content_time.setter
    def content_time(self, value):
        self._content_time = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def content_upload_time(self):
        return self._content_upload_time

    @content_upload_time.setter
    def content_upload_time(self, value):
        self._content_upload_time = value
    @property
    def detect_results(self):
        return self._detect_results

    @detect_results.setter
    def detect_results(self, value):
        if isinstance(value, list):
            self._detect_results = list()
            for i in value:
                if isinstance(i, DetectResult):
                    self._detect_results.append(i)
                else:
                    self._detect_results.append(DetectResult.from_alipay_dict(i))
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def out_content_id(self):
        return self._out_content_id

    @out_content_id.setter
    def out_content_id(self, value):
        self._out_content_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.content_time:
            if hasattr(self.content_time, 'to_alipay_dict'):
                params['content_time'] = self.content_time.to_alipay_dict()
            else:
                params['content_time'] = self.content_time
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.content_upload_time:
            if hasattr(self.content_upload_time, 'to_alipay_dict'):
                params['content_upload_time'] = self.content_upload_time.to_alipay_dict()
            else:
                params['content_upload_time'] = self.content_upload_time
        if self.detect_results:
            if isinstance(self.detect_results, list):
                for i in range(0, len(self.detect_results)):
                    element = self.detect_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detect_results[i] = element.to_alipay_dict()
            if hasattr(self.detect_results, 'to_alipay_dict'):
                params['detect_results'] = self.detect_results.to_alipay_dict()
            else:
                params['detect_results'] = self.detect_results
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.out_content_id:
            if hasattr(self.out_content_id, 'to_alipay_dict'):
                params['out_content_id'] = self.out_content_id.to_alipay_dict()
            else:
                params['out_content_id'] = self.out_content_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceContentDTO()
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'content_time' in d:
            o.content_time = d['content_time']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'content_upload_time' in d:
            o.content_upload_time = d['content_upload_time']
        if 'detect_results' in d:
            o.detect_results = d['detect_results']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'out_content_id' in d:
            o.out_content_id = d['out_content_id']
        return o


