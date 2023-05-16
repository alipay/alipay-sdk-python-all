#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrISVUserDTO import IndrISVUserDTO
from alipay.aop.api.domain.IndrISVUserDTO import IndrISVUserDTO
from alipay.aop.api.domain.IndrISVPaymentInfoDTO import IndrISVPaymentInfoDTO


class AlipayOverseasOpenIndrpreorderCreateModel(object):

    def __init__(self):
        self._alipay_login_id = None
        self._buyer_info = None
        self._payer_info = None
        self._payment_info = None
        self._pre_order_id = None
        self._request_id = None
        self._scene_custom_param = None
        self._scene_type = None

    @property
    def alipay_login_id(self):
        return self._alipay_login_id

    @alipay_login_id.setter
    def alipay_login_id(self, value):
        self._alipay_login_id = value
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, IndrISVUserDTO):
            self._buyer_info = value
        else:
            self._buyer_info = IndrISVUserDTO.from_alipay_dict(value)
    @property
    def payer_info(self):
        return self._payer_info

    @payer_info.setter
    def payer_info(self, value):
        if isinstance(value, IndrISVUserDTO):
            self._payer_info = value
        else:
            self._payer_info = IndrISVUserDTO.from_alipay_dict(value)
    @property
    def payment_info(self):
        return self._payment_info

    @payment_info.setter
    def payment_info(self, value):
        if isinstance(value, IndrISVPaymentInfoDTO):
            self._payment_info = value
        else:
            self._payment_info = IndrISVPaymentInfoDTO.from_alipay_dict(value)
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_custom_param(self):
        return self._scene_custom_param

    @scene_custom_param.setter
    def scene_custom_param(self, value):
        self._scene_custom_param = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_login_id:
            if hasattr(self.alipay_login_id, 'to_alipay_dict'):
                params['alipay_login_id'] = self.alipay_login_id.to_alipay_dict()
            else:
                params['alipay_login_id'] = self.alipay_login_id
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.payer_info:
            if hasattr(self.payer_info, 'to_alipay_dict'):
                params['payer_info'] = self.payer_info.to_alipay_dict()
            else:
                params['payer_info'] = self.payer_info
        if self.payment_info:
            if hasattr(self.payment_info, 'to_alipay_dict'):
                params['payment_info'] = self.payment_info.to_alipay_dict()
            else:
                params['payment_info'] = self.payment_info
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_custom_param:
            if hasattr(self.scene_custom_param, 'to_alipay_dict'):
                params['scene_custom_param'] = self.scene_custom_param.to_alipay_dict()
            else:
                params['scene_custom_param'] = self.scene_custom_param
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenIndrpreorderCreateModel()
        if 'alipay_login_id' in d:
            o.alipay_login_id = d['alipay_login_id']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'payer_info' in d:
            o.payer_info = d['payer_info']
        if 'payment_info' in d:
            o.payment_info = d['payment_info']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_custom_param' in d:
            o.scene_custom_param = d['scene_custom_param']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


