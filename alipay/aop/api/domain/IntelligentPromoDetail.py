#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BudgetInfo import BudgetInfo
from alipay.aop.api.domain.ConstraintInfo import ConstraintInfo
from alipay.aop.api.domain.CrowdConstraintInfo import CrowdConstraintInfo
from alipay.aop.api.domain.IntelligentPromoEffect import IntelligentPromoEffect
from alipay.aop.api.domain.PromoTool import PromoTool
from alipay.aop.api.domain.PublishChannel import PublishChannel


class IntelligentPromoDetail(object):

    def __init__(self):
        self._budget = None
        self._camp_id = None
        self._constraint = None
        self._crowd_constraint = None
        self._desc = None
        self._ext_info = None
        self._forecast_effect = None
        self._merchant_promo_type = None
        self._name = None
        self._promo_tools = None
        self._publish_channels = None
        self._template_id = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if isinstance(value, BudgetInfo):
            self._budget = value
        else:
            self._budget = BudgetInfo.from_alipay_dict(value)
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def constraint(self):
        return self._constraint

    @constraint.setter
    def constraint(self, value):
        if isinstance(value, ConstraintInfo):
            self._constraint = value
        else:
            self._constraint = ConstraintInfo.from_alipay_dict(value)
    @property
    def crowd_constraint(self):
        return self._crowd_constraint

    @crowd_constraint.setter
    def crowd_constraint(self, value):
        if isinstance(value, CrowdConstraintInfo):
            self._crowd_constraint = value
        else:
            self._crowd_constraint = CrowdConstraintInfo.from_alipay_dict(value)
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def forecast_effect(self):
        return self._forecast_effect

    @forecast_effect.setter
    def forecast_effect(self, value):
        if isinstance(value, IntelligentPromoEffect):
            self._forecast_effect = value
        else:
            self._forecast_effect = IntelligentPromoEffect.from_alipay_dict(value)
    @property
    def merchant_promo_type(self):
        return self._merchant_promo_type

    @merchant_promo_type.setter
    def merchant_promo_type(self, value):
        self._merchant_promo_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def promo_tools(self):
        return self._promo_tools

    @promo_tools.setter
    def promo_tools(self, value):
        if isinstance(value, list):
            self._promo_tools = list()
            for i in value:
                if isinstance(i, PromoTool):
                    self._promo_tools.append(i)
                else:
                    self._promo_tools.append(PromoTool.from_alipay_dict(i))
    @property
    def publish_channels(self):
        return self._publish_channels

    @publish_channels.setter
    def publish_channels(self, value):
        if isinstance(value, list):
            self._publish_channels = list()
            for i in value:
                if isinstance(i, PublishChannel):
                    self._publish_channels.append(i)
                else:
                    self._publish_channels.append(PublishChannel.from_alipay_dict(i))
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget:
            if hasattr(self.budget, 'to_alipay_dict'):
                params['budget'] = self.budget.to_alipay_dict()
            else:
                params['budget'] = self.budget
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.constraint:
            if hasattr(self.constraint, 'to_alipay_dict'):
                params['constraint'] = self.constraint.to_alipay_dict()
            else:
                params['constraint'] = self.constraint
        if self.crowd_constraint:
            if hasattr(self.crowd_constraint, 'to_alipay_dict'):
                params['crowd_constraint'] = self.crowd_constraint.to_alipay_dict()
            else:
                params['crowd_constraint'] = self.crowd_constraint
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.forecast_effect:
            if hasattr(self.forecast_effect, 'to_alipay_dict'):
                params['forecast_effect'] = self.forecast_effect.to_alipay_dict()
            else:
                params['forecast_effect'] = self.forecast_effect
        if self.merchant_promo_type:
            if hasattr(self.merchant_promo_type, 'to_alipay_dict'):
                params['merchant_promo_type'] = self.merchant_promo_type.to_alipay_dict()
            else:
                params['merchant_promo_type'] = self.merchant_promo_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.promo_tools:
            if isinstance(self.promo_tools, list):
                for i in range(0, len(self.promo_tools)):
                    element = self.promo_tools[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_tools[i] = element.to_alipay_dict()
            if hasattr(self.promo_tools, 'to_alipay_dict'):
                params['promo_tools'] = self.promo_tools.to_alipay_dict()
            else:
                params['promo_tools'] = self.promo_tools
        if self.publish_channels:
            if isinstance(self.publish_channels, list):
                for i in range(0, len(self.publish_channels)):
                    element = self.publish_channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.publish_channels[i] = element.to_alipay_dict()
            if hasattr(self.publish_channels, 'to_alipay_dict'):
                params['publish_channels'] = self.publish_channels.to_alipay_dict()
            else:
                params['publish_channels'] = self.publish_channels
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
        o = IntelligentPromoDetail()
        if 'budget' in d:
            o.budget = d['budget']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'constraint' in d:
            o.constraint = d['constraint']
        if 'crowd_constraint' in d:
            o.crowd_constraint = d['crowd_constraint']
        if 'desc' in d:
            o.desc = d['desc']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'forecast_effect' in d:
            o.forecast_effect = d['forecast_effect']
        if 'merchant_promo_type' in d:
            o.merchant_promo_type = d['merchant_promo_type']
        if 'name' in d:
            o.name = d['name']
        if 'promo_tools' in d:
            o.promo_tools = d['promo_tools']
        if 'publish_channels' in d:
            o.publish_channels = d['publish_channels']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


