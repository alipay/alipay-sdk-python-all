#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoyaltyDetailInfo import RoyaltyDetailInfo


class AlipayTradeBatchTransferModel(object):

    def __init__(self):
        self._extend_params = None
        self._out_request_no = None
        self._royalty_parameters = None

    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
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
                if isinstance(i, RoyaltyDetailInfo):
                    self._royalty_parameters.append(i)
                else:
                    self._royalty_parameters.append(RoyaltyDetailInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeBatchTransferModel()
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'royalty_parameters' in d:
            o.royalty_parameters = d['royalty_parameters']
        return o


