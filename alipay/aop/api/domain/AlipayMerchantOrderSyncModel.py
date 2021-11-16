#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserInfomation import UserInfomation
from alipay.aop.api.domain.DiscountInfoData import DiscountInfoData
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo
from alipay.aop.api.domain.ItemOrderInfo import ItemOrderInfo
from alipay.aop.api.domain.OrderJourneyInfo import OrderJourneyInfo
from alipay.aop.api.domain.OrderLogisticsInformationRequest import OrderLogisticsInformationRequest
from alipay.aop.api.domain.OrderShopInfo import OrderShopInfo
from alipay.aop.api.domain.TicketInfo import TicketInfo
from alipay.aop.api.domain.TicketOrderInfo import TicketOrderInfo


class AlipayMerchantOrderSyncModel(object):

    def __init__(self):
        self._amount = None
        self._buyer_id = None
        self._buyer_info = None
        self._discount_amount = None
        self._discount_info_list = None
        self._ext_info = None
        self._item_order_list = None
        self._journey_order_list = None
        self._logistics_info_list = None
        self._order_auth_code = None
        self._order_create_time = None
        self._order_modified_time = None
        self._order_pay_time = None
        self._order_type = None
        self._out_biz_no = None
        self._partner_id = None
        self._pay_amount = None
        self._pay_timeout_express = None
        self._record_id = None
        self._seller_id = None
        self._send_msg = None
        self._service_code = None
        self._shop_info = None
        self._source_app = None
        self._sync_content = None
        self._ticket_info = None
        self._ticket_order_list = None
        self._trade_no = None
        self._trade_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, UserInfomation):
            self._buyer_info = value
        else:
            self._buyer_info = UserInfomation.from_alipay_dict(value)
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
                if isinstance(i, DiscountInfoData):
                    self._discount_info_list.append(i)
                else:
                    self._discount_info_list.append(DiscountInfoData.from_alipay_dict(i))
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
    def item_order_list(self):
        return self._item_order_list

    @item_order_list.setter
    def item_order_list(self, value):
        if isinstance(value, list):
            self._item_order_list = list()
            for i in value:
                if isinstance(i, ItemOrderInfo):
                    self._item_order_list.append(i)
                else:
                    self._item_order_list.append(ItemOrderInfo.from_alipay_dict(i))
    @property
    def journey_order_list(self):
        return self._journey_order_list

    @journey_order_list.setter
    def journey_order_list(self, value):
        if isinstance(value, list):
            self._journey_order_list = list()
            for i in value:
                if isinstance(i, OrderJourneyInfo):
                    self._journey_order_list.append(i)
                else:
                    self._journey_order_list.append(OrderJourneyInfo.from_alipay_dict(i))
    @property
    def logistics_info_list(self):
        return self._logistics_info_list

    @logistics_info_list.setter
    def logistics_info_list(self, value):
        if isinstance(value, list):
            self._logistics_info_list = list()
            for i in value:
                if isinstance(i, OrderLogisticsInformationRequest):
                    self._logistics_info_list.append(i)
                else:
                    self._logistics_info_list.append(OrderLogisticsInformationRequest.from_alipay_dict(i))
    @property
    def order_auth_code(self):
        return self._order_auth_code

    @order_auth_code.setter
    def order_auth_code(self, value):
        self._order_auth_code = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
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
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_timeout_express(self):
        return self._pay_timeout_express

    @pay_timeout_express.setter
    def pay_timeout_express(self, value):
        self._pay_timeout_express = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def send_msg(self):
        return self._send_msg

    @send_msg.setter
    def send_msg(self, value):
        self._send_msg = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, OrderShopInfo):
            self._shop_info = value
        else:
            self._shop_info = OrderShopInfo.from_alipay_dict(value)
    @property
    def source_app(self):
        return self._source_app

    @source_app.setter
    def source_app(self, value):
        self._source_app = value
    @property
    def sync_content(self):
        return self._sync_content

    @sync_content.setter
    def sync_content(self, value):
        self._sync_content = value
    @property
    def ticket_info(self):
        return self._ticket_info

    @ticket_info.setter
    def ticket_info(self, value):
        if isinstance(value, TicketInfo):
            self._ticket_info = value
        else:
            self._ticket_info = TicketInfo.from_alipay_dict(value)
    @property
    def ticket_order_list(self):
        return self._ticket_order_list

    @ticket_order_list.setter
    def ticket_order_list(self, value):
        if isinstance(value, list):
            self._ticket_order_list = list()
            for i in value:
                if isinstance(i, TicketOrderInfo):
                    self._ticket_order_list.append(i)
                else:
                    self._ticket_order_list.append(TicketOrderInfo.from_alipay_dict(i))
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
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
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
        if self.journey_order_list:
            if isinstance(self.journey_order_list, list):
                for i in range(0, len(self.journey_order_list)):
                    element = self.journey_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.journey_order_list[i] = element.to_alipay_dict()
            if hasattr(self.journey_order_list, 'to_alipay_dict'):
                params['journey_order_list'] = self.journey_order_list.to_alipay_dict()
            else:
                params['journey_order_list'] = self.journey_order_list
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
        if self.order_auth_code:
            if hasattr(self.order_auth_code, 'to_alipay_dict'):
                params['order_auth_code'] = self.order_auth_code.to_alipay_dict()
            else:
                params['order_auth_code'] = self.order_auth_code
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
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
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_timeout_express:
            if hasattr(self.pay_timeout_express, 'to_alipay_dict'):
                params['pay_timeout_express'] = self.pay_timeout_express.to_alipay_dict()
            else:
                params['pay_timeout_express'] = self.pay_timeout_express
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.send_msg:
            if hasattr(self.send_msg, 'to_alipay_dict'):
                params['send_msg'] = self.send_msg.to_alipay_dict()
            else:
                params['send_msg'] = self.send_msg
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
        if self.source_app:
            if hasattr(self.source_app, 'to_alipay_dict'):
                params['source_app'] = self.source_app.to_alipay_dict()
            else:
                params['source_app'] = self.source_app
        if self.sync_content:
            if hasattr(self.sync_content, 'to_alipay_dict'):
                params['sync_content'] = self.sync_content.to_alipay_dict()
            else:
                params['sync_content'] = self.sync_content
        if self.ticket_info:
            if hasattr(self.ticket_info, 'to_alipay_dict'):
                params['ticket_info'] = self.ticket_info.to_alipay_dict()
            else:
                params['ticket_info'] = self.ticket_info
        if self.ticket_order_list:
            if isinstance(self.ticket_order_list, list):
                for i in range(0, len(self.ticket_order_list)):
                    element = self.ticket_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ticket_order_list[i] = element.to_alipay_dict()
            if hasattr(self.ticket_order_list, 'to_alipay_dict'):
                params['ticket_order_list'] = self.ticket_order_list.to_alipay_dict()
            else:
                params['ticket_order_list'] = self.ticket_order_list
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
        o = AlipayMerchantOrderSyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_info_list' in d:
            o.discount_info_list = d['discount_info_list']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_order_list' in d:
            o.item_order_list = d['item_order_list']
        if 'journey_order_list' in d:
            o.journey_order_list = d['journey_order_list']
        if 'logistics_info_list' in d:
            o.logistics_info_list = d['logistics_info_list']
        if 'order_auth_code' in d:
            o.order_auth_code = d['order_auth_code']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_modified_time' in d:
            o.order_modified_time = d['order_modified_time']
        if 'order_pay_time' in d:
            o.order_pay_time = d['order_pay_time']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_timeout_express' in d:
            o.pay_timeout_express = d['pay_timeout_express']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'send_msg' in d:
            o.send_msg = d['send_msg']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        if 'source_app' in d:
            o.source_app = d['source_app']
        if 'sync_content' in d:
            o.sync_content = d['sync_content']
        if 'ticket_info' in d:
            o.ticket_info = d['ticket_info']
        if 'ticket_order_list' in d:
            o.ticket_order_list = d['ticket_order_list']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


