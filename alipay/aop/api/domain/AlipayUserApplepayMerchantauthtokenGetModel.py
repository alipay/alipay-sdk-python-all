#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAppleRequestHeader import OpenApiAppleRequestHeader


class AlipayUserApplepayMerchantauthtokenGetModel(object):

    def __init__(self):
        self._amount = None
        self._currency_code = None
        self._partner_owned_merchant_identifier = None
        self._provisioning_bundle_identifier = None
        self._request_header = None
        self._transaction_notification_identifier = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def partner_owned_merchant_identifier(self):
        return self._partner_owned_merchant_identifier

    @partner_owned_merchant_identifier.setter
    def partner_owned_merchant_identifier(self, value):
        self._partner_owned_merchant_identifier = value
    @property
    def provisioning_bundle_identifier(self):
        return self._provisioning_bundle_identifier

    @provisioning_bundle_identifier.setter
    def provisioning_bundle_identifier(self, value):
        self._provisioning_bundle_identifier = value
    @property
    def request_header(self):
        return self._request_header

    @request_header.setter
    def request_header(self, value):
        if isinstance(value, OpenApiAppleRequestHeader):
            self._request_header = value
        else:
            self._request_header = OpenApiAppleRequestHeader.from_alipay_dict(value)
    @property
    def transaction_notification_identifier(self):
        return self._transaction_notification_identifier

    @transaction_notification_identifier.setter
    def transaction_notification_identifier(self, value):
        self._transaction_notification_identifier = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.partner_owned_merchant_identifier:
            if hasattr(self.partner_owned_merchant_identifier, 'to_alipay_dict'):
                params['partner_owned_merchant_identifier'] = self.partner_owned_merchant_identifier.to_alipay_dict()
            else:
                params['partner_owned_merchant_identifier'] = self.partner_owned_merchant_identifier
        if self.provisioning_bundle_identifier:
            if hasattr(self.provisioning_bundle_identifier, 'to_alipay_dict'):
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier.to_alipay_dict()
            else:
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier
        if self.request_header:
            if hasattr(self.request_header, 'to_alipay_dict'):
                params['request_header'] = self.request_header.to_alipay_dict()
            else:
                params['request_header'] = self.request_header
        if self.transaction_notification_identifier:
            if hasattr(self.transaction_notification_identifier, 'to_alipay_dict'):
                params['transaction_notification_identifier'] = self.transaction_notification_identifier.to_alipay_dict()
            else:
                params['transaction_notification_identifier'] = self.transaction_notification_identifier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserApplepayMerchantauthtokenGetModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'partner_owned_merchant_identifier' in d:
            o.partner_owned_merchant_identifier = d['partner_owned_merchant_identifier']
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        if 'request_header' in d:
            o.request_header = d['request_header']
        if 'transaction_notification_identifier' in d:
            o.transaction_notification_identifier = d['transaction_notification_identifier']
        return o


