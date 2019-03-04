#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneProductAgreementCancelModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._channel = None
        self._product_sign_no = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def product_sign_no(self):
        return self._product_sign_no

    @product_sign_no.setter
    def product_sign_no(self, value):
        self._product_sign_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.product_sign_no:
            if hasattr(self.product_sign_no, 'to_alipay_dict'):
                params['product_sign_no'] = self.product_sign_no.to_alipay_dict()
            else:
                params['product_sign_no'] = self.product_sign_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneProductAgreementCancelModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'product_sign_no' in d:
            o.product_sign_no = d['product_sign_no']
        return o


