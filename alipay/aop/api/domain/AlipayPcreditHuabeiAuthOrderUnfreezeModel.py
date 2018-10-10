#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiAuthOrderUnfreezeModel(object):

    def __init__(self):
        self._agreement_no = None
        self._alipay_user_id = None
        self._need_terminated = None
        self._order_title = None
        self._out_request_no = None
        self._seller_id = None
        self._unfreeze_amount = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def need_terminated(self):
        return self._need_terminated

    @need_terminated.setter
    def need_terminated(self, value):
        self._need_terminated = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
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
    def unfreeze_amount(self):
        return self._unfreeze_amount

    @unfreeze_amount.setter
    def unfreeze_amount(self, value):
        self._unfreeze_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.need_terminated:
            if hasattr(self.need_terminated, 'to_alipay_dict'):
                params['need_terminated'] = self.need_terminated.to_alipay_dict()
            else:
                params['need_terminated'] = self.need_terminated
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
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
        if self.unfreeze_amount:
            if hasattr(self.unfreeze_amount, 'to_alipay_dict'):
                params['unfreeze_amount'] = self.unfreeze_amount.to_alipay_dict()
            else:
                params['unfreeze_amount'] = self.unfreeze_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiAuthOrderUnfreezeModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'need_terminated' in d:
            o.need_terminated = d['need_terminated']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'unfreeze_amount' in d:
            o.unfreeze_amount = d['unfreeze_amount']
        return o


