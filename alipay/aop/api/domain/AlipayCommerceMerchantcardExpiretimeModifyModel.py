#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardExpiretimeModifyModel(object):

    def __init__(self):
        self._card_id = None
        self._expand_expire_time = None
        self._expand_reason = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def expand_expire_time(self):
        return self._expand_expire_time

    @expand_expire_time.setter
    def expand_expire_time(self, value):
        self._expand_expire_time = value
    @property
    def expand_reason(self):
        return self._expand_reason

    @expand_reason.setter
    def expand_reason(self, value):
        self._expand_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.expand_expire_time:
            if hasattr(self.expand_expire_time, 'to_alipay_dict'):
                params['expand_expire_time'] = self.expand_expire_time.to_alipay_dict()
            else:
                params['expand_expire_time'] = self.expand_expire_time
        if self.expand_reason:
            if hasattr(self.expand_reason, 'to_alipay_dict'):
                params['expand_reason'] = self.expand_reason.to_alipay_dict()
            else:
                params['expand_reason'] = self.expand_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardExpiretimeModifyModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'expand_expire_time' in d:
            o.expand_expire_time = d['expand_expire_time']
        if 'expand_reason' in d:
            o.expand_reason = d['expand_reason']
        return o


