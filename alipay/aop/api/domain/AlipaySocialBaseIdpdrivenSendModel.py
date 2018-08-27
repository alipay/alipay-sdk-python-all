#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseIdpdrivenSendModel(object):

    def __init__(self):
        self._asset_id = None
        self._data = None
        self._data_time = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def data_time(self):
        return self._data_time

    @data_time.setter
    def data_time(self, value):
        self._data_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.data_time:
            if hasattr(self.data_time, 'to_alipay_dict'):
                params['data_time'] = self.data_time.to_alipay_dict()
            else:
                params['data_time'] = self.data_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseIdpdrivenSendModel()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'data' in d:
            o.data = d['data']
        if 'data_time' in d:
            o.data_time = d['data_time']
        return o


