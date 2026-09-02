#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentProcurementAddressInfoVO import RentProcurementAddressInfoVO


class AlipayCommerceRentProcurementOrderModifyModel(object):

    def __init__(self):
        self._address_info = None
        self._out_procurement_order_id = None
        self._procurement_order_id = None
        self._type = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, RentProcurementAddressInfoVO):
            self._address_info = value
        else:
            self._address_info = RentProcurementAddressInfoVO.from_alipay_dict(value)
    @property
    def out_procurement_order_id(self):
        return self._out_procurement_order_id

    @out_procurement_order_id.setter
    def out_procurement_order_id(self, value):
        self._out_procurement_order_id = value
    @property
    def procurement_order_id(self):
        return self._procurement_order_id

    @procurement_order_id.setter
    def procurement_order_id(self, value):
        self._procurement_order_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
        if self.out_procurement_order_id:
            if hasattr(self.out_procurement_order_id, 'to_alipay_dict'):
                params['out_procurement_order_id'] = self.out_procurement_order_id.to_alipay_dict()
            else:
                params['out_procurement_order_id'] = self.out_procurement_order_id
        if self.procurement_order_id:
            if hasattr(self.procurement_order_id, 'to_alipay_dict'):
                params['procurement_order_id'] = self.procurement_order_id.to_alipay_dict()
            else:
                params['procurement_order_id'] = self.procurement_order_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentProcurementOrderModifyModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'out_procurement_order_id' in d:
            o.out_procurement_order_id = d['out_procurement_order_id']
        if 'procurement_order_id' in d:
            o.procurement_order_id = d['procurement_order_id']
        if 'type' in d:
            o.type = d['type']
        return o


