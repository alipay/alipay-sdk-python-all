#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankMarketingCampaignPrizeListConsultModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._biz_amt = None
        self._biz_context = None
        self._biz_id = None
        self._channel = None
        self._ip_id = None
        self._ip_role_id = None
        self._product_code = None
        self._type_list = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_amt(self):
        return self._biz_amt

    @biz_amt.setter
    def biz_amt(self, value):
        self._biz_amt = value
    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        self._biz_context = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def type_list(self):
        return self._type_list

    @type_list.setter
    def type_list(self, value):
        self._type_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_amt:
            if hasattr(self.biz_amt, 'to_alipay_dict'):
                params['biz_amt'] = self.biz_amt.to_alipay_dict()
            else:
                params['biz_amt'] = self.biz_amt
        if self.biz_context:
            if hasattr(self.biz_context, 'to_alipay_dict'):
                params['biz_context'] = self.biz_context.to_alipay_dict()
            else:
                params['biz_context'] = self.biz_context
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.type_list:
            if hasattr(self.type_list, 'to_alipay_dict'):
                params['type_list'] = self.type_list.to_alipay_dict()
            else:
                params['type_list'] = self.type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankMarketingCampaignPrizeListConsultModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_amt' in d:
            o.biz_amt = d['biz_amt']
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'type_list' in d:
            o.type_list = d['type_list']
        return o


