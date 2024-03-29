#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentServiceInfoDTO(object):

    def __init__(self):
        self._account_book_id = None
        self._available_amount = None
        self._service_no = None

    @property
    def account_book_id(self):
        return self._account_book_id

    @account_book_id.setter
    def account_book_id(self, value):
        self._account_book_id = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def service_no(self):
        return self._service_no

    @service_no.setter
    def service_no(self, value):
        self._service_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_book_id:
            if hasattr(self.account_book_id, 'to_alipay_dict'):
                params['account_book_id'] = self.account_book_id.to_alipay_dict()
            else:
                params['account_book_id'] = self.account_book_id
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.service_no:
            if hasattr(self.service_no, 'to_alipay_dict'):
                params['service_no'] = self.service_no.to_alipay_dict()
            else:
                params['service_no'] = self.service_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentServiceInfoDTO()
        if 'account_book_id' in d:
            o.account_book_id = d['account_book_id']
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'service_no' in d:
            o.service_no = d['service_no']
        return o


