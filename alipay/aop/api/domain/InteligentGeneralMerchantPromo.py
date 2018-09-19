#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CrowdConstraintInfo import CrowdConstraintInfo
from alipay.aop.api.domain.IntelligentPromoEffect import IntelligentPromoEffect
from alipay.aop.api.domain.InteligentBudgetInfo import InteligentBudgetInfo
from alipay.aop.api.domain.InteligentConstraintInfo import InteligentConstraintInfo
from alipay.aop.api.domain.InteligentPromoTool import InteligentPromoTool
from alipay.aop.api.domain.InteligentPublishChannel import InteligentPublishChannel


class InteligentGeneralMerchantPromo(object):

    def __init__(self):
        self._camp_id = None
        self._crowd_constraint = None
        self._desc = None
        self._ext_info = None
        self._forecast_effect = None
        self._inteligent_budget = None
        self._inteligent_constraint = None
        self._inteligent_promo_tools = None
        self._inteligent_publish_channels = None
        self._merchant_promo_type = None
        self._name = None
        self._template_id = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
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
    def inteligent_budget(self):
        return self._inteligent_budget

    @inteligent_budget.setter
    def inteligent_budget(self, value):
        if isinstance(value, InteligentBudgetInfo):
            self._inteligent_budget = value
        else:
            self._inteligent_budget = InteligentBudgetInfo.from_alipay_dict(value)
    @property
    def inteligent_constraint(self):
        return self._inteligent_constraint

    @inteligent_constraint.setter
    def inteligent_constraint(self, value):
        if isinstance(value, InteligentConstraintInfo):
            self._inteligent_constraint = value
        else:
            self._inteligent_constraint = InteligentConstraintInfo.from_alipay_dict(value)
    @property
    def inteligent_promo_tools(self):
        return self._inteligent_promo_tools

    @inteligent_promo_tools.setter
    def inteligent_promo_tools(self, value):
        if isinstance(value, list):
            self._inteligent_promo_tools = list()
            for i in value:
                if isinstance(i, InteligentPromoTool):
                    self._inteligent_promo_tools.append(i)
                else:
                    self._inteligent_promo_tools.append(InteligentPromoTool.from_alipay_dict(i))
    @property
    def inteligent_publish_channels(self):
        return self._inteligent_publish_channels

    @inteligent_publish_channels.setter
    def inteligent_publish_channels(self, value):
        if isinstance(value, list):
            self._inteligent_publish_channels = list()
            for i in value:
                if isinstance(i, InteligentPublishChannel):
                    self._inteligent_publish_channels.append(i)
                else:
                    self._inteligent_publish_channels.append(InteligentPublishChannel.from_alipay_dict(i))
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
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
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
        if self.inteligent_budget:
            if hasattr(self.inteligent_budget, 'to_alipay_dict'):
                params['inteligent_budget'] = self.inteligent_budget.to_alipay_dict()
            else:
                params['inteligent_budget'] = self.inteligent_budget
        if self.inteligent_constraint:
            if hasattr(self.inteligent_constraint, 'to_alipay_dict'):
                params['inteligent_constraint'] = self.inteligent_constraint.to_alipay_dict()
            else:
                params['inteligent_constraint'] = self.inteligent_constraint
        if self.inteligent_promo_tools:
            if isinstance(self.inteligent_promo_tools, list):
                for i in range(0, len(self.inteligent_promo_tools)):
                    element = self.inteligent_promo_tools[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inteligent_promo_tools[i] = element.to_alipay_dict()
            if hasattr(self.inteligent_promo_tools, 'to_alipay_dict'):
                params['inteligent_promo_tools'] = self.inteligent_promo_tools.to_alipay_dict()
            else:
                params['inteligent_promo_tools'] = self.inteligent_promo_tools
        if self.inteligent_publish_channels:
            if isinstance(self.inteligent_publish_channels, list):
                for i in range(0, len(self.inteligent_publish_channels)):
                    element = self.inteligent_publish_channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inteligent_publish_channels[i] = element.to_alipay_dict()
            if hasattr(self.inteligent_publish_channels, 'to_alipay_dict'):
                params['inteligent_publish_channels'] = self.inteligent_publish_channels.to_alipay_dict()
            else:
                params['inteligent_publish_channels'] = self.inteligent_publish_channels
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
        o = InteligentGeneralMerchantPromo()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'crowd_constraint' in d:
            o.crowd_constraint = d['crowd_constraint']
        if 'desc' in d:
            o.desc = d['desc']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'forecast_effect' in d:
            o.forecast_effect = d['forecast_effect']
        if 'inteligent_budget' in d:
            o.inteligent_budget = d['inteligent_budget']
        if 'inteligent_constraint' in d:
            o.inteligent_constraint = d['inteligent_constraint']
        if 'inteligent_promo_tools' in d:
            o.inteligent_promo_tools = d['inteligent_promo_tools']
        if 'inteligent_publish_channels' in d:
            o.inteligent_publish_channels = d['inteligent_publish_channels']
        if 'merchant_promo_type' in d:
            o.merchant_promo_type = d['merchant_promo_type']
        if 'name' in d:
            o.name = d['name']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


