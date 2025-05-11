#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLiveLiveroomStreamUploadModel(object):

    def __init__(self):
        self._alipay_live_id = None
        self._alipay_public_id = None
        self._live_stream_url = None

    @property
    def alipay_live_id(self):
        return self._alipay_live_id

    @alipay_live_id.setter
    def alipay_live_id(self, value):
        self._alipay_live_id = value
    @property
    def alipay_public_id(self):
        return self._alipay_public_id

    @alipay_public_id.setter
    def alipay_public_id(self, value):
        self._alipay_public_id = value
    @property
    def live_stream_url(self):
        return self._live_stream_url

    @live_stream_url.setter
    def live_stream_url(self, value):
        self._live_stream_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_live_id:
            if hasattr(self.alipay_live_id, 'to_alipay_dict'):
                params['alipay_live_id'] = self.alipay_live_id.to_alipay_dict()
            else:
                params['alipay_live_id'] = self.alipay_live_id
        if self.alipay_public_id:
            if hasattr(self.alipay_public_id, 'to_alipay_dict'):
                params['alipay_public_id'] = self.alipay_public_id.to_alipay_dict()
            else:
                params['alipay_public_id'] = self.alipay_public_id
        if self.live_stream_url:
            if hasattr(self.live_stream_url, 'to_alipay_dict'):
                params['live_stream_url'] = self.live_stream_url.to_alipay_dict()
            else:
                params['live_stream_url'] = self.live_stream_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLiveLiveroomStreamUploadModel()
        if 'alipay_live_id' in d:
            o.alipay_live_id = d['alipay_live_id']
        if 'alipay_public_id' in d:
            o.alipay_public_id = d['alipay_public_id']
        if 'live_stream_url' in d:
            o.live_stream_url = d['live_stream_url']
        return o


