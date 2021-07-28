#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CountControlConfig import CountControlConfig
from alipay.aop.api.domain.PrizePriceStrategy import PrizePriceStrategy


class AlipayMarketingCampaignPrizepoolPrizeCreateModel(object):

    def __init__(self):
        self._budget_amount = None
        self._budget_type = None
        self._count_control_config = None
        self._ext_properties = None
        self._gmt_begin = None
        self._gmt_end = None
        self._modulus = None
        self._out_biz_id = None
        self._owner = None
        self._pool_id = None
        self._prize_name = None
        self._prize_price_strategy = None
        self._prize_sub_type = None
        self._prize_type = None
        self._source = None
        self._template_id = None

    @property
    def budget_amount(self):
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, value):
        self._budget_amount = value
    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def count_control_config(self):
        return self._count_control_config

    @count_control_config.setter
    def count_control_config(self, value):
        if isinstance(value, list):
            self._count_control_config = list()
            for i in value:
                if isinstance(i, CountControlConfig):
                    self._count_control_config.append(i)
                else:
                    self._count_control_config.append(CountControlConfig.from_alipay_dict(i))
    @property
    def ext_properties(self):
        return self._ext_properties

    @ext_properties.setter
    def ext_properties(self, value):
        self._ext_properties = value
    @property
    def gmt_begin(self):
        return self._gmt_begin

    @gmt_begin.setter
    def gmt_begin(self, value):
        self._gmt_begin = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def modulus(self):
        return self._modulus

    @modulus.setter
    def modulus(self, value):
        self._modulus = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def pool_id(self):
        return self._pool_id

    @pool_id.setter
    def pool_id(self, value):
        self._pool_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_price_strategy(self):
        return self._prize_price_strategy

    @prize_price_strategy.setter
    def prize_price_strategy(self, value):
        if isinstance(value, PrizePriceStrategy):
            self._prize_price_strategy = value
        else:
            self._prize_price_strategy = PrizePriceStrategy.from_alipay_dict(value)
    @property
    def prize_sub_type(self):
        return self._prize_sub_type

    @prize_sub_type.setter
    def prize_sub_type(self, value):
        self._prize_sub_type = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_amount:
            if hasattr(self.budget_amount, 'to_alipay_dict'):
                params['budget_amount'] = self.budget_amount.to_alipay_dict()
            else:
                params['budget_amount'] = self.budget_amount
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.count_control_config:
            if isinstance(self.count_control_config, list):
                for i in range(0, len(self.count_control_config)):
                    element = self.count_control_config[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.count_control_config[i] = element.to_alipay_dict()
            if hasattr(self.count_control_config, 'to_alipay_dict'):
                params['count_control_config'] = self.count_control_config.to_alipay_dict()
            else:
                params['count_control_config'] = self.count_control_config
        if self.ext_properties:
            if hasattr(self.ext_properties, 'to_alipay_dict'):
                params['ext_properties'] = self.ext_properties.to_alipay_dict()
            else:
                params['ext_properties'] = self.ext_properties
        if self.gmt_begin:
            if hasattr(self.gmt_begin, 'to_alipay_dict'):
                params['gmt_begin'] = self.gmt_begin.to_alipay_dict()
            else:
                params['gmt_begin'] = self.gmt_begin
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.modulus:
            if hasattr(self.modulus, 'to_alipay_dict'):
                params['modulus'] = self.modulus.to_alipay_dict()
            else:
                params['modulus'] = self.modulus
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.pool_id:
            if hasattr(self.pool_id, 'to_alipay_dict'):
                params['pool_id'] = self.pool_id.to_alipay_dict()
            else:
                params['pool_id'] = self.pool_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_price_strategy:
            if hasattr(self.prize_price_strategy, 'to_alipay_dict'):
                params['prize_price_strategy'] = self.prize_price_strategy.to_alipay_dict()
            else:
                params['prize_price_strategy'] = self.prize_price_strategy
        if self.prize_sub_type:
            if hasattr(self.prize_sub_type, 'to_alipay_dict'):
                params['prize_sub_type'] = self.prize_sub_type.to_alipay_dict()
            else:
                params['prize_sub_type'] = self.prize_sub_type
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayMarketingCampaignPrizepoolPrizeCreateModel()
        if 'budget_amount' in d:
            o.budget_amount = d['budget_amount']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'count_control_config' in d:
            o.count_control_config = d['count_control_config']
        if 'ext_properties' in d:
            o.ext_properties = d['ext_properties']
        if 'gmt_begin' in d:
            o.gmt_begin = d['gmt_begin']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'modulus' in d:
            o.modulus = d['modulus']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'owner' in d:
            o.owner = d['owner']
        if 'pool_id' in d:
            o.pool_id = d['pool_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_price_strategy' in d:
            o.prize_price_strategy = d['prize_price_strategy']
        if 'prize_sub_type' in d:
            o.prize_sub_type = d['prize_sub_type']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'source' in d:
            o.source = d['source']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


