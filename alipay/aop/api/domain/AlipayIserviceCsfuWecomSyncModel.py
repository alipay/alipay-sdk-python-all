#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCsfuWecomSyncModel(object):

    def __init__(self):
        self._data = None
        self._env_id = None
        self._event_timestamp = None
        self._id = None
        self._im_app_id = None
        self._source = None
        self._tnt_inst_id = None
        self._type = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def event_timestamp(self):
        return self._event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, value):
        self._event_timestamp = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def im_app_id(self):
        return self._im_app_id

    @im_app_id.setter
    def im_app_id(self, value):
        self._im_app_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.env_id:
            if hasattr(self.env_id, 'to_alipay_dict'):
                params['env_id'] = self.env_id.to_alipay_dict()
            else:
                params['env_id'] = self.env_id
        if self.event_timestamp:
            if hasattr(self.event_timestamp, 'to_alipay_dict'):
                params['event_timestamp'] = self.event_timestamp.to_alipay_dict()
            else:
                params['event_timestamp'] = self.event_timestamp
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.im_app_id:
            if hasattr(self.im_app_id, 'to_alipay_dict'):
                params['im_app_id'] = self.im_app_id.to_alipay_dict()
            else:
                params['im_app_id'] = self.im_app_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCsfuWecomSyncModel()
        if 'data' in d:
            o.data = d['data']
        if 'env_id' in d:
            o.env_id = d['env_id']
        if 'event_timestamp' in d:
            o.event_timestamp = d['event_timestamp']
        if 'id' in d:
            o.id = d['id']
        if 'im_app_id' in d:
            o.im_app_id = d['im_app_id']
        if 'source' in d:
            o.source = d['source']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'type' in d:
            o.type = d['type']
        return o


