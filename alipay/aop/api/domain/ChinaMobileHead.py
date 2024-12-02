#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChinaMobileHead(object):

    def __init__(self):
        self._api_id = None
        self._channel_code = None
        self._china_mobile_sign = None
        self._china_mobile_version = None
        self._req_time = None
        self._transaction_id = None

    @property
    def api_id(self):
        return self._api_id

    @api_id.setter
    def api_id(self, value):
        self._api_id = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def china_mobile_sign(self):
        return self._china_mobile_sign

    @china_mobile_sign.setter
    def china_mobile_sign(self, value):
        self._china_mobile_sign = value
    @property
    def china_mobile_version(self):
        return self._china_mobile_version

    @china_mobile_version.setter
    def china_mobile_version(self, value):
        self._china_mobile_version = value
    @property
    def req_time(self):
        return self._req_time

    @req_time.setter
    def req_time(self, value):
        self._req_time = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_id:
            if hasattr(self.api_id, 'to_alipay_dict'):
                params['api_id'] = self.api_id.to_alipay_dict()
            else:
                params['api_id'] = self.api_id
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.china_mobile_sign:
            if hasattr(self.china_mobile_sign, 'to_alipay_dict'):
                params['china_mobile_sign'] = self.china_mobile_sign.to_alipay_dict()
            else:
                params['china_mobile_sign'] = self.china_mobile_sign
        if self.china_mobile_version:
            if hasattr(self.china_mobile_version, 'to_alipay_dict'):
                params['china_mobile_version'] = self.china_mobile_version.to_alipay_dict()
            else:
                params['china_mobile_version'] = self.china_mobile_version
        if self.req_time:
            if hasattr(self.req_time, 'to_alipay_dict'):
                params['req_time'] = self.req_time.to_alipay_dict()
            else:
                params['req_time'] = self.req_time
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChinaMobileHead()
        if 'api_id' in d:
            o.api_id = d['api_id']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'china_mobile_sign' in d:
            o.china_mobile_sign = d['china_mobile_sign']
        if 'china_mobile_version' in d:
            o.china_mobile_version = d['china_mobile_version']
        if 'req_time' in d:
            o.req_time = d['req_time']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


