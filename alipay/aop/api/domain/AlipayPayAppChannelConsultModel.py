#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizOrderInfo import BizOrderInfo
from alipay.aop.api.domain.BizExtInfo import BizExtInfo


class AlipayPayAppChannelConsultModel(object):

    def __init__(self):
        self._amount = None
        self._biz_identity = None
        self._biz_order_list = None
        self._biz_scene = None
        self._ext_params = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def biz_order_list(self):
        return self._biz_order_list

    @biz_order_list.setter
    def biz_order_list(self, value):
        if isinstance(value, list):
            self._biz_order_list = list()
            for i in value:
                if isinstance(i, BizOrderInfo):
                    self._biz_order_list.append(i)
                else:
                    self._biz_order_list.append(BizOrderInfo.from_alipay_dict(i))
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        if isinstance(value, BizExtInfo):
            self._ext_params = value
        else:
            self._ext_params = BizExtInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_identity:
            if hasattr(self.biz_identity, 'to_alipay_dict'):
                params['biz_identity'] = self.biz_identity.to_alipay_dict()
            else:
                params['biz_identity'] = self.biz_identity
        if self.biz_order_list:
            if isinstance(self.biz_order_list, list):
                for i in range(0, len(self.biz_order_list)):
                    element = self.biz_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_order_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_order_list, 'to_alipay_dict'):
                params['biz_order_list'] = self.biz_order_list.to_alipay_dict()
            else:
                params['biz_order_list'] = self.biz_order_list
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppChannelConsultModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_identity' in d:
            o.biz_identity = d['biz_identity']
        if 'biz_order_list' in d:
            o.biz_order_list = d['biz_order_list']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


