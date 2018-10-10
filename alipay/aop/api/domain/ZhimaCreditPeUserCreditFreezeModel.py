#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditFreezeSubOrder import CreditFreezeSubOrder


class ZhimaCreditPeUserCreditFreezeModel(object):

    def __init__(self):
        self._buyer_id = None
        self._category_code = None
        self._credit_scene = None
        self._ext_info = None
        self._out_order_no = None
        self._out_request_no = None
        self._risk_info = None
        self._seller_id = None
        self._sub_order_info = None
        self._total_credit_amount = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def credit_scene(self):
        return self._credit_scene

    @credit_scene.setter
    def credit_scene(self, value):
        self._credit_scene = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        self._risk_info = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def sub_order_info(self):
        return self._sub_order_info

    @sub_order_info.setter
    def sub_order_info(self, value):
        if isinstance(value, list):
            self._sub_order_info = list()
            for i in value:
                if isinstance(i, CreditFreezeSubOrder):
                    self._sub_order_info.append(i)
                else:
                    self._sub_order_info.append(CreditFreezeSubOrder.from_alipay_dict(i))
    @property
    def total_credit_amount(self):
        return self._total_credit_amount

    @total_credit_amount.setter
    def total_credit_amount(self, value):
        self._total_credit_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.credit_scene:
            if hasattr(self.credit_scene, 'to_alipay_dict'):
                params['credit_scene'] = self.credit_scene.to_alipay_dict()
            else:
                params['credit_scene'] = self.credit_scene
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.risk_info:
            if hasattr(self.risk_info, 'to_alipay_dict'):
                params['risk_info'] = self.risk_info.to_alipay_dict()
            else:
                params['risk_info'] = self.risk_info
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.sub_order_info:
            if isinstance(self.sub_order_info, list):
                for i in range(0, len(self.sub_order_info)):
                    element = self.sub_order_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_order_info[i] = element.to_alipay_dict()
            if hasattr(self.sub_order_info, 'to_alipay_dict'):
                params['sub_order_info'] = self.sub_order_info.to_alipay_dict()
            else:
                params['sub_order_info'] = self.sub_order_info
        if self.total_credit_amount:
            if hasattr(self.total_credit_amount, 'to_alipay_dict'):
                params['total_credit_amount'] = self.total_credit_amount.to_alipay_dict()
            else:
                params['total_credit_amount'] = self.total_credit_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeUserCreditFreezeModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'credit_scene' in d:
            o.credit_scene = d['credit_scene']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'risk_info' in d:
            o.risk_info = d['risk_info']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'sub_order_info' in d:
            o.sub_order_info = d['sub_order_info']
        if 'total_credit_amount' in d:
            o.total_credit_amount = d['total_credit_amount']
        return o


