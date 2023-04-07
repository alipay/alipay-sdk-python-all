#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddressInfoVO import AddressInfoVO
from alipay.aop.api.domain.AddressInfoVO import AddressInfoVO
from alipay.aop.api.domain.DeliveryDetailInfoVO import DeliveryDetailInfoVO
from alipay.aop.api.domain.OrderDetailInfoVO import OrderDetailInfoVO
from alipay.aop.api.domain.RefundInfoVO import RefundInfoVO


class AlipayOpenMiniOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderQueryResponse, self).__init__()
        self._address_info = None
        self._create_time = None
        self._default_receiving_address = None
        self._delivery_detail = None
        self._fund_type = None
        self._openid = None
        self._order_detail = None
        self._out_order_id = None
        self._path = None
        self._receive_time = None
        self._refund_info = None
        self._scene = None
        self._status = None

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
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def openid(self):
        return self._openid

    @openid.setter
    def openid(self, value):
        self._openid = value
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
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderQueryResponse, self).parse_response_content(response_content)
        if 'address_info' in response:
            self.address_info = response['address_info']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'default_receiving_address' in response:
            self.default_receiving_address = response['default_receiving_address']
        if 'delivery_detail' in response:
            self.delivery_detail = response['delivery_detail']
        if 'fund_type' in response:
            self.fund_type = response['fund_type']
        if 'openid' in response:
            self.openid = response['openid']
        if 'order_detail' in response:
            self.order_detail = response['order_detail']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'path' in response:
            self.path = response['path']
        if 'receive_time' in response:
            self.receive_time = response['receive_time']
        if 'refund_info' in response:
            self.refund_info = response['refund_info']
        if 'scene' in response:
            self.scene = response['scene']
        if 'status' in response:
            self.status = response['status']
