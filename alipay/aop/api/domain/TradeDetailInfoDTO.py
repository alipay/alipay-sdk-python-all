#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeDetailInfoDTO(object):

    def __init__(self):
        self._gmt_occur = None
        self._order_amount = None
        self._partner_trade_no = None
        self._trade_mode = None
        self._trade_platform = None
        self._trade_title = None
        self._trans_in_amount = None
        self._trans_in_unique_id = None
        self._user_identity = None

    @property
    def gmt_occur(self):
        return self._gmt_occur

    @gmt_occur.setter
    def gmt_occur(self, value):
        self._gmt_occur = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def partner_trade_no(self):
        return self._partner_trade_no

    @partner_trade_no.setter
    def partner_trade_no(self, value):
        self._partner_trade_no = value
    @property
    def trade_mode(self):
        return self._trade_mode

    @trade_mode.setter
    def trade_mode(self, value):
        self._trade_mode = value
    @property
    def trade_platform(self):
        return self._trade_platform

    @trade_platform.setter
    def trade_platform(self, value):
        self._trade_platform = value
    @property
    def trade_title(self):
        return self._trade_title

    @trade_title.setter
    def trade_title(self, value):
        self._trade_title = value
    @property
    def trans_in_amount(self):
        return self._trans_in_amount

    @trans_in_amount.setter
    def trans_in_amount(self, value):
        self._trans_in_amount = value
    @property
    def trans_in_unique_id(self):
        return self._trans_in_unique_id

    @trans_in_unique_id.setter
    def trans_in_unique_id(self, value):
        self._trans_in_unique_id = value
    @property
    def user_identity(self):
        return self._user_identity

    @user_identity.setter
    def user_identity(self, value):
        self._user_identity = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_occur:
            if hasattr(self.gmt_occur, 'to_alipay_dict'):
                params['gmt_occur'] = self.gmt_occur.to_alipay_dict()
            else:
                params['gmt_occur'] = self.gmt_occur
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.partner_trade_no:
            if hasattr(self.partner_trade_no, 'to_alipay_dict'):
                params['partner_trade_no'] = self.partner_trade_no.to_alipay_dict()
            else:
                params['partner_trade_no'] = self.partner_trade_no
        if self.trade_mode:
            if hasattr(self.trade_mode, 'to_alipay_dict'):
                params['trade_mode'] = self.trade_mode.to_alipay_dict()
            else:
                params['trade_mode'] = self.trade_mode
        if self.trade_platform:
            if hasattr(self.trade_platform, 'to_alipay_dict'):
                params['trade_platform'] = self.trade_platform.to_alipay_dict()
            else:
                params['trade_platform'] = self.trade_platform
        if self.trade_title:
            if hasattr(self.trade_title, 'to_alipay_dict'):
                params['trade_title'] = self.trade_title.to_alipay_dict()
            else:
                params['trade_title'] = self.trade_title
        if self.trans_in_amount:
            if hasattr(self.trans_in_amount, 'to_alipay_dict'):
                params['trans_in_amount'] = self.trans_in_amount.to_alipay_dict()
            else:
                params['trans_in_amount'] = self.trans_in_amount
        if self.trans_in_unique_id:
            if hasattr(self.trans_in_unique_id, 'to_alipay_dict'):
                params['trans_in_unique_id'] = self.trans_in_unique_id.to_alipay_dict()
            else:
                params['trans_in_unique_id'] = self.trans_in_unique_id
        if self.user_identity:
            if hasattr(self.user_identity, 'to_alipay_dict'):
                params['user_identity'] = self.user_identity.to_alipay_dict()
            else:
                params['user_identity'] = self.user_identity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeDetailInfoDTO()
        if 'gmt_occur' in d:
            o.gmt_occur = d['gmt_occur']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'partner_trade_no' in d:
            o.partner_trade_no = d['partner_trade_no']
        if 'trade_mode' in d:
            o.trade_mode = d['trade_mode']
        if 'trade_platform' in d:
            o.trade_platform = d['trade_platform']
        if 'trade_title' in d:
            o.trade_title = d['trade_title']
        if 'trans_in_amount' in d:
            o.trans_in_amount = d['trans_in_amount']
        if 'trans_in_unique_id' in d:
            o.trans_in_unique_id = d['trans_in_unique_id']
        if 'user_identity' in d:
            o.user_identity = d['user_identity']
        return o


