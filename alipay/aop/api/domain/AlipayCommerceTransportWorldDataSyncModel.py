#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportWorldDataSyncModel(object):

    def __init__(self):
        self._biz_data = None
        self._event_no = None
        self._event_type = None
        self._source = None
        self._sync_data = None
        self._user_id = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def event_no(self):
        return self._event_no

    @event_no.setter
    def event_no(self, value):
        self._event_no = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sync_data(self):
        return self._sync_data

    @sync_data.setter
    def sync_data(self, value):
        self._sync_data = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.event_no:
            if hasattr(self.event_no, 'to_alipay_dict'):
                params['event_no'] = self.event_no.to_alipay_dict()
            else:
                params['event_no'] = self.event_no
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.sync_data:
            if hasattr(self.sync_data, 'to_alipay_dict'):
                params['sync_data'] = self.sync_data.to_alipay_dict()
            else:
                params['sync_data'] = self.sync_data
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportWorldDataSyncModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'event_no' in d:
            o.event_no = d['event_no']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'source' in d:
            o.source = d['source']
        if 'sync_data' in d:
            o.sync_data = d['sync_data']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


