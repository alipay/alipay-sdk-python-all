#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardUserInfo import CardUserInfo


class AlipayMarketingPointOrderQueryModel(object):

    def __init__(self):
        self._card_template_id = None
        self._card_user_info = None
        self._exchange_order_id = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def card_user_info(self):
        return self._card_user_info

    @card_user_info.setter
    def card_user_info(self, value):
        if isinstance(value, CardUserInfo):
            self._card_user_info = value
        else:
            self._card_user_info = CardUserInfo.from_alipay_dict(value)
    @property
    def exchange_order_id(self):
        return self._exchange_order_id

    @exchange_order_id.setter
    def exchange_order_id(self, value):
        self._exchange_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.card_user_info:
            if hasattr(self.card_user_info, 'to_alipay_dict'):
                params['card_user_info'] = self.card_user_info.to_alipay_dict()
            else:
                params['card_user_info'] = self.card_user_info
        if self.exchange_order_id:
            if hasattr(self.exchange_order_id, 'to_alipay_dict'):
                params['exchange_order_id'] = self.exchange_order_id.to_alipay_dict()
            else:
                params['exchange_order_id'] = self.exchange_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingPointOrderQueryModel()
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'card_user_info' in d:
            o.card_user_info = d['card_user_info']
        if 'exchange_order_id' in d:
            o.exchange_order_id = d['exchange_order_id']
        return o


