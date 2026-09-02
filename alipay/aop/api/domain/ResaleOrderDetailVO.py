#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ResaleDeliveryInfoVO import ResaleDeliveryInfoVO
from alipay.aop.api.domain.ResaleOrderItemVO import ResaleOrderItemVO
from alipay.aop.api.domain.ResaleFundInfoVO import ResaleFundInfoVO


class ResaleOrderDetailVO(object):

    def __init__(self):
        self._delivery_info = None
        self._item_info_list = None
        self._open_id = None
        self._order_amount = None
        self._order_detail_url = None
        self._order_id = None
        self._order_memo = None
        self._order_status = None
        self._order_title = None
        self._out_order_id = None
        self._ppi_order_id = None
        self._trade_info_list = None
        self._user_id = None

    @property
    def delivery_info(self):
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, value):
        if isinstance(value, ResaleDeliveryInfoVO):
            self._delivery_info = value
        else:
            self._delivery_info = ResaleDeliveryInfoVO.from_alipay_dict(value)
    @property
    def item_info_list(self):
        return self._item_info_list

    @item_info_list.setter
    def item_info_list(self, value):
        if isinstance(value, ResaleOrderItemVO):
            self._item_info_list = value
        else:
            self._item_info_list = ResaleOrderItemVO.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_detail_url(self):
        return self._order_detail_url

    @order_detail_url.setter
    def order_detail_url(self, value):
        self._order_detail_url = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_memo(self):
        return self._order_memo

    @order_memo.setter
    def order_memo(self, value):
        self._order_memo = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def ppi_order_id(self):
        return self._ppi_order_id

    @ppi_order_id.setter
    def ppi_order_id(self, value):
        self._ppi_order_id = value
    @property
    def trade_info_list(self):
        return self._trade_info_list

    @trade_info_list.setter
    def trade_info_list(self, value):
        if isinstance(value, list):
            self._trade_info_list = list()
            for i in value:
                if isinstance(i, ResaleFundInfoVO):
                    self._trade_info_list.append(i)
                else:
                    self._trade_info_list.append(ResaleFundInfoVO.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_info:
            if hasattr(self.delivery_info, 'to_alipay_dict'):
                params['delivery_info'] = self.delivery_info.to_alipay_dict()
            else:
                params['delivery_info'] = self.delivery_info
        if self.item_info_list:
            if hasattr(self.item_info_list, 'to_alipay_dict'):
                params['item_info_list'] = self.item_info_list.to_alipay_dict()
            else:
                params['item_info_list'] = self.item_info_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_detail_url:
            if hasattr(self.order_detail_url, 'to_alipay_dict'):
                params['order_detail_url'] = self.order_detail_url.to_alipay_dict()
            else:
                params['order_detail_url'] = self.order_detail_url
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_memo:
            if hasattr(self.order_memo, 'to_alipay_dict'):
                params['order_memo'] = self.order_memo.to_alipay_dict()
            else:
                params['order_memo'] = self.order_memo
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.ppi_order_id:
            if hasattr(self.ppi_order_id, 'to_alipay_dict'):
                params['ppi_order_id'] = self.ppi_order_id.to_alipay_dict()
            else:
                params['ppi_order_id'] = self.ppi_order_id
        if self.trade_info_list:
            if isinstance(self.trade_info_list, list):
                for i in range(0, len(self.trade_info_list)):
                    element = self.trade_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_info_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_info_list, 'to_alipay_dict'):
                params['trade_info_list'] = self.trade_info_list.to_alipay_dict()
            else:
                params['trade_info_list'] = self.trade_info_list
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
        o = ResaleOrderDetailVO()
        if 'delivery_info' in d:
            o.delivery_info = d['delivery_info']
        if 'item_info_list' in d:
            o.item_info_list = d['item_info_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_detail_url' in d:
            o.order_detail_url = d['order_detail_url']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_memo' in d:
            o.order_memo = d['order_memo']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'ppi_order_id' in d:
            o.ppi_order_id = d['ppi_order_id']
        if 'trade_info_list' in d:
            o.trade_info_list = d['trade_info_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


