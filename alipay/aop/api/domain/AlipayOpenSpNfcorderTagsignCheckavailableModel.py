#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNfcorderTagsignCheckavailableModel(object):

    def __init__(self):
        self._open_tag_id = None
        self._signature = None

    @property
    def open_tag_id(self):
        return self._open_tag_id

    @open_tag_id.setter
    def open_tag_id(self, value):
        self._open_tag_id = value
    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_tag_id:
            if hasattr(self.open_tag_id, 'to_alipay_dict'):
                params['open_tag_id'] = self.open_tag_id.to_alipay_dict()
            else:
                params['open_tag_id'] = self.open_tag_id
        if self.signature:
            if hasattr(self.signature, 'to_alipay_dict'):
                params['signature'] = self.signature.to_alipay_dict()
            else:
                params['signature'] = self.signature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNfcorderTagsignCheckavailableModel()
        if 'open_tag_id' in d:
            o.open_tag_id = d['open_tag_id']
        if 'signature' in d:
            o.signature = d['signature']
        return o


