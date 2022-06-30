#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotDeliveryAgencyMerchantInfo import IotDeliveryAgencyMerchantInfo
from alipay.aop.api.domain.IotDeliveryBaseInfo import IotDeliveryBaseInfo
from alipay.aop.api.domain.IotDeliveryPlayConfig import IotDeliveryPlayConfig


class AlipayMarketingActivityIotdeliveryCreateModel(object):

    def __init__(self):
        self._belong_merchant_info = None
        self._delivery_base_info = None
        self._delivery_booth_code = None
        self._delivery_play_config = None
        self._out_biz_no = None

    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, IotDeliveryAgencyMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = IotDeliveryAgencyMerchantInfo.from_alipay_dict(value)
    @property
    def delivery_base_info(self):
        return self._delivery_base_info

    @delivery_base_info.setter
    def delivery_base_info(self, value):
        if isinstance(value, IotDeliveryBaseInfo):
            self._delivery_base_info = value
        else:
            self._delivery_base_info = IotDeliveryBaseInfo.from_alipay_dict(value)
    @property
    def delivery_booth_code(self):
        return self._delivery_booth_code

    @delivery_booth_code.setter
    def delivery_booth_code(self, value):
        self._delivery_booth_code = value
    @property
    def delivery_play_config(self):
        return self._delivery_play_config

    @delivery_play_config.setter
    def delivery_play_config(self, value):
        if isinstance(value, IotDeliveryPlayConfig):
            self._delivery_play_config = value
        else:
            self._delivery_play_config = IotDeliveryPlayConfig.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.belong_merchant_info:
            if hasattr(self.belong_merchant_info, 'to_alipay_dict'):
                params['belong_merchant_info'] = self.belong_merchant_info.to_alipay_dict()
            else:
                params['belong_merchant_info'] = self.belong_merchant_info
        if self.delivery_base_info:
            if hasattr(self.delivery_base_info, 'to_alipay_dict'):
                params['delivery_base_info'] = self.delivery_base_info.to_alipay_dict()
            else:
                params['delivery_base_info'] = self.delivery_base_info
        if self.delivery_booth_code:
            if hasattr(self.delivery_booth_code, 'to_alipay_dict'):
                params['delivery_booth_code'] = self.delivery_booth_code.to_alipay_dict()
            else:
                params['delivery_booth_code'] = self.delivery_booth_code
        if self.delivery_play_config:
            if hasattr(self.delivery_play_config, 'to_alipay_dict'):
                params['delivery_play_config'] = self.delivery_play_config.to_alipay_dict()
            else:
                params['delivery_play_config'] = self.delivery_play_config
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityIotdeliveryCreateModel()
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'delivery_base_info' in d:
            o.delivery_base_info = d['delivery_base_info']
        if 'delivery_booth_code' in d:
            o.delivery_booth_code = d['delivery_booth_code']
        if 'delivery_play_config' in d:
            o.delivery_play_config = d['delivery_play_config']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


