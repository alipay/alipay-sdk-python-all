#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingExchangevoucherTemplateCreateModel(object):

    def __init__(self):
        self._brand_name = None
        self._extension_info = None
        self._notify_uri = None
        self._out_biz_no = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._use_type = None
        self._voucher_available_time = None
        self._voucher_description = None
        self._voucher_name = None
        self._voucher_quantity = None
        self._voucher_type = None
        self._voucher_valid_period = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def extension_info(self):
        return self._extension_info

    @extension_info.setter
    def extension_info(self, value):
        self._extension_info = value
    @property
    def notify_uri(self):
        return self._notify_uri

    @notify_uri.setter
    def notify_uri(self, value):
        self._notify_uri = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
    @property
    def use_type(self):
        return self._use_type

    @use_type.setter
    def use_type(self, value):
        self._use_type = value
    @property
    def voucher_available_time(self):
        return self._voucher_available_time

    @voucher_available_time.setter
    def voucher_available_time(self, value):
        self._voucher_available_time = value
    @property
    def voucher_description(self):
        return self._voucher_description

    @voucher_description.setter
    def voucher_description(self, value):
        self._voucher_description = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_quantity(self):
        return self._voucher_quantity

    @voucher_quantity.setter
    def voucher_quantity(self, value):
        self._voucher_quantity = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def voucher_valid_period(self):
        return self._voucher_valid_period

    @voucher_valid_period.setter
    def voucher_valid_period(self, value):
        self._voucher_valid_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.extension_info:
            if hasattr(self.extension_info, 'to_alipay_dict'):
                params['extension_info'] = self.extension_info.to_alipay_dict()
            else:
                params['extension_info'] = self.extension_info
        if self.notify_uri:
            if hasattr(self.notify_uri, 'to_alipay_dict'):
                params['notify_uri'] = self.notify_uri.to_alipay_dict()
            else:
                params['notify_uri'] = self.notify_uri
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.publish_end_time:
            if hasattr(self.publish_end_time, 'to_alipay_dict'):
                params['publish_end_time'] = self.publish_end_time.to_alipay_dict()
            else:
                params['publish_end_time'] = self.publish_end_time
        if self.publish_start_time:
            if hasattr(self.publish_start_time, 'to_alipay_dict'):
                params['publish_start_time'] = self.publish_start_time.to_alipay_dict()
            else:
                params['publish_start_time'] = self.publish_start_time
        if self.use_type:
            if hasattr(self.use_type, 'to_alipay_dict'):
                params['use_type'] = self.use_type.to_alipay_dict()
            else:
                params['use_type'] = self.use_type
        if self.voucher_available_time:
            if hasattr(self.voucher_available_time, 'to_alipay_dict'):
                params['voucher_available_time'] = self.voucher_available_time.to_alipay_dict()
            else:
                params['voucher_available_time'] = self.voucher_available_time
        if self.voucher_description:
            if hasattr(self.voucher_description, 'to_alipay_dict'):
                params['voucher_description'] = self.voucher_description.to_alipay_dict()
            else:
                params['voucher_description'] = self.voucher_description
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_quantity:
            if hasattr(self.voucher_quantity, 'to_alipay_dict'):
                params['voucher_quantity'] = self.voucher_quantity.to_alipay_dict()
            else:
                params['voucher_quantity'] = self.voucher_quantity
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        if self.voucher_valid_period:
            if hasattr(self.voucher_valid_period, 'to_alipay_dict'):
                params['voucher_valid_period'] = self.voucher_valid_period.to_alipay_dict()
            else:
                params['voucher_valid_period'] = self.voucher_valid_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingExchangevoucherTemplateCreateModel()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'extension_info' in d:
            o.extension_info = d['extension_info']
        if 'notify_uri' in d:
            o.notify_uri = d['notify_uri']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'publish_start_time' in d:
            o.publish_start_time = d['publish_start_time']
        if 'use_type' in d:
            o.use_type = d['use_type']
        if 'voucher_available_time' in d:
            o.voucher_available_time = d['voucher_available_time']
        if 'voucher_description' in d:
            o.voucher_description = d['voucher_description']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_quantity' in d:
            o.voucher_quantity = d['voucher_quantity']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        if 'voucher_valid_period' in d:
            o.voucher_valid_period = d['voucher_valid_period']
        return o


