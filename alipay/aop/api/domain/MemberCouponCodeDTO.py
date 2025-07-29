#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberCouponCodeDTO(object):

    def __init__(self):
        self._card_no = None
        self._member_code = None
        self._redirect_url = None
        self._validity_period = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def member_code(self):
        return self._member_code

    @member_code.setter
    def member_code(self, value):
        self._member_code = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def validity_period(self):
        return self._validity_period

    @validity_period.setter
    def validity_period(self, value):
        self._validity_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.member_code:
            if hasattr(self.member_code, 'to_alipay_dict'):
                params['member_code'] = self.member_code.to_alipay_dict()
            else:
                params['member_code'] = self.member_code
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.validity_period:
            if hasattr(self.validity_period, 'to_alipay_dict'):
                params['validity_period'] = self.validity_period.to_alipay_dict()
            else:
                params['validity_period'] = self.validity_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MemberCouponCodeDTO()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'member_code' in d:
            o.member_code = d['member_code']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'validity_period' in d:
            o.validity_period = d['validity_period']
        return o


