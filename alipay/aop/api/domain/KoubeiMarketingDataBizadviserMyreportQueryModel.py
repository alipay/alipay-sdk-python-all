#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataBizadviserMyreportQueryModel(object):

    def __init__(self):
        self._req_parameters = None
        self._uniq_key = None
        self._user_id = None

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
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataBizadviserMyreportQueryModel()
        if 'req_parameters' in d:
            o.req_parameters = d['req_parameters']
        if 'uniq_key' in d:
            o.uniq_key = d['uniq_key']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


