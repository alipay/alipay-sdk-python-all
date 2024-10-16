#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundedRecordListDTO import RefundedRecordListDTO
from alipay.aop.api.domain.SettleInfoListDTO import SettleInfoListDTO


class DeductionOrderDTO(object):

    def __init__(self):
        self._actual_deduction_time = None
        self._cancel_time = None
        self._deduction_amount = None
        self._deduction_fail_reason = None
        self._deduction_order_no = None
        self._deduction_order_status = None
        self._deduction_order_type = None
        self._deduction_reason = None
        self._open_id = None
        self._order_no = None
        self._pay_channel = None
        self._period_num = None
        self._plan_deduction_time = None
        self._product_no = None
        self._refunded_record_list = None
        self._settle_info_list = None
        self._smid = None
        self._u_open_id = None
        self._user_id = None

    @property
    def actual_deduction_time(self):
        return self._actual_deduction_time

    @actual_deduction_time.setter
    def actual_deduction_time(self, value):
        self._actual_deduction_time = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
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
    def deduction_order_no(self):
        return self._deduction_order_no

    @deduction_order_no.setter
    def deduction_order_no(self, value):
        self._deduction_order_no = value
    @property
    def deduction_order_status(self):
        return self._deduction_order_status

    @deduction_order_status.setter
    def deduction_order_status(self, value):
        self._deduction_order_status = value
    @property
    def deduction_order_type(self):
        return self._deduction_order_type

    @deduction_order_type.setter
    def deduction_order_type(self, value):
        self._deduction_order_type = value
    @property
    def deduction_reason(self):
        return self._deduction_reason

    @deduction_reason.setter
    def deduction_reason(self, value):
        self._deduction_reason = value
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
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def period_num(self):
        return self._period_num

    @period_num.setter
    def period_num(self, value):
        self._period_num = value
    @property
    def plan_deduction_time(self):
        return self._plan_deduction_time

    @plan_deduction_time.setter
    def plan_deduction_time(self, value):
        self._plan_deduction_time = value
    @property
    def product_no(self):
        return self._product_no

    @product_no.setter
    def product_no(self, value):
        self._product_no = value
    @property
    def refunded_record_list(self):
        return self._refunded_record_list

    @refunded_record_list.setter
    def refunded_record_list(self, value):
        if isinstance(value, list):
            self._refunded_record_list = list()
            for i in value:
                if isinstance(i, RefundedRecordListDTO):
                    self._refunded_record_list.append(i)
                else:
                    self._refunded_record_list.append(RefundedRecordListDTO.from_alipay_dict(i))
    @property
    def settle_info_list(self):
        return self._settle_info_list

    @settle_info_list.setter
    def settle_info_list(self, value):
        if isinstance(value, list):
            self._settle_info_list = list()
            for i in value:
                if isinstance(i, SettleInfoListDTO):
                    self._settle_info_list.append(i)
                else:
                    self._settle_info_list.append(SettleInfoListDTO.from_alipay_dict(i))
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def u_open_id(self):
        return self._u_open_id

    @u_open_id.setter
    def u_open_id(self, value):
        self._u_open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_deduction_time:
            if hasattr(self.actual_deduction_time, 'to_alipay_dict'):
                params['actual_deduction_time'] = self.actual_deduction_time.to_alipay_dict()
            else:
                params['actual_deduction_time'] = self.actual_deduction_time
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
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
        if self.deduction_order_no:
            if hasattr(self.deduction_order_no, 'to_alipay_dict'):
                params['deduction_order_no'] = self.deduction_order_no.to_alipay_dict()
            else:
                params['deduction_order_no'] = self.deduction_order_no
        if self.deduction_order_status:
            if hasattr(self.deduction_order_status, 'to_alipay_dict'):
                params['deduction_order_status'] = self.deduction_order_status.to_alipay_dict()
            else:
                params['deduction_order_status'] = self.deduction_order_status
        if self.deduction_order_type:
            if hasattr(self.deduction_order_type, 'to_alipay_dict'):
                params['deduction_order_type'] = self.deduction_order_type.to_alipay_dict()
            else:
                params['deduction_order_type'] = self.deduction_order_type
        if self.deduction_reason:
            if hasattr(self.deduction_reason, 'to_alipay_dict'):
                params['deduction_reason'] = self.deduction_reason.to_alipay_dict()
            else:
                params['deduction_reason'] = self.deduction_reason
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
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.period_num:
            if hasattr(self.period_num, 'to_alipay_dict'):
                params['period_num'] = self.period_num.to_alipay_dict()
            else:
                params['period_num'] = self.period_num
        if self.plan_deduction_time:
            if hasattr(self.plan_deduction_time, 'to_alipay_dict'):
                params['plan_deduction_time'] = self.plan_deduction_time.to_alipay_dict()
            else:
                params['plan_deduction_time'] = self.plan_deduction_time
        if self.product_no:
            if hasattr(self.product_no, 'to_alipay_dict'):
                params['product_no'] = self.product_no.to_alipay_dict()
            else:
                params['product_no'] = self.product_no
        if self.refunded_record_list:
            if isinstance(self.refunded_record_list, list):
                for i in range(0, len(self.refunded_record_list)):
                    element = self.refunded_record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refunded_record_list[i] = element.to_alipay_dict()
            if hasattr(self.refunded_record_list, 'to_alipay_dict'):
                params['refunded_record_list'] = self.refunded_record_list.to_alipay_dict()
            else:
                params['refunded_record_list'] = self.refunded_record_list
        if self.settle_info_list:
            if isinstance(self.settle_info_list, list):
                for i in range(0, len(self.settle_info_list)):
                    element = self.settle_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_info_list[i] = element.to_alipay_dict()
            if hasattr(self.settle_info_list, 'to_alipay_dict'):
                params['settle_info_list'] = self.settle_info_list.to_alipay_dict()
            else:
                params['settle_info_list'] = self.settle_info_list
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.u_open_id:
            if hasattr(self.u_open_id, 'to_alipay_dict'):
                params['u_open_id'] = self.u_open_id.to_alipay_dict()
            else:
                params['u_open_id'] = self.u_open_id
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
        o = DeductionOrderDTO()
        if 'actual_deduction_time' in d:
            o.actual_deduction_time = d['actual_deduction_time']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'deduction_fail_reason' in d:
            o.deduction_fail_reason = d['deduction_fail_reason']
        if 'deduction_order_no' in d:
            o.deduction_order_no = d['deduction_order_no']
        if 'deduction_order_status' in d:
            o.deduction_order_status = d['deduction_order_status']
        if 'deduction_order_type' in d:
            o.deduction_order_type = d['deduction_order_type']
        if 'deduction_reason' in d:
            o.deduction_reason = d['deduction_reason']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'period_num' in d:
            o.period_num = d['period_num']
        if 'plan_deduction_time' in d:
            o.plan_deduction_time = d['plan_deduction_time']
        if 'product_no' in d:
            o.product_no = d['product_no']
        if 'refunded_record_list' in d:
            o.refunded_record_list = d['refunded_record_list']
        if 'settle_info_list' in d:
            o.settle_info_list = d['settle_info_list']
        if 'smid' in d:
            o.smid = d['smid']
        if 'u_open_id' in d:
            o.u_open_id = d['u_open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


