#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseMonitorAlarmhistorydetailQueryModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._end = None
        self._history_id = None
        self._page_index = None
        self._page_size = None
        self._start = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value
    @property
    def history_id(self):
        return self._history_id

    @history_id.setter
    def history_id(self, value):
        self._history_id = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.end:
            if hasattr(self.end, 'to_alipay_dict'):
                params['end'] = self.end.to_alipay_dict()
            else:
                params['end'] = self.end
        if self.history_id:
            if hasattr(self.history_id, 'to_alipay_dict'):
                params['history_id'] = self.history_id.to_alipay_dict()
            else:
                params['history_id'] = self.history_id
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.start:
            if hasattr(self.start, 'to_alipay_dict'):
                params['start'] = self.start.to_alipay_dict()
            else:
                params['start'] = self.start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseMonitorAlarmhistorydetailQueryModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'end' in d:
            o.end = d['end']
        if 'history_id' in d:
            o.history_id = d['history_id']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start' in d:
            o.start = d['start']
        return o


