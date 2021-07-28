#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IntelligentGuideTradeDetail import IntelligentGuideTradeDetail


class InvalidTradeDetail(object):

    def __init__(self):
        self._error_message = None
        self._shop_id = None
        self._shop_name = None
        self._trade_detail = None

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def trade_detail(self):
        return self._trade_detail

    @trade_detail.setter
    def trade_detail(self, value):
        if isinstance(value, IntelligentGuideTradeDetail):
            self._trade_detail = value
        else:
            self._trade_detail = IntelligentGuideTradeDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.error_message:
            if hasattr(self.error_message, 'to_alipay_dict'):
                params['error_message'] = self.error_message.to_alipay_dict()
            else:
                params['error_message'] = self.error_message
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.trade_detail:
            if hasattr(self.trade_detail, 'to_alipay_dict'):
                params['trade_detail'] = self.trade_detail.to_alipay_dict()
            else:
                params['trade_detail'] = self.trade_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvalidTradeDetail()
        if 'error_message' in d:
            o.error_message = d['error_message']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'trade_detail' in d:
            o.trade_detail = d['trade_detail']
        return o


