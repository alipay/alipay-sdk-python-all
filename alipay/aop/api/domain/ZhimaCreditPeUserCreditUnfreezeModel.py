#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeUserCreditUnfreezeModel(object):

    def __init__(self):
        self._amount = None
        self._buyer_id = None
        self._ext_info = None
        self._out_order_no = None
        self._out_request_no = None
        self._seller_id = None
        self._sub_out_order_no = None
        self._unfreeze_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
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
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def sub_out_order_no(self):
        return self._sub_out_order_no

    @sub_out_order_no.setter
    def sub_out_order_no(self, value):
        self._sub_out_order_no = value
    @property
    def unfreeze_type(self):
        return self._unfreeze_type

    @unfreeze_type.setter
    def unfreeze_type(self, value):
        self._unfreeze_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
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
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.sub_out_order_no:
            if hasattr(self.sub_out_order_no, 'to_alipay_dict'):
                params['sub_out_order_no'] = self.sub_out_order_no.to_alipay_dict()
            else:
                params['sub_out_order_no'] = self.sub_out_order_no
        if self.unfreeze_type:
            if hasattr(self.unfreeze_type, 'to_alipay_dict'):
                params['unfreeze_type'] = self.unfreeze_type.to_alipay_dict()
            else:
                params['unfreeze_type'] = self.unfreeze_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeUserCreditUnfreezeModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'sub_out_order_no' in d:
            o.sub_out_order_no = d['sub_out_order_no']
        if 'unfreeze_type' in d:
            o.unfreeze_type = d['unfreeze_type']
        return o


