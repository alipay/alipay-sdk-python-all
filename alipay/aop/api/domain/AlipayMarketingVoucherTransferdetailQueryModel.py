#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingVoucherTransferdetailQueryModel(object):

    def __init__(self):
        self._asset_types = None
        self._open_id = None
        self._trade_no = None
        self._user_id = None

    @property
    def asset_types(self):
        return self._asset_types

    @asset_types.setter
    def asset_types(self, value):
        if isinstance(value, list):
            self._asset_types = list()
            for i in value:
                self._asset_types.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_types:
            if isinstance(self.asset_types, list):
                for i in range(0, len(self.asset_types)):
                    element = self.asset_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_types[i] = element.to_alipay_dict()
            if hasattr(self.asset_types, 'to_alipay_dict'):
                params['asset_types'] = self.asset_types.to_alipay_dict()
            else:
                params['asset_types'] = self.asset_types
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingVoucherTransferdetailQueryModel()
        if 'asset_types' in d:
            o.asset_types = d['asset_types']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


