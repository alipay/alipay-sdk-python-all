#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryClearApplyModel(object):

    def __init__(self):
        self._biz_type = None
        self._business_date = None
        self._memo = None
        self._org_code = None
        self._passive_no = None
        self._sub_org_code = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def business_date(self):
        return self._business_date

    @business_date.setter
    def business_date(self, value):
        self._business_date = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def passive_no(self):
        return self._passive_no

    @passive_no.setter
    def passive_no(self, value):
        self._passive_no = value
    @property
    def sub_org_code(self):
        return self._sub_org_code

    @sub_org_code.setter
    def sub_org_code(self, value):
        self._sub_org_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.business_date:
            if hasattr(self.business_date, 'to_alipay_dict'):
                params['business_date'] = self.business_date.to_alipay_dict()
            else:
                params['business_date'] = self.business_date
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.passive_no:
            if hasattr(self.passive_no, 'to_alipay_dict'):
                params['passive_no'] = self.passive_no.to_alipay_dict()
            else:
                params['passive_no'] = self.passive_no
        if self.sub_org_code:
            if hasattr(self.sub_org_code, 'to_alipay_dict'):
                params['sub_org_code'] = self.sub_org_code.to_alipay_dict()
            else:
                params['sub_org_code'] = self.sub_org_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryClearApplyModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'business_date' in d:
            o.business_date = d['business_date']
        if 'memo' in d:
            o.memo = d['memo']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'passive_no' in d:
            o.passive_no = d['passive_no']
        if 'sub_org_code' in d:
            o.sub_org_code = d['sub_org_code']
        return o


