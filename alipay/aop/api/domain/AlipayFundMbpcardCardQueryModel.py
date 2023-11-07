#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundMbpcardCardQueryModel(object):

    def __init__(self):
        self._alipay_identity_id = None
        self._alipay_identity_type = None
        self._bind_user_name = None
        self._card_no = None
        self._open_id = None
        self._page_num = None
        self._page_size = None

    @property
    def alipay_identity_id(self):
        return self._alipay_identity_id

    @alipay_identity_id.setter
    def alipay_identity_id(self, value):
        self._alipay_identity_id = value
    @property
    def alipay_identity_type(self):
        return self._alipay_identity_type

    @alipay_identity_type.setter
    def alipay_identity_type(self, value):
        self._alipay_identity_type = value
    @property
    def bind_user_name(self):
        return self._bind_user_name

    @bind_user_name.setter
    def bind_user_name(self, value):
        self._bind_user_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_identity_id:
            if hasattr(self.alipay_identity_id, 'to_alipay_dict'):
                params['alipay_identity_id'] = self.alipay_identity_id.to_alipay_dict()
            else:
                params['alipay_identity_id'] = self.alipay_identity_id
        if self.alipay_identity_type:
            if hasattr(self.alipay_identity_type, 'to_alipay_dict'):
                params['alipay_identity_type'] = self.alipay_identity_type.to_alipay_dict()
            else:
                params['alipay_identity_type'] = self.alipay_identity_type
        if self.bind_user_name:
            if hasattr(self.bind_user_name, 'to_alipay_dict'):
                params['bind_user_name'] = self.bind_user_name.to_alipay_dict()
            else:
                params['bind_user_name'] = self.bind_user_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundMbpcardCardQueryModel()
        if 'alipay_identity_id' in d:
            o.alipay_identity_id = d['alipay_identity_id']
        if 'alipay_identity_type' in d:
            o.alipay_identity_type = d['alipay_identity_type']
        if 'bind_user_name' in d:
            o.bind_user_name = d['bind_user_name']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


