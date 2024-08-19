#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAnalysisCommonRequest import OpenApiAnalysisCommonRequest


class AlipayCloudCloudpromoAnalysiscustomerConsumptionlevelQueryModel(object):

    def __init__(self):
        self._common_request = None
        self._trade_level_granularity = None

    @property
    def common_request(self):
        return self._common_request

    @common_request.setter
    def common_request(self, value):
        if isinstance(value, OpenApiAnalysisCommonRequest):
            self._common_request = value
        else:
            self._common_request = OpenApiAnalysisCommonRequest.from_alipay_dict(value)
    @property
    def trade_level_granularity(self):
        return self._trade_level_granularity

    @trade_level_granularity.setter
    def trade_level_granularity(self, value):
        self._trade_level_granularity = value


    def to_alipay_dict(self):
        params = dict()
        if self.common_request:
            if hasattr(self.common_request, 'to_alipay_dict'):
                params['common_request'] = self.common_request.to_alipay_dict()
            else:
                params['common_request'] = self.common_request
        if self.trade_level_granularity:
            if hasattr(self.trade_level_granularity, 'to_alipay_dict'):
                params['trade_level_granularity'] = self.trade_level_granularity.to_alipay_dict()
            else:
                params['trade_level_granularity'] = self.trade_level_granularity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoAnalysiscustomerConsumptionlevelQueryModel()
        if 'common_request' in d:
            o.common_request = d['common_request']
        if 'trade_level_granularity' in d:
            o.trade_level_granularity = d['trade_level_granularity']
        return o


