#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechMorseMarketingSrtaNanonymousQueryModel(object):

    def __init__(self):
        self._anonymous_mobile_sha_256_list = None
        self._blind_mobile_sha_256 = None
        self._extend_params = None
        self._order_amount = None
        self._req_id = None

    @property
    def anonymous_mobile_sha_256_list(self):
        return self._anonymous_mobile_sha_256_list

    @anonymous_mobile_sha_256_list.setter
    def anonymous_mobile_sha_256_list(self, value):
        self._anonymous_mobile_sha_256_list = value
    @property
    def blind_mobile_sha_256(self):
        return self._blind_mobile_sha_256

    @blind_mobile_sha_256.setter
    def blind_mobile_sha_256(self, value):
        self._blind_mobile_sha_256 = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def req_id(self):
        return self._req_id

    @req_id.setter
    def req_id(self, value):
        self._req_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.anonymous_mobile_sha_256_list:
            if hasattr(self.anonymous_mobile_sha_256_list, 'to_alipay_dict'):
                params['anonymous_mobile_sha_256_list'] = self.anonymous_mobile_sha_256_list.to_alipay_dict()
            else:
                params['anonymous_mobile_sha_256_list'] = self.anonymous_mobile_sha_256_list
        if self.blind_mobile_sha_256:
            if hasattr(self.blind_mobile_sha_256, 'to_alipay_dict'):
                params['blind_mobile_sha_256'] = self.blind_mobile_sha_256.to_alipay_dict()
            else:
                params['blind_mobile_sha_256'] = self.blind_mobile_sha_256
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.req_id:
            if hasattr(self.req_id, 'to_alipay_dict'):
                params['req_id'] = self.req_id.to_alipay_dict()
            else:
                params['req_id'] = self.req_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechMorseMarketingSrtaNanonymousQueryModel()
        if 'anonymous_mobile_sha_256_list' in d:
            o.anonymous_mobile_sha_256_list = d['anonymous_mobile_sha_256_list']
        if 'blind_mobile_sha_256' in d:
            o.blind_mobile_sha_256 = d['blind_mobile_sha_256']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'req_id' in d:
            o.req_id = d['req_id']
        return o


