#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayForPrivilegeCardTemplateConfig import PayForPrivilegeCardTemplateConfig


class AlipayMerchantPayforprivilegeProfileSetModel(object):

    def __init__(self):
        self._card_template_config = None

    @property
    def card_template_config(self):
        return self._card_template_config

    @card_template_config.setter
    def card_template_config(self, value):
        if isinstance(value, PayForPrivilegeCardTemplateConfig):
            self._card_template_config = value
        else:
            self._card_template_config = PayForPrivilegeCardTemplateConfig.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_config:
            if hasattr(self.card_template_config, 'to_alipay_dict'):
                params['card_template_config'] = self.card_template_config.to_alipay_dict()
            else:
                params['card_template_config'] = self.card_template_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantPayforprivilegeProfileSetModel()
        if 'card_template_config' in d:
            o.card_template_config = d['card_template_config']
        return o


