#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpLabelPlateinfoNotifyModel(object):

    def __init__(self):
        self._channel = None
        self._commission = None
        self._created_at = None
        self._delivered_at = None
        self._delivered_signed_at = None
        self._granted_at = None
        self._inner_biz_no = None
        self._order_extends = None
        self._pay_amount = None
        self._pay_at = None
        self._postage_amount = None
        self._product_amount = None
        self._refund_amount = None
        self._refund_at = None
        self._status = None
        self._trigger_event_flag = None
        self._trigger_order_sn = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, value):
        self._commission = value
    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value
    @property
    def delivered_at(self):
        return self._delivered_at

    @delivered_at.setter
    def delivered_at(self, value):
        self._delivered_at = value
    @property
    def delivered_signed_at(self):
        return self._delivered_signed_at

    @delivered_signed_at.setter
    def delivered_signed_at(self, value):
        self._delivered_signed_at = value
    @property
    def granted_at(self):
        return self._granted_at

    @granted_at.setter
    def granted_at(self, value):
        self._granted_at = value
    @property
    def inner_biz_no(self):
        return self._inner_biz_no

    @inner_biz_no.setter
    def inner_biz_no(self, value):
        self._inner_biz_no = value
    @property
    def order_extends(self):
        return self._order_extends

    @order_extends.setter
    def order_extends(self, value):
        self._order_extends = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_at(self):
        return self._pay_at

    @pay_at.setter
    def pay_at(self, value):
        self._pay_at = value
    @property
    def postage_amount(self):
        return self._postage_amount

    @postage_amount.setter
    def postage_amount(self, value):
        self._postage_amount = value
    @property
    def product_amount(self):
        return self._product_amount

    @product_amount.setter
    def product_amount(self, value):
        self._product_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_at(self):
        return self._refund_at

    @refund_at.setter
    def refund_at(self, value):
        self._refund_at = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trigger_event_flag(self):
        return self._trigger_event_flag

    @trigger_event_flag.setter
    def trigger_event_flag(self, value):
        self._trigger_event_flag = value
    @property
    def trigger_order_sn(self):
        return self._trigger_order_sn

    @trigger_order_sn.setter
    def trigger_order_sn(self, value):
        self._trigger_order_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.commission:
            if hasattr(self.commission, 'to_alipay_dict'):
                params['commission'] = self.commission.to_alipay_dict()
            else:
                params['commission'] = self.commission
        if self.created_at:
            if hasattr(self.created_at, 'to_alipay_dict'):
                params['created_at'] = self.created_at.to_alipay_dict()
            else:
                params['created_at'] = self.created_at
        if self.delivered_at:
            if hasattr(self.delivered_at, 'to_alipay_dict'):
                params['delivered_at'] = self.delivered_at.to_alipay_dict()
            else:
                params['delivered_at'] = self.delivered_at
        if self.delivered_signed_at:
            if hasattr(self.delivered_signed_at, 'to_alipay_dict'):
                params['delivered_signed_at'] = self.delivered_signed_at.to_alipay_dict()
            else:
                params['delivered_signed_at'] = self.delivered_signed_at
        if self.granted_at:
            if hasattr(self.granted_at, 'to_alipay_dict'):
                params['granted_at'] = self.granted_at.to_alipay_dict()
            else:
                params['granted_at'] = self.granted_at
        if self.inner_biz_no:
            if hasattr(self.inner_biz_no, 'to_alipay_dict'):
                params['inner_biz_no'] = self.inner_biz_no.to_alipay_dict()
            else:
                params['inner_biz_no'] = self.inner_biz_no
        if self.order_extends:
            if hasattr(self.order_extends, 'to_alipay_dict'):
                params['order_extends'] = self.order_extends.to_alipay_dict()
            else:
                params['order_extends'] = self.order_extends
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_at:
            if hasattr(self.pay_at, 'to_alipay_dict'):
                params['pay_at'] = self.pay_at.to_alipay_dict()
            else:
                params['pay_at'] = self.pay_at
        if self.postage_amount:
            if hasattr(self.postage_amount, 'to_alipay_dict'):
                params['postage_amount'] = self.postage_amount.to_alipay_dict()
            else:
                params['postage_amount'] = self.postage_amount
        if self.product_amount:
            if hasattr(self.product_amount, 'to_alipay_dict'):
                params['product_amount'] = self.product_amount.to_alipay_dict()
            else:
                params['product_amount'] = self.product_amount
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_at:
            if hasattr(self.refund_at, 'to_alipay_dict'):
                params['refund_at'] = self.refund_at.to_alipay_dict()
            else:
                params['refund_at'] = self.refund_at
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trigger_event_flag:
            if hasattr(self.trigger_event_flag, 'to_alipay_dict'):
                params['trigger_event_flag'] = self.trigger_event_flag.to_alipay_dict()
            else:
                params['trigger_event_flag'] = self.trigger_event_flag
        if self.trigger_order_sn:
            if hasattr(self.trigger_order_sn, 'to_alipay_dict'):
                params['trigger_order_sn'] = self.trigger_order_sn.to_alipay_dict()
            else:
                params['trigger_order_sn'] = self.trigger_order_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpLabelPlateinfoNotifyModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'commission' in d:
            o.commission = d['commission']
        if 'created_at' in d:
            o.created_at = d['created_at']
        if 'delivered_at' in d:
            o.delivered_at = d['delivered_at']
        if 'delivered_signed_at' in d:
            o.delivered_signed_at = d['delivered_signed_at']
        if 'granted_at' in d:
            o.granted_at = d['granted_at']
        if 'inner_biz_no' in d:
            o.inner_biz_no = d['inner_biz_no']
        if 'order_extends' in d:
            o.order_extends = d['order_extends']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_at' in d:
            o.pay_at = d['pay_at']
        if 'postage_amount' in d:
            o.postage_amount = d['postage_amount']
        if 'product_amount' in d:
            o.product_amount = d['product_amount']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_at' in d:
            o.refund_at = d['refund_at']
        if 'status' in d:
            o.status = d['status']
        if 'trigger_event_flag' in d:
            o.trigger_event_flag = d['trigger_event_flag']
        if 'trigger_order_sn' in d:
            o.trigger_order_sn = d['trigger_order_sn']
        return o


