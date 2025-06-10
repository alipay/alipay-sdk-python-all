#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportCarsaleOrderSyncModel(object):

    def __init__(self):
        self._cancel_reason = None
        self._delivery_method = None
        self._notice_status = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._seller_partner_id = None
        self._seller_price = None
        self._user_id = None

    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def delivery_method(self):
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, value):
        self._delivery_method = value
    @property
    def notice_status(self):
        return self._notice_status

    @notice_status.setter
    def notice_status(self, value):
        self._notice_status = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def seller_partner_id(self):
        return self._seller_partner_id

    @seller_partner_id.setter
    def seller_partner_id(self, value):
        self._seller_partner_id = value
    @property
    def seller_price(self):
        return self._seller_price

    @seller_price.setter
    def seller_price(self, value):
        self._seller_price = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.delivery_method:
            if hasattr(self.delivery_method, 'to_alipay_dict'):
                params['delivery_method'] = self.delivery_method.to_alipay_dict()
            else:
                params['delivery_method'] = self.delivery_method
        if self.notice_status:
            if hasattr(self.notice_status, 'to_alipay_dict'):
                params['notice_status'] = self.notice_status.to_alipay_dict()
            else:
                params['notice_status'] = self.notice_status
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.seller_partner_id:
            if hasattr(self.seller_partner_id, 'to_alipay_dict'):
                params['seller_partner_id'] = self.seller_partner_id.to_alipay_dict()
            else:
                params['seller_partner_id'] = self.seller_partner_id
        if self.seller_price:
            if hasattr(self.seller_price, 'to_alipay_dict'):
                params['seller_price'] = self.seller_price.to_alipay_dict()
            else:
                params['seller_price'] = self.seller_price
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
        o = AlipayCommerceTransportCarsaleOrderSyncModel()
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'delivery_method' in d:
            o.delivery_method = d['delivery_method']
        if 'notice_status' in d:
            o.notice_status = d['notice_status']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'seller_partner_id' in d:
            o.seller_partner_id = d['seller_partner_id']
        if 'seller_price' in d:
            o.seller_price = d['seller_price']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


