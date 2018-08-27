#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpusInfo import OpusInfo
from alipay.aop.api.domain.PortfolioOperatorInfo import PortfolioOperatorInfo


class KoubeiServindustryPortfolioOpusCreateModel(object):

    def __init__(self):
        self._commodity_id = None
        self._opuses = None
        self._portfolio_id = None
        self._portfolio_operator_info = None

    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def opuses(self):
        return self._opuses

    @opuses.setter
    def opuses(self, value):
        if isinstance(value, list):
            self._opuses = list()
            for i in value:
                if isinstance(i, OpusInfo):
                    self._opuses.append(i)
                else:
                    self._opuses.append(OpusInfo.from_alipay_dict(i))
    @property
    def portfolio_id(self):
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, value):
        self._portfolio_id = value
    @property
    def portfolio_operator_info(self):
        return self._portfolio_operator_info

    @portfolio_operator_info.setter
    def portfolio_operator_info(self, value):
        if isinstance(value, PortfolioOperatorInfo):
            self._portfolio_operator_info = value
        else:
            self._portfolio_operator_info = PortfolioOperatorInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_id:
            if hasattr(self.commodity_id, 'to_alipay_dict'):
                params['commodity_id'] = self.commodity_id.to_alipay_dict()
            else:
                params['commodity_id'] = self.commodity_id
        if self.opuses:
            if isinstance(self.opuses, list):
                for i in range(0, len(self.opuses)):
                    element = self.opuses[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.opuses[i] = element.to_alipay_dict()
            if hasattr(self.opuses, 'to_alipay_dict'):
                params['opuses'] = self.opuses.to_alipay_dict()
            else:
                params['opuses'] = self.opuses
        if self.portfolio_id:
            if hasattr(self.portfolio_id, 'to_alipay_dict'):
                params['portfolio_id'] = self.portfolio_id.to_alipay_dict()
            else:
                params['portfolio_id'] = self.portfolio_id
        if self.portfolio_operator_info:
            if hasattr(self.portfolio_operator_info, 'to_alipay_dict'):
                params['portfolio_operator_info'] = self.portfolio_operator_info.to_alipay_dict()
            else:
                params['portfolio_operator_info'] = self.portfolio_operator_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiServindustryPortfolioOpusCreateModel()
        if 'commodity_id' in d:
            o.commodity_id = d['commodity_id']
        if 'opuses' in d:
            o.opuses = d['opuses']
        if 'portfolio_id' in d:
            o.portfolio_id = d['portfolio_id']
        if 'portfolio_operator_info' in d:
            o.portfolio_operator_info = d['portfolio_operator_info']
        return o


