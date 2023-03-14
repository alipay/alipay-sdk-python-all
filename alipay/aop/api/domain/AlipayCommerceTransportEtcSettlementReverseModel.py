#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcSettlementReverseModel(object):

    def __init__(self):
        self._biz_agreement_no = None
        self._out_order_id = None
        self._reverse_reason = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def reverse_reason(self):
        return self._reverse_reason

    @reverse_reason.setter
    def reverse_reason(self, value):
        self._reverse_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_agreement_no:
            if hasattr(self.biz_agreement_no, 'to_alipay_dict'):
                params['biz_agreement_no'] = self.biz_agreement_no.to_alipay_dict()
            else:
                params['biz_agreement_no'] = self.biz_agreement_no
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.reverse_reason:
            if hasattr(self.reverse_reason, 'to_alipay_dict'):
                params['reverse_reason'] = self.reverse_reason.to_alipay_dict()
            else:
                params['reverse_reason'] = self.reverse_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcSettlementReverseModel()
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'reverse_reason' in d:
            o.reverse_reason = d['reverse_reason']
        return o


