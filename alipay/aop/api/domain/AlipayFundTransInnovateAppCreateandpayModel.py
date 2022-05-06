#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Participant import Participant
from alipay.aop.api.domain.Participant import Participant


class AlipayFundTransInnovateAppCreateandpayModel(object):

    def __init__(self):
        self._biz_scene = None
        self._business_params = None
        self._order_title = None
        self._out_biz_no = None
        self._payee_info = None
        self._payer_info = None
        self._product_code = None
        self._remark = None
        self._time_expire = None
        self._trans_amount = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
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
    def payee_info(self):
        return self._payee_info

    @payee_info.setter
    def payee_info(self, value):
        if isinstance(value, Participant):
            self._payee_info = value
        else:
            self._payee_info = Participant.from_alipay_dict(value)
    @property
    def payer_info(self):
        return self._payer_info

    @payer_info.setter
    def payer_info(self, value):
        if isinstance(value, Participant):
            self._payer_info = value
        else:
            self._payer_info = Participant.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def time_expire(self):
        return self._time_expire

    @time_expire.setter
    def time_expire(self, value):
        self._time_expire = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
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
        if self.payee_info:
            if hasattr(self.payee_info, 'to_alipay_dict'):
                params['payee_info'] = self.payee_info.to_alipay_dict()
            else:
                params['payee_info'] = self.payee_info
        if self.payer_info:
            if hasattr(self.payer_info, 'to_alipay_dict'):
                params['payer_info'] = self.payer_info.to_alipay_dict()
            else:
                params['payer_info'] = self.payer_info
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.time_expire:
            if hasattr(self.time_expire, 'to_alipay_dict'):
                params['time_expire'] = self.time_expire.to_alipay_dict()
            else:
                params['time_expire'] = self.time_expire
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransInnovateAppCreateandpayModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payee_info' in d:
            o.payee_info = d['payee_info']
        if 'payer_info' in d:
            o.payer_info = d['payer_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'remark' in d:
            o.remark = d['remark']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        return o


