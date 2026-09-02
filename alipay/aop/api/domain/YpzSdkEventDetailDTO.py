#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YpzSdkEventDetailDTO(object):

    def __init__(self):
        self._event_code = None
        self._event_count = None
        self._event_description = None
        self._event_name = None
        self._event_occur_date = None
        self._event_update_date = None
        self._greater_than_10m = None
        self._greater_than_15s = None
        self._greater_than_1h = None
        self._greater_than_1m = None
        self._greater_than_30m = None
        self._greater_than_5s = None
        self._less_than_0s = None
        self._less_than_negative_1s = None
        self._medical_institution_name = None
        self._range_negative_1_to_10_s = None
        self._range_negative_1_to_15_s = None
        self._range_negative_1_to_5_s = None
        self._rate_negative_1_to_10_s = None
        self._rate_negative_1_to_15_s = None
        self._rate_negative_1_to_5_s = None
        self._uscc = None

    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def event_count(self):
        return self._event_count

    @event_count.setter
    def event_count(self, value):
        self._event_count = value
    @property
    def event_description(self):
        return self._event_description

    @event_description.setter
    def event_description(self, value):
        self._event_description = value
    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value
    @property
    def event_occur_date(self):
        return self._event_occur_date

    @event_occur_date.setter
    def event_occur_date(self, value):
        self._event_occur_date = value
    @property
    def event_update_date(self):
        return self._event_update_date

    @event_update_date.setter
    def event_update_date(self, value):
        self._event_update_date = value
    @property
    def greater_than_10m(self):
        return self._greater_than_10m

    @greater_than_10m.setter
    def greater_than_10m(self, value):
        self._greater_than_10m = value
    @property
    def greater_than_15s(self):
        return self._greater_than_15s

    @greater_than_15s.setter
    def greater_than_15s(self, value):
        self._greater_than_15s = value
    @property
    def greater_than_1h(self):
        return self._greater_than_1h

    @greater_than_1h.setter
    def greater_than_1h(self, value):
        self._greater_than_1h = value
    @property
    def greater_than_1m(self):
        return self._greater_than_1m

    @greater_than_1m.setter
    def greater_than_1m(self, value):
        self._greater_than_1m = value
    @property
    def greater_than_30m(self):
        return self._greater_than_30m

    @greater_than_30m.setter
    def greater_than_30m(self, value):
        self._greater_than_30m = value
    @property
    def greater_than_5s(self):
        return self._greater_than_5s

    @greater_than_5s.setter
    def greater_than_5s(self, value):
        self._greater_than_5s = value
    @property
    def less_than_0s(self):
        return self._less_than_0s

    @less_than_0s.setter
    def less_than_0s(self, value):
        self._less_than_0s = value
    @property
    def less_than_negative_1s(self):
        return self._less_than_negative_1s

    @less_than_negative_1s.setter
    def less_than_negative_1s(self, value):
        self._less_than_negative_1s = value
    @property
    def medical_institution_name(self):
        return self._medical_institution_name

    @medical_institution_name.setter
    def medical_institution_name(self, value):
        self._medical_institution_name = value
    @property
    def range_negative_1_to_10_s(self):
        return self._range_negative_1_to_10_s

    @range_negative_1_to_10_s.setter
    def range_negative_1_to_10_s(self, value):
        self._range_negative_1_to_10_s = value
    @property
    def range_negative_1_to_15_s(self):
        return self._range_negative_1_to_15_s

    @range_negative_1_to_15_s.setter
    def range_negative_1_to_15_s(self, value):
        self._range_negative_1_to_15_s = value
    @property
    def range_negative_1_to_5_s(self):
        return self._range_negative_1_to_5_s

    @range_negative_1_to_5_s.setter
    def range_negative_1_to_5_s(self, value):
        self._range_negative_1_to_5_s = value
    @property
    def rate_negative_1_to_10_s(self):
        return self._rate_negative_1_to_10_s

    @rate_negative_1_to_10_s.setter
    def rate_negative_1_to_10_s(self, value):
        self._rate_negative_1_to_10_s = value
    @property
    def rate_negative_1_to_15_s(self):
        return self._rate_negative_1_to_15_s

    @rate_negative_1_to_15_s.setter
    def rate_negative_1_to_15_s(self, value):
        self._rate_negative_1_to_15_s = value
    @property
    def rate_negative_1_to_5_s(self):
        return self._rate_negative_1_to_5_s

    @rate_negative_1_to_5_s.setter
    def rate_negative_1_to_5_s(self, value):
        self._rate_negative_1_to_5_s = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.event_count:
            if hasattr(self.event_count, 'to_alipay_dict'):
                params['event_count'] = self.event_count.to_alipay_dict()
            else:
                params['event_count'] = self.event_count
        if self.event_description:
            if hasattr(self.event_description, 'to_alipay_dict'):
                params['event_description'] = self.event_description.to_alipay_dict()
            else:
                params['event_description'] = self.event_description
        if self.event_name:
            if hasattr(self.event_name, 'to_alipay_dict'):
                params['event_name'] = self.event_name.to_alipay_dict()
            else:
                params['event_name'] = self.event_name
        if self.event_occur_date:
            if hasattr(self.event_occur_date, 'to_alipay_dict'):
                params['event_occur_date'] = self.event_occur_date.to_alipay_dict()
            else:
                params['event_occur_date'] = self.event_occur_date
        if self.event_update_date:
            if hasattr(self.event_update_date, 'to_alipay_dict'):
                params['event_update_date'] = self.event_update_date.to_alipay_dict()
            else:
                params['event_update_date'] = self.event_update_date
        if self.greater_than_10m:
            if hasattr(self.greater_than_10m, 'to_alipay_dict'):
                params['greater_than_10m'] = self.greater_than_10m.to_alipay_dict()
            else:
                params['greater_than_10m'] = self.greater_than_10m
        if self.greater_than_15s:
            if hasattr(self.greater_than_15s, 'to_alipay_dict'):
                params['greater_than_15s'] = self.greater_than_15s.to_alipay_dict()
            else:
                params['greater_than_15s'] = self.greater_than_15s
        if self.greater_than_1h:
            if hasattr(self.greater_than_1h, 'to_alipay_dict'):
                params['greater_than_1h'] = self.greater_than_1h.to_alipay_dict()
            else:
                params['greater_than_1h'] = self.greater_than_1h
        if self.greater_than_1m:
            if hasattr(self.greater_than_1m, 'to_alipay_dict'):
                params['greater_than_1m'] = self.greater_than_1m.to_alipay_dict()
            else:
                params['greater_than_1m'] = self.greater_than_1m
        if self.greater_than_30m:
            if hasattr(self.greater_than_30m, 'to_alipay_dict'):
                params['greater_than_30m'] = self.greater_than_30m.to_alipay_dict()
            else:
                params['greater_than_30m'] = self.greater_than_30m
        if self.greater_than_5s:
            if hasattr(self.greater_than_5s, 'to_alipay_dict'):
                params['greater_than_5s'] = self.greater_than_5s.to_alipay_dict()
            else:
                params['greater_than_5s'] = self.greater_than_5s
        if self.less_than_0s:
            if hasattr(self.less_than_0s, 'to_alipay_dict'):
                params['less_than_0s'] = self.less_than_0s.to_alipay_dict()
            else:
                params['less_than_0s'] = self.less_than_0s
        if self.less_than_negative_1s:
            if hasattr(self.less_than_negative_1s, 'to_alipay_dict'):
                params['less_than_negative_1s'] = self.less_than_negative_1s.to_alipay_dict()
            else:
                params['less_than_negative_1s'] = self.less_than_negative_1s
        if self.medical_institution_name:
            if hasattr(self.medical_institution_name, 'to_alipay_dict'):
                params['medical_institution_name'] = self.medical_institution_name.to_alipay_dict()
            else:
                params['medical_institution_name'] = self.medical_institution_name
        if self.range_negative_1_to_10_s:
            if hasattr(self.range_negative_1_to_10_s, 'to_alipay_dict'):
                params['range_negative_1_to_10_s'] = self.range_negative_1_to_10_s.to_alipay_dict()
            else:
                params['range_negative_1_to_10_s'] = self.range_negative_1_to_10_s
        if self.range_negative_1_to_15_s:
            if hasattr(self.range_negative_1_to_15_s, 'to_alipay_dict'):
                params['range_negative_1_to_15_s'] = self.range_negative_1_to_15_s.to_alipay_dict()
            else:
                params['range_negative_1_to_15_s'] = self.range_negative_1_to_15_s
        if self.range_negative_1_to_5_s:
            if hasattr(self.range_negative_1_to_5_s, 'to_alipay_dict'):
                params['range_negative_1_to_5_s'] = self.range_negative_1_to_5_s.to_alipay_dict()
            else:
                params['range_negative_1_to_5_s'] = self.range_negative_1_to_5_s
        if self.rate_negative_1_to_10_s:
            if hasattr(self.rate_negative_1_to_10_s, 'to_alipay_dict'):
                params['rate_negative_1_to_10_s'] = self.rate_negative_1_to_10_s.to_alipay_dict()
            else:
                params['rate_negative_1_to_10_s'] = self.rate_negative_1_to_10_s
        if self.rate_negative_1_to_15_s:
            if hasattr(self.rate_negative_1_to_15_s, 'to_alipay_dict'):
                params['rate_negative_1_to_15_s'] = self.rate_negative_1_to_15_s.to_alipay_dict()
            else:
                params['rate_negative_1_to_15_s'] = self.rate_negative_1_to_15_s
        if self.rate_negative_1_to_5_s:
            if hasattr(self.rate_negative_1_to_5_s, 'to_alipay_dict'):
                params['rate_negative_1_to_5_s'] = self.rate_negative_1_to_5_s.to_alipay_dict()
            else:
                params['rate_negative_1_to_5_s'] = self.rate_negative_1_to_5_s
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YpzSdkEventDetailDTO()
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'event_count' in d:
            o.event_count = d['event_count']
        if 'event_description' in d:
            o.event_description = d['event_description']
        if 'event_name' in d:
            o.event_name = d['event_name']
        if 'event_occur_date' in d:
            o.event_occur_date = d['event_occur_date']
        if 'event_update_date' in d:
            o.event_update_date = d['event_update_date']
        if 'greater_than_10m' in d:
            o.greater_than_10m = d['greater_than_10m']
        if 'greater_than_15s' in d:
            o.greater_than_15s = d['greater_than_15s']
        if 'greater_than_1h' in d:
            o.greater_than_1h = d['greater_than_1h']
        if 'greater_than_1m' in d:
            o.greater_than_1m = d['greater_than_1m']
        if 'greater_than_30m' in d:
            o.greater_than_30m = d['greater_than_30m']
        if 'greater_than_5s' in d:
            o.greater_than_5s = d['greater_than_5s']
        if 'less_than_0s' in d:
            o.less_than_0s = d['less_than_0s']
        if 'less_than_negative_1s' in d:
            o.less_than_negative_1s = d['less_than_negative_1s']
        if 'medical_institution_name' in d:
            o.medical_institution_name = d['medical_institution_name']
        if 'range_negative_1_to_10_s' in d:
            o.range_negative_1_to_10_s = d['range_negative_1_to_10_s']
        if 'range_negative_1_to_15_s' in d:
            o.range_negative_1_to_15_s = d['range_negative_1_to_15_s']
        if 'range_negative_1_to_5_s' in d:
            o.range_negative_1_to_5_s = d['range_negative_1_to_5_s']
        if 'rate_negative_1_to_10_s' in d:
            o.rate_negative_1_to_10_s = d['rate_negative_1_to_10_s']
        if 'rate_negative_1_to_15_s' in d:
            o.rate_negative_1_to_15_s = d['rate_negative_1_to_15_s']
        if 'rate_negative_1_to_5_s' in d:
            o.rate_negative_1_to_5_s = d['rate_negative_1_to_5_s']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


