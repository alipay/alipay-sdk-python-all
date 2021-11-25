#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitVoucherRule(object):

    def __init__(self):
        self._amount_max = None
        self._amount_min = None
        self._denomination_percent_max = None
        self._denomination_percent_min = None
        self._floor_amount_max = None
        self._floor_amount_min = None
        self._origin_amount_max = None
        self._origin_amount_min = None
        self._publish_end_time_max = None
        self._publish_end_time_min = None
        self._publish_start_time_max = None
        self._publish_start_time_min = None
        self._refund_type = None
        self._sale_amount_max = None
        self._sale_amount_min = None
        self._use_channel = None
        self._valid_days_after_receive_min = None
        self._voucher_activity_type = None
        self._voucher_quantity_limit_per_user_max = None
        self._voucher_quantity_limit_per_user_min = None
        self._voucher_quantity_max = None
        self._voucher_quantity_min = None
        self._voucher_valid_begin_time_min = None
        self._voucher_valid_end_time_max = None

    @property
    def amount_max(self):
        return self._amount_max

    @amount_max.setter
    def amount_max(self, value):
        self._amount_max = value
    @property
    def amount_min(self):
        return self._amount_min

    @amount_min.setter
    def amount_min(self, value):
        self._amount_min = value
    @property
    def denomination_percent_max(self):
        return self._denomination_percent_max

    @denomination_percent_max.setter
    def denomination_percent_max(self, value):
        self._denomination_percent_max = value
    @property
    def denomination_percent_min(self):
        return self._denomination_percent_min

    @denomination_percent_min.setter
    def denomination_percent_min(self, value):
        self._denomination_percent_min = value
    @property
    def floor_amount_max(self):
        return self._floor_amount_max

    @floor_amount_max.setter
    def floor_amount_max(self, value):
        self._floor_amount_max = value
    @property
    def floor_amount_min(self):
        return self._floor_amount_min

    @floor_amount_min.setter
    def floor_amount_min(self, value):
        self._floor_amount_min = value
    @property
    def origin_amount_max(self):
        return self._origin_amount_max

    @origin_amount_max.setter
    def origin_amount_max(self, value):
        self._origin_amount_max = value
    @property
    def origin_amount_min(self):
        return self._origin_amount_min

    @origin_amount_min.setter
    def origin_amount_min(self, value):
        self._origin_amount_min = value
    @property
    def publish_end_time_max(self):
        return self._publish_end_time_max

    @publish_end_time_max.setter
    def publish_end_time_max(self, value):
        self._publish_end_time_max = value
    @property
    def publish_end_time_min(self):
        return self._publish_end_time_min

    @publish_end_time_min.setter
    def publish_end_time_min(self, value):
        self._publish_end_time_min = value
    @property
    def publish_start_time_max(self):
        return self._publish_start_time_max

    @publish_start_time_max.setter
    def publish_start_time_max(self, value):
        self._publish_start_time_max = value
    @property
    def publish_start_time_min(self):
        return self._publish_start_time_min

    @publish_start_time_min.setter
    def publish_start_time_min(self, value):
        self._publish_start_time_min = value
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        if isinstance(value, list):
            self._refund_type = list()
            for i in value:
                self._refund_type.append(i)
    @property
    def sale_amount_max(self):
        return self._sale_amount_max

    @sale_amount_max.setter
    def sale_amount_max(self, value):
        self._sale_amount_max = value
    @property
    def sale_amount_min(self):
        return self._sale_amount_min

    @sale_amount_min.setter
    def sale_amount_min(self, value):
        self._sale_amount_min = value
    @property
    def use_channel(self):
        return self._use_channel

    @use_channel.setter
    def use_channel(self, value):
        if isinstance(value, list):
            self._use_channel = list()
            for i in value:
                self._use_channel.append(i)
    @property
    def valid_days_after_receive_min(self):
        return self._valid_days_after_receive_min

    @valid_days_after_receive_min.setter
    def valid_days_after_receive_min(self, value):
        self._valid_days_after_receive_min = value
    @property
    def voucher_activity_type(self):
        return self._voucher_activity_type

    @voucher_activity_type.setter
    def voucher_activity_type(self, value):
        self._voucher_activity_type = value
    @property
    def voucher_quantity_limit_per_user_max(self):
        return self._voucher_quantity_limit_per_user_max

    @voucher_quantity_limit_per_user_max.setter
    def voucher_quantity_limit_per_user_max(self, value):
        self._voucher_quantity_limit_per_user_max = value
    @property
    def voucher_quantity_limit_per_user_min(self):
        return self._voucher_quantity_limit_per_user_min

    @voucher_quantity_limit_per_user_min.setter
    def voucher_quantity_limit_per_user_min(self, value):
        self._voucher_quantity_limit_per_user_min = value
    @property
    def voucher_quantity_max(self):
        return self._voucher_quantity_max

    @voucher_quantity_max.setter
    def voucher_quantity_max(self, value):
        self._voucher_quantity_max = value
    @property
    def voucher_quantity_min(self):
        return self._voucher_quantity_min

    @voucher_quantity_min.setter
    def voucher_quantity_min(self, value):
        self._voucher_quantity_min = value
    @property
    def voucher_valid_begin_time_min(self):
        return self._voucher_valid_begin_time_min

    @voucher_valid_begin_time_min.setter
    def voucher_valid_begin_time_min(self, value):
        self._voucher_valid_begin_time_min = value
    @property
    def voucher_valid_end_time_max(self):
        return self._voucher_valid_end_time_max

    @voucher_valid_end_time_max.setter
    def voucher_valid_end_time_max(self, value):
        self._voucher_valid_end_time_max = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_max:
            if hasattr(self.amount_max, 'to_alipay_dict'):
                params['amount_max'] = self.amount_max.to_alipay_dict()
            else:
                params['amount_max'] = self.amount_max
        if self.amount_min:
            if hasattr(self.amount_min, 'to_alipay_dict'):
                params['amount_min'] = self.amount_min.to_alipay_dict()
            else:
                params['amount_min'] = self.amount_min
        if self.denomination_percent_max:
            if hasattr(self.denomination_percent_max, 'to_alipay_dict'):
                params['denomination_percent_max'] = self.denomination_percent_max.to_alipay_dict()
            else:
                params['denomination_percent_max'] = self.denomination_percent_max
        if self.denomination_percent_min:
            if hasattr(self.denomination_percent_min, 'to_alipay_dict'):
                params['denomination_percent_min'] = self.denomination_percent_min.to_alipay_dict()
            else:
                params['denomination_percent_min'] = self.denomination_percent_min
        if self.floor_amount_max:
            if hasattr(self.floor_amount_max, 'to_alipay_dict'):
                params['floor_amount_max'] = self.floor_amount_max.to_alipay_dict()
            else:
                params['floor_amount_max'] = self.floor_amount_max
        if self.floor_amount_min:
            if hasattr(self.floor_amount_min, 'to_alipay_dict'):
                params['floor_amount_min'] = self.floor_amount_min.to_alipay_dict()
            else:
                params['floor_amount_min'] = self.floor_amount_min
        if self.origin_amount_max:
            if hasattr(self.origin_amount_max, 'to_alipay_dict'):
                params['origin_amount_max'] = self.origin_amount_max.to_alipay_dict()
            else:
                params['origin_amount_max'] = self.origin_amount_max
        if self.origin_amount_min:
            if hasattr(self.origin_amount_min, 'to_alipay_dict'):
                params['origin_amount_min'] = self.origin_amount_min.to_alipay_dict()
            else:
                params['origin_amount_min'] = self.origin_amount_min
        if self.publish_end_time_max:
            if hasattr(self.publish_end_time_max, 'to_alipay_dict'):
                params['publish_end_time_max'] = self.publish_end_time_max.to_alipay_dict()
            else:
                params['publish_end_time_max'] = self.publish_end_time_max
        if self.publish_end_time_min:
            if hasattr(self.publish_end_time_min, 'to_alipay_dict'):
                params['publish_end_time_min'] = self.publish_end_time_min.to_alipay_dict()
            else:
                params['publish_end_time_min'] = self.publish_end_time_min
        if self.publish_start_time_max:
            if hasattr(self.publish_start_time_max, 'to_alipay_dict'):
                params['publish_start_time_max'] = self.publish_start_time_max.to_alipay_dict()
            else:
                params['publish_start_time_max'] = self.publish_start_time_max
        if self.publish_start_time_min:
            if hasattr(self.publish_start_time_min, 'to_alipay_dict'):
                params['publish_start_time_min'] = self.publish_start_time_min.to_alipay_dict()
            else:
                params['publish_start_time_min'] = self.publish_start_time_min
        if self.refund_type:
            if isinstance(self.refund_type, list):
                for i in range(0, len(self.refund_type)):
                    element = self.refund_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_type[i] = element.to_alipay_dict()
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        if self.sale_amount_max:
            if hasattr(self.sale_amount_max, 'to_alipay_dict'):
                params['sale_amount_max'] = self.sale_amount_max.to_alipay_dict()
            else:
                params['sale_amount_max'] = self.sale_amount_max
        if self.sale_amount_min:
            if hasattr(self.sale_amount_min, 'to_alipay_dict'):
                params['sale_amount_min'] = self.sale_amount_min.to_alipay_dict()
            else:
                params['sale_amount_min'] = self.sale_amount_min
        if self.use_channel:
            if isinstance(self.use_channel, list):
                for i in range(0, len(self.use_channel)):
                    element = self.use_channel[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.use_channel[i] = element.to_alipay_dict()
            if hasattr(self.use_channel, 'to_alipay_dict'):
                params['use_channel'] = self.use_channel.to_alipay_dict()
            else:
                params['use_channel'] = self.use_channel
        if self.valid_days_after_receive_min:
            if hasattr(self.valid_days_after_receive_min, 'to_alipay_dict'):
                params['valid_days_after_receive_min'] = self.valid_days_after_receive_min.to_alipay_dict()
            else:
                params['valid_days_after_receive_min'] = self.valid_days_after_receive_min
        if self.voucher_activity_type:
            if hasattr(self.voucher_activity_type, 'to_alipay_dict'):
                params['voucher_activity_type'] = self.voucher_activity_type.to_alipay_dict()
            else:
                params['voucher_activity_type'] = self.voucher_activity_type
        if self.voucher_quantity_limit_per_user_max:
            if hasattr(self.voucher_quantity_limit_per_user_max, 'to_alipay_dict'):
                params['voucher_quantity_limit_per_user_max'] = self.voucher_quantity_limit_per_user_max.to_alipay_dict()
            else:
                params['voucher_quantity_limit_per_user_max'] = self.voucher_quantity_limit_per_user_max
        if self.voucher_quantity_limit_per_user_min:
            if hasattr(self.voucher_quantity_limit_per_user_min, 'to_alipay_dict'):
                params['voucher_quantity_limit_per_user_min'] = self.voucher_quantity_limit_per_user_min.to_alipay_dict()
            else:
                params['voucher_quantity_limit_per_user_min'] = self.voucher_quantity_limit_per_user_min
        if self.voucher_quantity_max:
            if hasattr(self.voucher_quantity_max, 'to_alipay_dict'):
                params['voucher_quantity_max'] = self.voucher_quantity_max.to_alipay_dict()
            else:
                params['voucher_quantity_max'] = self.voucher_quantity_max
        if self.voucher_quantity_min:
            if hasattr(self.voucher_quantity_min, 'to_alipay_dict'):
                params['voucher_quantity_min'] = self.voucher_quantity_min.to_alipay_dict()
            else:
                params['voucher_quantity_min'] = self.voucher_quantity_min
        if self.voucher_valid_begin_time_min:
            if hasattr(self.voucher_valid_begin_time_min, 'to_alipay_dict'):
                params['voucher_valid_begin_time_min'] = self.voucher_valid_begin_time_min.to_alipay_dict()
            else:
                params['voucher_valid_begin_time_min'] = self.voucher_valid_begin_time_min
        if self.voucher_valid_end_time_max:
            if hasattr(self.voucher_valid_end_time_max, 'to_alipay_dict'):
                params['voucher_valid_end_time_max'] = self.voucher_valid_end_time_max.to_alipay_dict()
            else:
                params['voucher_valid_end_time_max'] = self.voucher_valid_end_time_max
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitVoucherRule()
        if 'amount_max' in d:
            o.amount_max = d['amount_max']
        if 'amount_min' in d:
            o.amount_min = d['amount_min']
        if 'denomination_percent_max' in d:
            o.denomination_percent_max = d['denomination_percent_max']
        if 'denomination_percent_min' in d:
            o.denomination_percent_min = d['denomination_percent_min']
        if 'floor_amount_max' in d:
            o.floor_amount_max = d['floor_amount_max']
        if 'floor_amount_min' in d:
            o.floor_amount_min = d['floor_amount_min']
        if 'origin_amount_max' in d:
            o.origin_amount_max = d['origin_amount_max']
        if 'origin_amount_min' in d:
            o.origin_amount_min = d['origin_amount_min']
        if 'publish_end_time_max' in d:
            o.publish_end_time_max = d['publish_end_time_max']
        if 'publish_end_time_min' in d:
            o.publish_end_time_min = d['publish_end_time_min']
        if 'publish_start_time_max' in d:
            o.publish_start_time_max = d['publish_start_time_max']
        if 'publish_start_time_min' in d:
            o.publish_start_time_min = d['publish_start_time_min']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        if 'sale_amount_max' in d:
            o.sale_amount_max = d['sale_amount_max']
        if 'sale_amount_min' in d:
            o.sale_amount_min = d['sale_amount_min']
        if 'use_channel' in d:
            o.use_channel = d['use_channel']
        if 'valid_days_after_receive_min' in d:
            o.valid_days_after_receive_min = d['valid_days_after_receive_min']
        if 'voucher_activity_type' in d:
            o.voucher_activity_type = d['voucher_activity_type']
        if 'voucher_quantity_limit_per_user_max' in d:
            o.voucher_quantity_limit_per_user_max = d['voucher_quantity_limit_per_user_max']
        if 'voucher_quantity_limit_per_user_min' in d:
            o.voucher_quantity_limit_per_user_min = d['voucher_quantity_limit_per_user_min']
        if 'voucher_quantity_max' in d:
            o.voucher_quantity_max = d['voucher_quantity_max']
        if 'voucher_quantity_min' in d:
            o.voucher_quantity_min = d['voucher_quantity_min']
        if 'voucher_valid_begin_time_min' in d:
            o.voucher_valid_begin_time_min = d['voucher_valid_begin_time_min']
        if 'voucher_valid_end_time_max' in d:
            o.voucher_valid_end_time_max = d['voucher_valid_end_time_max']
        return o


