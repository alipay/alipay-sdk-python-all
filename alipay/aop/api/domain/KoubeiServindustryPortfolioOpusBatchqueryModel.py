#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiServindustryPortfolioOpusBatchqueryModel(object):

    def __init__(self):
        self._commodity_id = None
        self._page_no = None
        self._page_size = None
        self._portfolio_id = None

    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def portfolio_id(self):
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, value):
        self._portfolio_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_id:
            if hasattr(self.commodity_id, 'to_alipay_dict'):
                params['commodity_id'] = self.commodity_id.to_alipay_dict()
            else:
                params['commodity_id'] = self.commodity_id
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.portfolio_id:
            if hasattr(self.portfolio_id, 'to_alipay_dict'):
                params['portfolio_id'] = self.portfolio_id.to_alipay_dict()
            else:
                params['portfolio_id'] = self.portfolio_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiServindustryPortfolioOpusBatchqueryModel()
        if 'commodity_id' in d:
            o.commodity_id = d['commodity_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'portfolio_id' in d:
            o.portfolio_id = d['portfolio_id']
        return o


