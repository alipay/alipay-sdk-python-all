#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsMarketingGiftQueryModel(object):

    def __init__(self):
        self._channel = None
        self._entrance = None
        self._gift_prod_code = None
        self._insured_user_id = None
        self._relation_to_apply = None
        self._right_no_list = None
        self._source = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def entrance(self):
        return self._entrance

    @entrance.setter
    def entrance(self, value):
        self._entrance = value
    @property
    def gift_prod_code(self):
        return self._gift_prod_code

    @gift_prod_code.setter
    def gift_prod_code(self, value):
        self._gift_prod_code = value
    @property
    def insured_user_id(self):
        return self._insured_user_id

    @insured_user_id.setter
    def insured_user_id(self, value):
        self._insured_user_id = value
    @property
    def relation_to_apply(self):
        return self._relation_to_apply

    @relation_to_apply.setter
    def relation_to_apply(self, value):
        self._relation_to_apply = value
    @property
    def right_no_list(self):
        return self._right_no_list

    @right_no_list.setter
    def right_no_list(self, value):
        if isinstance(value, list):
            self._right_no_list = list()
            for i in value:
                self._right_no_list.append(i)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.entrance:
            if hasattr(self.entrance, 'to_alipay_dict'):
                params['entrance'] = self.entrance.to_alipay_dict()
            else:
                params['entrance'] = self.entrance
        if self.gift_prod_code:
            if hasattr(self.gift_prod_code, 'to_alipay_dict'):
                params['gift_prod_code'] = self.gift_prod_code.to_alipay_dict()
            else:
                params['gift_prod_code'] = self.gift_prod_code
        if self.insured_user_id:
            if hasattr(self.insured_user_id, 'to_alipay_dict'):
                params['insured_user_id'] = self.insured_user_id.to_alipay_dict()
            else:
                params['insured_user_id'] = self.insured_user_id
        if self.relation_to_apply:
            if hasattr(self.relation_to_apply, 'to_alipay_dict'):
                params['relation_to_apply'] = self.relation_to_apply.to_alipay_dict()
            else:
                params['relation_to_apply'] = self.relation_to_apply
        if self.right_no_list:
            if isinstance(self.right_no_list, list):
                for i in range(0, len(self.right_no_list)):
                    element = self.right_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.right_no_list[i] = element.to_alipay_dict()
            if hasattr(self.right_no_list, 'to_alipay_dict'):
                params['right_no_list'] = self.right_no_list.to_alipay_dict()
            else:
                params['right_no_list'] = self.right_no_list
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsMarketingGiftQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'entrance' in d:
            o.entrance = d['entrance']
        if 'gift_prod_code' in d:
            o.gift_prod_code = d['gift_prod_code']
        if 'insured_user_id' in d:
            o.insured_user_id = d['insured_user_id']
        if 'relation_to_apply' in d:
            o.relation_to_apply = d['relation_to_apply']
        if 'right_no_list' in d:
            o.right_no_list = d['right_no_list']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


