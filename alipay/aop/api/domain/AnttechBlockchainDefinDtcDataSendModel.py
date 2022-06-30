#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinDtcDataSendModel(object):

    def __init__(self):
        self._api_code = None
        self._biz_param = None
        self._request_id = None

    @property
    def api_code(self):
        return self._api_code

    @api_code.setter
    def api_code(self, value):
        self._api_code = value
    @property
    def biz_param(self):
        return self._biz_param

    @biz_param.setter
    def biz_param(self, value):
        self._biz_param = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_code:
            if hasattr(self.api_code, 'to_alipay_dict'):
                params['api_code'] = self.api_code.to_alipay_dict()
            else:
                params['api_code'] = self.api_code
        if self.biz_param:
            if hasattr(self.biz_param, 'to_alipay_dict'):
                params['biz_param'] = self.biz_param.to_alipay_dict()
            else:
                params['biz_param'] = self.biz_param
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinDtcDataSendModel()
        if 'api_code' in d:
            o.api_code = d['api_code']
        if 'biz_param' in d:
            o.biz_param = d['biz_param']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


