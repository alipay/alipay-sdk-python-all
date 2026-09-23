#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAipayNowpayQuotaVerifyModel(object):

    def __init__(self):
        self._amount = None
        self._consume_reason = None
        self._external_buyer_id = None
        self._external_owner_id = None
        self._out_product_id = None
        self._out_request_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def consume_reason(self):
        return self._consume_reason

    @consume_reason.setter
    def consume_reason(self, value):
        self._consume_reason = value
    @property
    def external_buyer_id(self):
        return self._external_buyer_id

    @external_buyer_id.setter
    def external_buyer_id(self, value):
        self._external_buyer_id = value
    @property
    def external_owner_id(self):
        return self._external_owner_id

    @external_owner_id.setter
    def external_owner_id(self, value):
        self._external_owner_id = value
    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.consume_reason:
            if hasattr(self.consume_reason, 'to_alipay_dict'):
                params['consume_reason'] = self.consume_reason.to_alipay_dict()
            else:
                params['consume_reason'] = self.consume_reason
        if self.external_buyer_id:
            if hasattr(self.external_buyer_id, 'to_alipay_dict'):
                params['external_buyer_id'] = self.external_buyer_id.to_alipay_dict()
            else:
                params['external_buyer_id'] = self.external_buyer_id
        if self.external_owner_id:
            if hasattr(self.external_owner_id, 'to_alipay_dict'):
                params['external_owner_id'] = self.external_owner_id.to_alipay_dict()
            else:
                params['external_owner_id'] = self.external_owner_id
        if self.out_product_id:
            if hasattr(self.out_product_id, 'to_alipay_dict'):
                params['out_product_id'] = self.out_product_id.to_alipay_dict()
            else:
                params['out_product_id'] = self.out_product_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipayNowpayQuotaVerifyModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'consume_reason' in d:
            o.consume_reason = d['consume_reason']
        if 'external_buyer_id' in d:
            o.external_buyer_id = d['external_buyer_id']
        if 'external_owner_id' in d:
            o.external_owner_id = d['external_owner_id']
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


