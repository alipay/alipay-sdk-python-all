#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryMerchantInfoDTO import DeliveryMerchantInfoDTO


class LogisticsInfoDTO(object):

    def __init__(self):
        self._delivery_end_time = None
        self._delivery_merchant_info = None
        self._delivery_start_time = None
        self._delivery_time = None
        self._delivery_type = None

    @property
    def delivery_end_time(self):
        return self._delivery_end_time

    @delivery_end_time.setter
    def delivery_end_time(self, value):
        self._delivery_end_time = value
    @property
    def delivery_merchant_info(self):
        return self._delivery_merchant_info

    @delivery_merchant_info.setter
    def delivery_merchant_info(self, value):
        if isinstance(value, DeliveryMerchantInfoDTO):
            self._delivery_merchant_info = value
        else:
            self._delivery_merchant_info = DeliveryMerchantInfoDTO.from_alipay_dict(value)
    @property
    def delivery_start_time(self):
        return self._delivery_start_time

    @delivery_start_time.setter
    def delivery_start_time(self, value):
        self._delivery_start_time = value
    @property
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, value):
        self._delivery_time = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_end_time:
            if hasattr(self.delivery_end_time, 'to_alipay_dict'):
                params['delivery_end_time'] = self.delivery_end_time.to_alipay_dict()
            else:
                params['delivery_end_time'] = self.delivery_end_time
        if self.delivery_merchant_info:
            if hasattr(self.delivery_merchant_info, 'to_alipay_dict'):
                params['delivery_merchant_info'] = self.delivery_merchant_info.to_alipay_dict()
            else:
                params['delivery_merchant_info'] = self.delivery_merchant_info
        if self.delivery_start_time:
            if hasattr(self.delivery_start_time, 'to_alipay_dict'):
                params['delivery_start_time'] = self.delivery_start_time.to_alipay_dict()
            else:
                params['delivery_start_time'] = self.delivery_start_time
        if self.delivery_time:
            if hasattr(self.delivery_time, 'to_alipay_dict'):
                params['delivery_time'] = self.delivery_time.to_alipay_dict()
            else:
                params['delivery_time'] = self.delivery_time
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsInfoDTO()
        if 'delivery_end_time' in d:
            o.delivery_end_time = d['delivery_end_time']
        if 'delivery_merchant_info' in d:
            o.delivery_merchant_info = d['delivery_merchant_info']
        if 'delivery_start_time' in d:
            o.delivery_start_time = d['delivery_start_time']
        if 'delivery_time' in d:
            o.delivery_time = d['delivery_time']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        return o


