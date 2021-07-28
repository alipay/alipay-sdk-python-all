#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumerNotifyIstd import ConsumerNotifyIstd
from alipay.aop.api.domain.GoodsDetailIstd import GoodsDetailIstd
from alipay.aop.api.domain.GoodsInfoIstd import GoodsInfoIstd
from alipay.aop.api.domain.OrderExtIstd import OrderExtIstd
from alipay.aop.api.domain.ReceiverIstd import ReceiverIstd
from alipay.aop.api.domain.SenderIstd import SenderIstd


class AlipayCommerceLogisticsOrderInstantdeliveryCreateModel(object):

    def __init__(self):
        self._consumer_id = None
        self._consumer_notify = None
        self._consumer_source = None
        self._goods_details = None
        self._goods_info = None
        self._logistics_code = None
        self._logistics_token = None
        self._order_ext_istd = None
        self._out_order_no = None
        self._receiver = None
        self._sender = None
        self._shop_no = None

    @property
    def consumer_id(self):
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, value):
        self._consumer_id = value
    @property
    def consumer_notify(self):
        return self._consumer_notify

    @consumer_notify.setter
    def consumer_notify(self, value):
        if isinstance(value, ConsumerNotifyIstd):
            self._consumer_notify = value
        else:
            self._consumer_notify = ConsumerNotifyIstd.from_alipay_dict(value)
    @property
    def consumer_source(self):
        return self._consumer_source

    @consumer_source.setter
    def consumer_source(self, value):
        self._consumer_source = value
    @property
    def goods_details(self):
        return self._goods_details

    @goods_details.setter
    def goods_details(self, value):
        if isinstance(value, list):
            self._goods_details = list()
            for i in value:
                if isinstance(i, GoodsDetailIstd):
                    self._goods_details.append(i)
                else:
                    self._goods_details.append(GoodsDetailIstd.from_alipay_dict(i))
    @property
    def goods_info(self):
        return self._goods_info

    @goods_info.setter
    def goods_info(self, value):
        if isinstance(value, GoodsInfoIstd):
            self._goods_info = value
        else:
            self._goods_info = GoodsInfoIstd.from_alipay_dict(value)
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def logistics_token(self):
        return self._logistics_token

    @logistics_token.setter
    def logistics_token(self, value):
        self._logistics_token = value
    @property
    def order_ext_istd(self):
        return self._order_ext_istd

    @order_ext_istd.setter
    def order_ext_istd(self, value):
        if isinstance(value, OrderExtIstd):
            self._order_ext_istd = value
        else:
            self._order_ext_istd = OrderExtIstd.from_alipay_dict(value)
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, value):
        if isinstance(value, ReceiverIstd):
            self._receiver = value
        else:
            self._receiver = ReceiverIstd.from_alipay_dict(value)
    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        if isinstance(value, SenderIstd):
            self._sender = value
        else:
            self._sender = SenderIstd.from_alipay_dict(value)
    @property
    def shop_no(self):
        return self._shop_no

    @shop_no.setter
    def shop_no(self, value):
        self._shop_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.consumer_id:
            if hasattr(self.consumer_id, 'to_alipay_dict'):
                params['consumer_id'] = self.consumer_id.to_alipay_dict()
            else:
                params['consumer_id'] = self.consumer_id
        if self.consumer_notify:
            if hasattr(self.consumer_notify, 'to_alipay_dict'):
                params['consumer_notify'] = self.consumer_notify.to_alipay_dict()
            else:
                params['consumer_notify'] = self.consumer_notify
        if self.consumer_source:
            if hasattr(self.consumer_source, 'to_alipay_dict'):
                params['consumer_source'] = self.consumer_source.to_alipay_dict()
            else:
                params['consumer_source'] = self.consumer_source
        if self.goods_details:
            if isinstance(self.goods_details, list):
                for i in range(0, len(self.goods_details)):
                    element = self.goods_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_details[i] = element.to_alipay_dict()
            if hasattr(self.goods_details, 'to_alipay_dict'):
                params['goods_details'] = self.goods_details.to_alipay_dict()
            else:
                params['goods_details'] = self.goods_details
        if self.goods_info:
            if hasattr(self.goods_info, 'to_alipay_dict'):
                params['goods_info'] = self.goods_info.to_alipay_dict()
            else:
                params['goods_info'] = self.goods_info
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.logistics_token:
            if hasattr(self.logistics_token, 'to_alipay_dict'):
                params['logistics_token'] = self.logistics_token.to_alipay_dict()
            else:
                params['logistics_token'] = self.logistics_token
        if self.order_ext_istd:
            if hasattr(self.order_ext_istd, 'to_alipay_dict'):
                params['order_ext_istd'] = self.order_ext_istd.to_alipay_dict()
            else:
                params['order_ext_istd'] = self.order_ext_istd
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.receiver:
            if hasattr(self.receiver, 'to_alipay_dict'):
                params['receiver'] = self.receiver.to_alipay_dict()
            else:
                params['receiver'] = self.receiver
        if self.sender:
            if hasattr(self.sender, 'to_alipay_dict'):
                params['sender'] = self.sender.to_alipay_dict()
            else:
                params['sender'] = self.sender
        if self.shop_no:
            if hasattr(self.shop_no, 'to_alipay_dict'):
                params['shop_no'] = self.shop_no.to_alipay_dict()
            else:
                params['shop_no'] = self.shop_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsOrderInstantdeliveryCreateModel()
        if 'consumer_id' in d:
            o.consumer_id = d['consumer_id']
        if 'consumer_notify' in d:
            o.consumer_notify = d['consumer_notify']
        if 'consumer_source' in d:
            o.consumer_source = d['consumer_source']
        if 'goods_details' in d:
            o.goods_details = d['goods_details']
        if 'goods_info' in d:
            o.goods_info = d['goods_info']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_token' in d:
            o.logistics_token = d['logistics_token']
        if 'order_ext_istd' in d:
            o.order_ext_istd = d['order_ext_istd']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'receiver' in d:
            o.receiver = d['receiver']
        if 'sender' in d:
            o.sender = d['sender']
        if 'shop_no' in d:
            o.shop_no = d['shop_no']
        return o


