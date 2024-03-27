#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MongoRollbackTaskHistory(object):

    def __init__(self):
        self._archive_time = None
        self._create_time = None
        self._history_id = None
        self._status = None

    @property
    def archive_time(self):
        return self._archive_time

    @archive_time.setter
    def archive_time(self, value):
        self._archive_time = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def history_id(self):
        return self._history_id

    @history_id.setter
    def history_id(self, value):
        self._history_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.archive_time:
            if hasattr(self.archive_time, 'to_alipay_dict'):
                params['archive_time'] = self.archive_time.to_alipay_dict()
            else:
                params['archive_time'] = self.archive_time
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.history_id:
            if hasattr(self.history_id, 'to_alipay_dict'):
                params['history_id'] = self.history_id.to_alipay_dict()
            else:
                params['history_id'] = self.history_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MongoRollbackTaskHistory()
        if 'archive_time' in d:
            o.archive_time = d['archive_time']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'history_id' in d:
            o.history_id = d['history_id']
        if 'status' in d:
            o.status = d['status']
        return o


