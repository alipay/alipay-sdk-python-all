#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtHrcominsuInsuclaimAttachmentQueryModel(object):

    def __init__(self):
        self._attachment_url = None
        self._data_key = None

    @property
    def attachment_url(self):
        return self._attachment_url

    @attachment_url.setter
    def attachment_url(self, value):
        self._attachment_url = value
    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_url:
            if hasattr(self.attachment_url, 'to_alipay_dict'):
                params['attachment_url'] = self.attachment_url.to_alipay_dict()
            else:
                params['attachment_url'] = self.attachment_url
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrcominsuInsuclaimAttachmentQueryModel()
        if 'attachment_url' in d:
            o.attachment_url = d['attachment_url']
        if 'data_key' in d:
            o.data_key = d['data_key']
        return o


