#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdProductModifyModel(object):

    def __init__(self):
        self._alipay_pid = None
        self._biz_token = None
        self._entity_type = None
        self._out_id = None
        self._source = None
        self._source_status = None

    @property
    def alipay_pid(self):
        return self._alipay_pid

    @alipay_pid.setter
    def alipay_pid(self, value):
        self._alipay_pid = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def source_status(self):
        return self._source_status

    @source_status.setter
    def source_status(self, value):
        self._source_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pid:
            if hasattr(self.alipay_pid, 'to_alipay_dict'):
                params['alipay_pid'] = self.alipay_pid.to_alipay_dict()
            else:
                params['alipay_pid'] = self.alipay_pid
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.source_status:
            if hasattr(self.source_status, 'to_alipay_dict'):
                params['source_status'] = self.source_status.to_alipay_dict()
            else:
                params['source_status'] = self.source_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdProductModifyModel()
        if 'alipay_pid' in d:
            o.alipay_pid = d['alipay_pid']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'source' in d:
            o.source = d['source']
        if 'source_status' in d:
            o.source_status = d['source_status']
        return o


