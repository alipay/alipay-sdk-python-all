#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiscountInfos import DiscountInfos


class RefundList(object):

    def __init__(self):
        self._discount_infos = None
        self._ext_infos = None
        self._out_refund_id = None
        self._refund_amount = None
        self._refund_discount_amount = None
        self._refund_id = None
        self._refund_method = None

    @property
    def discount_infos(self):
        return self._discount_infos

    @discount_infos.setter
    def discount_infos(self, value):
        if isinstance(value, list):
            self._discount_infos = list()
            for i in value:
                if isinstance(i, DiscountInfos):
                    self._discount_infos.append(i)
                else:
                    self._discount_infos.append(DiscountInfos.from_alipay_dict(i))
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def out_refund_id(self):
        return self._out_refund_id

    @out_refund_id.setter
    def out_refund_id(self, value):
        self._out_refund_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_discount_amount(self):
        return self._refund_discount_amount

    @refund_discount_amount.setter
    def refund_discount_amount(self, value):
        self._refund_discount_amount = value
    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, value):
        self._refund_id = value
    @property
    def refund_method(self):
        return self._refund_method

    @refund_method.setter
    def refund_method(self, value):
        self._refund_method = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_infos:
            if isinstance(self.discount_infos, list):
                for i in range(0, len(self.discount_infos)):
                    element = self.discount_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_infos[i] = element.to_alipay_dict()
            if hasattr(self.discount_infos, 'to_alipay_dict'):
                params['discount_infos'] = self.discount_infos.to_alipay_dict()
            else:
                params['discount_infos'] = self.discount_infos
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.out_refund_id:
            if hasattr(self.out_refund_id, 'to_alipay_dict'):
                params['out_refund_id'] = self.out_refund_id.to_alipay_dict()
            else:
                params['out_refund_id'] = self.out_refund_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_discount_amount:
            if hasattr(self.refund_discount_amount, 'to_alipay_dict'):
                params['refund_discount_amount'] = self.refund_discount_amount.to_alipay_dict()
            else:
                params['refund_discount_amount'] = self.refund_discount_amount
        if self.refund_id:
            if hasattr(self.refund_id, 'to_alipay_dict'):
                params['refund_id'] = self.refund_id.to_alipay_dict()
            else:
                params['refund_id'] = self.refund_id
        if self.refund_method:
            if hasattr(self.refund_method, 'to_alipay_dict'):
                params['refund_method'] = self.refund_method.to_alipay_dict()
            else:
                params['refund_method'] = self.refund_method
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundList()
        if 'discount_infos' in d:
            o.discount_infos = d['discount_infos']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'out_refund_id' in d:
            o.out_refund_id = d['out_refund_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_discount_amount' in d:
            o.refund_discount_amount = d['refund_discount_amount']
        if 'refund_id' in d:
            o.refund_id = d['refund_id']
        if 'refund_method' in d:
            o.refund_method = d['refund_method']
        return o


