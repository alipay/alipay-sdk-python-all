#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IntlBrandInfo import IntlBrandInfo
from alipay.aop.api.domain.ExternalInfo import ExternalInfo


class AlipayOverseasTravelIntlBrandSyncModel(object):

    def __init__(self):
        self._brand_info = None
        self._external_list = None
        self._request_id = None

    @property
    def brand_info(self):
        return self._brand_info

    @brand_info.setter
    def brand_info(self, value):
        if isinstance(value, IntlBrandInfo):
            self._brand_info = value
        else:
            self._brand_info = IntlBrandInfo.from_alipay_dict(value)
    @property
    def external_list(self):
        return self._external_list

    @external_list.setter
    def external_list(self, value):
        if isinstance(value, list):
            self._external_list = list()
            for i in value:
                if isinstance(i, ExternalInfo):
                    self._external_list.append(i)
                else:
                    self._external_list.append(ExternalInfo.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_info:
            if hasattr(self.brand_info, 'to_alipay_dict'):
                params['brand_info'] = self.brand_info.to_alipay_dict()
            else:
                params['brand_info'] = self.brand_info
        if self.external_list:
            if isinstance(self.external_list, list):
                for i in range(0, len(self.external_list)):
                    element = self.external_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.external_list[i] = element.to_alipay_dict()
            if hasattr(self.external_list, 'to_alipay_dict'):
                params['external_list'] = self.external_list.to_alipay_dict()
            else:
                params['external_list'] = self.external_list
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelIntlBrandSyncModel()
        if 'brand_info' in d:
            o.brand_info = d['brand_info']
        if 'external_list' in d:
            o.external_list = d['external_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


