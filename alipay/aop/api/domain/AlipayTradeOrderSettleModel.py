#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiRoyaltyDetailInfoPojo import OpenApiRoyaltyDetailInfoPojo


class AlipayTradeOrderSettleModel(object):

    def __init__(self):
        self._operator_id = None
        self._out_request_no = None
        self._royalty_parameters = None
        self._trade_no = None

    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def royalty_parameters(self):
        return self._royalty_parameters

    @royalty_parameters.setter
    def royalty_parameters(self, value):
        if isinstance(value, list):
            self._royalty_parameters = list()
            for i in value:
                if isinstance(i, OpenApiRoyaltyDetailInfoPojo):
                    self._royalty_parameters.append(i)
                else:
                    self._royalty_parameters.append(OpenApiRoyaltyDetailInfoPojo.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.royalty_parameters:
            if isinstance(self.royalty_parameters, list):
                for i in range(0, len(self.royalty_parameters)):
                    element = self.royalty_parameters[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_parameters[i] = element.to_alipay_dict()
            if hasattr(self.royalty_parameters, 'to_alipay_dict'):
                params['royalty_parameters'] = self.royalty_parameters.to_alipay_dict()
            else:
                params['royalty_parameters'] = self.royalty_parameters
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeOrderSettleModel()
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'royalty_parameters' in d:
            o.royalty_parameters = d['royalty_parameters']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


