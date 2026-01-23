#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardExpandOrderInfo(object):

    def __init__(self):
        self._card_expand_order_id = None
        self._card_expand_order_status = None
        self._card_id = None
        self._customer_confirm_timeout = None
        self._expand_expire_date = None
        self._expand_reason = None
        self._expand_reject_reason = None
        self._original_expire_date = None

    @property
    def card_expand_order_id(self):
        return self._card_expand_order_id

    @card_expand_order_id.setter
    def card_expand_order_id(self, value):
        self._card_expand_order_id = value
    @property
    def card_expand_order_status(self):
        return self._card_expand_order_status

    @card_expand_order_status.setter
    def card_expand_order_status(self, value):
        self._card_expand_order_status = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def customer_confirm_timeout(self):
        return self._customer_confirm_timeout

    @customer_confirm_timeout.setter
    def customer_confirm_timeout(self, value):
        self._customer_confirm_timeout = value
    @property
    def expand_expire_date(self):
        return self._expand_expire_date

    @expand_expire_date.setter
    def expand_expire_date(self, value):
        self._expand_expire_date = value
    @property
    def expand_reason(self):
        return self._expand_reason

    @expand_reason.setter
    def expand_reason(self, value):
        self._expand_reason = value
    @property
    def expand_reject_reason(self):
        return self._expand_reject_reason

    @expand_reject_reason.setter
    def expand_reject_reason(self, value):
        self._expand_reject_reason = value
    @property
    def original_expire_date(self):
        return self._original_expire_date

    @original_expire_date.setter
    def original_expire_date(self, value):
        self._original_expire_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_expand_order_id:
            if hasattr(self.card_expand_order_id, 'to_alipay_dict'):
                params['card_expand_order_id'] = self.card_expand_order_id.to_alipay_dict()
            else:
                params['card_expand_order_id'] = self.card_expand_order_id
        if self.card_expand_order_status:
            if hasattr(self.card_expand_order_status, 'to_alipay_dict'):
                params['card_expand_order_status'] = self.card_expand_order_status.to_alipay_dict()
            else:
                params['card_expand_order_status'] = self.card_expand_order_status
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.customer_confirm_timeout:
            if hasattr(self.customer_confirm_timeout, 'to_alipay_dict'):
                params['customer_confirm_timeout'] = self.customer_confirm_timeout.to_alipay_dict()
            else:
                params['customer_confirm_timeout'] = self.customer_confirm_timeout
        if self.expand_expire_date:
            if hasattr(self.expand_expire_date, 'to_alipay_dict'):
                params['expand_expire_date'] = self.expand_expire_date.to_alipay_dict()
            else:
                params['expand_expire_date'] = self.expand_expire_date
        if self.expand_reason:
            if hasattr(self.expand_reason, 'to_alipay_dict'):
                params['expand_reason'] = self.expand_reason.to_alipay_dict()
            else:
                params['expand_reason'] = self.expand_reason
        if self.expand_reject_reason:
            if hasattr(self.expand_reject_reason, 'to_alipay_dict'):
                params['expand_reject_reason'] = self.expand_reject_reason.to_alipay_dict()
            else:
                params['expand_reject_reason'] = self.expand_reject_reason
        if self.original_expire_date:
            if hasattr(self.original_expire_date, 'to_alipay_dict'):
                params['original_expire_date'] = self.original_expire_date.to_alipay_dict()
            else:
                params['original_expire_date'] = self.original_expire_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardExpandOrderInfo()
        if 'card_expand_order_id' in d:
            o.card_expand_order_id = d['card_expand_order_id']
        if 'card_expand_order_status' in d:
            o.card_expand_order_status = d['card_expand_order_status']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'customer_confirm_timeout' in d:
            o.customer_confirm_timeout = d['customer_confirm_timeout']
        if 'expand_expire_date' in d:
            o.expand_expire_date = d['expand_expire_date']
        if 'expand_reason' in d:
            o.expand_reason = d['expand_reason']
        if 'expand_reject_reason' in d:
            o.expand_reject_reason = d['expand_reject_reason']
        if 'original_expire_date' in d:
            o.original_expire_date = d['original_expire_date']
        return o


