#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo
from alipay.aop.api.domain.PaymentInformation import PaymentInformation


class AlipayMerchantOrderRefundModel(object):

    def __init__(self):
        self._biz_scene = None
        self._buyer = None
        self._ext_info = None
        self._order_id = None
        self._out_biz_no = None
        self._refund_reason = None
        self._refund_request = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, UserIdentity):
            self._buyer = value
        else:
            self._buyer = UserIdentity.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, OrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(OrderExtInfo.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_request(self):
        return self._refund_request

    @refund_request.setter
    def refund_request(self, value):
        if isinstance(value, list):
            self._refund_request = list()
            for i in value:
                if isinstance(i, PaymentInformation):
                    self._refund_request.append(i)
                else:
                    self._refund_request.append(PaymentInformation.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.refund_request:
            if isinstance(self.refund_request, list):
                for i in range(0, len(self.refund_request)):
                    element = self.refund_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_request[i] = element.to_alipay_dict()
            if hasattr(self.refund_request, 'to_alipay_dict'):
                params['refund_request'] = self.refund_request.to_alipay_dict()
            else:
                params['refund_request'] = self.refund_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantOrderRefundModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_request' in d:
            o.refund_request = d['refund_request']
        return o


