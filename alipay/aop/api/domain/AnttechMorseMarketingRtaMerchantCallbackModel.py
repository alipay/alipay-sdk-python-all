#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingRtaMerchantCallbackModel(object):

    def __init__(self):
        self._campaign_id = None
        self._commodity_category = None
        self._dividend_amt = None
        self._mobile_sha_256 = None
        self._payment_amt = None
        self._request_id = None
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
    def commodity_category(self):
        return self._commodity_category

    @commodity_category.setter
    def commodity_category(self, value):
        self._commodity_category = value
    @property
    def dividend_amt(self):
        return self._dividend_amt

    @dividend_amt.setter
    def dividend_amt(self, value):
        self._dividend_amt = value
    @property
    def mobile_sha_256(self):
        return self._mobile_sha_256

    @mobile_sha_256.setter
    def mobile_sha_256(self, value):
        self._mobile_sha_256 = value
    @property
    def payment_amt(self):
        return self._payment_amt

    @payment_amt.setter
    def payment_amt(self, value):
        self._payment_amt = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
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
        if self.commodity_category:
            if hasattr(self.commodity_category, 'to_alipay_dict'):
                params['commodity_category'] = self.commodity_category.to_alipay_dict()
            else:
                params['commodity_category'] = self.commodity_category
        if self.dividend_amt:
            if hasattr(self.dividend_amt, 'to_alipay_dict'):
                params['dividend_amt'] = self.dividend_amt.to_alipay_dict()
            else:
                params['dividend_amt'] = self.dividend_amt
        if self.mobile_sha_256:
            if hasattr(self.mobile_sha_256, 'to_alipay_dict'):
                params['mobile_sha_256'] = self.mobile_sha_256.to_alipay_dict()
            else:
                params['mobile_sha_256'] = self.mobile_sha_256
        if self.payment_amt:
            if hasattr(self.payment_amt, 'to_alipay_dict'):
                params['payment_amt'] = self.payment_amt.to_alipay_dict()
            else:
                params['payment_amt'] = self.payment_amt
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
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
        o = AnttechMorseMarketingRtaMerchantCallbackModel()
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'commodity_category' in d:
            o.commodity_category = d['commodity_category']
        if 'dividend_amt' in d:
            o.dividend_amt = d['dividend_amt']
        if 'mobile_sha_256' in d:
            o.mobile_sha_256 = d['mobile_sha_256']
        if 'payment_amt' in d:
            o.payment_amt = d['payment_amt']
        if 'request_id' in d:
            o.request_id = d['request_id']
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


