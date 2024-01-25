#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ThirdTrackUrlUnit(object):

    def __init__(self):
        self._biz_type = None
        self._report_type = None
        self._track_type = None
        self._track_url = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value
    @property
    def track_type(self):
        return self._track_type

    @track_type.setter
    def track_type(self, value):
        self._track_type = value
    @property
    def track_url(self):
        return self._track_url

    @track_url.setter
    def track_url(self, value):
        self._track_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        if self.track_type:
            if hasattr(self.track_type, 'to_alipay_dict'):
                params['track_type'] = self.track_type.to_alipay_dict()
            else:
                params['track_type'] = self.track_type
        if self.track_url:
            if hasattr(self.track_url, 'to_alipay_dict'):
                params['track_url'] = self.track_url.to_alipay_dict()
            else:
                params['track_url'] = self.track_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ThirdTrackUrlUnit()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'report_type' in d:
            o.report_type = d['report_type']
        if 'track_type' in d:
            o.track_type = d['track_type']
        if 'track_url' in d:
            o.track_url = d['track_url']
        return o


