#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditGuaranteeTradedrivePayModel(object):

    def __init__(self):
        self._biz_date = None
        self._order_encash_amt = None
        self._order_encash_ccy = None
        self._out_biz_no = None
        self._seller_login_id = None
        self._site = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def order_encash_amt(self):
        return self._order_encash_amt

    @order_encash_amt.setter
    def order_encash_amt(self, value):
        self._order_encash_amt = value
    @property
    def order_encash_ccy(self):
        return self._order_encash_ccy

    @order_encash_ccy.setter
    def order_encash_ccy(self, value):
        self._order_encash_ccy = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.order_encash_amt:
            if hasattr(self.order_encash_amt, 'to_alipay_dict'):
                params['order_encash_amt'] = self.order_encash_amt.to_alipay_dict()
            else:
                params['order_encash_amt'] = self.order_encash_amt
        if self.order_encash_ccy:
            if hasattr(self.order_encash_ccy, 'to_alipay_dict'):
                params['order_encash_ccy'] = self.order_encash_ccy.to_alipay_dict()
            else:
                params['order_encash_ccy'] = self.order_encash_ccy
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditGuaranteeTradedrivePayModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'order_encash_amt' in d:
            o.order_encash_amt = d['order_encash_amt']
        if 'order_encash_ccy' in d:
            o.order_encash_ccy = d['order_encash_ccy']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        if 'site' in d:
            o.site = d['site']
        return o


