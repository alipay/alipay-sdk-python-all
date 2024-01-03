#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherVerifyInfo(object):

    def __init__(self):
        self._card_no = None
        self._expiry_date = None
        self._out_item_id = None
        self._out_voucher_id = None
        self._service_link_url = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_voucher_id(self):
        return self._out_voucher_id

    @out_voucher_id.setter
    def out_voucher_id(self, value):
        self._out_voucher_id = value
    @property
    def service_link_url(self):
        return self._service_link_url

    @service_link_url.setter
    def service_link_url(self, value):
        self._service_link_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.expiry_date:
            if hasattr(self.expiry_date, 'to_alipay_dict'):
                params['expiry_date'] = self.expiry_date.to_alipay_dict()
            else:
                params['expiry_date'] = self.expiry_date
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_voucher_id:
            if hasattr(self.out_voucher_id, 'to_alipay_dict'):
                params['out_voucher_id'] = self.out_voucher_id.to_alipay_dict()
            else:
                params['out_voucher_id'] = self.out_voucher_id
        if self.service_link_url:
            if hasattr(self.service_link_url, 'to_alipay_dict'):
                params['service_link_url'] = self.service_link_url.to_alipay_dict()
            else:
                params['service_link_url'] = self.service_link_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherVerifyInfo()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'expiry_date' in d:
            o.expiry_date = d['expiry_date']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_voucher_id' in d:
            o.out_voucher_id = d['out_voucher_id']
        if 'service_link_url' in d:
            o.service_link_url = d['service_link_url']
        return o


