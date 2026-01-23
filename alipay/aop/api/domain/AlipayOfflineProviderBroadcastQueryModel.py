#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderBroadcastQueryModel(object):

    def __init__(self):
        self._bind_end_date = None
        self._bind_start_date = None
        self._biz_active_end_time = None
        self._biz_active_start_time = None
        self._biz_touch_active_end_time = None
        self._biz_touch_active_start_time = None
        self._end_date = None
        self._smid = None

    @property
    def bind_end_date(self):
        return self._bind_end_date

    @bind_end_date.setter
    def bind_end_date(self, value):
        self._bind_end_date = value
    @property
    def bind_start_date(self):
        return self._bind_start_date

    @bind_start_date.setter
    def bind_start_date(self, value):
        self._bind_start_date = value
    @property
    def biz_active_end_time(self):
        return self._biz_active_end_time

    @biz_active_end_time.setter
    def biz_active_end_time(self, value):
        self._biz_active_end_time = value
    @property
    def biz_active_start_time(self):
        return self._biz_active_start_time

    @biz_active_start_time.setter
    def biz_active_start_time(self, value):
        self._biz_active_start_time = value
    @property
    def biz_touch_active_end_time(self):
        return self._biz_touch_active_end_time

    @biz_touch_active_end_time.setter
    def biz_touch_active_end_time(self, value):
        self._biz_touch_active_end_time = value
    @property
    def biz_touch_active_start_time(self):
        return self._biz_touch_active_start_time

    @biz_touch_active_start_time.setter
    def biz_touch_active_start_time(self, value):
        self._biz_touch_active_start_time = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_end_date:
            if hasattr(self.bind_end_date, 'to_alipay_dict'):
                params['bind_end_date'] = self.bind_end_date.to_alipay_dict()
            else:
                params['bind_end_date'] = self.bind_end_date
        if self.bind_start_date:
            if hasattr(self.bind_start_date, 'to_alipay_dict'):
                params['bind_start_date'] = self.bind_start_date.to_alipay_dict()
            else:
                params['bind_start_date'] = self.bind_start_date
        if self.biz_active_end_time:
            if hasattr(self.biz_active_end_time, 'to_alipay_dict'):
                params['biz_active_end_time'] = self.biz_active_end_time.to_alipay_dict()
            else:
                params['biz_active_end_time'] = self.biz_active_end_time
        if self.biz_active_start_time:
            if hasattr(self.biz_active_start_time, 'to_alipay_dict'):
                params['biz_active_start_time'] = self.biz_active_start_time.to_alipay_dict()
            else:
                params['biz_active_start_time'] = self.biz_active_start_time
        if self.biz_touch_active_end_time:
            if hasattr(self.biz_touch_active_end_time, 'to_alipay_dict'):
                params['biz_touch_active_end_time'] = self.biz_touch_active_end_time.to_alipay_dict()
            else:
                params['biz_touch_active_end_time'] = self.biz_touch_active_end_time
        if self.biz_touch_active_start_time:
            if hasattr(self.biz_touch_active_start_time, 'to_alipay_dict'):
                params['biz_touch_active_start_time'] = self.biz_touch_active_start_time.to_alipay_dict()
            else:
                params['biz_touch_active_start_time'] = self.biz_touch_active_start_time
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderBroadcastQueryModel()
        if 'bind_end_date' in d:
            o.bind_end_date = d['bind_end_date']
        if 'bind_start_date' in d:
            o.bind_start_date = d['bind_start_date']
        if 'biz_active_end_time' in d:
            o.biz_active_end_time = d['biz_active_end_time']
        if 'biz_active_start_time' in d:
            o.biz_active_start_time = d['biz_active_start_time']
        if 'biz_touch_active_end_time' in d:
            o.biz_touch_active_end_time = d['biz_touch_active_end_time']
        if 'biz_touch_active_start_time' in d:
            o.biz_touch_active_start_time = d['biz_touch_active_start_time']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'smid' in d:
            o.smid = d['smid']
        return o


