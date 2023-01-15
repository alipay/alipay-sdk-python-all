#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenBatchExpireVoucher import OpenBatchExpireVoucher


class AlipayMarketingVoucherBatchExpireModel(object):

    def __init__(self):
        self._biz_from = None
        self._extend_info = None
        self._open_id = None
        self._out_biz_no = None
        self._user_id = None
        self._vouchers = None

    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
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
                if isinstance(i, OpenBatchExpireVoucher):
                    self._vouchers.append(i)
                else:
                    self._vouchers.append(OpenBatchExpireVoucher.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
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
        o = AlipayMarketingVoucherBatchExpireModel()
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vouchers' in d:
            o.vouchers = d['vouchers']
        return o


