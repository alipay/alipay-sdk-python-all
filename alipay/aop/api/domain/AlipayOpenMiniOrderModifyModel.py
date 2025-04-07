#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniReceiverAddressInfoDTO import MiniReceiverAddressInfoDTO
from alipay.aop.api.domain.AllocAmountInfoDTO import AllocAmountInfoDTO
from alipay.aop.api.domain.MiniDeliveryInfoUpdateDTO import MiniDeliveryInfoUpdateDTO
from alipay.aop.api.domain.GoodsInfoModifyDTO import GoodsInfoModifyDTO
from alipay.aop.api.domain.PriceInfoModifyDTO import PriceInfoModifyDTO
from alipay.aop.api.domain.MiniOrderAddressInfoDTO import MiniOrderAddressInfoDTO
from alipay.aop.api.domain.StagePayPlanDTO import StagePayPlanDTO
from alipay.aop.api.domain.SubMerchantModifyDTO import SubMerchantModifyDTO


class AlipayOpenMiniOrderModifyModel(object):

    def __init__(self):
        self._address_info = None
        self._alloc_amount_info = None
        self._delivery_detail = None
        self._item_infos = None
        self._open_id = None
        self._order_id = None
        self._out_order_id = None
        self._price_info = None
        self._send_address_info = None
        self._stage_pay_plans = None
        self._sub_merchant = None
        self._user_id = None

    @property
    def address_info(self):
        return self._address_info

    @address_info.setter
    def address_info(self, value):
        if isinstance(value, MiniReceiverAddressInfoDTO):
            self._address_info = value
        else:
            self._address_info = MiniReceiverAddressInfoDTO.from_alipay_dict(value)
    @property
    def alloc_amount_info(self):
        return self._alloc_amount_info

    @alloc_amount_info.setter
    def alloc_amount_info(self, value):
        if isinstance(value, AllocAmountInfoDTO):
            self._alloc_amount_info = value
        else:
            self._alloc_amount_info = AllocAmountInfoDTO.from_alipay_dict(value)
    @property
    def delivery_detail(self):
        return self._delivery_detail

    @delivery_detail.setter
    def delivery_detail(self, value):
        if isinstance(value, MiniDeliveryInfoUpdateDTO):
            self._delivery_detail = value
        else:
            self._delivery_detail = MiniDeliveryInfoUpdateDTO.from_alipay_dict(value)
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, GoodsInfoModifyDTO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(GoodsInfoModifyDTO.from_alipay_dict(i))
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
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, PriceInfoModifyDTO):
            self._price_info = value
        else:
            self._price_info = PriceInfoModifyDTO.from_alipay_dict(value)
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
    def stage_pay_plans(self):
        return self._stage_pay_plans

    @stage_pay_plans.setter
    def stage_pay_plans(self, value):
        if isinstance(value, list):
            self._stage_pay_plans = list()
            for i in value:
                if isinstance(i, StagePayPlanDTO):
                    self._stage_pay_plans.append(i)
                else:
                    self._stage_pay_plans.append(StagePayPlanDTO.from_alipay_dict(i))
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, SubMerchantModifyDTO):
            self._sub_merchant = value
        else:
            self._sub_merchant = SubMerchantModifyDTO.from_alipay_dict(value)
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
        if self.alloc_amount_info:
            if hasattr(self.alloc_amount_info, 'to_alipay_dict'):
                params['alloc_amount_info'] = self.alloc_amount_info.to_alipay_dict()
            else:
                params['alloc_amount_info'] = self.alloc_amount_info
        if self.delivery_detail:
            if hasattr(self.delivery_detail, 'to_alipay_dict'):
                params['delivery_detail'] = self.delivery_detail.to_alipay_dict()
            else:
                params['delivery_detail'] = self.delivery_detail
        if self.item_infos:
            if isinstance(self.item_infos, list):
                for i in range(0, len(self.item_infos)):
                    element = self.item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
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
        if self.price_info:
            if hasattr(self.price_info, 'to_alipay_dict'):
                params['price_info'] = self.price_info.to_alipay_dict()
            else:
                params['price_info'] = self.price_info
        if self.send_address_info:
            if hasattr(self.send_address_info, 'to_alipay_dict'):
                params['send_address_info'] = self.send_address_info.to_alipay_dict()
            else:
                params['send_address_info'] = self.send_address_info
        if self.stage_pay_plans:
            if isinstance(self.stage_pay_plans, list):
                for i in range(0, len(self.stage_pay_plans)):
                    element = self.stage_pay_plans[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stage_pay_plans[i] = element.to_alipay_dict()
            if hasattr(self.stage_pay_plans, 'to_alipay_dict'):
                params['stage_pay_plans'] = self.stage_pay_plans.to_alipay_dict()
            else:
                params['stage_pay_plans'] = self.stage_pay_plans
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
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
        o = AlipayOpenMiniOrderModifyModel()
        if 'address_info' in d:
            o.address_info = d['address_info']
        if 'alloc_amount_info' in d:
            o.alloc_amount_info = d['alloc_amount_info']
        if 'delivery_detail' in d:
            o.delivery_detail = d['delivery_detail']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'price_info' in d:
            o.price_info = d['price_info']
        if 'send_address_info' in d:
            o.send_address_info = d['send_address_info']
        if 'stage_pay_plans' in d:
            o.stage_pay_plans = d['stage_pay_plans']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


