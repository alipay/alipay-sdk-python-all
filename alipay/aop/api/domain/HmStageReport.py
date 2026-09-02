#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HmStageReport(object):

    def __init__(self):
        self._activity_id = None
        self._content_markdown = None
        self._period_end = None
        self._period_index = None
        self._period_start = None
        self._report_id = None
        self._report_name = None
        self._report_type = None
        self._send_time = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def content_markdown(self):
        return self._content_markdown

    @content_markdown.setter
    def content_markdown(self, value):
        self._content_markdown = value
    @property
    def period_end(self):
        return self._period_end

    @period_end.setter
    def period_end(self, value):
        self._period_end = value
    @property
    def period_index(self):
        return self._period_index

    @period_index.setter
    def period_index(self, value):
        self._period_index = value
    @property
    def period_start(self):
        return self._period_start

    @period_start.setter
    def period_start(self, value):
        self._period_start = value
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
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.content_markdown:
            if hasattr(self.content_markdown, 'to_alipay_dict'):
                params['content_markdown'] = self.content_markdown.to_alipay_dict()
            else:
                params['content_markdown'] = self.content_markdown
        if self.period_end:
            if hasattr(self.period_end, 'to_alipay_dict'):
                params['period_end'] = self.period_end.to_alipay_dict()
            else:
                params['period_end'] = self.period_end
        if self.period_index:
            if hasattr(self.period_index, 'to_alipay_dict'):
                params['period_index'] = self.period_index.to_alipay_dict()
            else:
                params['period_index'] = self.period_index
        if self.period_start:
            if hasattr(self.period_start, 'to_alipay_dict'):
                params['period_start'] = self.period_start.to_alipay_dict()
            else:
                params['period_start'] = self.period_start
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
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HmStageReport()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'content_markdown' in d:
            o.content_markdown = d['content_markdown']
        if 'period_end' in d:
            o.period_end = d['period_end']
        if 'period_index' in d:
            o.period_index = d['period_index']
        if 'period_start' in d:
            o.period_start = d['period_start']
        if 'report_id' in d:
            o.report_id = d['report_id']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_type' in d:
            o.report_type = d['report_type']
        if 'send_time' in d:
            o.send_time = d['send_time']
        return o


