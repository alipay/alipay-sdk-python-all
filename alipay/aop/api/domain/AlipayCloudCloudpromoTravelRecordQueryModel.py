#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoTravelRecordQueryModel(object):

    def __init__(self):
        self._record_id = None
        self._source_id = None
        self._source_u_id = None

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_u_id(self):
        return self._source_u_id

    @source_u_id.setter
    def source_u_id(self, value):
        self._source_u_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.source_u_id:
            if hasattr(self.source_u_id, 'to_alipay_dict'):
                params['source_u_id'] = self.source_u_id.to_alipay_dict()
            else:
                params['source_u_id'] = self.source_u_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoTravelRecordQueryModel()
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_u_id' in d:
            o.source_u_id = d['source_u_id']
        return o


