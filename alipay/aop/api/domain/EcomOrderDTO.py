#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPeriodDTO import InsPeriodDTO
from alipay.aop.api.domain.EcomLogisticsOrderDTO import EcomLogisticsOrderDTO
from alipay.aop.api.domain.PayOrderDTO import PayOrderDTO
from alipay.aop.api.domain.EcomSubOrderDTO import EcomSubOrderDTO


class EcomOrderDTO(object):

    def __init__(self):
        self._actual_pay_fee = None
        self._attributes = None
        self._buy_amount = None
        self._buyer_id = None
        self._buyer_nick = None
        self._charge_duration = None
        self._charge_guarantee_plan_type = None
        self._credit_deposit_money = None
        self._discount_fee = None
        self._ext_info = None
        self._gmt_create = None
        self._item_id = None
        self._item_pict_url = None
        self._item_price = None
        self._item_title = None
        self._item_total_value = None
        self._logistics_order = None
        self._main_order_id = None
        self._order_fee = None
        self._order_id = None
        self._order_type = None
        self._pay_order = None
        self._post_fee = None
        self._seller_id = None
        self._seller_nick = None
        self._sub_order_list = None
        self._trade_days = None
        self._trade_end_time = None
        self._trade_start_time = None

    @property
    def actual_pay_fee(self):
        return self._actual_pay_fee

    @actual_pay_fee.setter
    def actual_pay_fee(self, value):
        self._actual_pay_fee = value
    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value
    @property
    def buy_amount(self):
        return self._buy_amount

    @buy_amount.setter
    def buy_amount(self, value):
        self._buy_amount = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_nick(self):
        return self._buyer_nick

    @buyer_nick.setter
    def buyer_nick(self, value):
        self._buyer_nick = value
    @property
    def charge_duration(self):
        return self._charge_duration

    @charge_duration.setter
    def charge_duration(self, value):
        if isinstance(value, InsPeriodDTO):
            self._charge_duration = value
        else:
            self._charge_duration = InsPeriodDTO.from_alipay_dict(value)
    @property
    def charge_guarantee_plan_type(self):
        return self._charge_guarantee_plan_type

    @charge_guarantee_plan_type.setter
    def charge_guarantee_plan_type(self, value):
        self._charge_guarantee_plan_type = value
    @property
    def credit_deposit_money(self):
        return self._credit_deposit_money

    @credit_deposit_money.setter
    def credit_deposit_money(self, value):
        self._credit_deposit_money = value
    @property
    def discount_fee(self):
        return self._discount_fee

    @discount_fee.setter
    def discount_fee(self, value):
        self._discount_fee = value
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
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_pict_url(self):
        return self._item_pict_url

    @item_pict_url.setter
    def item_pict_url(self, value):
        self._item_pict_url = value
    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def item_title(self):
        return self._item_title

    @item_title.setter
    def item_title(self, value):
        self._item_title = value
    @property
    def item_total_value(self):
        return self._item_total_value

    @item_total_value.setter
    def item_total_value(self, value):
        self._item_total_value = value
    @property
    def logistics_order(self):
        return self._logistics_order

    @logistics_order.setter
    def logistics_order(self, value):
        if isinstance(value, EcomLogisticsOrderDTO):
            self._logistics_order = value
        else:
            self._logistics_order = EcomLogisticsOrderDTO.from_alipay_dict(value)
    @property
    def main_order_id(self):
        return self._main_order_id

    @main_order_id.setter
    def main_order_id(self, value):
        self._main_order_id = value
    @property
    def order_fee(self):
        return self._order_fee

    @order_fee.setter
    def order_fee(self, value):
        self._order_fee = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def pay_order(self):
        return self._pay_order

    @pay_order.setter
    def pay_order(self, value):
        if isinstance(value, PayOrderDTO):
            self._pay_order = value
        else:
            self._pay_order = PayOrderDTO.from_alipay_dict(value)
    @property
    def post_fee(self):
        return self._post_fee

    @post_fee.setter
    def post_fee(self, value):
        self._post_fee = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_nick(self):
        return self._seller_nick

    @seller_nick.setter
    def seller_nick(self, value):
        self._seller_nick = value
    @property
    def sub_order_list(self):
        return self._sub_order_list

    @sub_order_list.setter
    def sub_order_list(self, value):
        if isinstance(value, list):
            self._sub_order_list = list()
            for i in value:
                if isinstance(i, EcomSubOrderDTO):
                    self._sub_order_list.append(i)
                else:
                    self._sub_order_list.append(EcomSubOrderDTO.from_alipay_dict(i))
    @property
    def trade_days(self):
        return self._trade_days

    @trade_days.setter
    def trade_days(self, value):
        self._trade_days = value
    @property
    def trade_end_time(self):
        return self._trade_end_time

    @trade_end_time.setter
    def trade_end_time(self, value):
        self._trade_end_time = value
    @property
    def trade_start_time(self):
        return self._trade_start_time

    @trade_start_time.setter
    def trade_start_time(self, value):
        self._trade_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_pay_fee:
            if hasattr(self.actual_pay_fee, 'to_alipay_dict'):
                params['actual_pay_fee'] = self.actual_pay_fee.to_alipay_dict()
            else:
                params['actual_pay_fee'] = self.actual_pay_fee
        if self.attributes:
            if hasattr(self.attributes, 'to_alipay_dict'):
                params['attributes'] = self.attributes.to_alipay_dict()
            else:
                params['attributes'] = self.attributes
        if self.buy_amount:
            if hasattr(self.buy_amount, 'to_alipay_dict'):
                params['buy_amount'] = self.buy_amount.to_alipay_dict()
            else:
                params['buy_amount'] = self.buy_amount
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_nick:
            if hasattr(self.buyer_nick, 'to_alipay_dict'):
                params['buyer_nick'] = self.buyer_nick.to_alipay_dict()
            else:
                params['buyer_nick'] = self.buyer_nick
        if self.charge_duration:
            if hasattr(self.charge_duration, 'to_alipay_dict'):
                params['charge_duration'] = self.charge_duration.to_alipay_dict()
            else:
                params['charge_duration'] = self.charge_duration
        if self.charge_guarantee_plan_type:
            if hasattr(self.charge_guarantee_plan_type, 'to_alipay_dict'):
                params['charge_guarantee_plan_type'] = self.charge_guarantee_plan_type.to_alipay_dict()
            else:
                params['charge_guarantee_plan_type'] = self.charge_guarantee_plan_type
        if self.credit_deposit_money:
            if hasattr(self.credit_deposit_money, 'to_alipay_dict'):
                params['credit_deposit_money'] = self.credit_deposit_money.to_alipay_dict()
            else:
                params['credit_deposit_money'] = self.credit_deposit_money
        if self.discount_fee:
            if hasattr(self.discount_fee, 'to_alipay_dict'):
                params['discount_fee'] = self.discount_fee.to_alipay_dict()
            else:
                params['discount_fee'] = self.discount_fee
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
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_pict_url:
            if hasattr(self.item_pict_url, 'to_alipay_dict'):
                params['item_pict_url'] = self.item_pict_url.to_alipay_dict()
            else:
                params['item_pict_url'] = self.item_pict_url
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.item_title:
            if hasattr(self.item_title, 'to_alipay_dict'):
                params['item_title'] = self.item_title.to_alipay_dict()
            else:
                params['item_title'] = self.item_title
        if self.item_total_value:
            if hasattr(self.item_total_value, 'to_alipay_dict'):
                params['item_total_value'] = self.item_total_value.to_alipay_dict()
            else:
                params['item_total_value'] = self.item_total_value
        if self.logistics_order:
            if hasattr(self.logistics_order, 'to_alipay_dict'):
                params['logistics_order'] = self.logistics_order.to_alipay_dict()
            else:
                params['logistics_order'] = self.logistics_order
        if self.main_order_id:
            if hasattr(self.main_order_id, 'to_alipay_dict'):
                params['main_order_id'] = self.main_order_id.to_alipay_dict()
            else:
                params['main_order_id'] = self.main_order_id
        if self.order_fee:
            if hasattr(self.order_fee, 'to_alipay_dict'):
                params['order_fee'] = self.order_fee.to_alipay_dict()
            else:
                params['order_fee'] = self.order_fee
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.pay_order:
            if hasattr(self.pay_order, 'to_alipay_dict'):
                params['pay_order'] = self.pay_order.to_alipay_dict()
            else:
                params['pay_order'] = self.pay_order
        if self.post_fee:
            if hasattr(self.post_fee, 'to_alipay_dict'):
                params['post_fee'] = self.post_fee.to_alipay_dict()
            else:
                params['post_fee'] = self.post_fee
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_nick:
            if hasattr(self.seller_nick, 'to_alipay_dict'):
                params['seller_nick'] = self.seller_nick.to_alipay_dict()
            else:
                params['seller_nick'] = self.seller_nick
        if self.sub_order_list:
            if isinstance(self.sub_order_list, list):
                for i in range(0, len(self.sub_order_list)):
                    element = self.sub_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_order_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_order_list, 'to_alipay_dict'):
                params['sub_order_list'] = self.sub_order_list.to_alipay_dict()
            else:
                params['sub_order_list'] = self.sub_order_list
        if self.trade_days:
            if hasattr(self.trade_days, 'to_alipay_dict'):
                params['trade_days'] = self.trade_days.to_alipay_dict()
            else:
                params['trade_days'] = self.trade_days
        if self.trade_end_time:
            if hasattr(self.trade_end_time, 'to_alipay_dict'):
                params['trade_end_time'] = self.trade_end_time.to_alipay_dict()
            else:
                params['trade_end_time'] = self.trade_end_time
        if self.trade_start_time:
            if hasattr(self.trade_start_time, 'to_alipay_dict'):
                params['trade_start_time'] = self.trade_start_time.to_alipay_dict()
            else:
                params['trade_start_time'] = self.trade_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomOrderDTO()
        if 'actual_pay_fee' in d:
            o.actual_pay_fee = d['actual_pay_fee']
        if 'attributes' in d:
            o.attributes = d['attributes']
        if 'buy_amount' in d:
            o.buy_amount = d['buy_amount']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_nick' in d:
            o.buyer_nick = d['buyer_nick']
        if 'charge_duration' in d:
            o.charge_duration = d['charge_duration']
        if 'charge_guarantee_plan_type' in d:
            o.charge_guarantee_plan_type = d['charge_guarantee_plan_type']
        if 'credit_deposit_money' in d:
            o.credit_deposit_money = d['credit_deposit_money']
        if 'discount_fee' in d:
            o.discount_fee = d['discount_fee']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_pict_url' in d:
            o.item_pict_url = d['item_pict_url']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'item_title' in d:
            o.item_title = d['item_title']
        if 'item_total_value' in d:
            o.item_total_value = d['item_total_value']
        if 'logistics_order' in d:
            o.logistics_order = d['logistics_order']
        if 'main_order_id' in d:
            o.main_order_id = d['main_order_id']
        if 'order_fee' in d:
            o.order_fee = d['order_fee']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'pay_order' in d:
            o.pay_order = d['pay_order']
        if 'post_fee' in d:
            o.post_fee = d['post_fee']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_nick' in d:
            o.seller_nick = d['seller_nick']
        if 'sub_order_list' in d:
            o.sub_order_list = d['sub_order_list']
        if 'trade_days' in d:
            o.trade_days = d['trade_days']
        if 'trade_end_time' in d:
            o.trade_end_time = d['trade_end_time']
        if 'trade_start_time' in d:
            o.trade_start_time = d['trade_start_time']
        return o


