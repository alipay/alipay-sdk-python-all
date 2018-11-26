#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Participant import Participant
from alipay.aop.api.domain.TransOrderDetail import TransOrderDetail


class AlipayFundTransMergePrecreateModel(object):

    def __init__(self):
        self._biz_scene = None
        self._business_params = None
        self._order_title = None
        self._payer_info = None
        self._product_code = None
        self._time_expire = None
        self._trans_order_list = None

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
    def time_expire(self):
        return self._time_expire

    @time_expire.setter
    def time_expire(self, value):
        self._time_expire = value
    @property
    def trans_order_list(self):
        return self._trans_order_list

    @trans_order_list.setter
    def trans_order_list(self, value):
        if isinstance(value, list):
            self._trans_order_list = list()
            for i in value:
                if isinstance(i, TransOrderDetail):
                    self._trans_order_list.append(i)
                else:
                    self._trans_order_list.append(TransOrderDetail.from_alipay_dict(i))


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
        if self.time_expire:
            if hasattr(self.time_expire, 'to_alipay_dict'):
                params['time_expire'] = self.time_expire.to_alipay_dict()
            else:
                params['time_expire'] = self.time_expire
        if self.trans_order_list:
            if isinstance(self.trans_order_list, list):
                for i in range(0, len(self.trans_order_list)):
                    element = self.trans_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trans_order_list[i] = element.to_alipay_dict()
            if hasattr(self.trans_order_list, 'to_alipay_dict'):
                params['trans_order_list'] = self.trans_order_list.to_alipay_dict()
            else:
                params['trans_order_list'] = self.trans_order_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransMergePrecreateModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'payer_info' in d:
            o.payer_info = d['payer_info']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'time_expire' in d:
            o.time_expire = d['time_expire']
        if 'trans_order_list' in d:
            o.trans_order_list = d['trans_order_list']
        return o


