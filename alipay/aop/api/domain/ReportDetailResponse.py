#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportDetailResponse(object):

    def __init__(self):
        self._file_source = None
        self._file_url = None
        self._id = None
        self._report_id = None
        self._report_name = None
        self._report_time = None
        self._scene = None

    @property
    def file_source(self):
        return self._file_source

    @file_source.setter
    def file_source(self, value):
        self._file_source = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def report_id(self):
        return self._report_id

    @report_id.setter
    def report_id(self, value):
        self._report_id = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
    @property
    def report_time(self):
        return self._report_time

    @report_time.setter
    def report_time(self, value):
        self._report_time = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_source:
            if hasattr(self.file_source, 'to_alipay_dict'):
                params['file_source'] = self.file_source.to_alipay_dict()
            else:
                params['file_source'] = self.file_source
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.report_id:
            if hasattr(self.report_id, 'to_alipay_dict'):
                params['report_id'] = self.report_id.to_alipay_dict()
            else:
                params['report_id'] = self.report_id
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
        if self.report_time:
            if hasattr(self.report_time, 'to_alipay_dict'):
                params['report_time'] = self.report_time.to_alipay_dict()
            else:
                params['report_time'] = self.report_time
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportDetailResponse()
        if 'file_source' in d:
            o.file_source = d['file_source']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'id' in d:
            o.id = d['id']
        if 'report_id' in d:
            o.report_id = d['report_id']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_time' in d:
            o.report_time = d['report_time']
        if 'scene' in d:
            o.scene = d['scene']
        return o


