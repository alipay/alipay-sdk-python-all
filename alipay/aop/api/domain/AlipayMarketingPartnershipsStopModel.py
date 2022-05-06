#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MarketingAuthorizedData import MarketingAuthorizedData
from alipay.aop.api.domain.MarketingPartner import MarketingPartner


class AlipayMarketingPartnershipsStopModel(object):

    def __init__(self):
        self._authorized_data = None
        self._partner = None

    @property
    def authorized_data(self):
        return self._authorized_data

    @authorized_data.setter
    def authorized_data(self, value):
        if isinstance(value, MarketingAuthorizedData):
            self._authorized_data = value
        else:
            self._authorized_data = MarketingAuthorizedData.from_alipay_dict(value)
    @property
    def partner(self):
        return self._partner

    @partner.setter
    def partner(self, value):
        if isinstance(value, MarketingPartner):
            self._partner = value
        else:
            self._partner = MarketingPartner.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.authorized_data:
            if hasattr(self.authorized_data, 'to_alipay_dict'):
                params['authorized_data'] = self.authorized_data.to_alipay_dict()
            else:
                params['authorized_data'] = self.authorized_data
        if self.partner:
            if hasattr(self.partner, 'to_alipay_dict'):
                params['partner'] = self.partner.to_alipay_dict()
            else:
                params['partner'] = self.partner
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingPartnershipsStopModel()
        if 'authorized_data' in d:
            o.authorized_data = d['authorized_data']
        if 'partner' in d:
            o.partner = d['partner']
        return o


