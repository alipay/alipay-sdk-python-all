#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ThirdPartyExtInfo import ThirdPartyExtInfo
from alipay.aop.api.domain.ItemThirdPartyInfo import ItemThirdPartyInfo
from alipay.aop.api.domain.OrderTimestampInfo import OrderTimestampInfo
from alipay.aop.api.domain.ReverseOrderInfo import ReverseOrderInfo
from alipay.aop.api.domain.ShopThirdPartyInfo import ShopThirdPartyInfo


class AlipayCommerceMedicalOrderSyncModel(object):

    def __init__(self):
        self._alipay_order_no = None
        self._buyer_id = None
        self._buyer_id_type = None
        self._channel_order_no = None
        self._channel_type = None
        self._delivery_fee = None
        self._ext_info = None
        self._item_list = None
        self._medical_insurance_amount = None
        self._order_scene = None
        self._order_status = None
        self._order_time_info = None
        self._packing_fee = None
        self._pay_amount = None
        self._reverse_order_list = None
        self._self_pay_amount = None
        self._shop_info = None
        self._total_amount = None
        self._trade_type = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_id_type(self):
        return self._buyer_id_type

    @buyer_id_type.setter
    def buyer_id_type(self, value):
        self._buyer_id_type = value
    @property
    def channel_order_no(self):
        return self._channel_order_no

    @channel_order_no.setter
    def channel_order_no(self, value):
        self._channel_order_no = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def delivery_fee(self):
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, value):
        self._delivery_fee = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ThirdPartyExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ThirdPartyExtInfo.from_alipay_dict(i))
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ItemThirdPartyInfo):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ItemThirdPartyInfo.from_alipay_dict(i))
    @property
    def medical_insurance_amount(self):
        return self._medical_insurance_amount

    @medical_insurance_amount.setter
    def medical_insurance_amount(self, value):
        self._medical_insurance_amount = value
    @property
    def order_scene(self):
        return self._order_scene

    @order_scene.setter
    def order_scene(self, value):
        self._order_scene = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_time_info(self):
        return self._order_time_info

    @order_time_info.setter
    def order_time_info(self, value):
        if isinstance(value, OrderTimestampInfo):
            self._order_time_info = value
        else:
            self._order_time_info = OrderTimestampInfo.from_alipay_dict(value)
    @property
    def packing_fee(self):
        return self._packing_fee

    @packing_fee.setter
    def packing_fee(self, value):
        self._packing_fee = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def reverse_order_list(self):
        return self._reverse_order_list

    @reverse_order_list.setter
    def reverse_order_list(self, value):
        if isinstance(value, list):
            self._reverse_order_list = list()
            for i in value:
                if isinstance(i, ReverseOrderInfo):
                    self._reverse_order_list.append(i)
                else:
                    self._reverse_order_list.append(ReverseOrderInfo.from_alipay_dict(i))
    @property
    def self_pay_amount(self):
        return self._self_pay_amount

    @self_pay_amount.setter
    def self_pay_amount(self, value):
        self._self_pay_amount = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, ShopThirdPartyInfo):
            self._shop_info = value
        else:
            self._shop_info = ShopThirdPartyInfo.from_alipay_dict(value)
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_id_type:
            if hasattr(self.buyer_id_type, 'to_alipay_dict'):
                params['buyer_id_type'] = self.buyer_id_type.to_alipay_dict()
            else:
                params['buyer_id_type'] = self.buyer_id_type
        if self.channel_order_no:
            if hasattr(self.channel_order_no, 'to_alipay_dict'):
                params['channel_order_no'] = self.channel_order_no.to_alipay_dict()
            else:
                params['channel_order_no'] = self.channel_order_no
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.delivery_fee:
            if hasattr(self.delivery_fee, 'to_alipay_dict'):
                params['delivery_fee'] = self.delivery_fee.to_alipay_dict()
            else:
                params['delivery_fee'] = self.delivery_fee
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
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        if self.medical_insurance_amount:
            if hasattr(self.medical_insurance_amount, 'to_alipay_dict'):
                params['medical_insurance_amount'] = self.medical_insurance_amount.to_alipay_dict()
            else:
                params['medical_insurance_amount'] = self.medical_insurance_amount
        if self.order_scene:
            if hasattr(self.order_scene, 'to_alipay_dict'):
                params['order_scene'] = self.order_scene.to_alipay_dict()
            else:
                params['order_scene'] = self.order_scene
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_time_info:
            if hasattr(self.order_time_info, 'to_alipay_dict'):
                params['order_time_info'] = self.order_time_info.to_alipay_dict()
            else:
                params['order_time_info'] = self.order_time_info
        if self.packing_fee:
            if hasattr(self.packing_fee, 'to_alipay_dict'):
                params['packing_fee'] = self.packing_fee.to_alipay_dict()
            else:
                params['packing_fee'] = self.packing_fee
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.reverse_order_list:
            if isinstance(self.reverse_order_list, list):
                for i in range(0, len(self.reverse_order_list)):
                    element = self.reverse_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.reverse_order_list[i] = element.to_alipay_dict()
            if hasattr(self.reverse_order_list, 'to_alipay_dict'):
                params['reverse_order_list'] = self.reverse_order_list.to_alipay_dict()
            else:
                params['reverse_order_list'] = self.reverse_order_list
        if self.self_pay_amount:
            if hasattr(self.self_pay_amount, 'to_alipay_dict'):
                params['self_pay_amount'] = self.self_pay_amount.to_alipay_dict()
            else:
                params['self_pay_amount'] = self.self_pay_amount
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
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
        o = AlipayCommerceMedicalOrderSyncModel()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_id_type' in d:
            o.buyer_id_type = d['buyer_id_type']
        if 'channel_order_no' in d:
            o.channel_order_no = d['channel_order_no']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'delivery_fee' in d:
            o.delivery_fee = d['delivery_fee']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'medical_insurance_amount' in d:
            o.medical_insurance_amount = d['medical_insurance_amount']
        if 'order_scene' in d:
            o.order_scene = d['order_scene']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_time_info' in d:
            o.order_time_info = d['order_time_info']
        if 'packing_fee' in d:
            o.packing_fee = d['packing_fee']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'reverse_order_list' in d:
            o.reverse_order_list = d['reverse_order_list']
        if 'self_pay_amount' in d:
            o.self_pay_amount = d['self_pay_amount']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


