#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneCouponSendModel(object):

    def __init__(self):
        self._channel_user_id = None
        self._channel_user_source = None
        self._dimension_id = None
        self._dimension_type = None
        self._market_type = None
        self._out_biz_no = None
        self._service_scenario = None

    @property
    def channel_user_id(self):
        return self._channel_user_id

    @channel_user_id.setter
    def channel_user_id(self, value):
        self._channel_user_id = value
    @property
    def channel_user_source(self):
        return self._channel_user_source

    @channel_user_source.setter
    def channel_user_source(self, value):
        self._channel_user_source = value
    @property
    def dimension_id(self):
        return self._dimension_id

    @dimension_id.setter
    def dimension_id(self, value):
        self._dimension_id = value
    @property
    def dimension_type(self):
        return self._dimension_type

    @dimension_type.setter
    def dimension_type(self, value):
        self._dimension_type = value
    @property
    def market_type(self):
        return self._market_type

    @market_type.setter
    def market_type(self, value):
        self._market_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def service_scenario(self):
        return self._service_scenario

    @service_scenario.setter
    def service_scenario(self, value):
        self._service_scenario = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_user_id:
            if hasattr(self.channel_user_id, 'to_alipay_dict'):
                params['channel_user_id'] = self.channel_user_id.to_alipay_dict()
            else:
                params['channel_user_id'] = self.channel_user_id
        if self.channel_user_source:
            if hasattr(self.channel_user_source, 'to_alipay_dict'):
                params['channel_user_source'] = self.channel_user_source.to_alipay_dict()
            else:
                params['channel_user_source'] = self.channel_user_source
        if self.dimension_id:
            if hasattr(self.dimension_id, 'to_alipay_dict'):
                params['dimension_id'] = self.dimension_id.to_alipay_dict()
            else:
                params['dimension_id'] = self.dimension_id
        if self.dimension_type:
            if hasattr(self.dimension_type, 'to_alipay_dict'):
                params['dimension_type'] = self.dimension_type.to_alipay_dict()
            else:
                params['dimension_type'] = self.dimension_type
        if self.market_type:
            if hasattr(self.market_type, 'to_alipay_dict'):
                params['market_type'] = self.market_type.to_alipay_dict()
            else:
                params['market_type'] = self.market_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.service_scenario:
            if hasattr(self.service_scenario, 'to_alipay_dict'):
                params['service_scenario'] = self.service_scenario.to_alipay_dict()
            else:
                params['service_scenario'] = self.service_scenario
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneCouponSendModel()
        if 'channel_user_id' in d:
            o.channel_user_id = d['channel_user_id']
        if 'channel_user_source' in d:
            o.channel_user_source = d['channel_user_source']
        if 'dimension_id' in d:
            o.dimension_id = d['dimension_id']
        if 'dimension_type' in d:
            o.dimension_type = d['dimension_type']
        if 'market_type' in d:
            o.market_type = d['market_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'service_scenario' in d:
            o.service_scenario = d['service_scenario']
        return o


