#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayGongyiUserInfoTest import AlipayGongyiUserInfoTest


class AlipayGongyiModelTest(object):

    def __init__(self):
        self._buyer = None
        self._buyer_email = None
        self._price = None
        self._seller = None
        self._seller_email = None
        self._userinfo = None

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        self._buyer = value
    @property
    def buyer_email(self):
        return self._buyer_email

    @buyer_email.setter
    def buyer_email(self, value):
        self._buyer_email = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        self._seller = value
    @property
    def seller_email(self):
        return self._seller_email

    @seller_email.setter
    def seller_email(self, value):
        self._seller_email = value
    @property
    def userinfo(self):
        return self._userinfo

    @userinfo.setter
    def userinfo(self, value):
        if isinstance(value, AlipayGongyiUserInfoTest):
            self._userinfo = value
        else:
            self._userinfo = AlipayGongyiUserInfoTest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.buyer_email:
            if hasattr(self.buyer_email, 'to_alipay_dict'):
                params['buyer_email'] = self.buyer_email.to_alipay_dict()
            else:
                params['buyer_email'] = self.buyer_email
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        if self.seller_email:
            if hasattr(self.seller_email, 'to_alipay_dict'):
                params['seller_email'] = self.seller_email.to_alipay_dict()
            else:
                params['seller_email'] = self.seller_email
        if self.userinfo:
            if hasattr(self.userinfo, 'to_alipay_dict'):
                params['userinfo'] = self.userinfo.to_alipay_dict()
            else:
                params['userinfo'] = self.userinfo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayGongyiModelTest()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'buyer_email' in d:
            o.buyer_email = d['buyer_email']
        if 'price' in d:
            o.price = d['price']
        if 'seller' in d:
            o.seller = d['seller']
        if 'seller_email' in d:
            o.seller_email = d['seller_email']
        if 'userinfo' in d:
            o.userinfo = d['userinfo']
        return o


