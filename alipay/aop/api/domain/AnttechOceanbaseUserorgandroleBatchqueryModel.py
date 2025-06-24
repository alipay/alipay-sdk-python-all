#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseUserorgandroleBatchqueryModel(object):

    def __init__(self):
        self._end_time = None
        self._passport_id_list = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def passport_id_list(self):
        return self._passport_id_list

    @passport_id_list.setter
    def passport_id_list(self, value):
        if isinstance(value, list):
            self._passport_id_list = list()
            for i in value:
                self._passport_id_list.append(i)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.passport_id_list:
            if isinstance(self.passport_id_list, list):
                for i in range(0, len(self.passport_id_list)):
                    element = self.passport_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.passport_id_list[i] = element.to_alipay_dict()
            if hasattr(self.passport_id_list, 'to_alipay_dict'):
                params['passport_id_list'] = self.passport_id_list.to_alipay_dict()
            else:
                params['passport_id_list'] = self.passport_id_list
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseUserorgandroleBatchqueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'passport_id_list' in d:
            o.passport_id_list = d['passport_id_list']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


