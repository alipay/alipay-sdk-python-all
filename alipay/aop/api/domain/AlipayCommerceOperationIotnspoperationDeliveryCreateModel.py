#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NDeliveryBaseInfo import NDeliveryBaseInfo
from alipay.aop.api.domain.NDeliveryPalyConfig import NDeliveryPalyConfig
from alipay.aop.api.domain.NDeliveryTargetRule import NDeliveryTargetRule


class AlipayCommerceOperationIotnspoperationDeliveryCreateModel(object):

    def __init__(self):
        self._merchant_access_mode = None
        self._n_delivery_base_info = None
        self._n_delivery_paly_config = None
        self._n_delivery_target_rule = None
        self._out_biz_no = None

    @property
    def merchant_access_mode(self):
        return self._merchant_access_mode

    @merchant_access_mode.setter
    def merchant_access_mode(self, value):
        self._merchant_access_mode = value
    @property
    def n_delivery_base_info(self):
        return self._n_delivery_base_info

    @n_delivery_base_info.setter
    def n_delivery_base_info(self, value):
        if isinstance(value, NDeliveryBaseInfo):
            self._n_delivery_base_info = value
        else:
            self._n_delivery_base_info = NDeliveryBaseInfo.from_alipay_dict(value)
    @property
    def n_delivery_paly_config(self):
        return self._n_delivery_paly_config

    @n_delivery_paly_config.setter
    def n_delivery_paly_config(self, value):
        if isinstance(value, NDeliveryPalyConfig):
            self._n_delivery_paly_config = value
        else:
            self._n_delivery_paly_config = NDeliveryPalyConfig.from_alipay_dict(value)
    @property
    def n_delivery_target_rule(self):
        return self._n_delivery_target_rule

    @n_delivery_target_rule.setter
    def n_delivery_target_rule(self, value):
        if isinstance(value, NDeliveryTargetRule):
            self._n_delivery_target_rule = value
        else:
            self._n_delivery_target_rule = NDeliveryTargetRule.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_access_mode:
            if hasattr(self.merchant_access_mode, 'to_alipay_dict'):
                params['merchant_access_mode'] = self.merchant_access_mode.to_alipay_dict()
            else:
                params['merchant_access_mode'] = self.merchant_access_mode
        if self.n_delivery_base_info:
            if hasattr(self.n_delivery_base_info, 'to_alipay_dict'):
                params['n_delivery_base_info'] = self.n_delivery_base_info.to_alipay_dict()
            else:
                params['n_delivery_base_info'] = self.n_delivery_base_info
        if self.n_delivery_paly_config:
            if hasattr(self.n_delivery_paly_config, 'to_alipay_dict'):
                params['n_delivery_paly_config'] = self.n_delivery_paly_config.to_alipay_dict()
            else:
                params['n_delivery_paly_config'] = self.n_delivery_paly_config
        if self.n_delivery_target_rule:
            if hasattr(self.n_delivery_target_rule, 'to_alipay_dict'):
                params['n_delivery_target_rule'] = self.n_delivery_target_rule.to_alipay_dict()
            else:
                params['n_delivery_target_rule'] = self.n_delivery_target_rule
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
        o = AlipayCommerceOperationIotnspoperationDeliveryCreateModel()
        if 'merchant_access_mode' in d:
            o.merchant_access_mode = d['merchant_access_mode']
        if 'n_delivery_base_info' in d:
            o.n_delivery_base_info = d['n_delivery_base_info']
        if 'n_delivery_paly_config' in d:
            o.n_delivery_paly_config = d['n_delivery_paly_config']
        if 'n_delivery_target_rule' in d:
            o.n_delivery_target_rule = d['n_delivery_target_rule']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


