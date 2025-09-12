#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorCreditApplyResultDTO(object):

    def __init__(self):
        self._apply_no = None
        self._apply_status = None
        self._apr = None
        self._channel_customer_id = None
        self._credit_limit = None
        self._day_rate = None
        self._limit_expire_date = None
        self._limit_type = None
        self._out_order_no = None
        self._refuse_code = None
        self._refuse_control_time = None
        self._refuse_msg = None
        self._refuse_msg_data = None
        self._remain_limit = None
        self._total_available_limit = None
        self._total_credit_limit = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def apr(self):
        return self._apr

    @apr.setter
    def apr(self, value):
        self._apr = value
    @property
    def channel_customer_id(self):
        return self._channel_customer_id

    @channel_customer_id.setter
    def channel_customer_id(self, value):
        self._channel_customer_id = value
    @property
    def credit_limit(self):
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, value):
        self._credit_limit = value
    @property
    def day_rate(self):
        return self._day_rate

    @day_rate.setter
    def day_rate(self, value):
        self._day_rate = value
    @property
    def limit_expire_date(self):
        return self._limit_expire_date

    @limit_expire_date.setter
    def limit_expire_date(self, value):
        self._limit_expire_date = value
    @property
    def limit_type(self):
        return self._limit_type

    @limit_type.setter
    def limit_type(self, value):
        self._limit_type = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_control_time(self):
        return self._refuse_control_time

    @refuse_control_time.setter
    def refuse_control_time(self, value):
        self._refuse_control_time = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def refuse_msg_data(self):
        return self._refuse_msg_data

    @refuse_msg_data.setter
    def refuse_msg_data(self, value):
        self._refuse_msg_data = value
    @property
    def remain_limit(self):
        return self._remain_limit

    @remain_limit.setter
    def remain_limit(self, value):
        self._remain_limit = value
    @property
    def total_available_limit(self):
        return self._total_available_limit

    @total_available_limit.setter
    def total_available_limit(self, value):
        self._total_available_limit = value
    @property
    def total_credit_limit(self):
        return self._total_credit_limit

    @total_credit_limit.setter
    def total_credit_limit(self, value):
        self._total_credit_limit = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.apr:
            if hasattr(self.apr, 'to_alipay_dict'):
                params['apr'] = self.apr.to_alipay_dict()
            else:
                params['apr'] = self.apr
        if self.channel_customer_id:
            if hasattr(self.channel_customer_id, 'to_alipay_dict'):
                params['channel_customer_id'] = self.channel_customer_id.to_alipay_dict()
            else:
                params['channel_customer_id'] = self.channel_customer_id
        if self.credit_limit:
            if hasattr(self.credit_limit, 'to_alipay_dict'):
                params['credit_limit'] = self.credit_limit.to_alipay_dict()
            else:
                params['credit_limit'] = self.credit_limit
        if self.day_rate:
            if hasattr(self.day_rate, 'to_alipay_dict'):
                params['day_rate'] = self.day_rate.to_alipay_dict()
            else:
                params['day_rate'] = self.day_rate
        if self.limit_expire_date:
            if hasattr(self.limit_expire_date, 'to_alipay_dict'):
                params['limit_expire_date'] = self.limit_expire_date.to_alipay_dict()
            else:
                params['limit_expire_date'] = self.limit_expire_date
        if self.limit_type:
            if hasattr(self.limit_type, 'to_alipay_dict'):
                params['limit_type'] = self.limit_type.to_alipay_dict()
            else:
                params['limit_type'] = self.limit_type
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.refuse_code:
            if hasattr(self.refuse_code, 'to_alipay_dict'):
                params['refuse_code'] = self.refuse_code.to_alipay_dict()
            else:
                params['refuse_code'] = self.refuse_code
        if self.refuse_control_time:
            if hasattr(self.refuse_control_time, 'to_alipay_dict'):
                params['refuse_control_time'] = self.refuse_control_time.to_alipay_dict()
            else:
                params['refuse_control_time'] = self.refuse_control_time
        if self.refuse_msg:
            if hasattr(self.refuse_msg, 'to_alipay_dict'):
                params['refuse_msg'] = self.refuse_msg.to_alipay_dict()
            else:
                params['refuse_msg'] = self.refuse_msg
        if self.refuse_msg_data:
            if hasattr(self.refuse_msg_data, 'to_alipay_dict'):
                params['refuse_msg_data'] = self.refuse_msg_data.to_alipay_dict()
            else:
                params['refuse_msg_data'] = self.refuse_msg_data
        if self.remain_limit:
            if hasattr(self.remain_limit, 'to_alipay_dict'):
                params['remain_limit'] = self.remain_limit.to_alipay_dict()
            else:
                params['remain_limit'] = self.remain_limit
        if self.total_available_limit:
            if hasattr(self.total_available_limit, 'to_alipay_dict'):
                params['total_available_limit'] = self.total_available_limit.to_alipay_dict()
            else:
                params['total_available_limit'] = self.total_available_limit
        if self.total_credit_limit:
            if hasattr(self.total_credit_limit, 'to_alipay_dict'):
                params['total_credit_limit'] = self.total_credit_limit.to_alipay_dict()
            else:
                params['total_credit_limit'] = self.total_credit_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorCreditApplyResultDTO()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'apr' in d:
            o.apr = d['apr']
        if 'channel_customer_id' in d:
            o.channel_customer_id = d['channel_customer_id']
        if 'credit_limit' in d:
            o.credit_limit = d['credit_limit']
        if 'day_rate' in d:
            o.day_rate = d['day_rate']
        if 'limit_expire_date' in d:
            o.limit_expire_date = d['limit_expire_date']
        if 'limit_type' in d:
            o.limit_type = d['limit_type']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'refuse_code' in d:
            o.refuse_code = d['refuse_code']
        if 'refuse_control_time' in d:
            o.refuse_control_time = d['refuse_control_time']
        if 'refuse_msg' in d:
            o.refuse_msg = d['refuse_msg']
        if 'refuse_msg_data' in d:
            o.refuse_msg_data = d['refuse_msg_data']
        if 'remain_limit' in d:
            o.remain_limit = d['remain_limit']
        if 'total_available_limit' in d:
            o.total_available_limit = d['total_available_limit']
        if 'total_credit_limit' in d:
            o.total_credit_limit = d['total_credit_limit']
        return o


