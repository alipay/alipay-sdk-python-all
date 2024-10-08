#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransportInfo(object):

    def __init__(self):
        self._afts_url = None
        self._batch_id = None

    @property
    def afts_url(self):
        return self._afts_url

    @afts_url.setter
    def afts_url(self, value):
        self._afts_url = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.afts_url:
            if hasattr(self.afts_url, 'to_alipay_dict'):
                params['afts_url'] = self.afts_url.to_alipay_dict()
            else:
                params['afts_url'] = self.afts_url
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransportInfo()
        if 'afts_url' in d:
            o.afts_url = d['afts_url']
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        return o


