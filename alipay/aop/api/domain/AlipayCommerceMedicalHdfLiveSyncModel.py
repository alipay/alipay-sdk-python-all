#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfLiveSyncModel(object):

    def __init__(self):
        self._alipay_public_id = None
        self._live_stream_url = None
        self._out_doc_app_url = None
        self._out_doc_id = None
        self._out_doc_live_id = None
        self._out_name = None
        self._out_prepare_id = None

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
    @property
    def out_doc_app_url(self):
        return self._out_doc_app_url

    @out_doc_app_url.setter
    def out_doc_app_url(self, value):
        self._out_doc_app_url = value
    @property
    def out_doc_id(self):
        return self._out_doc_id

    @out_doc_id.setter
    def out_doc_id(self, value):
        self._out_doc_id = value
    @property
    def out_doc_live_id(self):
        return self._out_doc_live_id

    @out_doc_live_id.setter
    def out_doc_live_id(self, value):
        self._out_doc_live_id = value
    @property
    def out_name(self):
        return self._out_name

    @out_name.setter
    def out_name(self, value):
        self._out_name = value
    @property
    def out_prepare_id(self):
        return self._out_prepare_id

    @out_prepare_id.setter
    def out_prepare_id(self, value):
        self._out_prepare_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.out_doc_app_url:
            if hasattr(self.out_doc_app_url, 'to_alipay_dict'):
                params['out_doc_app_url'] = self.out_doc_app_url.to_alipay_dict()
            else:
                params['out_doc_app_url'] = self.out_doc_app_url
        if self.out_doc_id:
            if hasattr(self.out_doc_id, 'to_alipay_dict'):
                params['out_doc_id'] = self.out_doc_id.to_alipay_dict()
            else:
                params['out_doc_id'] = self.out_doc_id
        if self.out_doc_live_id:
            if hasattr(self.out_doc_live_id, 'to_alipay_dict'):
                params['out_doc_live_id'] = self.out_doc_live_id.to_alipay_dict()
            else:
                params['out_doc_live_id'] = self.out_doc_live_id
        if self.out_name:
            if hasattr(self.out_name, 'to_alipay_dict'):
                params['out_name'] = self.out_name.to_alipay_dict()
            else:
                params['out_name'] = self.out_name
        if self.out_prepare_id:
            if hasattr(self.out_prepare_id, 'to_alipay_dict'):
                params['out_prepare_id'] = self.out_prepare_id.to_alipay_dict()
            else:
                params['out_prepare_id'] = self.out_prepare_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfLiveSyncModel()
        if 'alipay_public_id' in d:
            o.alipay_public_id = d['alipay_public_id']
        if 'live_stream_url' in d:
            o.live_stream_url = d['live_stream_url']
        if 'out_doc_app_url' in d:
            o.out_doc_app_url = d['out_doc_app_url']
        if 'out_doc_id' in d:
            o.out_doc_id = d['out_doc_id']
        if 'out_doc_live_id' in d:
            o.out_doc_live_id = d['out_doc_live_id']
        if 'out_name' in d:
            o.out_name = d['out_name']
        if 'out_prepare_id' in d:
            o.out_prepare_id = d['out_prepare_id']
        return o


