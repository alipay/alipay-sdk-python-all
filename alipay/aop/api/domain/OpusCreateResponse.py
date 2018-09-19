#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpusCreateResponse(object):

    def __init__(self):
        self._external_opus_id = None
        self._opus_id = None

    @property
    def external_opus_id(self):
        return self._external_opus_id

    @external_opus_id.setter
    def external_opus_id(self, value):
        self._external_opus_id = value
    @property
    def opus_id(self):
        return self._opus_id

    @opus_id.setter
    def opus_id(self, value):
        self._opus_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_opus_id:
            if hasattr(self.external_opus_id, 'to_alipay_dict'):
                params['external_opus_id'] = self.external_opus_id.to_alipay_dict()
            else:
                params['external_opus_id'] = self.external_opus_id
        if self.opus_id:
            if hasattr(self.opus_id, 'to_alipay_dict'):
                params['opus_id'] = self.opus_id.to_alipay_dict()
            else:
                params['opus_id'] = self.opus_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpusCreateResponse()
        if 'external_opus_id' in d:
            o.external_opus_id = d['external_opus_id']
        if 'opus_id' in d:
            o.opus_id = d['opus_id']
        return o


