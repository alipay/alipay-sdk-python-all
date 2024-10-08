#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QualityDetectDetail(object):

    def __init__(self):
        self._detect_detail = None
        self._nfc_url = None
        self._unique_id = None

    @property
    def detect_detail(self):
        return self._detect_detail

    @detect_detail.setter
    def detect_detail(self, value):
        self._detect_detail = value
    @property
    def nfc_url(self):
        return self._nfc_url

    @nfc_url.setter
    def nfc_url(self, value):
        self._nfc_url = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.detect_detail:
            if hasattr(self.detect_detail, 'to_alipay_dict'):
                params['detect_detail'] = self.detect_detail.to_alipay_dict()
            else:
                params['detect_detail'] = self.detect_detail
        if self.nfc_url:
            if hasattr(self.nfc_url, 'to_alipay_dict'):
                params['nfc_url'] = self.nfc_url.to_alipay_dict()
            else:
                params['nfc_url'] = self.nfc_url
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QualityDetectDetail()
        if 'detect_detail' in d:
            o.detect_detail = d['detect_detail']
        if 'nfc_url' in d:
            o.nfc_url = d['nfc_url']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


