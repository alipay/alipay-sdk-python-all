#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHdfServicerightConfirmModel(object):

    def __init__(self):
        self._biz_identity = None
        self._business_order_id = None
        self._open_partner_user_id = None
        self._order_id = None
        self._service_type = None

    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def business_order_id(self):
        return self._business_order_id

    @business_order_id.setter
    def business_order_id(self, value):
        self._business_order_id = value
    @property
    def open_partner_user_id(self):
        return self._open_partner_user_id

    @open_partner_user_id.setter
    def open_partner_user_id(self, value):
        self._open_partner_user_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_identity:
            if hasattr(self.biz_identity, 'to_alipay_dict'):
                params['biz_identity'] = self.biz_identity.to_alipay_dict()
            else:
                params['biz_identity'] = self.biz_identity
        if self.business_order_id:
            if hasattr(self.business_order_id, 'to_alipay_dict'):
                params['business_order_id'] = self.business_order_id.to_alipay_dict()
            else:
                params['business_order_id'] = self.business_order_id
        if self.open_partner_user_id:
            if hasattr(self.open_partner_user_id, 'to_alipay_dict'):
                params['open_partner_user_id'] = self.open_partner_user_id.to_alipay_dict()
            else:
                params['open_partner_user_id'] = self.open_partner_user_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHdfServicerightConfirmModel()
        if 'biz_identity' in d:
            o.biz_identity = d['biz_identity']
        if 'business_order_id' in d:
            o.business_order_id = d['business_order_id']
        if 'open_partner_user_id' in d:
            o.open_partner_user_id = d['open_partner_user_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'service_type' in d:
            o.service_type = d['service_type']
        return o


