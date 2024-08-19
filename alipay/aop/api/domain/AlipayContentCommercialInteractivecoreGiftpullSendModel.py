#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentCommercialInteractivecoreGiftpullSendModel(object):

    def __init__(self):
        self._biz_token = None
        self._msg_id = None
        self._query_start_time = None
        self._ts = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def query_start_time(self):
        return self._query_start_time

    @query_start_time.setter
    def query_start_time(self, value):
        self._query_start_time = value
    @property
    def ts(self):
        return self._ts

    @ts.setter
    def ts(self, value):
        self._ts = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.query_start_time:
            if hasattr(self.query_start_time, 'to_alipay_dict'):
                params['query_start_time'] = self.query_start_time.to_alipay_dict()
            else:
                params['query_start_time'] = self.query_start_time
        if self.ts:
            if hasattr(self.ts, 'to_alipay_dict'):
                params['ts'] = self.ts.to_alipay_dict()
            else:
                params['ts'] = self.ts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentCommercialInteractivecoreGiftpullSendModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'query_start_time' in d:
            o.query_start_time = d['query_start_time']
        if 'ts' in d:
            o.ts = d['ts']
        return o


