#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AxfCardBindInfo import AxfCardBindInfo
from alipay.aop.api.domain.DamagesConsultInfo import DamagesConsultInfo
from alipay.aop.api.domain.DamagesInfo import DamagesInfo
from alipay.aop.api.domain.DeductionPlanInfo import DeductionPlanInfo


class CardOrderInfo(object):

    def __init__(self):
        self._available_amount = None
        self._axf_card_bind_info = None
        self._cancel_type = None
        self._cancelled_cash = None
        self._card_id = None
        self._card_status = None
        self._card_template_id = None
        self._card_type = None
        self._create_date = None
        self._damages_consult = None
        self._damages_info = None
        self._deduction_plan_list = None
        self._discount_cash = None
        self._discount_plan_cash = None
        self._discount_refund_cash = None
        self._funding_model = None
        self._gmt_active = None
        self._gmt_expired = None
        self._merchant_pid = None
        self._name = None
        self._open_id = None
        self._order_id = None
        self._origin_price_total = None
        self._out_order_no = None
        self._refund_cash = None
        self._remain_count = None
        self._sale_price_total = None
        self._shop_id = None
        self._total_count = None
        self._trade_no = None
        self._usable_cash = None
        self._used_cash = None
        self._user_id = None
        self._user_name = None
        self._user_phone = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def axf_card_bind_info(self):
        return self._axf_card_bind_info

    @axf_card_bind_info.setter
    def axf_card_bind_info(self, value):
        if isinstance(value, AxfCardBindInfo):
            self._axf_card_bind_info = value
        else:
            self._axf_card_bind_info = AxfCardBindInfo.from_alipay_dict(value)
    @property
    def cancel_type(self):
        return self._cancel_type

    @cancel_type.setter
    def cancel_type(self, value):
        self._cancel_type = value
    @property
    def cancelled_cash(self):
        return self._cancelled_cash

    @cancelled_cash.setter
    def cancelled_cash(self, value):
        self._cancelled_cash = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def damages_consult(self):
        return self._damages_consult

    @damages_consult.setter
    def damages_consult(self, value):
        if isinstance(value, DamagesConsultInfo):
            self._damages_consult = value
        else:
            self._damages_consult = DamagesConsultInfo.from_alipay_dict(value)
    @property
    def damages_info(self):
        return self._damages_info

    @damages_info.setter
    def damages_info(self, value):
        if isinstance(value, DamagesInfo):
            self._damages_info = value
        else:
            self._damages_info = DamagesInfo.from_alipay_dict(value)
    @property
    def deduction_plan_list(self):
        return self._deduction_plan_list

    @deduction_plan_list.setter
    def deduction_plan_list(self, value):
        if isinstance(value, list):
            self._deduction_plan_list = list()
            for i in value:
                if isinstance(i, DeductionPlanInfo):
                    self._deduction_plan_list.append(i)
                else:
                    self._deduction_plan_list.append(DeductionPlanInfo.from_alipay_dict(i))
    @property
    def discount_cash(self):
        return self._discount_cash

    @discount_cash.setter
    def discount_cash(self, value):
        self._discount_cash = value
    @property
    def discount_plan_cash(self):
        return self._discount_plan_cash

    @discount_plan_cash.setter
    def discount_plan_cash(self, value):
        self._discount_plan_cash = value
    @property
    def discount_refund_cash(self):
        return self._discount_refund_cash

    @discount_refund_cash.setter
    def discount_refund_cash(self, value):
        self._discount_refund_cash = value
    @property
    def funding_model(self):
        return self._funding_model

    @funding_model.setter
    def funding_model(self, value):
        self._funding_model = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
    def origin_price_total(self):
        return self._origin_price_total

    @origin_price_total.setter
    def origin_price_total(self, value):
        self._origin_price_total = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def refund_cash(self):
        return self._refund_cash

    @refund_cash.setter
    def refund_cash(self, value):
        self._refund_cash = value
    @property
    def remain_count(self):
        return self._remain_count

    @remain_count.setter
    def remain_count(self, value):
        self._remain_count = value
    @property
    def sale_price_total(self):
        return self._sale_price_total

    @sale_price_total.setter
    def sale_price_total(self, value):
        self._sale_price_total = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def usable_cash(self):
        return self._usable_cash

    @usable_cash.setter
    def usable_cash(self, value):
        self._usable_cash = value
    @property
    def used_cash(self):
        return self._used_cash

    @used_cash.setter
    def used_cash(self, value):
        self._used_cash = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.axf_card_bind_info:
            if hasattr(self.axf_card_bind_info, 'to_alipay_dict'):
                params['axf_card_bind_info'] = self.axf_card_bind_info.to_alipay_dict()
            else:
                params['axf_card_bind_info'] = self.axf_card_bind_info
        if self.cancel_type:
            if hasattr(self.cancel_type, 'to_alipay_dict'):
                params['cancel_type'] = self.cancel_type.to_alipay_dict()
            else:
                params['cancel_type'] = self.cancel_type
        if self.cancelled_cash:
            if hasattr(self.cancelled_cash, 'to_alipay_dict'):
                params['cancelled_cash'] = self.cancelled_cash.to_alipay_dict()
            else:
                params['cancelled_cash'] = self.cancelled_cash
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.card_status:
            if hasattr(self.card_status, 'to_alipay_dict'):
                params['card_status'] = self.card_status.to_alipay_dict()
            else:
                params['card_status'] = self.card_status
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.damages_consult:
            if hasattr(self.damages_consult, 'to_alipay_dict'):
                params['damages_consult'] = self.damages_consult.to_alipay_dict()
            else:
                params['damages_consult'] = self.damages_consult
        if self.damages_info:
            if hasattr(self.damages_info, 'to_alipay_dict'):
                params['damages_info'] = self.damages_info.to_alipay_dict()
            else:
                params['damages_info'] = self.damages_info
        if self.deduction_plan_list:
            if isinstance(self.deduction_plan_list, list):
                for i in range(0, len(self.deduction_plan_list)):
                    element = self.deduction_plan_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.deduction_plan_list[i] = element.to_alipay_dict()
            if hasattr(self.deduction_plan_list, 'to_alipay_dict'):
                params['deduction_plan_list'] = self.deduction_plan_list.to_alipay_dict()
            else:
                params['deduction_plan_list'] = self.deduction_plan_list
        if self.discount_cash:
            if hasattr(self.discount_cash, 'to_alipay_dict'):
                params['discount_cash'] = self.discount_cash.to_alipay_dict()
            else:
                params['discount_cash'] = self.discount_cash
        if self.discount_plan_cash:
            if hasattr(self.discount_plan_cash, 'to_alipay_dict'):
                params['discount_plan_cash'] = self.discount_plan_cash.to_alipay_dict()
            else:
                params['discount_plan_cash'] = self.discount_plan_cash
        if self.discount_refund_cash:
            if hasattr(self.discount_refund_cash, 'to_alipay_dict'):
                params['discount_refund_cash'] = self.discount_refund_cash.to_alipay_dict()
            else:
                params['discount_refund_cash'] = self.discount_refund_cash
        if self.funding_model:
            if hasattr(self.funding_model, 'to_alipay_dict'):
                params['funding_model'] = self.funding_model.to_alipay_dict()
            else:
                params['funding_model'] = self.funding_model
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        if self.origin_price_total:
            if hasattr(self.origin_price_total, 'to_alipay_dict'):
                params['origin_price_total'] = self.origin_price_total.to_alipay_dict()
            else:
                params['origin_price_total'] = self.origin_price_total
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.refund_cash:
            if hasattr(self.refund_cash, 'to_alipay_dict'):
                params['refund_cash'] = self.refund_cash.to_alipay_dict()
            else:
                params['refund_cash'] = self.refund_cash
        if self.remain_count:
            if hasattr(self.remain_count, 'to_alipay_dict'):
                params['remain_count'] = self.remain_count.to_alipay_dict()
            else:
                params['remain_count'] = self.remain_count
        if self.sale_price_total:
            if hasattr(self.sale_price_total, 'to_alipay_dict'):
                params['sale_price_total'] = self.sale_price_total.to_alipay_dict()
            else:
                params['sale_price_total'] = self.sale_price_total
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.usable_cash:
            if hasattr(self.usable_cash, 'to_alipay_dict'):
                params['usable_cash'] = self.usable_cash.to_alipay_dict()
            else:
                params['usable_cash'] = self.usable_cash
        if self.used_cash:
            if hasattr(self.used_cash, 'to_alipay_dict'):
                params['used_cash'] = self.used_cash.to_alipay_dict()
            else:
                params['used_cash'] = self.used_cash
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardOrderInfo()
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'axf_card_bind_info' in d:
            o.axf_card_bind_info = d['axf_card_bind_info']
        if 'cancel_type' in d:
            o.cancel_type = d['cancel_type']
        if 'cancelled_cash' in d:
            o.cancelled_cash = d['cancelled_cash']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'card_status' in d:
            o.card_status = d['card_status']
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'damages_consult' in d:
            o.damages_consult = d['damages_consult']
        if 'damages_info' in d:
            o.damages_info = d['damages_info']
        if 'deduction_plan_list' in d:
            o.deduction_plan_list = d['deduction_plan_list']
        if 'discount_cash' in d:
            o.discount_cash = d['discount_cash']
        if 'discount_plan_cash' in d:
            o.discount_plan_cash = d['discount_plan_cash']
        if 'discount_refund_cash' in d:
            o.discount_refund_cash = d['discount_refund_cash']
        if 'funding_model' in d:
            o.funding_model = d['funding_model']
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'name' in d:
            o.name = d['name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'origin_price_total' in d:
            o.origin_price_total = d['origin_price_total']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'refund_cash' in d:
            o.refund_cash = d['refund_cash']
        if 'remain_count' in d:
            o.remain_count = d['remain_count']
        if 'sale_price_total' in d:
            o.sale_price_total = d['sale_price_total']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'usable_cash' in d:
            o.usable_cash = d['usable_cash']
        if 'used_cash' in d:
            o.used_cash = d['used_cash']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        return o


