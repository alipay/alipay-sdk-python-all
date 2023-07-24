#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserAssetInfoVO import UserAssetInfoVO


class JointAccountBillDetailDTO(object):

    def __init__(self):
        self._account_id = None
        self._amount = None
        self._bill_no = None
        self._biz_date = None
        self._biz_no = None
        self._in_out = None
        self._open_id = None
        self._out_trade_no = None
        self._payer_asset_info = None
        self._seller_full_name = None
        self._seller_logon_id = None
        self._title = None
        self._user_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def in_out(self):
        return self._in_out

    @in_out.setter
    def in_out(self, value):
        self._in_out = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def payer_asset_info(self):
        return self._payer_asset_info

    @payer_asset_info.setter
    def payer_asset_info(self, value):
        if isinstance(value, UserAssetInfoVO):
            self._payer_asset_info = value
        else:
            self._payer_asset_info = UserAssetInfoVO.from_alipay_dict(value)
    @property
    def seller_full_name(self):
        return self._seller_full_name

    @seller_full_name.setter
    def seller_full_name(self, value):
        self._seller_full_name = value
    @property
    def seller_logon_id(self):
        return self._seller_logon_id

    @seller_logon_id.setter
    def seller_logon_id(self, value):
        self._seller_logon_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.in_out:
            if hasattr(self.in_out, 'to_alipay_dict'):
                params['in_out'] = self.in_out.to_alipay_dict()
            else:
                params['in_out'] = self.in_out
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.payer_asset_info:
            if hasattr(self.payer_asset_info, 'to_alipay_dict'):
                params['payer_asset_info'] = self.payer_asset_info.to_alipay_dict()
            else:
                params['payer_asset_info'] = self.payer_asset_info
        if self.seller_full_name:
            if hasattr(self.seller_full_name, 'to_alipay_dict'):
                params['seller_full_name'] = self.seller_full_name.to_alipay_dict()
            else:
                params['seller_full_name'] = self.seller_full_name
        if self.seller_logon_id:
            if hasattr(self.seller_logon_id, 'to_alipay_dict'):
                params['seller_logon_id'] = self.seller_logon_id.to_alipay_dict()
            else:
                params['seller_logon_id'] = self.seller_logon_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
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
        o = JointAccountBillDetailDTO()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'in_out' in d:
            o.in_out = d['in_out']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'payer_asset_info' in d:
            o.payer_asset_info = d['payer_asset_info']
        if 'seller_full_name' in d:
            o.seller_full_name = d['seller_full_name']
        if 'seller_logon_id' in d:
            o.seller_logon_id = d['seller_logon_id']
        if 'title' in d:
            o.title = d['title']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


