#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentReceiverAddressInfoDTO import RentReceiverAddressInfoDTO
from alipay.aop.api.domain.BuyerInfoDTO import BuyerInfoDTO
from alipay.aop.api.domain.RentItemInfoDTO import RentItemInfoDTO
from alipay.aop.api.domain.RentPriceInfoDTO import RentPriceInfoDTO


class AlipayCommerceRentLoanConsultModel(object):

    def __init__(self):
        self._address_info = None
        self._buyer_id = None
        self._buyer_info = None
        self._buyer_open_id = None
        self._consult_invest_pid_list = None
        self._item_infos = None
        self._order_id = None
        self._out_order_id = None
        self._price_info = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, RentReceiverAddressInfoDTO):
            self._address_info = value
        else:
            self._address_info = RentReceiverAddressInfoDTO.from_alipay_dict(value)
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
        if isinstance(value, BuyerInfoDTO):
            self._buyer_info = value
        else:
            self._buyer_info = BuyerInfoDTO.from_alipay_dict(value)
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def consult_invest_pid_list(self):
        return self._consult_invest_pid_list

    @consult_invest_pid_list.setter
    def consult_invest_pid_list(self, value):
        if isinstance(value, list):
            self._consult_invest_pid_list = list()
            for i in value:
                self._consult_invest_pid_list.append(i)
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, RentItemInfoDTO):
            self._item_infos = value
        else:
            self._item_infos = RentItemInfoDTO.from_alipay_dict(value)
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
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, RentPriceInfoDTO):
            self._price_info = value
        else:
            self._price_info = RentPriceInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.address_info:
            if hasattr(self.address_info, 'to_alipay_dict'):
                params['address_info'] = self.address_info.to_alipay_dict()
            else:
                params['address_info'] = self.address_info
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
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.consult_invest_pid_list:
            if isinstance(self.consult_invest_pid_list, list):
                for i in range(0, len(self.consult_invest_pid_list)):
                    element = self.consult_invest_pid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.consult_invest_pid_list[i] = element.to_alipay_dict()
            if hasattr(self.consult_invest_pid_list, 'to_alipay_dict'):
                params['consult_invest_pid_list'] = self.consult_invest_pid_list.to_alipay_dict()
            else:
                params['consult_invest_pid_list'] = self.consult_invest_pid_list
        if self.item_infos:
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
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
        if self.price_info:
            if hasattr(self.price_info, 'to_alipay_dict'):
                params['price_info'] = self.price_info.to_alipay_dict()
            else:
                params['price_info'] = self.price_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentLoanConsultModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'consult_invest_pid_list' in d:
            o.consult_invest_pid_list = d['consult_invest_pid_list']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'price_info' in d:
            o.price_info = d['price_info']
        return o


