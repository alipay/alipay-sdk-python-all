#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QuoteInfo(object):

    def __init__(self):
        self._company_id = None
        self._quote_biz_id = None

    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def quote_biz_id(self):
        return self._quote_biz_id

    @quote_biz_id.setter
    def quote_biz_id(self, value):
        self._quote_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.quote_biz_id:
            if hasattr(self.quote_biz_id, 'to_alipay_dict'):
                params['quote_biz_id'] = self.quote_biz_id.to_alipay_dict()
            else:
                params['quote_biz_id'] = self.quote_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuoteInfo()
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'quote_biz_id' in d:
            o.quote_biz_id = d['quote_biz_id']
        return o


