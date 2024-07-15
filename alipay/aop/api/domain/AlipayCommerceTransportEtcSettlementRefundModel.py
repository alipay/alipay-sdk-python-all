#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ETCRefundItemDto import ETCRefundItemDto


class AlipayCommerceTransportEtcSettlementRefundModel(object):

    def __init__(self):
        self._biz_agreement_no = None
        self._out_order_id = None
        self._out_request_no = None
        self._refund_amount = None
        self._refund_item_list = None
        self._refund_reason = None

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
    def refund_item_list(self):
        return self._refund_item_list

    @refund_item_list.setter
    def refund_item_list(self, value):
        if isinstance(value, list):
            self._refund_item_list = list()
            for i in value:
                if isinstance(i, ETCRefundItemDto):
                    self._refund_item_list.append(i)
                else:
                    self._refund_item_list.append(ETCRefundItemDto.from_alipay_dict(i))
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value


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
        if self.refund_item_list:
            if isinstance(self.refund_item_list, list):
                for i in range(0, len(self.refund_item_list)):
                    element = self.refund_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_item_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_item_list, 'to_alipay_dict'):
                params['refund_item_list'] = self.refund_item_list.to_alipay_dict()
            else:
                params['refund_item_list'] = self.refund_item_list
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcSettlementRefundModel()
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_item_list' in d:
            o.refund_item_list = d['refund_item_list']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        return o


