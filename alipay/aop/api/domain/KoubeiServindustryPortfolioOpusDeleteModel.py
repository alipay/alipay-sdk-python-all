#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PortfolioOperatorInfo import PortfolioOperatorInfo


class KoubeiServindustryPortfolioOpusDeleteModel(object):

    def __init__(self):
        self._opus_ids = None
        self._portfolio_operator_info = None

    @property
    def opus_ids(self):
        return self._opus_ids

    @opus_ids.setter
    def opus_ids(self, value):
        if isinstance(value, list):
            self._opus_ids = list()
            for i in value:
                self._opus_ids.append(i)
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
        if self.opus_ids:
            if isinstance(self.opus_ids, list):
                for i in range(0, len(self.opus_ids)):
                    element = self.opus_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.opus_ids[i] = element.to_alipay_dict()
            if hasattr(self.opus_ids, 'to_alipay_dict'):
                params['opus_ids'] = self.opus_ids.to_alipay_dict()
            else:
                params['opus_ids'] = self.opus_ids
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
        o = KoubeiServindustryPortfolioOpusDeleteModel()
        if 'opus_ids' in d:
            o.opus_ids = d['opus_ids']
        if 'portfolio_operator_info' in d:
            o.portfolio_operator_info = d['portfolio_operator_info']
        return o


