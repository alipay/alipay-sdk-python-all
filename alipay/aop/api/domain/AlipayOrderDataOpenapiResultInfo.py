#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemOrderInfoResult import ItemOrderInfoResult
from alipay.aop.api.domain.OrderLogisticsInformation import OrderLogisticsInformation
from alipay.aop.api.domain.PreAmountInfoResult import PreAmountInfoResult
from alipay.aop.api.domain.PreAmountInfoResult import PreAmountInfoResult
from alipay.aop.api.domain.OrderShopInfoResult import OrderShopInfoResult
from alipay.aop.api.domain.TicketInfoResult import TicketInfoResult


class AlipayOrderDataOpenapiResultInfo(object):

    def __init__(self):
        self._amount = None
        self._biz_no_list = None
        self._buyer_id = None
        self._discount_amount = None
        self._ext_info = None
        self._gmt_create = None
        self._gmt_pay = None
        self._item_list = None
        self._logistics_info_list = None
        self._merchant_biz_type = None
        self._merchant_order_link_page = None
        self._merchant_order_no = None
        self._merchant_user_id = None
        self._order_detail_link_page = None
        self._order_id = None
        self._order_status = None
        self._order_type = None
        self._pre_cost = None
        self._pre_promotion = None
        self._real_pay_amount = None
        self._shop_info = None
        self._ticket_info = None
        self._tiny_app_id = None
        self._tiny_app_logo = None
        self._tiny_app_name = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_no_list(self):
        return self._biz_no_list

    @biz_no_list.setter
    def biz_no_list(self, value):
        if isinstance(value, list):
            self._biz_no_list = list()
            for i in value:
                self._biz_no_list.append(i)
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ItemOrderInfoResult):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ItemOrderInfoResult.from_alipay_dict(i))
    @property
    def logistics_info_list(self):
        return self._logistics_info_list

    @logistics_info_list.setter
    def logistics_info_list(self, value):
        if isinstance(value, list):
            self._logistics_info_list = list()
            for i in value:
                if isinstance(i, OrderLogisticsInformation):
                    self._logistics_info_list.append(i)
                else:
                    self._logistics_info_list.append(OrderLogisticsInformation.from_alipay_dict(i))
    @property
    def merchant_biz_type(self):
        return self._merchant_biz_type

    @merchant_biz_type.setter
    def merchant_biz_type(self, value):
        self._merchant_biz_type = value
    @property
    def merchant_order_link_page(self):
        return self._merchant_order_link_page

    @merchant_order_link_page.setter
    def merchant_order_link_page(self, value):
        self._merchant_order_link_page = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def order_detail_link_page(self):
        return self._order_detail_link_page

    @order_detail_link_page.setter
    def order_detail_link_page(self, value):
        self._order_detail_link_page = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def pre_cost(self):
        return self._pre_cost

    @pre_cost.setter
    def pre_cost(self, value):
        if isinstance(value, PreAmountInfoResult):
            self._pre_cost = value
        else:
            self._pre_cost = PreAmountInfoResult.from_alipay_dict(value)
    @property
    def pre_promotion(self):
        return self._pre_promotion

    @pre_promotion.setter
    def pre_promotion(self, value):
        if isinstance(value, PreAmountInfoResult):
            self._pre_promotion = value
        else:
            self._pre_promotion = PreAmountInfoResult.from_alipay_dict(value)
    @property
    def real_pay_amount(self):
        return self._real_pay_amount

    @real_pay_amount.setter
    def real_pay_amount(self, value):
        self._real_pay_amount = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, OrderShopInfoResult):
            self._shop_info = value
        else:
            self._shop_info = OrderShopInfoResult.from_alipay_dict(value)
    @property
    def ticket_info(self):
        return self._ticket_info

    @ticket_info.setter
    def ticket_info(self, value):
        if isinstance(value, TicketInfoResult):
            self._ticket_info = value
        else:
            self._ticket_info = TicketInfoResult.from_alipay_dict(value)
    @property
    def tiny_app_id(self):
        return self._tiny_app_id

    @tiny_app_id.setter
    def tiny_app_id(self, value):
        self._tiny_app_id = value
    @property
    def tiny_app_logo(self):
        return self._tiny_app_logo

    @tiny_app_logo.setter
    def tiny_app_logo(self, value):
        self._tiny_app_logo = value
    @property
    def tiny_app_name(self):
        return self._tiny_app_name

    @tiny_app_name.setter
    def tiny_app_name(self, value):
        self._tiny_app_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_no_list:
            if isinstance(self.biz_no_list, list):
                for i in range(0, len(self.biz_no_list)):
                    element = self.biz_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_no_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_no_list, 'to_alipay_dict'):
                params['biz_no_list'] = self.biz_no_list.to_alipay_dict()
            else:
                params['biz_no_list'] = self.biz_no_list
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        if self.logistics_info_list:
            if isinstance(self.logistics_info_list, list):
                for i in range(0, len(self.logistics_info_list)):
                    element = self.logistics_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_info_list[i] = element.to_alipay_dict()
            if hasattr(self.logistics_info_list, 'to_alipay_dict'):
                params['logistics_info_list'] = self.logistics_info_list.to_alipay_dict()
            else:
                params['logistics_info_list'] = self.logistics_info_list
        if self.merchant_biz_type:
            if hasattr(self.merchant_biz_type, 'to_alipay_dict'):
                params['merchant_biz_type'] = self.merchant_biz_type.to_alipay_dict()
            else:
                params['merchant_biz_type'] = self.merchant_biz_type
        if self.merchant_order_link_page:
            if hasattr(self.merchant_order_link_page, 'to_alipay_dict'):
                params['merchant_order_link_page'] = self.merchant_order_link_page.to_alipay_dict()
            else:
                params['merchant_order_link_page'] = self.merchant_order_link_page
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.order_detail_link_page:
            if hasattr(self.order_detail_link_page, 'to_alipay_dict'):
                params['order_detail_link_page'] = self.order_detail_link_page.to_alipay_dict()
            else:
                params['order_detail_link_page'] = self.order_detail_link_page
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.pre_cost:
            if hasattr(self.pre_cost, 'to_alipay_dict'):
                params['pre_cost'] = self.pre_cost.to_alipay_dict()
            else:
                params['pre_cost'] = self.pre_cost
        if self.pre_promotion:
            if hasattr(self.pre_promotion, 'to_alipay_dict'):
                params['pre_promotion'] = self.pre_promotion.to_alipay_dict()
            else:
                params['pre_promotion'] = self.pre_promotion
        if self.real_pay_amount:
            if hasattr(self.real_pay_amount, 'to_alipay_dict'):
                params['real_pay_amount'] = self.real_pay_amount.to_alipay_dict()
            else:
                params['real_pay_amount'] = self.real_pay_amount
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
        if self.ticket_info:
            if hasattr(self.ticket_info, 'to_alipay_dict'):
                params['ticket_info'] = self.ticket_info.to_alipay_dict()
            else:
                params['ticket_info'] = self.ticket_info
        if self.tiny_app_id:
            if hasattr(self.tiny_app_id, 'to_alipay_dict'):
                params['tiny_app_id'] = self.tiny_app_id.to_alipay_dict()
            else:
                params['tiny_app_id'] = self.tiny_app_id
        if self.tiny_app_logo:
            if hasattr(self.tiny_app_logo, 'to_alipay_dict'):
                params['tiny_app_logo'] = self.tiny_app_logo.to_alipay_dict()
            else:
                params['tiny_app_logo'] = self.tiny_app_logo
        if self.tiny_app_name:
            if hasattr(self.tiny_app_name, 'to_alipay_dict'):
                params['tiny_app_name'] = self.tiny_app_name.to_alipay_dict()
            else:
                params['tiny_app_name'] = self.tiny_app_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOrderDataOpenapiResultInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_no_list' in d:
            o.biz_no_list = d['biz_no_list']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'logistics_info_list' in d:
            o.logistics_info_list = d['logistics_info_list']
        if 'merchant_biz_type' in d:
            o.merchant_biz_type = d['merchant_biz_type']
        if 'merchant_order_link_page' in d:
            o.merchant_order_link_page = d['merchant_order_link_page']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'order_detail_link_page' in d:
            o.order_detail_link_page = d['order_detail_link_page']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'pre_cost' in d:
            o.pre_cost = d['pre_cost']
        if 'pre_promotion' in d:
            o.pre_promotion = d['pre_promotion']
        if 'real_pay_amount' in d:
            o.real_pay_amount = d['real_pay_amount']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        if 'ticket_info' in d:
            o.ticket_info = d['ticket_info']
        if 'tiny_app_id' in d:
            o.tiny_app_id = d['tiny_app_id']
        if 'tiny_app_logo' in d:
            o.tiny_app_logo = d['tiny_app_logo']
        if 'tiny_app_name' in d:
            o.tiny_app_name = d['tiny_app_name']
        return o


