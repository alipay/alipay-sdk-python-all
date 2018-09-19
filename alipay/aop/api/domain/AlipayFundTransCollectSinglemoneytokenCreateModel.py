#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransCollectSinglemoneytokenCreateModel(object):

    def __init__(self):
        self._biz_context = None
        self._collect_mode = None
        self._expire_date = None
        self._ext_info = None
        self._out_biz_no = None
        self._out_channel = None
        self._pay_amount = None
        self._pay_memo = None
        self._pay_mode = None
        self._payee_user_id = None

    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        self._biz_context = value
    @property
    def collect_mode(self):
        return self._collect_mode

    @collect_mode.setter
    def collect_mode(self, value):
        self._collect_mode = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_channel(self):
        return self._out_channel

    @out_channel.setter
    def out_channel(self, value):
        self._out_channel = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_memo(self):
        return self._pay_memo

    @pay_memo.setter
    def pay_memo(self, value):
        self._pay_memo = value
    @property
    def pay_mode(self):
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, value):
        self._pay_mode = value
    @property
    def payee_user_id(self):
        return self._payee_user_id

    @payee_user_id.setter
    def payee_user_id(self, value):
        self._payee_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_context:
            if hasattr(self.biz_context, 'to_alipay_dict'):
                params['biz_context'] = self.biz_context.to_alipay_dict()
            else:
                params['biz_context'] = self.biz_context
        if self.collect_mode:
            if hasattr(self.collect_mode, 'to_alipay_dict'):
                params['collect_mode'] = self.collect_mode.to_alipay_dict()
            else:
                params['collect_mode'] = self.collect_mode
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_channel:
            if hasattr(self.out_channel, 'to_alipay_dict'):
                params['out_channel'] = self.out_channel.to_alipay_dict()
            else:
                params['out_channel'] = self.out_channel
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_memo:
            if hasattr(self.pay_memo, 'to_alipay_dict'):
                params['pay_memo'] = self.pay_memo.to_alipay_dict()
            else:
                params['pay_memo'] = self.pay_memo
        if self.pay_mode:
            if hasattr(self.pay_mode, 'to_alipay_dict'):
                params['pay_mode'] = self.pay_mode.to_alipay_dict()
            else:
                params['pay_mode'] = self.pay_mode
        if self.payee_user_id:
            if hasattr(self.payee_user_id, 'to_alipay_dict'):
                params['payee_user_id'] = self.payee_user_id.to_alipay_dict()
            else:
                params['payee_user_id'] = self.payee_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransCollectSinglemoneytokenCreateModel()
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'collect_mode' in d:
            o.collect_mode = d['collect_mode']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_channel' in d:
            o.out_channel = d['out_channel']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_memo' in d:
            o.pay_memo = d['pay_memo']
        if 'pay_mode' in d:
            o.pay_mode = d['pay_mode']
        if 'payee_user_id' in d:
            o.payee_user_id = d['payee_user_id']
        return o


