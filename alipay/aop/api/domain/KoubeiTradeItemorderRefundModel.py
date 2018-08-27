#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundInfo import RefundInfo


class KoubeiTradeItemorderRefundModel(object):

    def __init__(self):
        self._order_no = None
        self._out_request_no = None
        self._reason = None
        self._refund_infos = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def refund_infos(self):
        return self._refund_infos

    @refund_infos.setter
    def refund_infos(self, value):
        if isinstance(value, list):
            self._refund_infos = list()
            for i in value:
                if isinstance(i, RefundInfo):
                    self._refund_infos.append(i)
                else:
                    self._refund_infos.append(RefundInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.refund_infos:
            if isinstance(self.refund_infos, list):
                for i in range(0, len(self.refund_infos)):
                    element = self.refund_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_infos[i] = element.to_alipay_dict()
            if hasattr(self.refund_infos, 'to_alipay_dict'):
                params['refund_infos'] = self.refund_infos.to_alipay_dict()
            else:
                params['refund_infos'] = self.refund_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeItemorderRefundModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'reason' in d:
            o.reason = d['reason']
        if 'refund_infos' in d:
            o.refund_infos = d['refund_infos']
        return o


