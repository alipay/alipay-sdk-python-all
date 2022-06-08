#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessRelationTradeInfo import BusinessRelationTradeInfo


class BusinessRelationShopTradeInfo(object):

    def __init__(self):
        self._real_shop_id = None
        self._real_shop_no = None
        self._shop_confirm_status = None
        self._shop_name = None
        self._shop_trade_data_info = None

    @property
    def real_shop_id(self):
        return self._real_shop_id

    @real_shop_id.setter
    def real_shop_id(self, value):
        self._real_shop_id = value
    @property
    def real_shop_no(self):
        return self._real_shop_no

    @real_shop_no.setter
    def real_shop_no(self, value):
        self._real_shop_no = value
    @property
    def shop_confirm_status(self):
        return self._shop_confirm_status

    @shop_confirm_status.setter
    def shop_confirm_status(self, value):
        self._shop_confirm_status = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_trade_data_info(self):
        return self._shop_trade_data_info

    @shop_trade_data_info.setter
    def shop_trade_data_info(self, value):
        if isinstance(value, BusinessRelationTradeInfo):
            self._shop_trade_data_info = value
        else:
            self._shop_trade_data_info = BusinessRelationTradeInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.real_shop_id:
            if hasattr(self.real_shop_id, 'to_alipay_dict'):
                params['real_shop_id'] = self.real_shop_id.to_alipay_dict()
            else:
                params['real_shop_id'] = self.real_shop_id
        if self.real_shop_no:
            if hasattr(self.real_shop_no, 'to_alipay_dict'):
                params['real_shop_no'] = self.real_shop_no.to_alipay_dict()
            else:
                params['real_shop_no'] = self.real_shop_no
        if self.shop_confirm_status:
            if hasattr(self.shop_confirm_status, 'to_alipay_dict'):
                params['shop_confirm_status'] = self.shop_confirm_status.to_alipay_dict()
            else:
                params['shop_confirm_status'] = self.shop_confirm_status
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_trade_data_info:
            if hasattr(self.shop_trade_data_info, 'to_alipay_dict'):
                params['shop_trade_data_info'] = self.shop_trade_data_info.to_alipay_dict()
            else:
                params['shop_trade_data_info'] = self.shop_trade_data_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessRelationShopTradeInfo()
        if 'real_shop_id' in d:
            o.real_shop_id = d['real_shop_id']
        if 'real_shop_no' in d:
            o.real_shop_no = d['real_shop_no']
        if 'shop_confirm_status' in d:
            o.shop_confirm_status = d['shop_confirm_status']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_trade_data_info' in d:
            o.shop_trade_data_info = d['shop_trade_data_info']
        return o


