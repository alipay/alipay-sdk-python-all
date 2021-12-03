#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeSubaccountCreateModel(object):

    def __init__(self):
        self._account_name = None
        self._currency_value = None
        self._out_channel_id = None
        self._out_channel_type = None
        self._parent_account_name = None
        self._parent_account_type = None
        self._parent_card_no = None
        self._request_no = None
        self._scene_code = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def currency_value(self):
        return self._currency_value

    @currency_value.setter
    def currency_value(self, value):
        self._currency_value = value
    @property
    def out_channel_id(self):
        return self._out_channel_id

    @out_channel_id.setter
    def out_channel_id(self, value):
        self._out_channel_id = value
    @property
    def out_channel_type(self):
        return self._out_channel_type

    @out_channel_type.setter
    def out_channel_type(self, value):
        self._out_channel_type = value
    @property
    def parent_account_name(self):
        return self._parent_account_name

    @parent_account_name.setter
    def parent_account_name(self, value):
        self._parent_account_name = value
    @property
    def parent_account_type(self):
        return self._parent_account_type

    @parent_account_type.setter
    def parent_account_type(self, value):
        self._parent_account_type = value
    @property
    def parent_card_no(self):
        return self._parent_card_no

    @parent_card_no.setter
    def parent_card_no(self, value):
        self._parent_card_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.currency_value:
            if hasattr(self.currency_value, 'to_alipay_dict'):
                params['currency_value'] = self.currency_value.to_alipay_dict()
            else:
                params['currency_value'] = self.currency_value
        if self.out_channel_id:
            if hasattr(self.out_channel_id, 'to_alipay_dict'):
                params['out_channel_id'] = self.out_channel_id.to_alipay_dict()
            else:
                params['out_channel_id'] = self.out_channel_id
        if self.out_channel_type:
            if hasattr(self.out_channel_type, 'to_alipay_dict'):
                params['out_channel_type'] = self.out_channel_type.to_alipay_dict()
            else:
                params['out_channel_type'] = self.out_channel_type
        if self.parent_account_name:
            if hasattr(self.parent_account_name, 'to_alipay_dict'):
                params['parent_account_name'] = self.parent_account_name.to_alipay_dict()
            else:
                params['parent_account_name'] = self.parent_account_name
        if self.parent_account_type:
            if hasattr(self.parent_account_type, 'to_alipay_dict'):
                params['parent_account_type'] = self.parent_account_type.to_alipay_dict()
            else:
                params['parent_account_type'] = self.parent_account_type
        if self.parent_card_no:
            if hasattr(self.parent_card_no, 'to_alipay_dict'):
                params['parent_card_no'] = self.parent_card_no.to_alipay_dict()
            else:
                params['parent_card_no'] = self.parent_card_no
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeSubaccountCreateModel()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'currency_value' in d:
            o.currency_value = d['currency_value']
        if 'out_channel_id' in d:
            o.out_channel_id = d['out_channel_id']
        if 'out_channel_type' in d:
            o.out_channel_type = d['out_channel_type']
        if 'parent_account_name' in d:
            o.parent_account_name = d['parent_account_name']
        if 'parent_account_type' in d:
            o.parent_account_type = d['parent_account_type']
        if 'parent_card_no' in d:
            o.parent_card_no = d['parent_card_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


