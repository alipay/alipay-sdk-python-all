#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoOperatorInfo import PromoOperatorInfo
from alipay.aop.api.domain.IntelligentPromoEffect import IntelligentPromoEffect
from alipay.aop.api.domain.InteligentMerchantPromo import InteligentMerchantPromo
from alipay.aop.api.domain.PromoOperatorInfo import PromoOperatorInfo
from alipay.aop.api.domain.IntelligentPromoDetail import IntelligentPromoDetail


class IntelligentPromo(object):

    def __init__(self):
        self._allow_auto_delay = None
        self._audit_status = None
        self._create_request_no = None
        self._creator_info = None
        self._desc = None
        self._ext_info = None
        self._forecast_effect = None
        self._gmt_closed = None
        self._gmt_enabled = None
        self._gmt_end = None
        self._gmt_start = None
        self._merchant_promos = None
        self._name = None
        self._owner_info = None
        self._parent_promo_id = None
        self._plan_id = None
        self._promo_id = None
        self._promos = None
        self._status = None
        self._sub_promo_ids = None
        self._sub_status = None
        self._template_id = None
        self._type = None

    @property
    def allow_auto_delay(self):
        return self._allow_auto_delay

    @allow_auto_delay.setter
    def allow_auto_delay(self, value):
        self._allow_auto_delay = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def create_request_no(self):
        return self._create_request_no

    @create_request_no.setter
    def create_request_no(self, value):
        self._create_request_no = value
    @property
    def creator_info(self):
        return self._creator_info

    @creator_info.setter
    def creator_info(self, value):
        if isinstance(value, PromoOperatorInfo):
            self._creator_info = value
        else:
            self._creator_info = PromoOperatorInfo.from_alipay_dict(value)
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
    def gmt_closed(self):
        return self._gmt_closed

    @gmt_closed.setter
    def gmt_closed(self, value):
        self._gmt_closed = value
    @property
    def gmt_enabled(self):
        return self._gmt_enabled

    @gmt_enabled.setter
    def gmt_enabled(self, value):
        self._gmt_enabled = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def merchant_promos(self):
        return self._merchant_promos

    @merchant_promos.setter
    def merchant_promos(self, value):
        if isinstance(value, list):
            self._merchant_promos = list()
            for i in value:
                if isinstance(i, InteligentMerchantPromo):
                    self._merchant_promos.append(i)
                else:
                    self._merchant_promos.append(InteligentMerchantPromo.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def owner_info(self):
        return self._owner_info

    @owner_info.setter
    def owner_info(self, value):
        if isinstance(value, PromoOperatorInfo):
            self._owner_info = value
        else:
            self._owner_info = PromoOperatorInfo.from_alipay_dict(value)
    @property
    def parent_promo_id(self):
        return self._parent_promo_id

    @parent_promo_id.setter
    def parent_promo_id(self, value):
        self._parent_promo_id = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def promo_id(self):
        return self._promo_id

    @promo_id.setter
    def promo_id(self, value):
        self._promo_id = value
    @property
    def promos(self):
        return self._promos

    @promos.setter
    def promos(self, value):
        if isinstance(value, list):
            self._promos = list()
            for i in value:
                if isinstance(i, IntelligentPromoDetail):
                    self._promos.append(i)
                else:
                    self._promos.append(IntelligentPromoDetail.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_promo_ids(self):
        return self._sub_promo_ids

    @sub_promo_ids.setter
    def sub_promo_ids(self, value):
        if isinstance(value, list):
            self._sub_promo_ids = list()
            for i in value:
                self._sub_promo_ids.append(i)
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.allow_auto_delay:
            if hasattr(self.allow_auto_delay, 'to_alipay_dict'):
                params['allow_auto_delay'] = self.allow_auto_delay.to_alipay_dict()
            else:
                params['allow_auto_delay'] = self.allow_auto_delay
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.create_request_no:
            if hasattr(self.create_request_no, 'to_alipay_dict'):
                params['create_request_no'] = self.create_request_no.to_alipay_dict()
            else:
                params['create_request_no'] = self.create_request_no
        if self.creator_info:
            if hasattr(self.creator_info, 'to_alipay_dict'):
                params['creator_info'] = self.creator_info.to_alipay_dict()
            else:
                params['creator_info'] = self.creator_info
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
        if self.gmt_closed:
            if hasattr(self.gmt_closed, 'to_alipay_dict'):
                params['gmt_closed'] = self.gmt_closed.to_alipay_dict()
            else:
                params['gmt_closed'] = self.gmt_closed
        if self.gmt_enabled:
            if hasattr(self.gmt_enabled, 'to_alipay_dict'):
                params['gmt_enabled'] = self.gmt_enabled.to_alipay_dict()
            else:
                params['gmt_enabled'] = self.gmt_enabled
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.merchant_promos:
            if isinstance(self.merchant_promos, list):
                for i in range(0, len(self.merchant_promos)):
                    element = self.merchant_promos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_promos[i] = element.to_alipay_dict()
            if hasattr(self.merchant_promos, 'to_alipay_dict'):
                params['merchant_promos'] = self.merchant_promos.to_alipay_dict()
            else:
                params['merchant_promos'] = self.merchant_promos
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.owner_info:
            if hasattr(self.owner_info, 'to_alipay_dict'):
                params['owner_info'] = self.owner_info.to_alipay_dict()
            else:
                params['owner_info'] = self.owner_info
        if self.parent_promo_id:
            if hasattr(self.parent_promo_id, 'to_alipay_dict'):
                params['parent_promo_id'] = self.parent_promo_id.to_alipay_dict()
            else:
                params['parent_promo_id'] = self.parent_promo_id
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.promo_id:
            if hasattr(self.promo_id, 'to_alipay_dict'):
                params['promo_id'] = self.promo_id.to_alipay_dict()
            else:
                params['promo_id'] = self.promo_id
        if self.promos:
            if isinstance(self.promos, list):
                for i in range(0, len(self.promos)):
                    element = self.promos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promos[i] = element.to_alipay_dict()
            if hasattr(self.promos, 'to_alipay_dict'):
                params['promos'] = self.promos.to_alipay_dict()
            else:
                params['promos'] = self.promos
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_promo_ids:
            if isinstance(self.sub_promo_ids, list):
                for i in range(0, len(self.sub_promo_ids)):
                    element = self.sub_promo_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_promo_ids[i] = element.to_alipay_dict()
            if hasattr(self.sub_promo_ids, 'to_alipay_dict'):
                params['sub_promo_ids'] = self.sub_promo_ids.to_alipay_dict()
            else:
                params['sub_promo_ids'] = self.sub_promo_ids
        if self.sub_status:
            if hasattr(self.sub_status, 'to_alipay_dict'):
                params['sub_status'] = self.sub_status.to_alipay_dict()
            else:
                params['sub_status'] = self.sub_status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IntelligentPromo()
        if 'allow_auto_delay' in d:
            o.allow_auto_delay = d['allow_auto_delay']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'create_request_no' in d:
            o.create_request_no = d['create_request_no']
        if 'creator_info' in d:
            o.creator_info = d['creator_info']
        if 'desc' in d:
            o.desc = d['desc']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'forecast_effect' in d:
            o.forecast_effect = d['forecast_effect']
        if 'gmt_closed' in d:
            o.gmt_closed = d['gmt_closed']
        if 'gmt_enabled' in d:
            o.gmt_enabled = d['gmt_enabled']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'merchant_promos' in d:
            o.merchant_promos = d['merchant_promos']
        if 'name' in d:
            o.name = d['name']
        if 'owner_info' in d:
            o.owner_info = d['owner_info']
        if 'parent_promo_id' in d:
            o.parent_promo_id = d['parent_promo_id']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'promo_id' in d:
            o.promo_id = d['promo_id']
        if 'promos' in d:
            o.promos = d['promos']
        if 'status' in d:
            o.status = d['status']
        if 'sub_promo_ids' in d:
            o.sub_promo_ids = d['sub_promo_ids']
        if 'sub_status' in d:
            o.sub_status = d['sub_status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'type' in d:
            o.type = d['type']
        return o


