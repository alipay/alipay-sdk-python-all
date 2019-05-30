#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAntdataassetsFixdataCreateModel(object):

    def __init__(self):
        self._end_date = None
        self._guid = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def guid(self):
        return self._guid

    @guid.setter
    def guid(self, value):
        self._guid = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.guid:
            if hasattr(self.guid, 'to_alipay_dict'):
                params['guid'] = self.guid.to_alipay_dict()
            else:
                params['guid'] = self.guid
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
        o = AlipayDataDataserviceAntdataassetsFixdataCreateModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'guid' in d:
            o.guid = d['guid']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


