#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BelongMerchantInfoDTO import BelongMerchantInfoDTO
from alipay.aop.api.domain.UserInformation import UserInformation
from alipay.aop.api.domain.DiscountInfoDataDTO import DiscountInfoDataDTO
from alipay.aop.api.domain.EnviromentalInfoDTO import EnviromentalInfoDTO
from alipay.aop.api.domain.GoodExpirationListDTO import GoodExpirationListDTO
from alipay.aop.api.domain.GreenCupsDTO import GreenCupsDTO
from alipay.aop.api.domain.ItemOrderInfoDTO import ItemOrderInfoDTO
from alipay.aop.api.domain.OrderLogisticsInformationRequestDTO import OrderLogisticsInformationRequestDTO
from alipay.aop.api.domain.OrderGoodsDTO import OrderGoodsDTO


class ReceiptOrderDTO(object):

    def __init__(self):
        self._alipay_uid = None
        self._amount = None
        self._belong_merchant_info = None
        self._borrow_time = None
        self._buyer_info = None
        self._currency = None
        self._discount_amount = None
        self._discount_info_list = None
        self._environmental_info = None
        self._good_expiration_list = None
        self._green_cups_list = None
        self._invoice_entry = None
        self._is_alipay_ticket = None
        self._item_order_list = None
        self._location = None
        self._logistics_info_list = None
        self._merchant_name = None
        self._order_create_time = None
        self._order_goods_list = None
        self._order_link = None
        self._order_modified_time = None
        self._order_pay_time = None
        self._order_type = None
        self._out_biz_no = None
        self._pay_amount = None
        self._pay_type = None
        self._shop_address = None
        self._shop_contract = None
        self._shop_name = None
        self._shop_type = None
        self._terminal_id = None
        self._trade_no = None
        self._trade_type = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, BelongMerchantInfoDTO):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = BelongMerchantInfoDTO.from_alipay_dict(value)
    @property
    def borrow_time(self):
        return self._borrow_time

    @borrow_time.setter
    def borrow_time(self, value):
        self._borrow_time = value
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, UserInformation):
            self._buyer_info = value
        else:
            self._buyer_info = UserInformation.from_alipay_dict(value)
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_info_list(self):
        return self._discount_info_list

    @discount_info_list.setter
    def discount_info_list(self, value):
        if isinstance(value, list):
            self._discount_info_list = list()
            for i in value:
                if isinstance(i, DiscountInfoDataDTO):
                    self._discount_info_list.append(i)
                else:
                    self._discount_info_list.append(DiscountInfoDataDTO.from_alipay_dict(i))
    @property
    def environmental_info(self):
        return self._environmental_info

    @environmental_info.setter
    def environmental_info(self, value):
        if isinstance(value, list):
            self._environmental_info = list()
            for i in value:
                if isinstance(i, EnviromentalInfoDTO):
                    self._environmental_info.append(i)
                else:
                    self._environmental_info.append(EnviromentalInfoDTO.from_alipay_dict(i))
    @property
    def good_expiration_list(self):
        return self._good_expiration_list

    @good_expiration_list.setter
    def good_expiration_list(self, value):
        if isinstance(value, list):
            self._good_expiration_list = list()
            for i in value:
                if isinstance(i, GoodExpirationListDTO):
                    self._good_expiration_list.append(i)
                else:
                    self._good_expiration_list.append(GoodExpirationListDTO.from_alipay_dict(i))
    @property
    def green_cups_list(self):
        return self._green_cups_list

    @green_cups_list.setter
    def green_cups_list(self, value):
        if isinstance(value, list):
            self._green_cups_list = list()
            for i in value:
                if isinstance(i, GreenCupsDTO):
                    self._green_cups_list.append(i)
                else:
                    self._green_cups_list.append(GreenCupsDTO.from_alipay_dict(i))
    @property
    def invoice_entry(self):
        return self._invoice_entry

    @invoice_entry.setter
    def invoice_entry(self, value):
        self._invoice_entry = value
    @property
    def is_alipay_ticket(self):
        return self._is_alipay_ticket

    @is_alipay_ticket.setter
    def is_alipay_ticket(self, value):
        self._is_alipay_ticket = value
    @property
    def item_order_list(self):
        return self._item_order_list

    @item_order_list.setter
    def item_order_list(self, value):
        if isinstance(value, list):
            self._item_order_list = list()
            for i in value:
                if isinstance(i, ItemOrderInfoDTO):
                    self._item_order_list.append(i)
                else:
                    self._item_order_list.append(ItemOrderInfoDTO.from_alipay_dict(i))
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def logistics_info_list(self):
        return self._logistics_info_list

    @logistics_info_list.setter
    def logistics_info_list(self, value):
        if isinstance(value, list):
            self._logistics_info_list = list()
            for i in value:
                if isinstance(i, OrderLogisticsInformationRequestDTO):
                    self._logistics_info_list.append(i)
                else:
                    self._logistics_info_list.append(OrderLogisticsInformationRequestDTO.from_alipay_dict(i))
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_goods_list(self):
        return self._order_goods_list

    @order_goods_list.setter
    def order_goods_list(self, value):
        if isinstance(value, list):
            self._order_goods_list = list()
            for i in value:
                if isinstance(i, OrderGoodsDTO):
                    self._order_goods_list.append(i)
                else:
                    self._order_goods_list.append(OrderGoodsDTO.from_alipay_dict(i))
    @property
    def order_link(self):
        return self._order_link

    @order_link.setter
    def order_link(self, value):
        self._order_link = value
    @property
    def order_modified_time(self):
        return self._order_modified_time

    @order_modified_time.setter
    def order_modified_time(self, value):
        self._order_modified_time = value
    @property
    def order_pay_time(self):
        return self._order_pay_time

    @order_pay_time.setter
    def order_pay_time(self, value):
        self._order_pay_time = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_contract(self):
        return self._shop_contract

    @shop_contract.setter
    def shop_contract(self, value):
        self._shop_contract = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.belong_merchant_info:
            if hasattr(self.belong_merchant_info, 'to_alipay_dict'):
                params['belong_merchant_info'] = self.belong_merchant_info.to_alipay_dict()
            else:
                params['belong_merchant_info'] = self.belong_merchant_info
        if self.borrow_time:
            if hasattr(self.borrow_time, 'to_alipay_dict'):
                params['borrow_time'] = self.borrow_time.to_alipay_dict()
            else:
                params['borrow_time'] = self.borrow_time
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_info_list:
            if isinstance(self.discount_info_list, list):
                for i in range(0, len(self.discount_info_list)):
                    element = self.discount_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_info_list[i] = element.to_alipay_dict()
            if hasattr(self.discount_info_list, 'to_alipay_dict'):
                params['discount_info_list'] = self.discount_info_list.to_alipay_dict()
            else:
                params['discount_info_list'] = self.discount_info_list
        if self.environmental_info:
            if isinstance(self.environmental_info, list):
                for i in range(0, len(self.environmental_info)):
                    element = self.environmental_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.environmental_info[i] = element.to_alipay_dict()
            if hasattr(self.environmental_info, 'to_alipay_dict'):
                params['environmental_info'] = self.environmental_info.to_alipay_dict()
            else:
                params['environmental_info'] = self.environmental_info
        if self.good_expiration_list:
            if isinstance(self.good_expiration_list, list):
                for i in range(0, len(self.good_expiration_list)):
                    element = self.good_expiration_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.good_expiration_list[i] = element.to_alipay_dict()
            if hasattr(self.good_expiration_list, 'to_alipay_dict'):
                params['good_expiration_list'] = self.good_expiration_list.to_alipay_dict()
            else:
                params['good_expiration_list'] = self.good_expiration_list
        if self.green_cups_list:
            if isinstance(self.green_cups_list, list):
                for i in range(0, len(self.green_cups_list)):
                    element = self.green_cups_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.green_cups_list[i] = element.to_alipay_dict()
            if hasattr(self.green_cups_list, 'to_alipay_dict'):
                params['green_cups_list'] = self.green_cups_list.to_alipay_dict()
            else:
                params['green_cups_list'] = self.green_cups_list
        if self.invoice_entry:
            if hasattr(self.invoice_entry, 'to_alipay_dict'):
                params['invoice_entry'] = self.invoice_entry.to_alipay_dict()
            else:
                params['invoice_entry'] = self.invoice_entry
        if self.is_alipay_ticket:
            if hasattr(self.is_alipay_ticket, 'to_alipay_dict'):
                params['is_alipay_ticket'] = self.is_alipay_ticket.to_alipay_dict()
            else:
                params['is_alipay_ticket'] = self.is_alipay_ticket
        if self.item_order_list:
            if isinstance(self.item_order_list, list):
                for i in range(0, len(self.item_order_list)):
                    element = self.item_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_order_list[i] = element.to_alipay_dict()
            if hasattr(self.item_order_list, 'to_alipay_dict'):
                params['item_order_list'] = self.item_order_list.to_alipay_dict()
            else:
                params['item_order_list'] = self.item_order_list
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
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
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_goods_list:
            if isinstance(self.order_goods_list, list):
                for i in range(0, len(self.order_goods_list)):
                    element = self.order_goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_goods_list[i] = element.to_alipay_dict()
            if hasattr(self.order_goods_list, 'to_alipay_dict'):
                params['order_goods_list'] = self.order_goods_list.to_alipay_dict()
            else:
                params['order_goods_list'] = self.order_goods_list
        if self.order_link:
            if hasattr(self.order_link, 'to_alipay_dict'):
                params['order_link'] = self.order_link.to_alipay_dict()
            else:
                params['order_link'] = self.order_link
        if self.order_modified_time:
            if hasattr(self.order_modified_time, 'to_alipay_dict'):
                params['order_modified_time'] = self.order_modified_time.to_alipay_dict()
            else:
                params['order_modified_time'] = self.order_modified_time
        if self.order_pay_time:
            if hasattr(self.order_pay_time, 'to_alipay_dict'):
                params['order_pay_time'] = self.order_pay_time.to_alipay_dict()
            else:
                params['order_pay_time'] = self.order_pay_time
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_contract:
            if hasattr(self.shop_contract, 'to_alipay_dict'):
                params['shop_contract'] = self.shop_contract.to_alipay_dict()
            else:
                params['shop_contract'] = self.shop_contract
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiptOrderDTO()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'amount' in d:
            o.amount = d['amount']
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'borrow_time' in d:
            o.borrow_time = d['borrow_time']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'currency' in d:
            o.currency = d['currency']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_info_list' in d:
            o.discount_info_list = d['discount_info_list']
        if 'environmental_info' in d:
            o.environmental_info = d['environmental_info']
        if 'good_expiration_list' in d:
            o.good_expiration_list = d['good_expiration_list']
        if 'green_cups_list' in d:
            o.green_cups_list = d['green_cups_list']
        if 'invoice_entry' in d:
            o.invoice_entry = d['invoice_entry']
        if 'is_alipay_ticket' in d:
            o.is_alipay_ticket = d['is_alipay_ticket']
        if 'item_order_list' in d:
            o.item_order_list = d['item_order_list']
        if 'location' in d:
            o.location = d['location']
        if 'logistics_info_list' in d:
            o.logistics_info_list = d['logistics_info_list']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_goods_list' in d:
            o.order_goods_list = d['order_goods_list']
        if 'order_link' in d:
            o.order_link = d['order_link']
        if 'order_modified_time' in d:
            o.order_modified_time = d['order_modified_time']
        if 'order_pay_time' in d:
            o.order_pay_time = d['order_pay_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_contract' in d:
            o.shop_contract = d['shop_contract']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


