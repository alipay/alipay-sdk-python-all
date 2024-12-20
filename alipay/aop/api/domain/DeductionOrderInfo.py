#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BillFeeInfo import BillFeeInfo
from alipay.aop.api.domain.DamagesInfo import DamagesInfo
from alipay.aop.api.domain.DeductionOrderOnceInfo import DeductionOrderOnceInfo


class DeductionOrderInfo(object):

    def __init__(self):
        self._bill_fee_info_list = None
        self._card_id = None
        self._certificate_id = None
        self._certificate_serial = None
        self._damages_info = None
        self._deduction_amount = None
        self._deduction_cash = None
        self._deduction_count = None
        self._deduction_fail_reason = None
        self._deduction_fail_times = None
        self._deduction_order_id = None
        self._deduction_order_once_info_list = None
        self._deduction_order_type = None
        self._deduction_status = None
        self._deduction_time = None
        self._gmt_create = None
        self._merchant_pid = None
        self._open_id = None
        self._order_id = None
        self._payment_no = None
        self._period = None
        self._plan_deduction_time = None
        self._platform_discount_price = None
        self._redeem_way = None
        self._refund_cash = None
        self._shop_id = None
        self._sub_order_id = None
        self._trade_no = None
        self._user_id = None
        self._user_refuse_reason = None

    @property
    def bill_fee_info_list(self):
        return self._bill_fee_info_list

    @bill_fee_info_list.setter
    def bill_fee_info_list(self, value):
        if isinstance(value, list):
            self._bill_fee_info_list = list()
            for i in value:
                if isinstance(i, BillFeeInfo):
                    self._bill_fee_info_list.append(i)
                else:
                    self._bill_fee_info_list.append(BillFeeInfo.from_alipay_dict(i))
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_serial(self):
        return self._certificate_serial

    @certificate_serial.setter
    def certificate_serial(self, value):
        self._certificate_serial = value
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
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def deduction_cash(self):
        return self._deduction_cash

    @deduction_cash.setter
    def deduction_cash(self, value):
        self._deduction_cash = value
    @property
    def deduction_count(self):
        return self._deduction_count

    @deduction_count.setter
    def deduction_count(self, value):
        self._deduction_count = value
    @property
    def deduction_fail_reason(self):
        return self._deduction_fail_reason

    @deduction_fail_reason.setter
    def deduction_fail_reason(self, value):
        self._deduction_fail_reason = value
    @property
    def deduction_fail_times(self):
        return self._deduction_fail_times

    @deduction_fail_times.setter
    def deduction_fail_times(self, value):
        self._deduction_fail_times = value
    @property
    def deduction_order_id(self):
        return self._deduction_order_id

    @deduction_order_id.setter
    def deduction_order_id(self, value):
        self._deduction_order_id = value
    @property
    def deduction_order_once_info_list(self):
        return self._deduction_order_once_info_list

    @deduction_order_once_info_list.setter
    def deduction_order_once_info_list(self, value):
        if isinstance(value, list):
            self._deduction_order_once_info_list = list()
            for i in value:
                if isinstance(i, DeductionOrderOnceInfo):
                    self._deduction_order_once_info_list.append(i)
                else:
                    self._deduction_order_once_info_list.append(DeductionOrderOnceInfo.from_alipay_dict(i))
    @property
    def deduction_order_type(self):
        return self._deduction_order_type

    @deduction_order_type.setter
    def deduction_order_type(self, value):
        self._deduction_order_type = value
    @property
    def deduction_status(self):
        return self._deduction_status

    @deduction_status.setter
    def deduction_status(self, value):
        self._deduction_status = value
    @property
    def deduction_time(self):
        return self._deduction_time

    @deduction_time.setter
    def deduction_time(self, value):
        self._deduction_time = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
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
    def payment_no(self):
        return self._payment_no

    @payment_no.setter
    def payment_no(self, value):
        self._payment_no = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def plan_deduction_time(self):
        return self._plan_deduction_time

    @plan_deduction_time.setter
    def plan_deduction_time(self, value):
        self._plan_deduction_time = value
    @property
    def platform_discount_price(self):
        return self._platform_discount_price

    @platform_discount_price.setter
    def platform_discount_price(self, value):
        self._platform_discount_price = value
    @property
    def redeem_way(self):
        return self._redeem_way

    @redeem_way.setter
    def redeem_way(self, value):
        self._redeem_way = value
    @property
    def refund_cash(self):
        return self._refund_cash

    @refund_cash.setter
    def refund_cash(self, value):
        self._refund_cash = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sub_order_id(self):
        return self._sub_order_id

    @sub_order_id.setter
    def sub_order_id(self, value):
        self._sub_order_id = value
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
    @property
    def user_refuse_reason(self):
        return self._user_refuse_reason

    @user_refuse_reason.setter
    def user_refuse_reason(self, value):
        self._user_refuse_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_fee_info_list:
            if isinstance(self.bill_fee_info_list, list):
                for i in range(0, len(self.bill_fee_info_list)):
                    element = self.bill_fee_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_fee_info_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_fee_info_list, 'to_alipay_dict'):
                params['bill_fee_info_list'] = self.bill_fee_info_list.to_alipay_dict()
            else:
                params['bill_fee_info_list'] = self.bill_fee_info_list
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_serial:
            if hasattr(self.certificate_serial, 'to_alipay_dict'):
                params['certificate_serial'] = self.certificate_serial.to_alipay_dict()
            else:
                params['certificate_serial'] = self.certificate_serial
        if self.damages_info:
            if hasattr(self.damages_info, 'to_alipay_dict'):
                params['damages_info'] = self.damages_info.to_alipay_dict()
            else:
                params['damages_info'] = self.damages_info
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.deduction_cash:
            if hasattr(self.deduction_cash, 'to_alipay_dict'):
                params['deduction_cash'] = self.deduction_cash.to_alipay_dict()
            else:
                params['deduction_cash'] = self.deduction_cash
        if self.deduction_count:
            if hasattr(self.deduction_count, 'to_alipay_dict'):
                params['deduction_count'] = self.deduction_count.to_alipay_dict()
            else:
                params['deduction_count'] = self.deduction_count
        if self.deduction_fail_reason:
            if hasattr(self.deduction_fail_reason, 'to_alipay_dict'):
                params['deduction_fail_reason'] = self.deduction_fail_reason.to_alipay_dict()
            else:
                params['deduction_fail_reason'] = self.deduction_fail_reason
        if self.deduction_fail_times:
            if hasattr(self.deduction_fail_times, 'to_alipay_dict'):
                params['deduction_fail_times'] = self.deduction_fail_times.to_alipay_dict()
            else:
                params['deduction_fail_times'] = self.deduction_fail_times
        if self.deduction_order_id:
            if hasattr(self.deduction_order_id, 'to_alipay_dict'):
                params['deduction_order_id'] = self.deduction_order_id.to_alipay_dict()
            else:
                params['deduction_order_id'] = self.deduction_order_id
        if self.deduction_order_once_info_list:
            if isinstance(self.deduction_order_once_info_list, list):
                for i in range(0, len(self.deduction_order_once_info_list)):
                    element = self.deduction_order_once_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.deduction_order_once_info_list[i] = element.to_alipay_dict()
            if hasattr(self.deduction_order_once_info_list, 'to_alipay_dict'):
                params['deduction_order_once_info_list'] = self.deduction_order_once_info_list.to_alipay_dict()
            else:
                params['deduction_order_once_info_list'] = self.deduction_order_once_info_list
        if self.deduction_order_type:
            if hasattr(self.deduction_order_type, 'to_alipay_dict'):
                params['deduction_order_type'] = self.deduction_order_type.to_alipay_dict()
            else:
                params['deduction_order_type'] = self.deduction_order_type
        if self.deduction_status:
            if hasattr(self.deduction_status, 'to_alipay_dict'):
                params['deduction_status'] = self.deduction_status.to_alipay_dict()
            else:
                params['deduction_status'] = self.deduction_status
        if self.deduction_time:
            if hasattr(self.deduction_time, 'to_alipay_dict'):
                params['deduction_time'] = self.deduction_time.to_alipay_dict()
            else:
                params['deduction_time'] = self.deduction_time
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
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
        if self.payment_no:
            if hasattr(self.payment_no, 'to_alipay_dict'):
                params['payment_no'] = self.payment_no.to_alipay_dict()
            else:
                params['payment_no'] = self.payment_no
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.plan_deduction_time:
            if hasattr(self.plan_deduction_time, 'to_alipay_dict'):
                params['plan_deduction_time'] = self.plan_deduction_time.to_alipay_dict()
            else:
                params['plan_deduction_time'] = self.plan_deduction_time
        if self.platform_discount_price:
            if hasattr(self.platform_discount_price, 'to_alipay_dict'):
                params['platform_discount_price'] = self.platform_discount_price.to_alipay_dict()
            else:
                params['platform_discount_price'] = self.platform_discount_price
        if self.redeem_way:
            if hasattr(self.redeem_way, 'to_alipay_dict'):
                params['redeem_way'] = self.redeem_way.to_alipay_dict()
            else:
                params['redeem_way'] = self.redeem_way
        if self.refund_cash:
            if hasattr(self.refund_cash, 'to_alipay_dict'):
                params['refund_cash'] = self.refund_cash.to_alipay_dict()
            else:
                params['refund_cash'] = self.refund_cash
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sub_order_id:
            if hasattr(self.sub_order_id, 'to_alipay_dict'):
                params['sub_order_id'] = self.sub_order_id.to_alipay_dict()
            else:
                params['sub_order_id'] = self.sub_order_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_refuse_reason:
            if hasattr(self.user_refuse_reason, 'to_alipay_dict'):
                params['user_refuse_reason'] = self.user_refuse_reason.to_alipay_dict()
            else:
                params['user_refuse_reason'] = self.user_refuse_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeductionOrderInfo()
        if 'bill_fee_info_list' in d:
            o.bill_fee_info_list = d['bill_fee_info_list']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_serial' in d:
            o.certificate_serial = d['certificate_serial']
        if 'damages_info' in d:
            o.damages_info = d['damages_info']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'deduction_cash' in d:
            o.deduction_cash = d['deduction_cash']
        if 'deduction_count' in d:
            o.deduction_count = d['deduction_count']
        if 'deduction_fail_reason' in d:
            o.deduction_fail_reason = d['deduction_fail_reason']
        if 'deduction_fail_times' in d:
            o.deduction_fail_times = d['deduction_fail_times']
        if 'deduction_order_id' in d:
            o.deduction_order_id = d['deduction_order_id']
        if 'deduction_order_once_info_list' in d:
            o.deduction_order_once_info_list = d['deduction_order_once_info_list']
        if 'deduction_order_type' in d:
            o.deduction_order_type = d['deduction_order_type']
        if 'deduction_status' in d:
            o.deduction_status = d['deduction_status']
        if 'deduction_time' in d:
            o.deduction_time = d['deduction_time']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'payment_no' in d:
            o.payment_no = d['payment_no']
        if 'period' in d:
            o.period = d['period']
        if 'plan_deduction_time' in d:
            o.plan_deduction_time = d['plan_deduction_time']
        if 'platform_discount_price' in d:
            o.platform_discount_price = d['platform_discount_price']
        if 'redeem_way' in d:
            o.redeem_way = d['redeem_way']
        if 'refund_cash' in d:
            o.refund_cash = d['refund_cash']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sub_order_id' in d:
            o.sub_order_id = d['sub_order_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_refuse_reason' in d:
            o.user_refuse_reason = d['user_refuse_reason']
        return o


