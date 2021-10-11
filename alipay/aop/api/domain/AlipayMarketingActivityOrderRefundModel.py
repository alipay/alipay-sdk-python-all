#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundActivityInfo import RefundActivityInfo


class AlipayMarketingActivityOrderRefundModel(object):

    def __init__(self):
        self._buyer_id = None
        self._order_no = None
        self._out_biz_no = None
        self._refund_activity_info_list = None
        self._refund_type = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def refund_activity_info_list(self):
        return self._refund_activity_info_list

    @refund_activity_info_list.setter
    def refund_activity_info_list(self, value):
        if isinstance(value, list):
            self._refund_activity_info_list = list()
            for i in value:
                if isinstance(i, RefundActivityInfo):
                    self._refund_activity_info_list.append(i)
                else:
                    self._refund_activity_info_list.append(RefundActivityInfo.from_alipay_dict(i))
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.refund_activity_info_list:
            if isinstance(self.refund_activity_info_list, list):
                for i in range(0, len(self.refund_activity_info_list)):
                    element = self.refund_activity_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_activity_info_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_activity_info_list, 'to_alipay_dict'):
                params['refund_activity_info_list'] = self.refund_activity_info_list.to_alipay_dict()
            else:
                params['refund_activity_info_list'] = self.refund_activity_info_list
        if self.refund_type:
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityOrderRefundModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'refund_activity_info_list' in d:
            o.refund_activity_info_list = d['refund_activity_info_list']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        return o


