#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPerson import InsPerson


class AlipayInsMarketingSellerSignModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._prod_code = None
        self._seller = None
        self._sign_alipay_id = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, InsPerson):
            self._seller = value
        else:
            self._seller = InsPerson.from_alipay_dict(value)
    @property
    def sign_alipay_id(self):
        return self._sign_alipay_id

    @sign_alipay_id.setter
    def sign_alipay_id(self, value):
        self._sign_alipay_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        if self.sign_alipay_id:
            if hasattr(self.sign_alipay_id, 'to_alipay_dict'):
                params['sign_alipay_id'] = self.sign_alipay_id.to_alipay_dict()
            else:
                params['sign_alipay_id'] = self.sign_alipay_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsMarketingSellerSignModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'seller' in d:
            o.seller = d['seller']
        if 'sign_alipay_id' in d:
            o.sign_alipay_id = d['sign_alipay_id']
        return o


