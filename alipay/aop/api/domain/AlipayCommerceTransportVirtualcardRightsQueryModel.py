#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportVirtualcardRightsQueryModel(object):

    def __init__(self):
        self._card_no = None
        self._card_type = None
        self._open_id = None
        self._right_type_list = None
        self._user_id = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def right_type_list(self):
        return self._right_type_list

    @right_type_list.setter
    def right_type_list(self, value):
        if isinstance(value, list):
            self._right_type_list = list()
            for i in value:
                self._right_type_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.right_type_list:
            if isinstance(self.right_type_list, list):
                for i in range(0, len(self.right_type_list)):
                    element = self.right_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.right_type_list[i] = element.to_alipay_dict()
            if hasattr(self.right_type_list, 'to_alipay_dict'):
                params['right_type_list'] = self.right_type_list.to_alipay_dict()
            else:
                params['right_type_list'] = self.right_type_list
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
        o = AlipayCommerceTransportVirtualcardRightsQueryModel()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'right_type_list' in d:
            o.right_type_list = d['right_type_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


