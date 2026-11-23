#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenbizmockSseMockEvent(object):

    def __init__(self):
        self._comment = None
        self._data = None
        self._event = None
        self._id = None
        self._repeat_count = None
        self._wait_time = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def repeat_count(self):
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, value):
        self._repeat_count = value
    @property
    def wait_time(self):
        return self._wait_time

    @wait_time.setter
    def wait_time(self, value):
        self._wait_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.event:
            if hasattr(self.event, 'to_alipay_dict'):
                params['event'] = self.event.to_alipay_dict()
            else:
                params['event'] = self.event
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.repeat_count:
            if hasattr(self.repeat_count, 'to_alipay_dict'):
                params['repeat_count'] = self.repeat_count.to_alipay_dict()
            else:
                params['repeat_count'] = self.repeat_count
        if self.wait_time:
            if hasattr(self.wait_time, 'to_alipay_dict'):
                params['wait_time'] = self.wait_time.to_alipay_dict()
            else:
                params['wait_time'] = self.wait_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenbizmockSseMockEvent()
        if 'comment' in d:
            o.comment = d['comment']
        if 'data' in d:
            o.data = d['data']
        if 'event' in d:
            o.event = d['event']
        if 'id' in d:
            o.id = d['id']
        if 'repeat_count' in d:
            o.repeat_count = d['repeat_count']
        if 'wait_time' in d:
            o.wait_time = d['wait_time']
        return o


