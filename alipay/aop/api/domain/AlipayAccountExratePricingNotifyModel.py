#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PricingVO import PricingVO


class AlipayAccountExratePricingNotifyModel(object):

    def __init__(self):
        self._client_id = None
        self._inst = None
        self._pricing_list = None
        self._segment_id = None
        self._time_zone = None

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def inst(self):
        return self._inst

    @inst.setter
    def inst(self, value):
        self._inst = value
    @property
    def pricing_list(self):
        return self._pricing_list

    @pricing_list.setter
    def pricing_list(self, value):
        if isinstance(value, list):
            self._pricing_list = list()
            for i in value:
                if isinstance(i, PricingVO):
                    self._pricing_list.append(i)
                else:
                    self._pricing_list.append(PricingVO.from_alipay_dict(i))
    @property
    def segment_id(self):
        return self._segment_id

    @segment_id.setter
    def segment_id(self, value):
        self._segment_id = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.inst:
            if hasattr(self.inst, 'to_alipay_dict'):
                params['inst'] = self.inst.to_alipay_dict()
            else:
                params['inst'] = self.inst
        if self.pricing_list:
            if isinstance(self.pricing_list, list):
                for i in range(0, len(self.pricing_list)):
                    element = self.pricing_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pricing_list[i] = element.to_alipay_dict()
            if hasattr(self.pricing_list, 'to_alipay_dict'):
                params['pricing_list'] = self.pricing_list.to_alipay_dict()
            else:
                params['pricing_list'] = self.pricing_list
        if self.segment_id:
            if hasattr(self.segment_id, 'to_alipay_dict'):
                params['segment_id'] = self.segment_id.to_alipay_dict()
            else:
                params['segment_id'] = self.segment_id
        if self.time_zone:
            if hasattr(self.time_zone, 'to_alipay_dict'):
                params['time_zone'] = self.time_zone.to_alipay_dict()
            else:
                params['time_zone'] = self.time_zone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountExratePricingNotifyModel()
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'inst' in d:
            o.inst = d['inst']
        if 'pricing_list' in d:
            o.pricing_list = d['pricing_list']
        if 'segment_id' in d:
            o.segment_id = d['segment_id']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        return o


