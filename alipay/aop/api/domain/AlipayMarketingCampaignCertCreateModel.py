#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignCertCreateModel(object):

    def __init__(self):
        self._cert_name = None
        self._extend_info = None
        self._memo = None
        self._valid_count = None

    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def valid_count(self):
        return self._valid_count

    @valid_count.setter
    def valid_count(self, value):
        self._valid_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.valid_count:
            if hasattr(self.valid_count, 'to_alipay_dict'):
                params['valid_count'] = self.valid_count.to_alipay_dict()
            else:
                params['valid_count'] = self.valid_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignCertCreateModel()
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'memo' in d:
            o.memo = d['memo']
        if 'valid_count' in d:
            o.valid_count = d['valid_count']
        return o


