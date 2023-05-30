#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemRefundInfoVO import ItemRefundInfoVO
from alipay.aop.api.domain.OrderCertificateInfoVO import OrderCertificateInfoVO


class OrderItemInfoVO(object):

    def __init__(self):
        self._item_cnt = None
        self._item_id = None
        self._item_refund_info = None
        self._order_certificate_infos = None
        self._out_item_id = None
        self._out_sku_id = None
        self._sale_price = None
        self._sku_id = None

    @property
    def item_cnt(self):
        return self._item_cnt

    @item_cnt.setter
    def item_cnt(self, value):
        self._item_cnt = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_refund_info(self):
        return self._item_refund_info

    @item_refund_info.setter
    def item_refund_info(self, value):
        if isinstance(value, ItemRefundInfoVO):
            self._item_refund_info = value
        else:
            self._item_refund_info = ItemRefundInfoVO.from_alipay_dict(value)
    @property
    def order_certificate_infos(self):
        return self._order_certificate_infos

    @order_certificate_infos.setter
    def order_certificate_infos(self, value):
        if isinstance(value, list):
            self._order_certificate_infos = list()
            for i in value:
                if isinstance(i, OrderCertificateInfoVO):
                    self._order_certificate_infos.append(i)
                else:
                    self._order_certificate_infos.append(OrderCertificateInfoVO.from_alipay_dict(i))
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_cnt:
            if hasattr(self.item_cnt, 'to_alipay_dict'):
                params['item_cnt'] = self.item_cnt.to_alipay_dict()
            else:
                params['item_cnt'] = self.item_cnt
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_refund_info:
            if hasattr(self.item_refund_info, 'to_alipay_dict'):
                params['item_refund_info'] = self.item_refund_info.to_alipay_dict()
            else:
                params['item_refund_info'] = self.item_refund_info
        if self.order_certificate_infos:
            if isinstance(self.order_certificate_infos, list):
                for i in range(0, len(self.order_certificate_infos)):
                    element = self.order_certificate_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_certificate_infos[i] = element.to_alipay_dict()
            if hasattr(self.order_certificate_infos, 'to_alipay_dict'):
                params['order_certificate_infos'] = self.order_certificate_infos.to_alipay_dict()
            else:
                params['order_certificate_infos'] = self.order_certificate_infos
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderItemInfoVO()
        if 'item_cnt' in d:
            o.item_cnt = d['item_cnt']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_refund_info' in d:
            o.item_refund_info = d['item_refund_info']
        if 'order_certificate_infos' in d:
            o.order_certificate_infos = d['order_certificate_infos']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


