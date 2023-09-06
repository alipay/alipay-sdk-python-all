#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradeAssetRequest import TradeAssetRequest
from alipay.aop.api.domain.ProfitSharingRequest import ProfitSharingRequest


class AlipayEbppIndustryPerformOrderCreateModel(object):

    def __init__(self):
        self._alipay_trade_asset = None
        self._bill_amount = None
        self._create_type = None
        self._open_id = None
        self._out_no = None
        self._profit_sharing_list = None
        self._service_account = None
        self._timeout_close = None
        self._unique_code = None
        self._user_id = None

    @property
    def alipay_trade_asset(self):
        return self._alipay_trade_asset

    @alipay_trade_asset.setter
    def alipay_trade_asset(self, value):
        if isinstance(value, TradeAssetRequest):
            self._alipay_trade_asset = value
        else:
            self._alipay_trade_asset = TradeAssetRequest.from_alipay_dict(value)
    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def create_type(self):
        return self._create_type

    @create_type.setter
    def create_type(self, value):
        self._create_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def profit_sharing_list(self):
        return self._profit_sharing_list

    @profit_sharing_list.setter
    def profit_sharing_list(self, value):
        if isinstance(value, list):
            self._profit_sharing_list = list()
            for i in value:
                if isinstance(i, ProfitSharingRequest):
                    self._profit_sharing_list.append(i)
                else:
                    self._profit_sharing_list.append(ProfitSharingRequest.from_alipay_dict(i))
    @property
    def service_account(self):
        return self._service_account

    @service_account.setter
    def service_account(self, value):
        self._service_account = value
    @property
    def timeout_close(self):
        return self._timeout_close

    @timeout_close.setter
    def timeout_close(self, value):
        self._timeout_close = value
    @property
    def unique_code(self):
        return self._unique_code

    @unique_code.setter
    def unique_code(self, value):
        self._unique_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_asset:
            if hasattr(self.alipay_trade_asset, 'to_alipay_dict'):
                params['alipay_trade_asset'] = self.alipay_trade_asset.to_alipay_dict()
            else:
                params['alipay_trade_asset'] = self.alipay_trade_asset
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.create_type:
            if hasattr(self.create_type, 'to_alipay_dict'):
                params['create_type'] = self.create_type.to_alipay_dict()
            else:
                params['create_type'] = self.create_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_no:
            if hasattr(self.out_no, 'to_alipay_dict'):
                params['out_no'] = self.out_no.to_alipay_dict()
            else:
                params['out_no'] = self.out_no
        if self.profit_sharing_list:
            if isinstance(self.profit_sharing_list, list):
                for i in range(0, len(self.profit_sharing_list)):
                    element = self.profit_sharing_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.profit_sharing_list[i] = element.to_alipay_dict()
            if hasattr(self.profit_sharing_list, 'to_alipay_dict'):
                params['profit_sharing_list'] = self.profit_sharing_list.to_alipay_dict()
            else:
                params['profit_sharing_list'] = self.profit_sharing_list
        if self.service_account:
            if hasattr(self.service_account, 'to_alipay_dict'):
                params['service_account'] = self.service_account.to_alipay_dict()
            else:
                params['service_account'] = self.service_account
        if self.timeout_close:
            if hasattr(self.timeout_close, 'to_alipay_dict'):
                params['timeout_close'] = self.timeout_close.to_alipay_dict()
            else:
                params['timeout_close'] = self.timeout_close
        if self.unique_code:
            if hasattr(self.unique_code, 'to_alipay_dict'):
                params['unique_code'] = self.unique_code.to_alipay_dict()
            else:
                params['unique_code'] = self.unique_code
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
        o = AlipayEbppIndustryPerformOrderCreateModel()
        if 'alipay_trade_asset' in d:
            o.alipay_trade_asset = d['alipay_trade_asset']
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'create_type' in d:
            o.create_type = d['create_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_no' in d:
            o.out_no = d['out_no']
        if 'profit_sharing_list' in d:
            o.profit_sharing_list = d['profit_sharing_list']
        if 'service_account' in d:
            o.service_account = d['service_account']
        if 'timeout_close' in d:
            o.timeout_close = d['timeout_close']
        if 'unique_code' in d:
            o.unique_code = d['unique_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


