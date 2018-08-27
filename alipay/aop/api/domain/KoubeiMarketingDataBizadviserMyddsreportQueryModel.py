#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataBizadviserMyddsreportQueryModel(object):

    def __init__(self):
        self._req_parameters = None
        self._uniq_key = None

    @property
    def req_parameters(self):
        return self._req_parameters

    @req_parameters.setter
    def req_parameters(self, value):
        self._req_parameters = value
    @property
    def uniq_key(self):
        return self._uniq_key

    @uniq_key.setter
    def uniq_key(self, value):
        self._uniq_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.req_parameters:
            if hasattr(self.req_parameters, 'to_alipay_dict'):
                params['req_parameters'] = self.req_parameters.to_alipay_dict()
            else:
                params['req_parameters'] = self.req_parameters
        if self.uniq_key:
            if hasattr(self.uniq_key, 'to_alipay_dict'):
                params['uniq_key'] = self.uniq_key.to_alipay_dict()
            else:
                params['uniq_key'] = self.uniq_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataBizadviserMyddsreportQueryModel()
        if 'req_parameters' in d:
            o.req_parameters = d['req_parameters']
        if 'uniq_key' in d:
            o.uniq_key = d['uniq_key']
        return o


