#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPointTaskCompleteModel(object):

    def __init__(self):
        self._biz_time = None
        self._kz_info = None
        self._open_id = None
        self._out_idem_id = None
        self._source = None
        self._task_id = None
        self._user_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def kz_info(self):
        return self._kz_info

    @kz_info.setter
    def kz_info(self, value):
        self._kz_info = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_idem_id(self):
        return self._out_idem_id

    @out_idem_id.setter
    def out_idem_id(self, value):
        self._out_idem_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.kz_info:
            if hasattr(self.kz_info, 'to_alipay_dict'):
                params['kz_info'] = self.kz_info.to_alipay_dict()
            else:
                params['kz_info'] = self.kz_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_idem_id:
            if hasattr(self.out_idem_id, 'to_alipay_dict'):
                params['out_idem_id'] = self.out_idem_id.to_alipay_dict()
            else:
                params['out_idem_id'] = self.out_idem_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
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
        o = AlipayCommerceMedicalPointTaskCompleteModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'kz_info' in d:
            o.kz_info = d['kz_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_idem_id' in d:
            o.out_idem_id = d['out_idem_id']
        if 'source' in d:
            o.source = d['source']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


