#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QualityDetectDetail(object):

    def __init__(self):
        self._burning_time_stamp = None
        self._detect_detail = None
        self._dynamic_nfc_url = None
        self._nfc_url = None
        self._quality_time_stamp = None
        self._unique_id = None

    @property
    def burning_time_stamp(self):
        return self._burning_time_stamp

    @burning_time_stamp.setter
    def burning_time_stamp(self, value):
        self._burning_time_stamp = value
    @property
    def detect_detail(self):
        return self._detect_detail

    @detect_detail.setter
    def detect_detail(self, value):
        self._detect_detail = value
    @property
    def dynamic_nfc_url(self):
        return self._dynamic_nfc_url

    @dynamic_nfc_url.setter
    def dynamic_nfc_url(self, value):
        self._dynamic_nfc_url = value
    @property
    def nfc_url(self):
        return self._nfc_url

    @nfc_url.setter
    def nfc_url(self, value):
        self._nfc_url = value
    @property
    def quality_time_stamp(self):
        return self._quality_time_stamp

    @quality_time_stamp.setter
    def quality_time_stamp(self, value):
        self._quality_time_stamp = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.burning_time_stamp:
            if hasattr(self.burning_time_stamp, 'to_alipay_dict'):
                params['burning_time_stamp'] = self.burning_time_stamp.to_alipay_dict()
            else:
                params['burning_time_stamp'] = self.burning_time_stamp
        if self.detect_detail:
            if hasattr(self.detect_detail, 'to_alipay_dict'):
                params['detect_detail'] = self.detect_detail.to_alipay_dict()
            else:
                params['detect_detail'] = self.detect_detail
        if self.dynamic_nfc_url:
            if hasattr(self.dynamic_nfc_url, 'to_alipay_dict'):
                params['dynamic_nfc_url'] = self.dynamic_nfc_url.to_alipay_dict()
            else:
                params['dynamic_nfc_url'] = self.dynamic_nfc_url
        if self.nfc_url:
            if hasattr(self.nfc_url, 'to_alipay_dict'):
                params['nfc_url'] = self.nfc_url.to_alipay_dict()
            else:
                params['nfc_url'] = self.nfc_url
        if self.quality_time_stamp:
            if hasattr(self.quality_time_stamp, 'to_alipay_dict'):
                params['quality_time_stamp'] = self.quality_time_stamp.to_alipay_dict()
            else:
                params['quality_time_stamp'] = self.quality_time_stamp
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
        if 'burning_time_stamp' in d:
            o.burning_time_stamp = d['burning_time_stamp']
        if 'detect_detail' in d:
            o.detect_detail = d['detect_detail']
        if 'dynamic_nfc_url' in d:
            o.dynamic_nfc_url = d['dynamic_nfc_url']
        if 'nfc_url' in d:
            o.nfc_url = d['nfc_url']
        if 'quality_time_stamp' in d:
            o.quality_time_stamp = d['quality_time_stamp']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


