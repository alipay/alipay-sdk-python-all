#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo
from alipay.aop.api.domain.GoodsInformation import GoodsInformation
from alipay.aop.api.domain.PriceInformation import PriceInformation
from alipay.aop.api.domain.PaymentInformation import PaymentInformation
from alipay.aop.api.domain.UserIdentity import UserIdentity


class AlipayMerchantOrderCreateandpayModel(object):

    def __init__(self):
        self._biz_scene = None
        self._buyer = None
        self._ext_info = None
        self._goods_infos = None
        self._order_amount = None
        self._out_biz_no = None
        self._payment_request = None
        self._seller = None
        self._service_type = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, UserIdentity):
            self._buyer = value
        else:
            self._buyer = UserIdentity.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, OrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(OrderExtInfo.from_alipay_dict(i))
    @property
    def goods_infos(self):
        return self._goods_infos

    @goods_infos.setter
    def goods_infos(self, value):
        if isinstance(value, list):
            self._goods_infos = list()
            for i in value:
                if isinstance(i, GoodsInformation):
                    self._goods_infos.append(i)
                else:
                    self._goods_infos.append(GoodsInformation.from_alipay_dict(i))
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        if isinstance(value, list):
            self._order_amount = list()
            for i in value:
                if isinstance(i, PriceInformation):
                    self._order_amount.append(i)
                else:
                    self._order_amount.append(PriceInformation.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payment_request(self):
        return self._payment_request

    @payment_request.setter
    def payment_request(self, value):
        if isinstance(value, list):
            self._payment_request = list()
            for i in value:
                if isinstance(i, PaymentInformation):
                    self._payment_request.append(i)
                else:
                    self._payment_request.append(PaymentInformation.from_alipay_dict(i))
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, UserIdentity):
            self._seller = value
        else:
            self._seller = UserIdentity.from_alipay_dict(value)
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.goods_infos:
            if isinstance(self.goods_infos, list):
                for i in range(0, len(self.goods_infos)):
                    element = self.goods_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_infos[i] = element.to_alipay_dict()
            if hasattr(self.goods_infos, 'to_alipay_dict'):
                params['goods_infos'] = self.goods_infos.to_alipay_dict()
            else:
                params['goods_infos'] = self.goods_infos
        if self.order_amount:
            if isinstance(self.order_amount, list):
                for i in range(0, len(self.order_amount)):
                    element = self.order_amount[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_amount[i] = element.to_alipay_dict()
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payment_request:
            if isinstance(self.payment_request, list):
                for i in range(0, len(self.payment_request)):
                    element = self.payment_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_request[i] = element.to_alipay_dict()
            if hasattr(self.payment_request, 'to_alipay_dict'):
                params['payment_request'] = self.payment_request.to_alipay_dict()
            else:
                params['payment_request'] = self.payment_request
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
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
        o = AlipayMerchantOrderCreateandpayModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'goods_infos' in d:
            o.goods_infos = d['goods_infos']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payment_request' in d:
            o.payment_request = d['payment_request']
        if 'seller' in d:
            o.seller = d['seller']
        if 'service_type' in d:
            o.service_type = d['service_type']
        return o


