#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainCreditpaySellerunsignCreateModel(object):

    def __init__(self):
        self._ar_no = None
        self._channel_tag = None
        self._request_id = None
        self._seller = None
        self._seller_scene_id = None
        self._shop_id = None
        self._shop_name = None
        self._trace_id = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def channel_tag(self):
        return self._channel_tag

    @channel_tag.setter
    def channel_tag(self, value):
        self._channel_tag = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, Member):
            self._seller = value
        else:
            self._seller = Member.from_alipay_dict(value)
    @property
    def seller_scene_id(self):
        return self._seller_scene_id

    @seller_scene_id.setter
    def seller_scene_id(self, value):
        self._seller_scene_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.channel_tag:
            if hasattr(self.channel_tag, 'to_alipay_dict'):
                params['channel_tag'] = self.channel_tag.to_alipay_dict()
            else:
                params['channel_tag'] = self.channel_tag
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        if self.seller_scene_id:
            if hasattr(self.seller_scene_id, 'to_alipay_dict'):
                params['seller_scene_id'] = self.seller_scene_id.to_alipay_dict()
            else:
                params['seller_scene_id'] = self.seller_scene_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainCreditpaySellerunsignCreateModel()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'channel_tag' in d:
            o.channel_tag = d['channel_tag']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'seller' in d:
            o.seller = d['seller']
        if 'seller_scene_id' in d:
            o.seller_scene_id = d['seller_scene_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


