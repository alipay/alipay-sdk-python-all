#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncGfsettleprodPresettleelementEffectModel(object):

    def __init__(self):
        self._enable_time = None
        self._idempotent_no_list = None
        self._source = None

    @property
    def enable_time(self):
        return self._enable_time

    @enable_time.setter
    def enable_time(self, value):
        self._enable_time = value
    @property
    def idempotent_no_list(self):
        return self._idempotent_no_list

    @idempotent_no_list.setter
    def idempotent_no_list(self, value):
        if isinstance(value, list):
            self._idempotent_no_list = list()
            for i in value:
                self._idempotent_no_list.append(i)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.enable_time:
            if hasattr(self.enable_time, 'to_alipay_dict'):
                params['enable_time'] = self.enable_time.to_alipay_dict()
            else:
                params['enable_time'] = self.enable_time
        if self.idempotent_no_list:
            if isinstance(self.idempotent_no_list, list):
                for i in range(0, len(self.idempotent_no_list)):
                    element = self.idempotent_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.idempotent_no_list[i] = element.to_alipay_dict()
            if hasattr(self.idempotent_no_list, 'to_alipay_dict'):
                params['idempotent_no_list'] = self.idempotent_no_list.to_alipay_dict()
            else:
                params['idempotent_no_list'] = self.idempotent_no_list
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodPresettleelementEffectModel()
        if 'enable_time' in d:
            o.enable_time = d['enable_time']
        if 'idempotent_no_list' in d:
            o.idempotent_no_list = d['idempotent_no_list']
        if 'source' in d:
            o.source = d['source']
        return o


