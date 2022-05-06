#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryAgencyMerchantInfo import DeliveryAgencyMerchantInfo
from alipay.aop.api.domain.DeliveryBaseInfo import DeliveryBaseInfo
from alipay.aop.api.domain.DeliveryConfig import DeliveryConfig
from alipay.aop.api.domain.DeliveryPlayConfig import DeliveryPlayConfig
from alipay.aop.api.domain.DeliveryTargetRule import DeliveryTargetRule


class AlipayMarketingActivityDeliveryCreateModel(object):

    def __init__(self):
        self._belong_merchant_info = None
        self._delivery_base_info = None
        self._delivery_booth_code = None
        self._delivery_config_list = None
        self._delivery_play_config = None
        self._delivery_target_rule = None
        self._out_biz_no = None

    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, DeliveryAgencyMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = DeliveryAgencyMerchantInfo.from_alipay_dict(value)
    @property
    def delivery_base_info(self):
        return self._delivery_base_info

    @delivery_base_info.setter
    def delivery_base_info(self, value):
        if isinstance(value, DeliveryBaseInfo):
            self._delivery_base_info = value
        else:
            self._delivery_base_info = DeliveryBaseInfo.from_alipay_dict(value)
    @property
    def delivery_booth_code(self):
        return self._delivery_booth_code

    @delivery_booth_code.setter
    def delivery_booth_code(self, value):
        self._delivery_booth_code = value
    @property
    def delivery_config_list(self):
        return self._delivery_config_list

    @delivery_config_list.setter
    def delivery_config_list(self, value):
        if isinstance(value, list):
            self._delivery_config_list = list()
            for i in value:
                if isinstance(i, DeliveryConfig):
                    self._delivery_config_list.append(i)
                else:
                    self._delivery_config_list.append(DeliveryConfig.from_alipay_dict(i))
    @property
    def delivery_play_config(self):
        return self._delivery_play_config

    @delivery_play_config.setter
    def delivery_play_config(self, value):
        if isinstance(value, DeliveryPlayConfig):
            self._delivery_play_config = value
        else:
            self._delivery_play_config = DeliveryPlayConfig.from_alipay_dict(value)
    @property
    def delivery_target_rule(self):
        return self._delivery_target_rule

    @delivery_target_rule.setter
    def delivery_target_rule(self, value):
        if isinstance(value, DeliveryTargetRule):
            self._delivery_target_rule = value
        else:
            self._delivery_target_rule = DeliveryTargetRule.from_alipay_dict(value)
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
        if self.delivery_config_list:
            if isinstance(self.delivery_config_list, list):
                for i in range(0, len(self.delivery_config_list)):
                    element = self.delivery_config_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_config_list[i] = element.to_alipay_dict()
            if hasattr(self.delivery_config_list, 'to_alipay_dict'):
                params['delivery_config_list'] = self.delivery_config_list.to_alipay_dict()
            else:
                params['delivery_config_list'] = self.delivery_config_list
        if self.delivery_play_config:
            if hasattr(self.delivery_play_config, 'to_alipay_dict'):
                params['delivery_play_config'] = self.delivery_play_config.to_alipay_dict()
            else:
                params['delivery_play_config'] = self.delivery_play_config
        if self.delivery_target_rule:
            if hasattr(self.delivery_target_rule, 'to_alipay_dict'):
                params['delivery_target_rule'] = self.delivery_target_rule.to_alipay_dict()
            else:
                params['delivery_target_rule'] = self.delivery_target_rule
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
        o = AlipayMarketingActivityDeliveryCreateModel()
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'delivery_base_info' in d:
            o.delivery_base_info = d['delivery_base_info']
        if 'delivery_booth_code' in d:
            o.delivery_booth_code = d['delivery_booth_code']
        if 'delivery_config_list' in d:
            o.delivery_config_list = d['delivery_config_list']
        if 'delivery_play_config' in d:
            o.delivery_play_config = d['delivery_play_config']
        if 'delivery_target_rule' in d:
            o.delivery_target_rule = d['delivery_target_rule']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


