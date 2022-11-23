#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardLevelConfigDTO import CardLevelConfigDTO


class AlipayUserCardLevelSetModel(object):

    def __init__(self):
        self._card_level_config = None
        self._operate_type = None
        self._template_id = None

    @property
    def card_level_config(self):
        return self._card_level_config

    @card_level_config.setter
    def card_level_config(self, value):
        if isinstance(value, CardLevelConfigDTO):
            self._card_level_config = value
        else:
            self._card_level_config = CardLevelConfigDTO.from_alipay_dict(value)
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_level_config:
            if hasattr(self.card_level_config, 'to_alipay_dict'):
                params['card_level_config'] = self.card_level_config.to_alipay_dict()
            else:
                params['card_level_config'] = self.card_level_config
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCardLevelSetModel()
        if 'card_level_config' in d:
            o.card_level_config = d['card_level_config']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


