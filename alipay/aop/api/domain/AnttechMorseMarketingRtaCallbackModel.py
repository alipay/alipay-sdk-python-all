#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingRtaCallbackModel(object):

    def __init__(self):
        self._campaign_id = None
        self._discount_amt = None
        self._extend_params = None
        self._mobile_sha_256 = None
        self._out_biz_no = None
        self._payment_amt = None
        self._resource_id = None
        self._trade_date = None
        self._trade_no = None
        self._trade_total_amt = None
        self._trade_type = None

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def discount_amt(self):
        return self._discount_amt

    @discount_amt.setter
    def discount_amt(self, value):
        self._discount_amt = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def mobile_sha_256(self):
        return self._mobile_sha_256

    @mobile_sha_256.setter
    def mobile_sha_256(self, value):
        self._mobile_sha_256 = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payment_amt(self):
        return self._payment_amt

    @payment_amt.setter
    def payment_amt(self, value):
        self._payment_amt = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def trade_date(self):
        return self._trade_date

    @trade_date.setter
    def trade_date(self, value):
        self._trade_date = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_total_amt(self):
        return self._trade_total_amt

    @trade_total_amt.setter
    def trade_total_amt(self, value):
        self._trade_total_amt = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.discount_amt:
            if hasattr(self.discount_amt, 'to_alipay_dict'):
                params['discount_amt'] = self.discount_amt.to_alipay_dict()
            else:
                params['discount_amt'] = self.discount_amt
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.mobile_sha_256:
            if hasattr(self.mobile_sha_256, 'to_alipay_dict'):
                params['mobile_sha_256'] = self.mobile_sha_256.to_alipay_dict()
            else:
                params['mobile_sha_256'] = self.mobile_sha_256
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payment_amt:
            if hasattr(self.payment_amt, 'to_alipay_dict'):
                params['payment_amt'] = self.payment_amt.to_alipay_dict()
            else:
                params['payment_amt'] = self.payment_amt
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.trade_date:
            if hasattr(self.trade_date, 'to_alipay_dict'):
                params['trade_date'] = self.trade_date.to_alipay_dict()
            else:
                params['trade_date'] = self.trade_date
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_total_amt:
            if hasattr(self.trade_total_amt, 'to_alipay_dict'):
                params['trade_total_amt'] = self.trade_total_amt.to_alipay_dict()
            else:
                params['trade_total_amt'] = self.trade_total_amt
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseMarketingRtaCallbackModel()
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'discount_amt' in d:
            o.discount_amt = d['discount_amt']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'mobile_sha_256' in d:
            o.mobile_sha_256 = d['mobile_sha_256']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payment_amt' in d:
            o.payment_amt = d['payment_amt']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'trade_date' in d:
            o.trade_date = d['trade_date']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_total_amt' in d:
            o.trade_total_amt = d['trade_total_amt']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


