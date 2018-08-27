#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PortfolioOperatorInfo import PortfolioOperatorInfo


class KoubeiServindustryPortfolioDataDeleteModel(object):

    def __init__(self):
        self._portfolio_id = None
        self._portfolio_operator_info = None

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
        o = KoubeiServindustryPortfolioDataDeleteModel()
        if 'portfolio_id' in d:
            o.portfolio_id = d['portfolio_id']
        if 'portfolio_operator_info' in d:
            o.portfolio_operator_info = d['portfolio_operator_info']
        return o


