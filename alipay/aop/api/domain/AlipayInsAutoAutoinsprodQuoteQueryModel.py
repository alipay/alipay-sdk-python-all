#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoAutoinsprodQuoteQueryModel(object):

    def __init__(self):
        self._enquiry_biz_id = None
        self._quote_biz_id = None

    @property
    def enquiry_biz_id(self):
        return self._enquiry_biz_id

    @enquiry_biz_id.setter
    def enquiry_biz_id(self, value):
        self._enquiry_biz_id = value
    @property
    def quote_biz_id(self):
        return self._quote_biz_id

    @quote_biz_id.setter
    def quote_biz_id(self, value):
        self._quote_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enquiry_biz_id:
            if hasattr(self.enquiry_biz_id, 'to_alipay_dict'):
                params['enquiry_biz_id'] = self.enquiry_biz_id.to_alipay_dict()
            else:
                params['enquiry_biz_id'] = self.enquiry_biz_id
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
        o = AlipayInsAutoAutoinsprodQuoteQueryModel()
        if 'enquiry_biz_id' in d:
            o.enquiry_biz_id = d['enquiry_biz_id']
        if 'quote_biz_id' in d:
            o.quote_biz_id = d['quote_biz_id']
        return o


