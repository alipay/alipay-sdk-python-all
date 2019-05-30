#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsHealthGiftBatchValidGiftResult(object):

    def __init__(self):
        self._biz_type = None
        self._latest_policy_no = None
        self._product_group_biz_type = None
        self._sp_no = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def latest_policy_no(self):
        return self._latest_policy_no

    @latest_policy_no.setter
    def latest_policy_no(self, value):
        self._latest_policy_no = value
    @property
    def product_group_biz_type(self):
        return self._product_group_biz_type

    @product_group_biz_type.setter
    def product_group_biz_type(self, value):
        self._product_group_biz_type = value
    @property
    def sp_no(self):
        return self._sp_no

    @sp_no.setter
    def sp_no(self, value):
        self._sp_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.latest_policy_no:
            if hasattr(self.latest_policy_no, 'to_alipay_dict'):
                params['latest_policy_no'] = self.latest_policy_no.to_alipay_dict()
            else:
                params['latest_policy_no'] = self.latest_policy_no
        if self.product_group_biz_type:
            if hasattr(self.product_group_biz_type, 'to_alipay_dict'):
                params['product_group_biz_type'] = self.product_group_biz_type.to_alipay_dict()
            else:
                params['product_group_biz_type'] = self.product_group_biz_type
        if self.sp_no:
            if hasattr(self.sp_no, 'to_alipay_dict'):
                params['sp_no'] = self.sp_no.to_alipay_dict()
            else:
                params['sp_no'] = self.sp_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsHealthGiftBatchValidGiftResult()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'latest_policy_no' in d:
            o.latest_policy_no = d['latest_policy_no']
        if 'product_group_biz_type' in d:
            o.product_group_biz_type = d['product_group_biz_type']
        if 'sp_no' in d:
            o.sp_no = d['sp_no']
        return o


