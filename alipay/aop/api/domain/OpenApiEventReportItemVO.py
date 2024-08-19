#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiEventReportItemVO(object):

    def __init__(self):
        self._dt = None
        self._event = None
        self._people_count = None
        self._people_visit_count = None
        self._people_visit_count_avg = None
        self._property = None
        self._property_value = None

    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value
    @property
    def people_count(self):
        return self._people_count

    @people_count.setter
    def people_count(self, value):
        self._people_count = value
    @property
    def people_visit_count(self):
        return self._people_visit_count

    @people_visit_count.setter
    def people_visit_count(self, value):
        self._people_visit_count = value
    @property
    def people_visit_count_avg(self):
        return self._people_visit_count_avg

    @people_visit_count_avg.setter
    def people_visit_count_avg(self, value):
        self._people_visit_count_avg = value
    @property
    def property(self):
        return self._property

    @property.setter
    def property(self, value):
        self._property = value
    @property
    def property_value(self):
        return self._property_value

    @property_value.setter
    def property_value(self, value):
        self._property_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.dt:
            if hasattr(self.dt, 'to_alipay_dict'):
                params['dt'] = self.dt.to_alipay_dict()
            else:
                params['dt'] = self.dt
        if self.event:
            if hasattr(self.event, 'to_alipay_dict'):
                params['event'] = self.event.to_alipay_dict()
            else:
                params['event'] = self.event
        if self.people_count:
            if hasattr(self.people_count, 'to_alipay_dict'):
                params['people_count'] = self.people_count.to_alipay_dict()
            else:
                params['people_count'] = self.people_count
        if self.people_visit_count:
            if hasattr(self.people_visit_count, 'to_alipay_dict'):
                params['people_visit_count'] = self.people_visit_count.to_alipay_dict()
            else:
                params['people_visit_count'] = self.people_visit_count
        if self.people_visit_count_avg:
            if hasattr(self.people_visit_count_avg, 'to_alipay_dict'):
                params['people_visit_count_avg'] = self.people_visit_count_avg.to_alipay_dict()
            else:
                params['people_visit_count_avg'] = self.people_visit_count_avg
        if self.property:
            if hasattr(self.property, 'to_alipay_dict'):
                params['property'] = self.property.to_alipay_dict()
            else:
                params['property'] = self.property
        if self.property_value:
            if hasattr(self.property_value, 'to_alipay_dict'):
                params['property_value'] = self.property_value.to_alipay_dict()
            else:
                params['property_value'] = self.property_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiEventReportItemVO()
        if 'dt' in d:
            o.dt = d['dt']
        if 'event' in d:
            o.event = d['event']
        if 'people_count' in d:
            o.people_count = d['people_count']
        if 'people_visit_count' in d:
            o.people_visit_count = d['people_visit_count']
        if 'people_visit_count_avg' in d:
            o.people_visit_count_avg = d['people_visit_count_avg']
        if 'property' in d:
            o.property = d['property']
        if 'property_value' in d:
            o.property_value = d['property_value']
        return o


