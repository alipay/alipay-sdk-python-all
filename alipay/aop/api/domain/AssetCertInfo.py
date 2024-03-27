#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetCertInfo(object):

    def __init__(self):
        self._card_no = None
        self._card_pwd = None
        self._card_template_id = None
        self._denomination = None
        self._order_id = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_pwd(self):
        return self._card_pwd

    @card_pwd.setter
    def card_pwd(self, value):
        self._card_pwd = value
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def denomination(self):
        return self._denomination

    @denomination.setter
    def denomination(self, value):
        self._denomination = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_pwd:
            if hasattr(self.card_pwd, 'to_alipay_dict'):
                params['card_pwd'] = self.card_pwd.to_alipay_dict()
            else:
                params['card_pwd'] = self.card_pwd
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.denomination:
            if hasattr(self.denomination, 'to_alipay_dict'):
                params['denomination'] = self.denomination.to_alipay_dict()
            else:
                params['denomination'] = self.denomination
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetCertInfo()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_pwd' in d:
            o.card_pwd = d['card_pwd']
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'denomination' in d:
            o.denomination = d['denomination']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o


