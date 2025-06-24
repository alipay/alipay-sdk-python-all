#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseInvoiceStatusQueryModel(object):

    def __init__(self):
        self._open_api_id = None

    @property
    def open_api_id(self):
        return self._open_api_id

    @open_api_id.setter
    def open_api_id(self, value):
        self._open_api_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_api_id:
            if hasattr(self.open_api_id, 'to_alipay_dict'):
                params['open_api_id'] = self.open_api_id.to_alipay_dict()
            else:
                params['open_api_id'] = self.open_api_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseInvoiceStatusQueryModel()
        if 'open_api_id' in d:
            o.open_api_id = d['open_api_id']
        return o


