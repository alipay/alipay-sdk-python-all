#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeductionDataSyncRequest(object):

    def __init__(self):
        self._biz_id = None
        self._create_time = None
        self._deduction_amount = None
        self._deduction_fail_reason = None
        self._deduction_fail_times = None
        self._deduction_invoke_appid = None
        self._deduction_order_type = None
        self._deduction_plan_id = None
        self._deduction_status = None
        self._deduction_time = None
        self._env = None
        self._merchant_pid = None
        self._open_id = None
        self._order_no = None
        self._partner_id = None
        self._period = None
        self._refund_price = None
        self._refund_time = None
        self._shop_id = None
        self._smid = None
        self._trade_no = None
        self._update_time = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
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
    def deduction_invoke_appid(self):
        return self._deduction_invoke_appid

    @deduction_invoke_appid.setter
    def deduction_invoke_appid(self, value):
        self._deduction_invoke_appid = value
    @property
    def deduction_order_type(self):
        return self._deduction_order_type

    @deduction_order_type.setter
    def deduction_order_type(self, value):
        self._deduction_order_type = value
    @property
    def deduction_plan_id(self):
        return self._deduction_plan_id

    @deduction_plan_id.setter
    def deduction_plan_id(self, value):
        self._deduction_plan_id = value
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
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
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
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def refund_price(self):
        return self._refund_price

    @refund_price.setter
    def refund_price(self, value):
        self._refund_price = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
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
        if self.deduction_invoke_appid:
            if hasattr(self.deduction_invoke_appid, 'to_alipay_dict'):
                params['deduction_invoke_appid'] = self.deduction_invoke_appid.to_alipay_dict()
            else:
                params['deduction_invoke_appid'] = self.deduction_invoke_appid
        if self.deduction_order_type:
            if hasattr(self.deduction_order_type, 'to_alipay_dict'):
                params['deduction_order_type'] = self.deduction_order_type.to_alipay_dict()
            else:
                params['deduction_order_type'] = self.deduction_order_type
        if self.deduction_plan_id:
            if hasattr(self.deduction_plan_id, 'to_alipay_dict'):
                params['deduction_plan_id'] = self.deduction_plan_id.to_alipay_dict()
            else:
                params['deduction_plan_id'] = self.deduction_plan_id
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
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
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
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.refund_price:
            if hasattr(self.refund_price, 'to_alipay_dict'):
                params['refund_price'] = self.refund_price.to_alipay_dict()
            else:
                params['refund_price'] = self.refund_price
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
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
        o = DeductionDataSyncRequest()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'deduction_fail_reason' in d:
            o.deduction_fail_reason = d['deduction_fail_reason']
        if 'deduction_fail_times' in d:
            o.deduction_fail_times = d['deduction_fail_times']
        if 'deduction_invoke_appid' in d:
            o.deduction_invoke_appid = d['deduction_invoke_appid']
        if 'deduction_order_type' in d:
            o.deduction_order_type = d['deduction_order_type']
        if 'deduction_plan_id' in d:
            o.deduction_plan_id = d['deduction_plan_id']
        if 'deduction_status' in d:
            o.deduction_status = d['deduction_status']
        if 'deduction_time' in d:
            o.deduction_time = d['deduction_time']
        if 'env' in d:
            o.env = d['env']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'period' in d:
            o.period = d['period']
        if 'refund_price' in d:
            o.refund_price = d['refund_price']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'smid' in d:
            o.smid = d['smid']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


