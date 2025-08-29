#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentOrderReceiverAddressInfoDTO import RentOrderReceiverAddressInfoDTO
from alipay.aop.api.domain.RentOrderReceiverAddressInfoDTO import RentOrderReceiverAddressInfoDTO
from alipay.aop.api.domain.RentOrderDeliveryInfoDTO import RentOrderDeliveryInfoDTO
from alipay.aop.api.domain.OrderModifyRentPlanInfo import OrderModifyRentPlanInfo


class AlipayCommerceRentOrderModifyModel(object):

    def __init__(self):
        self._address_info = None
        self._default_receiving_address = None
        self._delivery_info = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._rent_plan_info = None
        self._type = None
        self._user_id = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, RentOrderReceiverAddressInfoDTO):
            self._address_info = value
        else:
            self._address_info = RentOrderReceiverAddressInfoDTO.from_alipay_dict(value)
    @property
    def default_receiving_address(self):
        return self._default_receiving_address

    @default_receiving_address.setter
    def default_receiving_address(self, value):
        if isinstance(value, RentOrderReceiverAddressInfoDTO):
            self._default_receiving_address = value
        else:
            self._default_receiving_address = RentOrderReceiverAddressInfoDTO.from_alipay_dict(value)
    @property
    def delivery_info(self):
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, value):
        if isinstance(value, RentOrderDeliveryInfoDTO):
            self._delivery_info = value
        else:
            self._delivery_info = RentOrderDeliveryInfoDTO.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def rent_plan_info(self):
        return self._rent_plan_info

    @rent_plan_info.setter
    def rent_plan_info(self, value):
        if isinstance(value, OrderModifyRentPlanInfo):
            self._rent_plan_info = value
        else:
            self._rent_plan_info = OrderModifyRentPlanInfo.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.default_receiving_address:
            if hasattr(self.default_receiving_address, 'to_alipay_dict'):
                params['default_receiving_address'] = self.default_receiving_address.to_alipay_dict()
            else:
                params['default_receiving_address'] = self.default_receiving_address
        if self.delivery_info:
            if hasattr(self.delivery_info, 'to_alipay_dict'):
                params['delivery_info'] = self.delivery_info.to_alipay_dict()
            else:
                params['delivery_info'] = self.delivery_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.rent_plan_info:
            if hasattr(self.rent_plan_info, 'to_alipay_dict'):
                params['rent_plan_info'] = self.rent_plan_info.to_alipay_dict()
            else:
                params['rent_plan_info'] = self.rent_plan_info
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AlipayCommerceRentOrderModifyModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'default_receiving_address' in d:
            o.default_receiving_address = d['default_receiving_address']
        if 'delivery_info' in d:
            o.delivery_info = d['delivery_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'rent_plan_info' in d:
            o.rent_plan_info = d['rent_plan_info']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


