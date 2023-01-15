#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenBatchVoucher import OpenBatchVoucher


class AlipayMarketingVoucherBatchsendModel(object):

    def __init__(self):
        self._async = None
        self._biz_from = None
        self._memo = None
        self._open_id = None
        self._out_biz_no = None
        self._template_id = None
        self._to_claim = None
        self._user_id = None
        self._vouchers = None

    @property
    def async(self):
        return self._async

    @async.setter
    def async(self, value):
        self._async = value
    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def to_claim(self):
        return self._to_claim

    @to_claim.setter
    def to_claim(self, value):
        self._to_claim = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vouchers(self):
        return self._vouchers

    @vouchers.setter
    def vouchers(self, value):
        if isinstance(value, list):
            self._vouchers = list()
            for i in value:
                if isinstance(i, OpenBatchVoucher):
                    self._vouchers.append(i)
                else:
                    self._vouchers.append(OpenBatchVoucher.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.async:
            if hasattr(self.async, 'to_alipay_dict'):
                params['async'] = self.async.to_alipay_dict()
            else:
                params['async'] = self.async
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.to_claim:
            if hasattr(self.to_claim, 'to_alipay_dict'):
                params['to_claim'] = self.to_claim.to_alipay_dict()
            else:
                params['to_claim'] = self.to_claim
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vouchers:
            if isinstance(self.vouchers, list):
                for i in range(0, len(self.vouchers)):
                    element = self.vouchers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vouchers[i] = element.to_alipay_dict()
            if hasattr(self.vouchers, 'to_alipay_dict'):
                params['vouchers'] = self.vouchers.to_alipay_dict()
            else:
                params['vouchers'] = self.vouchers
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingVoucherBatchsendModel()
        if 'async' in d:
            o.async = d['async']
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'memo' in d:
            o.memo = d['memo']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'to_claim' in d:
            o.to_claim = d['to_claim']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vouchers' in d:
            o.vouchers = d['vouchers']
        return o


