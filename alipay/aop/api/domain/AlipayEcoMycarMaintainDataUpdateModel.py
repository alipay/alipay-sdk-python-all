#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarMaintainDataUpdateModel(object):

    def __init__(self):
        self._biz_id = None
        self._event_id = None
        self._source = None
        self._type_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def type_id(self):
        return self._type_id

    @type_id.setter
    def type_id(self, value):
        self._type_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.event_id:
            if hasattr(self.event_id, 'to_alipay_dict'):
                params['event_id'] = self.event_id.to_alipay_dict()
            else:
                params['event_id'] = self.event_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.type_id:
            if hasattr(self.type_id, 'to_alipay_dict'):
                params['type_id'] = self.type_id.to_alipay_dict()
            else:
                params['type_id'] = self.type_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarMaintainDataUpdateModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'event_id' in d:
            o.event_id = d['event_id']
        if 'source' in d:
            o.source = d['source']
        if 'type_id' in d:
            o.type_id = d['type_id']
        return o


