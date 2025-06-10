#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NRiskOrderRecord(object):

    def __init__(self):
        self._event_no = None
        self._handler_id = None
        self._handler_name = None
        self._notes = None
        self._order_no = None
        self._process_photos = None
        self._process_time = None
        self._solution_name = None

    @property
    def event_no(self):
        return self._event_no

    @event_no.setter
    def event_no(self, value):
        self._event_no = value
    @property
    def handler_id(self):
        return self._handler_id

    @handler_id.setter
    def handler_id(self, value):
        self._handler_id = value
    @property
    def handler_name(self):
        return self._handler_name

    @handler_name.setter
    def handler_name(self, value):
        self._handler_name = value
    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value):
        self._notes = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def process_photos(self):
        return self._process_photos

    @process_photos.setter
    def process_photos(self, value):
        self._process_photos = value
    @property
    def process_time(self):
        return self._process_time

    @process_time.setter
    def process_time(self, value):
        self._process_time = value
    @property
    def solution_name(self):
        return self._solution_name

    @solution_name.setter
    def solution_name(self, value):
        self._solution_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_no:
            if hasattr(self.event_no, 'to_alipay_dict'):
                params['event_no'] = self.event_no.to_alipay_dict()
            else:
                params['event_no'] = self.event_no
        if self.handler_id:
            if hasattr(self.handler_id, 'to_alipay_dict'):
                params['handler_id'] = self.handler_id.to_alipay_dict()
            else:
                params['handler_id'] = self.handler_id
        if self.handler_name:
            if hasattr(self.handler_name, 'to_alipay_dict'):
                params['handler_name'] = self.handler_name.to_alipay_dict()
            else:
                params['handler_name'] = self.handler_name
        if self.notes:
            if hasattr(self.notes, 'to_alipay_dict'):
                params['notes'] = self.notes.to_alipay_dict()
            else:
                params['notes'] = self.notes
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.process_photos:
            if hasattr(self.process_photos, 'to_alipay_dict'):
                params['process_photos'] = self.process_photos.to_alipay_dict()
            else:
                params['process_photos'] = self.process_photos
        if self.process_time:
            if hasattr(self.process_time, 'to_alipay_dict'):
                params['process_time'] = self.process_time.to_alipay_dict()
            else:
                params['process_time'] = self.process_time
        if self.solution_name:
            if hasattr(self.solution_name, 'to_alipay_dict'):
                params['solution_name'] = self.solution_name.to_alipay_dict()
            else:
                params['solution_name'] = self.solution_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NRiskOrderRecord()
        if 'event_no' in d:
            o.event_no = d['event_no']
        if 'handler_id' in d:
            o.handler_id = d['handler_id']
        if 'handler_name' in d:
            o.handler_name = d['handler_name']
        if 'notes' in d:
            o.notes = d['notes']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'process_photos' in d:
            o.process_photos = d['process_photos']
        if 'process_time' in d:
            o.process_time = d['process_time']
        if 'solution_name' in d:
            o.solution_name = d['solution_name']
        return o


