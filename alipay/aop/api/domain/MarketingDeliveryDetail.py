#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MarketingDeliveryDetail(object):

    def __init__(self):
        self._bind_id_list = None
        self._detail_id = None
        self._gmt_end = None
        self._gmt_start = None
        self._name = None
        self._status = None

    @property
    def bind_id_list(self):
        return self._bind_id_list

    @bind_id_list.setter
    def bind_id_list(self, value):
        if isinstance(value, list):
            self._bind_id_list = list()
            for i in value:
                self._bind_id_list.append(i)
    @property
    def detail_id(self):
        return self._detail_id

    @detail_id.setter
    def detail_id(self, value):
        self._detail_id = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_id_list:
            if isinstance(self.bind_id_list, list):
                for i in range(0, len(self.bind_id_list)):
                    element = self.bind_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bind_id_list[i] = element.to_alipay_dict()
            if hasattr(self.bind_id_list, 'to_alipay_dict'):
                params['bind_id_list'] = self.bind_id_list.to_alipay_dict()
            else:
                params['bind_id_list'] = self.bind_id_list
        if self.detail_id:
            if hasattr(self.detail_id, 'to_alipay_dict'):
                params['detail_id'] = self.detail_id.to_alipay_dict()
            else:
                params['detail_id'] = self.detail_id
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = MarketingDeliveryDetail()
        if 'bind_id_list' in d:
            o.bind_id_list = d['bind_id_list']
        if 'detail_id' in d:
            o.detail_id = d['detail_id']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        return o


