#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtraInfo import ExtraInfo


class AlipayCommerceIndustryOrderSyncModel(object):

    def __init__(self):
        self._buyer_id = None
        self._discount_amount = None
        self._industry_info = None
        self._merchant_order_no = None
        self._order_amount = None
        self._order_create_time = None
        self._order_detail_url = None
        self._order_extra_info = None
        self._order_modify_time = None
        self._order_source = None
        self._payment_amount = None
        self._record_id = None
        self._service_code = None
        self._service_type = None
        self._status = None
        self._sub_service_type = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def industry_info(self):
        return self._industry_info

    @industry_info.setter
    def industry_info(self, value):
        self._industry_info = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_detail_url(self):
        return self._order_detail_url

    @order_detail_url.setter
    def order_detail_url(self, value):
        self._order_detail_url = value
    @property
    def order_extra_info(self):
        return self._order_extra_info

    @order_extra_info.setter
    def order_extra_info(self, value):
        if isinstance(value, ExtraInfo):
            self._order_extra_info = value
        else:
            self._order_extra_info = ExtraInfo.from_alipay_dict(value)
    @property
    def order_modify_time(self):
        return self._order_modify_time

    @order_modify_time.setter
    def order_modify_time(self, value):
        self._order_modify_time = value
    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, value):
        self._order_source = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_service_type(self):
        return self._sub_service_type

    @sub_service_type.setter
    def sub_service_type(self, value):
        self._sub_service_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.industry_info:
            if hasattr(self.industry_info, 'to_alipay_dict'):
                params['industry_info'] = self.industry_info.to_alipay_dict()
            else:
                params['industry_info'] = self.industry_info
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_detail_url:
            if hasattr(self.order_detail_url, 'to_alipay_dict'):
                params['order_detail_url'] = self.order_detail_url.to_alipay_dict()
            else:
                params['order_detail_url'] = self.order_detail_url
        if self.order_extra_info:
            if hasattr(self.order_extra_info, 'to_alipay_dict'):
                params['order_extra_info'] = self.order_extra_info.to_alipay_dict()
            else:
                params['order_extra_info'] = self.order_extra_info
        if self.order_modify_time:
            if hasattr(self.order_modify_time, 'to_alipay_dict'):
                params['order_modify_time'] = self.order_modify_time.to_alipay_dict()
            else:
                params['order_modify_time'] = self.order_modify_time
        if self.order_source:
            if hasattr(self.order_source, 'to_alipay_dict'):
                params['order_source'] = self.order_source.to_alipay_dict()
            else:
                params['order_source'] = self.order_source
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_service_type:
            if hasattr(self.sub_service_type, 'to_alipay_dict'):
                params['sub_service_type'] = self.sub_service_type.to_alipay_dict()
            else:
                params['sub_service_type'] = self.sub_service_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIndustryOrderSyncModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'industry_info' in d:
            o.industry_info = d['industry_info']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_detail_url' in d:
            o.order_detail_url = d['order_detail_url']
        if 'order_extra_info' in d:
            o.order_extra_info = d['order_extra_info']
        if 'order_modify_time' in d:
            o.order_modify_time = d['order_modify_time']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'status' in d:
            o.status = d['status']
        if 'sub_service_type' in d:
            o.sub_service_type = d['sub_service_type']
        return o


