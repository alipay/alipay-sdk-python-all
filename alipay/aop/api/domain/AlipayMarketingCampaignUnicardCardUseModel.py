#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignUnicardCardUseModel(object):

    def __init__(self):
        self._biz_memo = None
        self._out_biz_no = None
        self._trade_date = None
        self._uni_card_no = None
        self._user_id = None

    @property
    def biz_memo(self):
        return self._biz_memo

    @biz_memo.setter
    def biz_memo(self, value):
        self._biz_memo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def trade_date(self):
        return self._trade_date

    @trade_date.setter
    def trade_date(self, value):
        self._trade_date = value
    @property
    def uni_card_no(self):
        return self._uni_card_no

    @uni_card_no.setter
    def uni_card_no(self, value):
        self._uni_card_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_memo:
            if hasattr(self.biz_memo, 'to_alipay_dict'):
                params['biz_memo'] = self.biz_memo.to_alipay_dict()
            else:
                params['biz_memo'] = self.biz_memo
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.trade_date:
            if hasattr(self.trade_date, 'to_alipay_dict'):
                params['trade_date'] = self.trade_date.to_alipay_dict()
            else:
                params['trade_date'] = self.trade_date
        if self.uni_card_no:
            if hasattr(self.uni_card_no, 'to_alipay_dict'):
                params['uni_card_no'] = self.uni_card_no.to_alipay_dict()
            else:
                params['uni_card_no'] = self.uni_card_no
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
        o = AlipayMarketingCampaignUnicardCardUseModel()
        if 'biz_memo' in d:
            o.biz_memo = d['biz_memo']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'trade_date' in d:
            o.trade_date = d['trade_date']
        if 'uni_card_no' in d:
            o.uni_card_no = d['uni_card_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


