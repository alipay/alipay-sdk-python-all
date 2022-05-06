#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MarketingAuthorizedData import MarketingAuthorizedData
from alipay.aop.api.domain.MarketingPartner import MarketingPartner


class AlipayMarketingPartnershipsBatchqueryModel(object):

    def __init__(self):
        self._authorized_data = None
        self._page_num = None
        self._page_size = None
        self._partner = None
        self._status = None

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
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def partner(self):
        return self._partner

    @partner.setter
    def partner(self, value):
        if isinstance(value, MarketingPartner):
            self._partner = value
        else:
            self._partner = MarketingPartner.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorized_data:
            if hasattr(self.authorized_data, 'to_alipay_dict'):
                params['authorized_data'] = self.authorized_data.to_alipay_dict()
            else:
                params['authorized_data'] = self.authorized_data
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.partner:
            if hasattr(self.partner, 'to_alipay_dict'):
                params['partner'] = self.partner.to_alipay_dict()
            else:
                params['partner'] = self.partner
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingPartnershipsBatchqueryModel()
        if 'authorized_data' in d:
            o.authorized_data = d['authorized_data']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'partner' in d:
            o.partner = d['partner']
        if 'status' in d:
            o.status = d['status']
        return o


