#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BehaviorQueryRequest(object):

    def __init__(self):
        self._feature = None
        self._object_id = None
        self._object_type = None
        self._relation_type = None
        self._report_date = None

    @property
    def feature(self):
        return self._feature

    @feature.setter
    def feature(self, value):
        self._feature = value
    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value
    @property
    def object_type(self):
        return self._object_type

    @object_type.setter
    def object_type(self, value):
        self._object_type = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.feature:
            if hasattr(self.feature, 'to_alipay_dict'):
                params['feature'] = self.feature.to_alipay_dict()
            else:
                params['feature'] = self.feature
        if self.object_id:
            if hasattr(self.object_id, 'to_alipay_dict'):
                params['object_id'] = self.object_id.to_alipay_dict()
            else:
                params['object_id'] = self.object_id
        if self.object_type:
            if hasattr(self.object_type, 'to_alipay_dict'):
                params['object_type'] = self.object_type.to_alipay_dict()
            else:
                params['object_type'] = self.object_type
        if self.relation_type:
            if hasattr(self.relation_type, 'to_alipay_dict'):
                params['relation_type'] = self.relation_type.to_alipay_dict()
            else:
                params['relation_type'] = self.relation_type
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BehaviorQueryRequest()
        if 'feature' in d:
            o.feature = d['feature']
        if 'object_id' in d:
            o.object_id = d['object_id']
        if 'object_type' in d:
            o.object_type = d['object_type']
        if 'relation_type' in d:
            o.relation_type = d['relation_type']
        if 'report_date' in d:
            o.report_date = d['report_date']
        return o


