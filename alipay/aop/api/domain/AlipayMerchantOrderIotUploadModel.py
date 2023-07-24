#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentBusinessInfo import PaymentBusinessInfo
from alipay.aop.api.domain.CustomInfo import CustomInfo


class AlipayMerchantOrderIotUploadModel(object):

    def __init__(self):
        self._abcp_app_id = None
        self._actual_pay_amount = None
        self._actual_pay_time = None
        self._business_infos = None
        self._change_amount = None
        self._custom_infos = None
        self._fail_info = None
        self._merchant_discount_amount = None
        self._origin_amount = None
        self._pay_channel = None
        self._pay_source = None
        self._pay_status = None
        self._result_type = None
        self._source = None
        self._trade_no = None

    @property
    def abcp_app_id(self):
        return self._abcp_app_id

    @abcp_app_id.setter
    def abcp_app_id(self, value):
        self._abcp_app_id = value
    @property
    def actual_pay_amount(self):
        return self._actual_pay_amount

    @actual_pay_amount.setter
    def actual_pay_amount(self, value):
        self._actual_pay_amount = value
    @property
    def actual_pay_time(self):
        return self._actual_pay_time

    @actual_pay_time.setter
    def actual_pay_time(self, value):
        self._actual_pay_time = value
    @property
    def business_infos(self):
        return self._business_infos

    @business_infos.setter
    def business_infos(self, value):
        if isinstance(value, PaymentBusinessInfo):
            self._business_infos = value
        else:
            self._business_infos = PaymentBusinessInfo.from_alipay_dict(value)
    @property
    def change_amount(self):
        return self._change_amount

    @change_amount.setter
    def change_amount(self, value):
        self._change_amount = value
    @property
    def custom_infos(self):
        return self._custom_infos

    @custom_infos.setter
    def custom_infos(self, value):
        if isinstance(value, list):
            self._custom_infos = list()
            for i in value:
                if isinstance(i, CustomInfo):
                    self._custom_infos.append(i)
                else:
                    self._custom_infos.append(CustomInfo.from_alipay_dict(i))
    @property
    def fail_info(self):
        return self._fail_info

    @fail_info.setter
    def fail_info(self, value):
        self._fail_info = value
    @property
    def merchant_discount_amount(self):
        return self._merchant_discount_amount

    @merchant_discount_amount.setter
    def merchant_discount_amount(self, value):
        self._merchant_discount_amount = value
    @property
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        self._origin_amount = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def pay_source(self):
        return self._pay_source

    @pay_source.setter
    def pay_source(self, value):
        self._pay_source = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def result_type(self):
        return self._result_type

    @result_type.setter
    def result_type(self, value):
        self._result_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.abcp_app_id:
            if hasattr(self.abcp_app_id, 'to_alipay_dict'):
                params['abcp_app_id'] = self.abcp_app_id.to_alipay_dict()
            else:
                params['abcp_app_id'] = self.abcp_app_id
        if self.actual_pay_amount:
            if hasattr(self.actual_pay_amount, 'to_alipay_dict'):
                params['actual_pay_amount'] = self.actual_pay_amount.to_alipay_dict()
            else:
                params['actual_pay_amount'] = self.actual_pay_amount
        if self.actual_pay_time:
            if hasattr(self.actual_pay_time, 'to_alipay_dict'):
                params['actual_pay_time'] = self.actual_pay_time.to_alipay_dict()
            else:
                params['actual_pay_time'] = self.actual_pay_time
        if self.business_infos:
            if hasattr(self.business_infos, 'to_alipay_dict'):
                params['business_infos'] = self.business_infos.to_alipay_dict()
            else:
                params['business_infos'] = self.business_infos
        if self.change_amount:
            if hasattr(self.change_amount, 'to_alipay_dict'):
                params['change_amount'] = self.change_amount.to_alipay_dict()
            else:
                params['change_amount'] = self.change_amount
        if self.custom_infos:
            if isinstance(self.custom_infos, list):
                for i in range(0, len(self.custom_infos)):
                    element = self.custom_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.custom_infos[i] = element.to_alipay_dict()
            if hasattr(self.custom_infos, 'to_alipay_dict'):
                params['custom_infos'] = self.custom_infos.to_alipay_dict()
            else:
                params['custom_infos'] = self.custom_infos
        if self.fail_info:
            if hasattr(self.fail_info, 'to_alipay_dict'):
                params['fail_info'] = self.fail_info.to_alipay_dict()
            else:
                params['fail_info'] = self.fail_info
        if self.merchant_discount_amount:
            if hasattr(self.merchant_discount_amount, 'to_alipay_dict'):
                params['merchant_discount_amount'] = self.merchant_discount_amount.to_alipay_dict()
            else:
                params['merchant_discount_amount'] = self.merchant_discount_amount
        if self.origin_amount:
            if hasattr(self.origin_amount, 'to_alipay_dict'):
                params['origin_amount'] = self.origin_amount.to_alipay_dict()
            else:
                params['origin_amount'] = self.origin_amount
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.pay_source:
            if hasattr(self.pay_source, 'to_alipay_dict'):
                params['pay_source'] = self.pay_source.to_alipay_dict()
            else:
                params['pay_source'] = self.pay_source
        if self.pay_status:
            if hasattr(self.pay_status, 'to_alipay_dict'):
                params['pay_status'] = self.pay_status.to_alipay_dict()
            else:
                params['pay_status'] = self.pay_status
        if self.result_type:
            if hasattr(self.result_type, 'to_alipay_dict'):
                params['result_type'] = self.result_type.to_alipay_dict()
            else:
                params['result_type'] = self.result_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantOrderIotUploadModel()
        if 'abcp_app_id' in d:
            o.abcp_app_id = d['abcp_app_id']
        if 'actual_pay_amount' in d:
            o.actual_pay_amount = d['actual_pay_amount']
        if 'actual_pay_time' in d:
            o.actual_pay_time = d['actual_pay_time']
        if 'business_infos' in d:
            o.business_infos = d['business_infos']
        if 'change_amount' in d:
            o.change_amount = d['change_amount']
        if 'custom_infos' in d:
            o.custom_infos = d['custom_infos']
        if 'fail_info' in d:
            o.fail_info = d['fail_info']
        if 'merchant_discount_amount' in d:
            o.merchant_discount_amount = d['merchant_discount_amount']
        if 'origin_amount' in d:
            o.origin_amount = d['origin_amount']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'pay_source' in d:
            o.pay_source = d['pay_source']
        if 'pay_status' in d:
            o.pay_status = d['pay_status']
        if 'result_type' in d:
            o.result_type = d['result_type']
        if 'source' in d:
            o.source = d['source']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


