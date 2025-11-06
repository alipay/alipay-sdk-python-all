#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentRefundItemVO import RentRefundItemVO


class RentRefundTransVO(object):

    def __init__(self):
        self._out_request_no = None
        self._refund_amount = None
        self._refund_items = None
        self._status = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_items(self):
        return self._refund_items

    @refund_items.setter
    def refund_items(self, value):
        if isinstance(value, list):
            self._refund_items = list()
            for i in value:
                if isinstance(i, RentRefundItemVO):
                    self._refund_items.append(i)
                else:
                    self._refund_items.append(RentRefundItemVO.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_items:
            if isinstance(self.refund_items, list):
                for i in range(0, len(self.refund_items)):
                    element = self.refund_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_items[i] = element.to_alipay_dict()
            if hasattr(self.refund_items, 'to_alipay_dict'):
                params['refund_items'] = self.refund_items.to_alipay_dict()
            else:
                params['refund_items'] = self.refund_items
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRefundTransVO()
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_items' in d:
            o.refund_items = d['refund_items']
        if 'status' in d:
            o.status = d['status']
        return o


