#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommercializationSyncDataReq(object):

    def __init__(self):
        self._data_link = None
        self._data_sync_type = None
        self._file_id = None
        self._request_id = None
        self._sync_timestamp = None

    @property
    def data_link(self):
        return self._data_link

    @data_link.setter
    def data_link(self, value):
        self._data_link = value
    @property
    def data_sync_type(self):
        return self._data_sync_type

    @data_sync_type.setter
    def data_sync_type(self, value):
        self._data_sync_type = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sync_timestamp(self):
        return self._sync_timestamp

    @sync_timestamp.setter
    def sync_timestamp(self, value):
        self._sync_timestamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_link:
            if hasattr(self.data_link, 'to_alipay_dict'):
                params['data_link'] = self.data_link.to_alipay_dict()
            else:
                params['data_link'] = self.data_link
        if self.data_sync_type:
            if hasattr(self.data_sync_type, 'to_alipay_dict'):
                params['data_sync_type'] = self.data_sync_type.to_alipay_dict()
            else:
                params['data_sync_type'] = self.data_sync_type
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.sync_timestamp:
            if hasattr(self.sync_timestamp, 'to_alipay_dict'):
                params['sync_timestamp'] = self.sync_timestamp.to_alipay_dict()
            else:
                params['sync_timestamp'] = self.sync_timestamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommercializationSyncDataReq()
        if 'data_link' in d:
            o.data_link = d['data_link']
        if 'data_sync_type' in d:
            o.data_sync_type = d['data_sync_type']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sync_timestamp' in d:
            o.sync_timestamp = d['sync_timestamp']
        return o


