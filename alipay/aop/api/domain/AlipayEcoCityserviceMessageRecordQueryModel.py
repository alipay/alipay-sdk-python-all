#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcoMessageRecordQuery import EcoMessageRecordQuery


class AlipayEcoCityserviceMessageRecordQueryModel(object):

    def __init__(self):
        self._batch_size = None
        self._begin_time = None
        self._encrypt_type = None
        self._end_time = None
        self._msg_list = None

    @property
    def batch_size(self):
        return self._batch_size

    @batch_size.setter
    def batch_size(self, value):
        self._batch_size = value
    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def encrypt_type(self):
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, value):
        self._encrypt_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def msg_list(self):
        return self._msg_list

    @msg_list.setter
    def msg_list(self, value):
        if isinstance(value, list):
            self._msg_list = list()
            for i in value:
                if isinstance(i, EcoMessageRecordQuery):
                    self._msg_list.append(i)
                else:
                    self._msg_list.append(EcoMessageRecordQuery.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.batch_size:
            if hasattr(self.batch_size, 'to_alipay_dict'):
                params['batch_size'] = self.batch_size.to_alipay_dict()
            else:
                params['batch_size'] = self.batch_size
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.encrypt_type:
            if hasattr(self.encrypt_type, 'to_alipay_dict'):
                params['encrypt_type'] = self.encrypt_type.to_alipay_dict()
            else:
                params['encrypt_type'] = self.encrypt_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.msg_list:
            if isinstance(self.msg_list, list):
                for i in range(0, len(self.msg_list)):
                    element = self.msg_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.msg_list[i] = element.to_alipay_dict()
            if hasattr(self.msg_list, 'to_alipay_dict'):
                params['msg_list'] = self.msg_list.to_alipay_dict()
            else:
                params['msg_list'] = self.msg_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCityserviceMessageRecordQueryModel()
        if 'batch_size' in d:
            o.batch_size = d['batch_size']
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'encrypt_type' in d:
            o.encrypt_type = d['encrypt_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'msg_list' in d:
            o.msg_list = d['msg_list']
        return o


