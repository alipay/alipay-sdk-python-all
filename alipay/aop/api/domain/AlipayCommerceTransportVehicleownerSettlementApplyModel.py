#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BankRepayData import BankRepayData
from alipay.aop.api.domain.HighwaySceneData import HighwaySceneData
from alipay.aop.api.domain.VehicleSettleInfo import VehicleSettleInfo


class AlipayCommerceTransportVehicleownerSettlementApplyModel(object):

    def __init__(self):
        self._alipay_store_id = None
        self._bank_repay_data = None
        self._biz_agreement_no = None
        self._biz_scene_code = None
        self._business_params = None
        self._card_no = None
        self._device_no = None
        self._disable_pay_channels = None
        self._discountable_amount = None
        self._extend_params = None
        self._highway_data = None
        self._operator_id = None
        self._out_trade_no = None
        self._plate_color = None
        self._plate_no = None
        self._seller_id = None
        self._settle_info = None
        self._store_id = None
        self._subject = None
        self._terminal_id = None
        self._timeout_express = None
        self._total_amount = None
        self._undiscountable_amount = None

    @property
    def alipay_store_id(self):
        return self._alipay_store_id

    @alipay_store_id.setter
    def alipay_store_id(self, value):
        self._alipay_store_id = value
    @property
    def bank_repay_data(self):
        return self._bank_repay_data

    @bank_repay_data.setter
    def bank_repay_data(self, value):
        if isinstance(value, BankRepayData):
            self._bank_repay_data = value
        else:
            self._bank_repay_data = BankRepayData.from_alipay_dict(value)
    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def biz_scene_code(self):
        return self._biz_scene_code

    @biz_scene_code.setter
    def biz_scene_code(self, value):
        self._biz_scene_code = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        self._business_params = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def disable_pay_channels(self):
        return self._disable_pay_channels

    @disable_pay_channels.setter
    def disable_pay_channels(self, value):
        self._disable_pay_channels = value
    @property
    def discountable_amount(self):
        return self._discountable_amount

    @discountable_amount.setter
    def discountable_amount(self, value):
        self._discountable_amount = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def highway_data(self):
        return self._highway_data

    @highway_data.setter
    def highway_data(self, value):
        if isinstance(value, HighwaySceneData):
            self._highway_data = value
        else:
            self._highway_data = HighwaySceneData.from_alipay_dict(value)
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def settle_info(self):
        return self._settle_info

    @settle_info.setter
    def settle_info(self, value):
        if isinstance(value, VehicleSettleInfo):
            self._settle_info = value
        else:
            self._settle_info = VehicleSettleInfo.from_alipay_dict(value)
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def undiscountable_amount(self):
        return self._undiscountable_amount

    @undiscountable_amount.setter
    def undiscountable_amount(self, value):
        self._undiscountable_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_store_id:
            if hasattr(self.alipay_store_id, 'to_alipay_dict'):
                params['alipay_store_id'] = self.alipay_store_id.to_alipay_dict()
            else:
                params['alipay_store_id'] = self.alipay_store_id
        if self.bank_repay_data:
            if hasattr(self.bank_repay_data, 'to_alipay_dict'):
                params['bank_repay_data'] = self.bank_repay_data.to_alipay_dict()
            else:
                params['bank_repay_data'] = self.bank_repay_data
        if self.biz_agreement_no:
            if hasattr(self.biz_agreement_no, 'to_alipay_dict'):
                params['biz_agreement_no'] = self.biz_agreement_no.to_alipay_dict()
            else:
                params['biz_agreement_no'] = self.biz_agreement_no
        if self.biz_scene_code:
            if hasattr(self.biz_scene_code, 'to_alipay_dict'):
                params['biz_scene_code'] = self.biz_scene_code.to_alipay_dict()
            else:
                params['biz_scene_code'] = self.biz_scene_code
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.disable_pay_channels:
            if hasattr(self.disable_pay_channels, 'to_alipay_dict'):
                params['disable_pay_channels'] = self.disable_pay_channels.to_alipay_dict()
            else:
                params['disable_pay_channels'] = self.disable_pay_channels
        if self.discountable_amount:
            if hasattr(self.discountable_amount, 'to_alipay_dict'):
                params['discountable_amount'] = self.discountable_amount.to_alipay_dict()
            else:
                params['discountable_amount'] = self.discountable_amount
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.highway_data:
            if hasattr(self.highway_data, 'to_alipay_dict'):
                params['highway_data'] = self.highway_data.to_alipay_dict()
            else:
                params['highway_data'] = self.highway_data
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.settle_info:
            if hasattr(self.settle_info, 'to_alipay_dict'):
                params['settle_info'] = self.settle_info.to_alipay_dict()
            else:
                params['settle_info'] = self.settle_info
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.undiscountable_amount:
            if hasattr(self.undiscountable_amount, 'to_alipay_dict'):
                params['undiscountable_amount'] = self.undiscountable_amount.to_alipay_dict()
            else:
                params['undiscountable_amount'] = self.undiscountable_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportVehicleownerSettlementApplyModel()
        if 'alipay_store_id' in d:
            o.alipay_store_id = d['alipay_store_id']
        if 'bank_repay_data' in d:
            o.bank_repay_data = d['bank_repay_data']
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        if 'biz_scene_code' in d:
            o.biz_scene_code = d['biz_scene_code']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'disable_pay_channels' in d:
            o.disable_pay_channels = d['disable_pay_channels']
        if 'discountable_amount' in d:
            o.discountable_amount = d['discountable_amount']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'highway_data' in d:
            o.highway_data = d['highway_data']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'settle_info' in d:
            o.settle_info = d['settle_info']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'subject' in d:
            o.subject = d['subject']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'undiscountable_amount' in d:
            o.undiscountable_amount = d['undiscountable_amount']
        return o


