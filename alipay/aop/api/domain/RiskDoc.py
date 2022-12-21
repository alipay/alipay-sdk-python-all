#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskDoc(object):

    def __init__(self):
        self._event_time = None
        self._source_doc_id = None
        self._source_doc_type = None
        self._summary = None
        self._title = None

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def source_doc_id(self):
        return self._source_doc_id

    @source_doc_id.setter
    def source_doc_id(self, value):
        self._source_doc_id = value
    @property
    def source_doc_type(self):
        return self._source_doc_type

    @source_doc_type.setter
    def source_doc_type(self, value):
        self._source_doc_type = value
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
        if self.event_time:
            if hasattr(self.event_time, 'to_alipay_dict'):
                params['event_time'] = self.event_time.to_alipay_dict()
            else:
                params['event_time'] = self.event_time
        if self.source_doc_id:
            if hasattr(self.source_doc_id, 'to_alipay_dict'):
                params['source_doc_id'] = self.source_doc_id.to_alipay_dict()
            else:
                params['source_doc_id'] = self.source_doc_id
        if self.source_doc_type:
            if hasattr(self.source_doc_type, 'to_alipay_dict'):
                params['source_doc_type'] = self.source_doc_type.to_alipay_dict()
            else:
                params['source_doc_type'] = self.source_doc_type
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
        o = RiskDoc()
        if 'event_time' in d:
            o.event_time = d['event_time']
        if 'source_doc_id' in d:
            o.source_doc_id = d['source_doc_id']
        if 'source_doc_type' in d:
            o.source_doc_type = d['source_doc_type']
        if 'summary' in d:
            o.summary = d['summary']
        if 'title' in d:
            o.title = d['title']
        return o


