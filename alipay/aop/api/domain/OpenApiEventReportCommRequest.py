#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiEventReportCommRequest(object):

    def __init__(self):
        self._async_query_id = None
        self._end_date = None
        self._events = None
        self._multi_app_id = None
        self._properties = None
        self._start_date = None

    @property
    def async_query_id(self):
        return self._async_query_id

    @async_query_id.setter
    def async_query_id(self, value):
        self._async_query_id = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def events(self):
        return self._events

    @events.setter
    def events(self, value):
        if isinstance(value, list):
            self._events = list()
            for i in value:
                self._events.append(i)
    @property
    def multi_app_id(self):
        return self._multi_app_id

    @multi_app_id.setter
    def multi_app_id(self, value):
        self._multi_app_id = value
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        if isinstance(value, list):
            self._properties = list()
            for i in value:
                self._properties.append(i)
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.async_query_id:
            if hasattr(self.async_query_id, 'to_alipay_dict'):
                params['async_query_id'] = self.async_query_id.to_alipay_dict()
            else:
                params['async_query_id'] = self.async_query_id
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.events:
            if isinstance(self.events, list):
                for i in range(0, len(self.events)):
                    element = self.events[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.events[i] = element.to_alipay_dict()
            if hasattr(self.events, 'to_alipay_dict'):
                params['events'] = self.events.to_alipay_dict()
            else:
                params['events'] = self.events
        if self.multi_app_id:
            if hasattr(self.multi_app_id, 'to_alipay_dict'):
                params['multi_app_id'] = self.multi_app_id.to_alipay_dict()
            else:
                params['multi_app_id'] = self.multi_app_id
        if self.properties:
            if isinstance(self.properties, list):
                for i in range(0, len(self.properties)):
                    element = self.properties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.properties[i] = element.to_alipay_dict()
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiEventReportCommRequest()
        if 'async_query_id' in d:
            o.async_query_id = d['async_query_id']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'events' in d:
            o.events = d['events']
        if 'multi_app_id' in d:
            o.multi_app_id = d['multi_app_id']
        if 'properties' in d:
            o.properties = d['properties']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


