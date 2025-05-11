#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EbikeChargeQrcodeParam import EbikeChargeQrcodeParam


class AlipayCommerceTransportIndustryQrcodeCreateModel(object):

    def __init__(self):
        self._detail_list = None
        self._qr_code_type = None
        self._use_short_url = None

    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, list):
            self._detail_list = list()
            for i in value:
                if isinstance(i, EbikeChargeQrcodeParam):
                    self._detail_list.append(i)
                else:
                    self._detail_list.append(EbikeChargeQrcodeParam.from_alipay_dict(i))
    @property
    def qr_code_type(self):
        return self._qr_code_type

    @qr_code_type.setter
    def qr_code_type(self, value):
        self._qr_code_type = value
    @property
    def use_short_url(self):
        return self._use_short_url

    @use_short_url.setter
    def use_short_url(self, value):
        self._use_short_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_list:
            if isinstance(self.detail_list, list):
                for i in range(0, len(self.detail_list)):
                    element = self.detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_list[i] = element.to_alipay_dict()
            if hasattr(self.detail_list, 'to_alipay_dict'):
                params['detail_list'] = self.detail_list.to_alipay_dict()
            else:
                params['detail_list'] = self.detail_list
        if self.qr_code_type:
            if hasattr(self.qr_code_type, 'to_alipay_dict'):
                params['qr_code_type'] = self.qr_code_type.to_alipay_dict()
            else:
                params['qr_code_type'] = self.qr_code_type
        if self.use_short_url:
            if hasattr(self.use_short_url, 'to_alipay_dict'):
                params['use_short_url'] = self.use_short_url.to_alipay_dict()
            else:
                params['use_short_url'] = self.use_short_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIndustryQrcodeCreateModel()
        if 'detail_list' in d:
            o.detail_list = d['detail_list']
        if 'qr_code_type' in d:
            o.qr_code_type = d['qr_code_type']
        if 'use_short_url' in d:
            o.use_short_url = d['use_short_url']
        return o


