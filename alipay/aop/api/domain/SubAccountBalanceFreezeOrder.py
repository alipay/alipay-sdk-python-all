#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoney import MultiCurrencyMoney
from alipay.aop.api.domain.SubAccountBaseInfo import SubAccountBaseInfo


class SubAccountBalanceFreezeOrder(object):

    def __init__(self):
        self._freeze_amount = None
        self._memo = None
        self._out_biz_no = None
        self._source = None
        self._sub_account_base_info = None

    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        if isinstance(value, MultiCurrencyMoney):
            self._freeze_amount = value
        else:
            self._freeze_amount = MultiCurrencyMoney.from_alipay_dict(value)
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sub_account_base_info(self):
        return self._sub_account_base_info

    @sub_account_base_info.setter
    def sub_account_base_info(self, value):
        if isinstance(value, SubAccountBaseInfo):
            self._sub_account_base_info = value
        else:
            self._sub_account_base_info = SubAccountBaseInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.sub_account_base_info:
            if hasattr(self.sub_account_base_info, 'to_alipay_dict'):
                params['sub_account_base_info'] = self.sub_account_base_info.to_alipay_dict()
            else:
                params['sub_account_base_info'] = self.sub_account_base_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountBalanceFreezeOrder()
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'source' in d:
            o.source = d['source']
        if 'sub_account_base_info' in d:
            o.sub_account_base_info = d['sub_account_base_info']
        return o


