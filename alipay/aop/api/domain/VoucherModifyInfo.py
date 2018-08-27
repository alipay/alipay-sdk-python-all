#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherTermInfo import VoucherTermInfo


class VoucherModifyInfo(object):

    def __init__(self):
        self._suitable_shops = None
        self._voucher_desc = None
        self._voucher_id = None
        self._voucher_name = None
        self._voucher_terms = None

    @property
    def suitable_shops(self):
        return self._suitable_shops

    @suitable_shops.setter
    def suitable_shops(self, value):
        if isinstance(value, list):
            self._suitable_shops = list()
            for i in value:
                self._suitable_shops.append(i)
    @property
    def voucher_desc(self):
        return self._voucher_desc

    @voucher_desc.setter
    def voucher_desc(self, value):
        self._voucher_desc = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_terms(self):
        return self._voucher_terms

    @voucher_terms.setter
    def voucher_terms(self, value):
        if isinstance(value, list):
            self._voucher_terms = list()
            for i in value:
                if isinstance(i, VoucherTermInfo):
                    self._voucher_terms.append(i)
                else:
                    self._voucher_terms.append(VoucherTermInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.suitable_shops:
            if isinstance(self.suitable_shops, list):
                for i in range(0, len(self.suitable_shops)):
                    element = self.suitable_shops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.suitable_shops[i] = element.to_alipay_dict()
            if hasattr(self.suitable_shops, 'to_alipay_dict'):
                params['suitable_shops'] = self.suitable_shops.to_alipay_dict()
            else:
                params['suitable_shops'] = self.suitable_shops
        if self.voucher_desc:
            if hasattr(self.voucher_desc, 'to_alipay_dict'):
                params['voucher_desc'] = self.voucher_desc.to_alipay_dict()
            else:
                params['voucher_desc'] = self.voucher_desc
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_terms:
            if isinstance(self.voucher_terms, list):
                for i in range(0, len(self.voucher_terms)):
                    element = self.voucher_terms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_terms[i] = element.to_alipay_dict()
            if hasattr(self.voucher_terms, 'to_alipay_dict'):
                params['voucher_terms'] = self.voucher_terms.to_alipay_dict()
            else:
                params['voucher_terms'] = self.voucher_terms
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherModifyInfo()
        if 'suitable_shops' in d:
            o.suitable_shops = d['suitable_shops']
        if 'voucher_desc' in d:
            o.voucher_desc = d['voucher_desc']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_terms' in d:
            o.voucher_terms = d['voucher_terms']
        return o


