#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallGoodsDetail import MallGoodsDetail


class AdvanceOrder(object):

    def __init__(self):
        self._advance_order_id = None
        self._biz_scene = None
        self._body = None
        self._channel = None
        self._ext_info = None
        self._goods_details = None
        self._mall_id = None
        self._operator_id = None
        self._out_order_no = None
        self._seller_user_id = None
        self._shop_id = None
        self._status = None
        self._store_id = None
        self._store_name = None
        self._subject = None
        self._terminal_id = None
        self._total_amount = None

    @property
    def advance_order_id(self):
        return self._advance_order_id

    @advance_order_id.setter
    def advance_order_id(self, value):
        self._advance_order_id = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def goods_details(self):
        return self._goods_details

    @goods_details.setter
    def goods_details(self, value):
        if isinstance(value, list):
            self._goods_details = list()
            for i in value:
                if isinstance(i, MallGoodsDetail):
                    self._goods_details.append(i)
                else:
                    self._goods_details.append(MallGoodsDetail.from_alipay_dict(i))
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def seller_user_id(self):
        return self._seller_user_id

    @seller_user_id.setter
    def seller_user_id(self, value):
        self._seller_user_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_order_id:
            if hasattr(self.advance_order_id, 'to_alipay_dict'):
                params['advance_order_id'] = self.advance_order_id.to_alipay_dict()
            else:
                params['advance_order_id'] = self.advance_order_id
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.seller_user_id:
            if hasattr(self.seller_user_id, 'to_alipay_dict'):
                params['seller_user_id'] = self.seller_user_id.to_alipay_dict()
            else:
                params['seller_user_id'] = self.seller_user_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdvanceOrder()
        if 'advance_order_id' in d:
            o.advance_order_id = d['advance_order_id']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'body' in d:
            o.body = d['body']
        if 'channel' in d:
            o.channel = d['channel']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'goods_details' in d:
            o.goods_details = d['goods_details']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'seller_user_id' in d:
            o.seller_user_id = d['seller_user_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'subject' in d:
            o.subject = d['subject']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


