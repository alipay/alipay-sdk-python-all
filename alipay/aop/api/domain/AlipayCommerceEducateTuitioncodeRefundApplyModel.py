#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundPaidDetail import RefundPaidDetail


class AlipayCommerceEducateTuitioncodeRefundApplyModel(object):

    def __init__(self):
        self._out_order_no = None
        self._refund_paid_detail_list = None
        self._refund_reason = None
        self._refund_type = None
        self._request_id = None
        self._smid = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def refund_paid_detail_list(self):
        return self._refund_paid_detail_list

    @refund_paid_detail_list.setter
    def refund_paid_detail_list(self, value):
        if isinstance(value, list):
            self._refund_paid_detail_list = list()
            for i in value:
                if isinstance(i, RefundPaidDetail):
                    self._refund_paid_detail_list.append(i)
                else:
                    self._refund_paid_detail_list.append(RefundPaidDetail.from_alipay_dict(i))
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.refund_paid_detail_list:
            if isinstance(self.refund_paid_detail_list, list):
                for i in range(0, len(self.refund_paid_detail_list)):
                    element = self.refund_paid_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_paid_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_paid_detail_list, 'to_alipay_dict'):
                params['refund_paid_detail_list'] = self.refund_paid_detail_list.to_alipay_dict()
            else:
                params['refund_paid_detail_list'] = self.refund_paid_detail_list
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.refund_type:
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTuitioncodeRefundApplyModel()
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'refund_paid_detail_list' in d:
            o.refund_paid_detail_list = d['refund_paid_detail_list']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'smid' in d:
            o.smid = d['smid']
        return o


