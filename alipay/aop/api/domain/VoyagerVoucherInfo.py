#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoyagerVoucherInfo(object):

    def __init__(self):
        self._action_url = None
        self._detail_url = None
        self._discount_unit = None
        self._discount_value = None
        self._gift_icon = None
        self._max_discount_unit = None
        self._max_discount_value = None
        self._threshold_unit = None
        self._threshold_value = None
        self._usage_condition = None
        self._valid_end_time = None
        self._valid_start_time = None
        self._valid_type = None
        self._voucher_icon = None
        self._voucher_name = None
        self._voucher_status = None
        self._voucher_type = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def discount_unit(self):
        return self._discount_unit

    @discount_unit.setter
    def discount_unit(self, value):
        self._discount_unit = value
    @property
    def discount_value(self):
        return self._discount_value

    @discount_value.setter
    def discount_value(self, value):
        self._discount_value = value
    @property
    def gift_icon(self):
        return self._gift_icon

    @gift_icon.setter
    def gift_icon(self, value):
        self._gift_icon = value
    @property
    def max_discount_unit(self):
        return self._max_discount_unit

    @max_discount_unit.setter
    def max_discount_unit(self, value):
        self._max_discount_unit = value
    @property
    def max_discount_value(self):
        return self._max_discount_value

    @max_discount_value.setter
    def max_discount_value(self, value):
        self._max_discount_value = value
    @property
    def threshold_unit(self):
        return self._threshold_unit

    @threshold_unit.setter
    def threshold_unit(self, value):
        self._threshold_unit = value
    @property
    def threshold_value(self):
        return self._threshold_value

    @threshold_value.setter
    def threshold_value(self, value):
        self._threshold_value = value
    @property
    def usage_condition(self):
        return self._usage_condition

    @usage_condition.setter
    def usage_condition(self, value):
        self._usage_condition = value
    @property
    def valid_end_time(self):
        return self._valid_end_time

    @valid_end_time.setter
    def valid_end_time(self, value):
        self._valid_end_time = value
    @property
    def valid_start_time(self):
        return self._valid_start_time

    @valid_start_time.setter
    def valid_start_time(self, value):
        self._valid_start_time = value
    @property
    def valid_type(self):
        return self._valid_type

    @valid_type.setter
    def valid_type(self, value):
        self._valid_type = value
    @property
    def voucher_icon(self):
        return self._voucher_icon

    @voucher_icon.setter
    def voucher_icon(self, value):
        self._voucher_icon = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.discount_unit:
            if hasattr(self.discount_unit, 'to_alipay_dict'):
                params['discount_unit'] = self.discount_unit.to_alipay_dict()
            else:
                params['discount_unit'] = self.discount_unit
        if self.discount_value:
            if hasattr(self.discount_value, 'to_alipay_dict'):
                params['discount_value'] = self.discount_value.to_alipay_dict()
            else:
                params['discount_value'] = self.discount_value
        if self.gift_icon:
            if hasattr(self.gift_icon, 'to_alipay_dict'):
                params['gift_icon'] = self.gift_icon.to_alipay_dict()
            else:
                params['gift_icon'] = self.gift_icon
        if self.max_discount_unit:
            if hasattr(self.max_discount_unit, 'to_alipay_dict'):
                params['max_discount_unit'] = self.max_discount_unit.to_alipay_dict()
            else:
                params['max_discount_unit'] = self.max_discount_unit
        if self.max_discount_value:
            if hasattr(self.max_discount_value, 'to_alipay_dict'):
                params['max_discount_value'] = self.max_discount_value.to_alipay_dict()
            else:
                params['max_discount_value'] = self.max_discount_value
        if self.threshold_unit:
            if hasattr(self.threshold_unit, 'to_alipay_dict'):
                params['threshold_unit'] = self.threshold_unit.to_alipay_dict()
            else:
                params['threshold_unit'] = self.threshold_unit
        if self.threshold_value:
            if hasattr(self.threshold_value, 'to_alipay_dict'):
                params['threshold_value'] = self.threshold_value.to_alipay_dict()
            else:
                params['threshold_value'] = self.threshold_value
        if self.usage_condition:
            if hasattr(self.usage_condition, 'to_alipay_dict'):
                params['usage_condition'] = self.usage_condition.to_alipay_dict()
            else:
                params['usage_condition'] = self.usage_condition
        if self.valid_end_time:
            if hasattr(self.valid_end_time, 'to_alipay_dict'):
                params['valid_end_time'] = self.valid_end_time.to_alipay_dict()
            else:
                params['valid_end_time'] = self.valid_end_time
        if self.valid_start_time:
            if hasattr(self.valid_start_time, 'to_alipay_dict'):
                params['valid_start_time'] = self.valid_start_time.to_alipay_dict()
            else:
                params['valid_start_time'] = self.valid_start_time
        if self.valid_type:
            if hasattr(self.valid_type, 'to_alipay_dict'):
                params['valid_type'] = self.valid_type.to_alipay_dict()
            else:
                params['valid_type'] = self.valid_type
        if self.voucher_icon:
            if hasattr(self.voucher_icon, 'to_alipay_dict'):
                params['voucher_icon'] = self.voucher_icon.to_alipay_dict()
            else:
                params['voucher_icon'] = self.voucher_icon
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerVoucherInfo()
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'discount_unit' in d:
            o.discount_unit = d['discount_unit']
        if 'discount_value' in d:
            o.discount_value = d['discount_value']
        if 'gift_icon' in d:
            o.gift_icon = d['gift_icon']
        if 'max_discount_unit' in d:
            o.max_discount_unit = d['max_discount_unit']
        if 'max_discount_value' in d:
            o.max_discount_value = d['max_discount_value']
        if 'threshold_unit' in d:
            o.threshold_unit = d['threshold_unit']
        if 'threshold_value' in d:
            o.threshold_value = d['threshold_value']
        if 'usage_condition' in d:
            o.usage_condition = d['usage_condition']
        if 'valid_end_time' in d:
            o.valid_end_time = d['valid_end_time']
        if 'valid_start_time' in d:
            o.valid_start_time = d['valid_start_time']
        if 'valid_type' in d:
            o.valid_type = d['valid_type']
        if 'voucher_icon' in d:
            o.voucher_icon = d['voucher_icon']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


