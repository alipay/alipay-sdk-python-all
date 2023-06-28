#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtCmallStatusSyncModel(object):

    def __init__(self):
        self._goods_data_source = None
        self._goods_source_value = None
        self._status = None

    @property
    def goods_data_source(self):
        return self._goods_data_source

    @goods_data_source.setter
    def goods_data_source(self, value):
        self._goods_data_source = value
    @property
    def goods_source_value(self):
        return self._goods_source_value

    @goods_source_value.setter
    def goods_source_value(self, value):
        self._goods_source_value = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_data_source:
            if hasattr(self.goods_data_source, 'to_alipay_dict'):
                params['goods_data_source'] = self.goods_data_source.to_alipay_dict()
            else:
                params['goods_data_source'] = self.goods_data_source
        if self.goods_source_value:
            if hasattr(self.goods_source_value, 'to_alipay_dict'):
                params['goods_source_value'] = self.goods_source_value.to_alipay_dict()
            else:
                params['goods_source_value'] = self.goods_source_value
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
        o = AlipayDigitalmgmtCmallStatusSyncModel()
        if 'goods_data_source' in d:
            o.goods_data_source = d['goods_data_source']
        if 'goods_source_value' in d:
            o.goods_source_value = d['goods_source_value']
        if 'status' in d:
            o.status = d['status']
        return o


