#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SourceVO(object):

    def __init__(self):
        self._source_group = None
        self._source_id = None
        self._source_no = None
        self._source_time = None
        self._treat_date = None

    @property
    def source_group(self):
        return self._source_group

    @source_group.setter
    def source_group(self, value):
        self._source_group = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_no(self):
        return self._source_no

    @source_no.setter
    def source_no(self, value):
        self._source_no = value
    @property
    def source_time(self):
        return self._source_time

    @source_time.setter
    def source_time(self, value):
        self._source_time = value
    @property
    def treat_date(self):
        return self._treat_date

    @treat_date.setter
    def treat_date(self, value):
        self._treat_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.source_group:
            if hasattr(self.source_group, 'to_alipay_dict'):
                params['source_group'] = self.source_group.to_alipay_dict()
            else:
                params['source_group'] = self.source_group
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.source_no:
            if hasattr(self.source_no, 'to_alipay_dict'):
                params['source_no'] = self.source_no.to_alipay_dict()
            else:
                params['source_no'] = self.source_no
        if self.source_time:
            if hasattr(self.source_time, 'to_alipay_dict'):
                params['source_time'] = self.source_time.to_alipay_dict()
            else:
                params['source_time'] = self.source_time
        if self.treat_date:
            if hasattr(self.treat_date, 'to_alipay_dict'):
                params['treat_date'] = self.treat_date.to_alipay_dict()
            else:
                params['treat_date'] = self.treat_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SourceVO()
        if 'source_group' in d:
            o.source_group = d['source_group']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_no' in d:
            o.source_no = d['source_no']
        if 'source_time' in d:
            o.source_time = d['source_time']
        if 'treat_date' in d:
            o.treat_date = d['treat_date']
        return o


