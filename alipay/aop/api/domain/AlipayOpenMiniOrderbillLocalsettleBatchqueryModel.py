#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniOrderbillLocalsettleBatchqueryModel(object):

    def __init__(self):
        self._page_size = None
        self._page_token = None
        self._settlement_date = None

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def page_token(self):
        return self._page_token

    @page_token.setter
    def page_token(self, value):
        self._page_token = value
    @property
    def settlement_date(self):
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, value):
        self._settlement_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.page_token:
            if hasattr(self.page_token, 'to_alipay_dict'):
                params['page_token'] = self.page_token.to_alipay_dict()
            else:
                params['page_token'] = self.page_token
        if self.settlement_date:
            if hasattr(self.settlement_date, 'to_alipay_dict'):
                params['settlement_date'] = self.settlement_date.to_alipay_dict()
            else:
                params['settlement_date'] = self.settlement_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniOrderbillLocalsettleBatchqueryModel()
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'page_token' in d:
            o.page_token = d['page_token']
        if 'settlement_date' in d:
            o.settlement_date = d['settlement_date']
        return o


