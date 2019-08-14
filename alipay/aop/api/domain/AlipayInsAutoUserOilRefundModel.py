#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoUserOilRefundModel(object):

    def __init__(self):
        self._exchange_request_id = None
        self._reason = None
        self._request_id = None
        self._source = None
        self._user_id = None

    @property
    def exchange_request_id(self):
        return self._exchange_request_id

    @exchange_request_id.setter
    def exchange_request_id(self, value):
        self._exchange_request_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.exchange_request_id:
            if hasattr(self.exchange_request_id, 'to_alipay_dict'):
                params['exchange_request_id'] = self.exchange_request_id.to_alipay_dict()
            else:
                params['exchange_request_id'] = self.exchange_request_id
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayInsAutoUserOilRefundModel()
        if 'exchange_request_id' in d:
            o.exchange_request_id = d['exchange_request_id']
        if 'reason' in d:
            o.reason = d['reason']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


