#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EventBacktrackingVO(object):

    def __init__(self):
        self._content_id = None
        self._content_time = None
        self._content_type = None
        self._content_upload_time = None
        self._detect_result = None
        self._detect_status = None
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
    def detect_result(self):
        return self._detect_result

    @detect_result.setter
    def detect_result(self, value):
        self._detect_result = value
    @property
    def detect_status(self):
        return self._detect_status

    @detect_status.setter
    def detect_status(self, value):
        self._detect_status = value
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
        if self.detect_result:
            if hasattr(self.detect_result, 'to_alipay_dict'):
                params['detect_result'] = self.detect_result.to_alipay_dict()
            else:
                params['detect_result'] = self.detect_result
        if self.detect_status:
            if hasattr(self.detect_status, 'to_alipay_dict'):
                params['detect_status'] = self.detect_status.to_alipay_dict()
            else:
                params['detect_status'] = self.detect_status
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
        o = EventBacktrackingVO()
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'content_time' in d:
            o.content_time = d['content_time']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'content_upload_time' in d:
            o.content_upload_time = d['content_upload_time']
        if 'detect_result' in d:
            o.detect_result = d['detect_result']
        if 'detect_status' in d:
            o.detect_status = d['detect_status']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'out_content_id' in d:
            o.out_content_id = d['out_content_id']
        return o


