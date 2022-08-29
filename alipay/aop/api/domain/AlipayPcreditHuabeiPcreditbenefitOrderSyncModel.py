#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditbenefitOrderSyncModel(object):

    def __init__(self):
        self._alipay_order_id = None
        self._alipay_user_id = None
        self._biz_item_id = None
        self._biz_timestamp = None
        self._num = None
        self._order_create = None
        self._order_expire = None
        self._order_status = None
        self._outer_order_id = None
        self._partner_id = None
        self._trade_amount = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_item_id(self):
        return self._biz_item_id

    @biz_item_id.setter
    def biz_item_id(self, value):
        self._biz_item_id = value
    @property
    def biz_timestamp(self):
        return self._biz_timestamp

    @biz_timestamp.setter
    def biz_timestamp(self, value):
        self._biz_timestamp = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def order_create(self):
        return self._order_create

    @order_create.setter
    def order_create(self, value):
        self._order_create = value
    @property
    def order_expire(self):
        return self._order_expire

    @order_expire.setter
    def order_expire(self, value):
        self._order_expire = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def outer_order_id(self):
        return self._outer_order_id

    @outer_order_id.setter
    def outer_order_id(self, value):
        self._outer_order_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_item_id:
            if hasattr(self.biz_item_id, 'to_alipay_dict'):
                params['biz_item_id'] = self.biz_item_id.to_alipay_dict()
            else:
                params['biz_item_id'] = self.biz_item_id
        if self.biz_timestamp:
            if hasattr(self.biz_timestamp, 'to_alipay_dict'):
                params['biz_timestamp'] = self.biz_timestamp.to_alipay_dict()
            else:
                params['biz_timestamp'] = self.biz_timestamp
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.order_create:
            if hasattr(self.order_create, 'to_alipay_dict'):
                params['order_create'] = self.order_create.to_alipay_dict()
            else:
                params['order_create'] = self.order_create
        if self.order_expire:
            if hasattr(self.order_expire, 'to_alipay_dict'):
                params['order_expire'] = self.order_expire.to_alipay_dict()
            else:
                params['order_expire'] = self.order_expire
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.outer_order_id:
            if hasattr(self.outer_order_id, 'to_alipay_dict'):
                params['outer_order_id'] = self.outer_order_id.to_alipay_dict()
            else:
                params['outer_order_id'] = self.outer_order_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditbenefitOrderSyncModel()
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_item_id' in d:
            o.biz_item_id = d['biz_item_id']
        if 'biz_timestamp' in d:
            o.biz_timestamp = d['biz_timestamp']
        if 'num' in d:
            o.num = d['num']
        if 'order_create' in d:
            o.order_create = d['order_create']
        if 'order_expire' in d:
            o.order_expire = d['order_expire']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'outer_order_id' in d:
            o.outer_order_id = d['outer_order_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        return o


