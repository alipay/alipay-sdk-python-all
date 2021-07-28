#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbPosOrderDishDetail import KbPosOrderDishDetail
from alipay.aop.api.domain.PosBillPayChannel import PosBillPayChannel


class KoubeiCateringOrderInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringOrderInfoQueryResponse, self).__init__()
        self._bill_amount = None
        self._biz_product = None
        self._business_type = None
        self._channel = None
        self._dinner_type = None
        self._dish_details = None
        self._ext_info = None
        self._external_shop_id = None
        self._member_flag = None
        self._memo = None
        self._merchant_id = None
        self._order_id = None
        self._order_style = None
        self._order_time = None
        self._other_amount = None
        self._packing_amount = None
        self._pay_amount = None
        self._pay_channels = None
        self._people_num = None
        self._receipt_amount = None
        self._service_amount = None
        self._shop_id = None
        self._table_time = None
        self._take_no = None
        self._take_style = None
        self._trade_amount = None
        self._user_mobile = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def dinner_type(self):
        return self._dinner_type

    @dinner_type.setter
    def dinner_type(self, value):
        self._dinner_type = value
    @property
    def dish_details(self):
        return self._dish_details

    @dish_details.setter
    def dish_details(self, value):
        if isinstance(value, list):
            self._dish_details = list()
            for i in value:
                if isinstance(i, KbPosOrderDishDetail):
                    self._dish_details.append(i)
                else:
                    self._dish_details.append(KbPosOrderDishDetail.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def external_shop_id(self):
        return self._external_shop_id

    @external_shop_id.setter
    def external_shop_id(self, value):
        self._external_shop_id = value
    @property
    def member_flag(self):
        return self._member_flag

    @member_flag.setter
    def member_flag(self, value):
        self._member_flag = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_style(self):
        return self._order_style

    @order_style.setter
    def order_style(self, value):
        self._order_style = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        self._other_amount = value
    @property
    def packing_amount(self):
        return self._packing_amount

    @packing_amount.setter
    def packing_amount(self, value):
        self._packing_amount = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_channels(self):
        return self._pay_channels

    @pay_channels.setter
    def pay_channels(self, value):
        if isinstance(value, list):
            self._pay_channels = list()
            for i in value:
                if isinstance(i, PosBillPayChannel):
                    self._pay_channels.append(i)
                else:
                    self._pay_channels.append(PosBillPayChannel.from_alipay_dict(i))
    @property
    def people_num(self):
        return self._people_num

    @people_num.setter
    def people_num(self, value):
        self._people_num = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def table_time(self):
        return self._table_time

    @table_time.setter
    def table_time(self, value):
        self._table_time = value
    @property
    def take_no(self):
        return self._take_no

    @take_no.setter
    def take_no(self, value):
        self._take_no = value
    @property
    def take_style(self):
        return self._take_style

    @take_style.setter
    def take_style(self, value):
        self._take_style = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def user_mobile(self):
        return self._user_mobile

    @user_mobile.setter
    def user_mobile(self, value):
        self._user_mobile = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringOrderInfoQueryResponse, self).parse_response_content(response_content)
        if 'bill_amount' in response:
            self.bill_amount = response['bill_amount']
        if 'biz_product' in response:
            self.biz_product = response['biz_product']
        if 'business_type' in response:
            self.business_type = response['business_type']
        if 'channel' in response:
            self.channel = response['channel']
        if 'dinner_type' in response:
            self.dinner_type = response['dinner_type']
        if 'dish_details' in response:
            self.dish_details = response['dish_details']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'external_shop_id' in response:
            self.external_shop_id = response['external_shop_id']
        if 'member_flag' in response:
            self.member_flag = response['member_flag']
        if 'memo' in response:
            self.memo = response['memo']
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_style' in response:
            self.order_style = response['order_style']
        if 'order_time' in response:
            self.order_time = response['order_time']
        if 'other_amount' in response:
            self.other_amount = response['other_amount']
        if 'packing_amount' in response:
            self.packing_amount = response['packing_amount']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pay_channels' in response:
            self.pay_channels = response['pay_channels']
        if 'people_num' in response:
            self.people_num = response['people_num']
        if 'receipt_amount' in response:
            self.receipt_amount = response['receipt_amount']
        if 'service_amount' in response:
            self.service_amount = response['service_amount']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'table_time' in response:
            self.table_time = response['table_time']
        if 'take_no' in response:
            self.take_no = response['take_no']
        if 'take_style' in response:
            self.take_style = response['take_style']
        if 'trade_amount' in response:
            self.trade_amount = response['trade_amount']
        if 'user_mobile' in response:
            self.user_mobile = response['user_mobile']
