#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZXZSessionDetail(object):

    def __init__(self):
        self._bu_unique_id = None
        self._last_activity_time = None
        self._session_id = None
        self._session_title = None

    @property
    def bu_unique_id(self):
        return self._bu_unique_id

    @bu_unique_id.setter
    def bu_unique_id(self, value):
        self._bu_unique_id = value
    @property
    def last_activity_time(self):
        return self._last_activity_time

    @last_activity_time.setter
    def last_activity_time(self, value):
        self._last_activity_time = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def session_title(self):
        return self._session_title

    @session_title.setter
    def session_title(self, value):
        self._session_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.bu_unique_id:
            if hasattr(self.bu_unique_id, 'to_alipay_dict'):
                params['bu_unique_id'] = self.bu_unique_id.to_alipay_dict()
            else:
                params['bu_unique_id'] = self.bu_unique_id
        if self.last_activity_time:
            if hasattr(self.last_activity_time, 'to_alipay_dict'):
                params['last_activity_time'] = self.last_activity_time.to_alipay_dict()
            else:
                params['last_activity_time'] = self.last_activity_time
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.session_title:
            if hasattr(self.session_title, 'to_alipay_dict'):
                params['session_title'] = self.session_title.to_alipay_dict()
            else:
                params['session_title'] = self.session_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZXZSessionDetail()
        if 'bu_unique_id' in d:
            o.bu_unique_id = d['bu_unique_id']
        if 'last_activity_time' in d:
            o.last_activity_time = d['last_activity_time']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'session_title' in d:
            o.session_title = d['session_title']
        return o


