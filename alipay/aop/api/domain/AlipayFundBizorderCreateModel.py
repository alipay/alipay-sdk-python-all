#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Participant import Participant


class AlipayFundBizorderCreateModel(object):

    def __init__(self):
        self._business_params = None
        self._order_amount = None
        self._order_title = None
        self._out_biz_no = None
        self._partner_user_id = None
        self._payee_info = None

    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_user_id(self):
        return self._partner_user_id

    @partner_user_id.setter
    def partner_user_id(self, value):
        self._partner_user_id = value
    @property
    def payee_info(self):
        return self._payee_info

    @payee_info.setter
    def payee_info(self, value):
        if isinstance(value, Participant):
            self._payee_info = value
        else:
            self._payee_info = Participant.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_user_id:
            if hasattr(self.partner_user_id, 'to_alipay_dict'):
                params['partner_user_id'] = self.partner_user_id.to_alipay_dict()
            else:
                params['partner_user_id'] = self.partner_user_id
        if self.payee_info:
            if hasattr(self.payee_info, 'to_alipay_dict'):
                params['payee_info'] = self.payee_info.to_alipay_dict()
            else:
                params['payee_info'] = self.payee_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundBizorderCreateModel()
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_user_id' in d:
            o.partner_user_id = d['partner_user_id']
        if 'payee_info' in d:
            o.payee_info = d['payee_info']
        return o


