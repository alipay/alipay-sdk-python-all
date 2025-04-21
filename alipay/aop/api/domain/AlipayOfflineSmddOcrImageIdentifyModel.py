#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineSmddOcrImageIdentifyModel(object):

    def __init__(self):
        self._afts_url = None
        self._ocr_type = None

    @property
    def afts_url(self):
        return self._afts_url

    @afts_url.setter
    def afts_url(self, value):
        self._afts_url = value
    @property
    def ocr_type(self):
        return self._ocr_type

    @ocr_type.setter
    def ocr_type(self, value):
        self._ocr_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.afts_url:
            if hasattr(self.afts_url, 'to_alipay_dict'):
                params['afts_url'] = self.afts_url.to_alipay_dict()
            else:
                params['afts_url'] = self.afts_url
        if self.ocr_type:
            if hasattr(self.ocr_type, 'to_alipay_dict'):
                params['ocr_type'] = self.ocr_type.to_alipay_dict()
            else:
                params['ocr_type'] = self.ocr_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineSmddOcrImageIdentifyModel()
        if 'afts_url' in d:
            o.afts_url = d['afts_url']
        if 'ocr_type' in d:
            o.ocr_type = d['ocr_type']
        return o


