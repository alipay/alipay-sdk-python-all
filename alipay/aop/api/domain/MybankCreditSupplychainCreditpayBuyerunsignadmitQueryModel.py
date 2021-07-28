#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainCreditpayBuyerunsignadmitQueryModel(object):

    def __init__(self):
        self._ar_no = None
        self._buyer = None
        self._buyer_scene_id = None
        self._channel_tag = None
        self._request_id = None
        self._trace_id = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, Member):
            self._buyer = value
        else:
            self._buyer = Member.from_alipay_dict(value)
    @property
    def buyer_scene_id(self):
        return self._buyer_scene_id

    @buyer_scene_id.setter
    def buyer_scene_id(self, value):
        self._buyer_scene_id = value
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
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.buyer_scene_id:
            if hasattr(self.buyer_scene_id, 'to_alipay_dict'):
                params['buyer_scene_id'] = self.buyer_scene_id.to_alipay_dict()
            else:
                params['buyer_scene_id'] = self.buyer_scene_id
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
        o = MybankCreditSupplychainCreditpayBuyerunsignadmitQueryModel()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'buyer_scene_id' in d:
            o.buyer_scene_id = d['buyer_scene_id']
        if 'channel_tag' in d:
            o.channel_tag = d['channel_tag']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


