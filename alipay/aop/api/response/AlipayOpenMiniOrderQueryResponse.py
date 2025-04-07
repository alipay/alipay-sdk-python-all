#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AcceptInfoVO import AcceptInfoVO
from alipay.aop.api.domain.AddressInfoVO import AddressInfoVO
from alipay.aop.api.domain.BookingInfoDTO import BookingInfoDTO
from alipay.aop.api.domain.ContactInfoVO import ContactInfoVO
from alipay.aop.api.domain.AddressInfoVO import AddressInfoVO
from alipay.aop.api.domain.DeliveryDetailInfoVO import DeliveryDetailInfoVO
from alipay.aop.api.domain.LandingChannelInfoVO import LandingChannelInfoVO
from alipay.aop.api.domain.OrderDetailInfoVO import OrderDetailInfoVO
from alipay.aop.api.domain.RefundInfoVO import RefundInfoVO
from alipay.aop.api.domain.RentInfoVO import RentInfoVO
from alipay.aop.api.domain.MiniOrderAddressInfoDTO import MiniOrderAddressInfoDTO
from alipay.aop.api.domain.ShopInfoDTO import ShopInfoDTO
from alipay.aop.api.domain.StagePayPlanVO import StagePayPlanVO


class AlipayOpenMiniOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderQueryResponse, self).__init__()
        self._accept_info = None
        self._address_info = None
        self._booking_info = None
        self._contact_info = None
        self._create_time = None
        self._default_receiving_address = None
        self._delivery_detail = None
        self._landing_channel_info = None
        self._merchant_biz_type = None
        self._open_id = None
        self._order_detail = None
        self._order_id = None
        self._out_order_id = None
        self._path = None
        self._receive_time = None
        self._refund_info = None
        self._rent_info = None
        self._send_address_info = None
        self._settle_type = None
        self._shop_info = None
        self._stage_pay_plans = None
        self._status = None
        self._trade_no = None
        self._user_id = None

    @property
    def accept_info(self):
        return self._accept_info

    @accept_info.setter
    def accept_info(self, value):
        if isinstance(value, AcceptInfoVO):
            self._accept_info = value
        else:
            self._accept_info = AcceptInfoVO.from_alipay_dict(value)
    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, AddressInfoVO):
            self._address_info = value
        else:
            self._address_info = AddressInfoVO.from_alipay_dict(value)
    @property
    def booking_info(self):
        return self._booking_info

    @booking_info.setter
    def booking_info(self, value):
        if isinstance(value, BookingInfoDTO):
            self._booking_info = value
        else:
            self._booking_info = BookingInfoDTO.from_alipay_dict(value)
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, ContactInfoVO):
            self._contact_info = value
        else:
            self._contact_info = ContactInfoVO.from_alipay_dict(value)
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def default_receiving_address(self):
        return self._default_receiving_address

    @default_receiving_address.setter
    def default_receiving_address(self, value):
        if isinstance(value, AddressInfoVO):
            self._default_receiving_address = value
        else:
            self._default_receiving_address = AddressInfoVO.from_alipay_dict(value)
    @property
    def delivery_detail(self):
        return self._delivery_detail

    @delivery_detail.setter
    def delivery_detail(self, value):
        if isinstance(value, DeliveryDetailInfoVO):
            self._delivery_detail = value
        else:
            self._delivery_detail = DeliveryDetailInfoVO.from_alipay_dict(value)
    @property
    def landing_channel_info(self):
        return self._landing_channel_info

    @landing_channel_info.setter
    def landing_channel_info(self, value):
        if isinstance(value, LandingChannelInfoVO):
            self._landing_channel_info = value
        else:
            self._landing_channel_info = LandingChannelInfoVO.from_alipay_dict(value)
    @property
    def merchant_biz_type(self):
        return self._merchant_biz_type

    @merchant_biz_type.setter
    def merchant_biz_type(self, value):
        self._merchant_biz_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_detail(self):
        return self._order_detail

    @order_detail.setter
    def order_detail(self, value):
        if isinstance(value, OrderDetailInfoVO):
            self._order_detail = value
        else:
            self._order_detail = OrderDetailInfoVO.from_alipay_dict(value)
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def receive_time(self):
        return self._receive_time

    @receive_time.setter
    def receive_time(self, value):
        self._receive_time = value
    @property
    def refund_info(self):
        return self._refund_info

    @refund_info.setter
    def refund_info(self, value):
        if isinstance(value, RefundInfoVO):
            self._refund_info = value
        else:
            self._refund_info = RefundInfoVO.from_alipay_dict(value)
    @property
    def rent_info(self):
        return self._rent_info

    @rent_info.setter
    def rent_info(self, value):
        if isinstance(value, RentInfoVO):
            self._rent_info = value
        else:
            self._rent_info = RentInfoVO.from_alipay_dict(value)
    @property
    def send_address_info(self):
        return self._send_address_info

    @send_address_info.setter
    def send_address_info(self, value):
        if isinstance(value, MiniOrderAddressInfoDTO):
            self._send_address_info = value
        else:
            self._send_address_info = MiniOrderAddressInfoDTO.from_alipay_dict(value)
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, ShopInfoDTO):
            self._shop_info = value
        else:
            self._shop_info = ShopInfoDTO.from_alipay_dict(value)
    @property
    def stage_pay_plans(self):
        return self._stage_pay_plans

    @stage_pay_plans.setter
    def stage_pay_plans(self, value):
        if isinstance(value, list):
            self._stage_pay_plans = list()
            for i in value:
                if isinstance(i, StagePayPlanVO):
                    self._stage_pay_plans.append(i)
                else:
                    self._stage_pay_plans.append(StagePayPlanVO.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderQueryResponse, self).parse_response_content(response_content)
        if 'accept_info' in response:
            self.accept_info = response['accept_info']
        if 'address_info' in response:
            self.address_info = response['address_info']
        if 'booking_info' in response:
            self.booking_info = response['booking_info']
        if 'contact_info' in response:
            self.contact_info = response['contact_info']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'default_receiving_address' in response:
            self.default_receiving_address = response['default_receiving_address']
        if 'delivery_detail' in response:
            self.delivery_detail = response['delivery_detail']
        if 'landing_channel_info' in response:
            self.landing_channel_info = response['landing_channel_info']
        if 'merchant_biz_type' in response:
            self.merchant_biz_type = response['merchant_biz_type']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_detail' in response:
            self.order_detail = response['order_detail']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'path' in response:
            self.path = response['path']
        if 'receive_time' in response:
            self.receive_time = response['receive_time']
        if 'refund_info' in response:
            self.refund_info = response['refund_info']
        if 'rent_info' in response:
            self.rent_info = response['rent_info']
        if 'send_address_info' in response:
            self.send_address_info = response['send_address_info']
        if 'settle_type' in response:
            self.settle_type = response['settle_type']
        if 'shop_info' in response:
            self.shop_info = response['shop_info']
        if 'stage_pay_plans' in response:
            self.stage_pay_plans = response['stage_pay_plans']
        if 'status' in response:
            self.status = response['status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
