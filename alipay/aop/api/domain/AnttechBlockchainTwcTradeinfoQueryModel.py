#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainTwcTradeinfoQueryModel(object):

    def __init__(self):
        self._buyer_open_id = None
        self._buyeruid = None
        self._seller_open_id = None
        self._selleruid = None
        self._tradefee = None
        self._tradeid = None

    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def buyeruid(self):
        return self._buyeruid

    @buyeruid.setter
    def buyeruid(self, value):
        self._buyeruid = value
    @property
    def seller_open_id(self):
        return self._seller_open_id

    @seller_open_id.setter
    def seller_open_id(self, value):
        self._seller_open_id = value
    @property
    def selleruid(self):
        return self._selleruid

    @selleruid.setter
    def selleruid(self, value):
        self._selleruid = value
    @property
    def tradefee(self):
        return self._tradefee

    @tradefee.setter
    def tradefee(self, value):
        self._tradefee = value
    @property
    def tradeid(self):
        return self._tradeid

    @tradeid.setter
    def tradeid(self, value):
        self._tradeid = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.buyeruid:
            if hasattr(self.buyeruid, 'to_alipay_dict'):
                params['buyeruid'] = self.buyeruid.to_alipay_dict()
            else:
                params['buyeruid'] = self.buyeruid
        if self.seller_open_id:
            if hasattr(self.seller_open_id, 'to_alipay_dict'):
                params['seller_open_id'] = self.seller_open_id.to_alipay_dict()
            else:
                params['seller_open_id'] = self.seller_open_id
        if self.selleruid:
            if hasattr(self.selleruid, 'to_alipay_dict'):
                params['selleruid'] = self.selleruid.to_alipay_dict()
            else:
                params['selleruid'] = self.selleruid
        if self.tradefee:
            if hasattr(self.tradefee, 'to_alipay_dict'):
                params['tradefee'] = self.tradefee.to_alipay_dict()
            else:
                params['tradefee'] = self.tradefee
        if self.tradeid:
            if hasattr(self.tradeid, 'to_alipay_dict'):
                params['tradeid'] = self.tradeid.to_alipay_dict()
            else:
                params['tradeid'] = self.tradeid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainTwcTradeinfoQueryModel()
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'buyeruid' in d:
            o.buyeruid = d['buyeruid']
        if 'seller_open_id' in d:
            o.seller_open_id = d['seller_open_id']
        if 'selleruid' in d:
            o.selleruid = d['selleruid']
        if 'tradefee' in d:
            o.tradefee = d['tradefee']
        if 'tradeid' in d:
            o.tradeid = d['tradeid']
        return o


