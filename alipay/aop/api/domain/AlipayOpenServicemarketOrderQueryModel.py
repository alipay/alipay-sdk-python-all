#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenServicemarketOrderQueryModel(object):

    def __init__(self):
        self._commodity_order_id = None
        self._start_page = None

    @property
    def commodity_order_id(self):
        return self._commodity_order_id

    @commodity_order_id.setter
    def commodity_order_id(self, value):
        self._commodity_order_id = value
    @property
    def start_page(self):
        return self._start_page

    @start_page.setter
    def start_page(self, value):
        self._start_page = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_order_id:
            if hasattr(self.commodity_order_id, 'to_alipay_dict'):
                params['commodity_order_id'] = self.commodity_order_id.to_alipay_dict()
            else:
                params['commodity_order_id'] = self.commodity_order_id
        if self.start_page:
            if hasattr(self.start_page, 'to_alipay_dict'):
                params['start_page'] = self.start_page.to_alipay_dict()
            else:
                params['start_page'] = self.start_page
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenServicemarketOrderQueryModel()
        if 'commodity_order_id' in d:
            o.commodity_order_id = d['commodity_order_id']
        if 'start_page' in d:
            o.start_page = d['start_page']
        return o


