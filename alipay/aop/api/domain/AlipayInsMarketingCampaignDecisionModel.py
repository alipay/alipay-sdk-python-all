#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsMarketingCampaignDecisionModel(object):

    def __init__(self):
        self._business_type = None
        self._market_types = None
        self._mkt_obj_id = None
        self._mkt_obj_type = None
        self._request_id = None

    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def market_types(self):
        return self._market_types

    @market_types.setter
    def market_types(self, value):
        if isinstance(value, list):
            self._market_types = list()
            for i in value:
                self._market_types.append(i)
    @property
    def mkt_obj_id(self):
        return self._mkt_obj_id

    @mkt_obj_id.setter
    def mkt_obj_id(self, value):
        self._mkt_obj_id = value
    @property
    def mkt_obj_type(self):
        return self._mkt_obj_type

    @mkt_obj_type.setter
    def mkt_obj_type(self, value):
        self._mkt_obj_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.market_types:
            if isinstance(self.market_types, list):
                for i in range(0, len(self.market_types)):
                    element = self.market_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.market_types[i] = element.to_alipay_dict()
            if hasattr(self.market_types, 'to_alipay_dict'):
                params['market_types'] = self.market_types.to_alipay_dict()
            else:
                params['market_types'] = self.market_types
        if self.mkt_obj_id:
            if hasattr(self.mkt_obj_id, 'to_alipay_dict'):
                params['mkt_obj_id'] = self.mkt_obj_id.to_alipay_dict()
            else:
                params['mkt_obj_id'] = self.mkt_obj_id
        if self.mkt_obj_type:
            if hasattr(self.mkt_obj_type, 'to_alipay_dict'):
                params['mkt_obj_type'] = self.mkt_obj_type.to_alipay_dict()
            else:
                params['mkt_obj_type'] = self.mkt_obj_type
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
        o = AlipayInsMarketingCampaignDecisionModel()
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'market_types' in d:
            o.market_types = d['market_types']
        if 'mkt_obj_id' in d:
            o.mkt_obj_id = d['mkt_obj_id']
        if 'mkt_obj_type' in d:
            o.mkt_obj_type = d['mkt_obj_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


