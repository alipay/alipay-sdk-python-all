#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLiveAdvanceCreateModel(object):

    def __init__(self):
        self._alipay_public_id = None
        self._live_advance_time = None
        self._live_title = None
        self._out_advance_id = None

    @property
    def alipay_public_id(self):
        return self._alipay_public_id

    @alipay_public_id.setter
    def alipay_public_id(self, value):
        self._alipay_public_id = value
    @property
    def live_advance_time(self):
        return self._live_advance_time

    @live_advance_time.setter
    def live_advance_time(self, value):
        self._live_advance_time = value
    @property
    def live_title(self):
        return self._live_title

    @live_title.setter
    def live_title(self, value):
        self._live_title = value
    @property
    def out_advance_id(self):
        return self._out_advance_id

    @out_advance_id.setter
    def out_advance_id(self, value):
        self._out_advance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_public_id:
            if hasattr(self.alipay_public_id, 'to_alipay_dict'):
                params['alipay_public_id'] = self.alipay_public_id.to_alipay_dict()
            else:
                params['alipay_public_id'] = self.alipay_public_id
        if self.live_advance_time:
            if hasattr(self.live_advance_time, 'to_alipay_dict'):
                params['live_advance_time'] = self.live_advance_time.to_alipay_dict()
            else:
                params['live_advance_time'] = self.live_advance_time
        if self.live_title:
            if hasattr(self.live_title, 'to_alipay_dict'):
                params['live_title'] = self.live_title.to_alipay_dict()
            else:
                params['live_title'] = self.live_title
        if self.out_advance_id:
            if hasattr(self.out_advance_id, 'to_alipay_dict'):
                params['out_advance_id'] = self.out_advance_id.to_alipay_dict()
            else:
                params['out_advance_id'] = self.out_advance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLiveAdvanceCreateModel()
        if 'alipay_public_id' in d:
            o.alipay_public_id = d['alipay_public_id']
        if 'live_advance_time' in d:
            o.live_advance_time = d['live_advance_time']
        if 'live_title' in d:
            o.live_title = d['live_title']
        if 'out_advance_id' in d:
            o.out_advance_id = d['out_advance_id']
        return o


