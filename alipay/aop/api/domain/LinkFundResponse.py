#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LinkFundResult import LinkFundResult


class LinkFundResponse(object):

    def __init__(self):
        self._fund_type = None
        self._link_funds = None

    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def link_funds(self):
        return self._link_funds

    @link_funds.setter
    def link_funds(self, value):
        if isinstance(value, list):
            self._link_funds = list()
            for i in value:
                if isinstance(i, LinkFundResult):
                    self._link_funds.append(i)
                else:
                    self._link_funds.append(LinkFundResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.link_funds:
            if isinstance(self.link_funds, list):
                for i in range(0, len(self.link_funds)):
                    element = self.link_funds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.link_funds[i] = element.to_alipay_dict()
            if hasattr(self.link_funds, 'to_alipay_dict'):
                params['link_funds'] = self.link_funds.to_alipay_dict()
            else:
                params['link_funds'] = self.link_funds
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LinkFundResponse()
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'link_funds' in d:
            o.link_funds = d['link_funds']
        return o


