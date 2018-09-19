#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInneraccountPidQueryModel(object):

    def __init__(self):
        self._client_type = None
        self._out_biz_id = None

    @property
    def client_type(self):
        return self._client_type

    @client_type.setter
    def client_type(self, value):
        self._client_type = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_type:
            if hasattr(self.client_type, 'to_alipay_dict'):
                params['client_type'] = self.client_type.to_alipay_dict()
            else:
                params['client_type'] = self.client_type
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInneraccountPidQueryModel()
        if 'client_type' in d:
            o.client_type = d['client_type']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        return o


