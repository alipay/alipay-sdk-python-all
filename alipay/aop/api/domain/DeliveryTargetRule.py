#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryAvailableScope import DeliveryAvailableScope
from alipay.aop.api.domain.DeliveryCityCodeRule import DeliveryCityCodeRule
from alipay.aop.api.domain.DeliveryCrowdRule import DeliveryCrowdRule
from alipay.aop.api.domain.DeliveryMerchantInfo import DeliveryMerchantInfo
from alipay.aop.api.domain.DeliveryMerchantRule import DeliveryMerchantRule
from alipay.aop.api.domain.DeliverySearchBoxRule import DeliverySearchBoxRule
from alipay.aop.api.domain.DeliveryTemplateRule import DeliveryTemplateRule


class DeliveryTargetRule(object):

    def __init__(self):
        self._brand_id_list = None
        self._delivery_available_scope = None
        self._delivery_city_code_rule = None
        self._delivery_crowd_rule = None
        self._delivery_merchant_infos = None
        self._delivery_merchant_mode = None
        self._delivery_merchant_rule = None
        self._delivery_promo_tags = None
        self._delivery_recall_mode = None
        self._delivery_search_box_rule = None
        self._delivery_template_rule = None
        self._delivery_type = None

    @property
    def brand_id_list(self):
        return self._brand_id_list

    @brand_id_list.setter
    def brand_id_list(self, value):
        if isinstance(value, list):
            self._brand_id_list = list()
            for i in value:
                self._brand_id_list.append(i)
    @property
    def delivery_available_scope(self):
        return self._delivery_available_scope

    @delivery_available_scope.setter
    def delivery_available_scope(self, value):
        if isinstance(value, DeliveryAvailableScope):
            self._delivery_available_scope = value
        else:
            self._delivery_available_scope = DeliveryAvailableScope.from_alipay_dict(value)
    @property
    def delivery_city_code_rule(self):
        return self._delivery_city_code_rule

    @delivery_city_code_rule.setter
    def delivery_city_code_rule(self, value):
        if isinstance(value, DeliveryCityCodeRule):
            self._delivery_city_code_rule = value
        else:
            self._delivery_city_code_rule = DeliveryCityCodeRule.from_alipay_dict(value)
    @property
    def delivery_crowd_rule(self):
        return self._delivery_crowd_rule

    @delivery_crowd_rule.setter
    def delivery_crowd_rule(self, value):
        if isinstance(value, DeliveryCrowdRule):
            self._delivery_crowd_rule = value
        else:
            self._delivery_crowd_rule = DeliveryCrowdRule.from_alipay_dict(value)
    @property
    def delivery_merchant_infos(self):
        return self._delivery_merchant_infos

    @delivery_merchant_infos.setter
    def delivery_merchant_infos(self, value):
        if isinstance(value, list):
            self._delivery_merchant_infos = list()
            for i in value:
                if isinstance(i, DeliveryMerchantInfo):
                    self._delivery_merchant_infos.append(i)
                else:
                    self._delivery_merchant_infos.append(DeliveryMerchantInfo.from_alipay_dict(i))
    @property
    def delivery_merchant_mode(self):
        return self._delivery_merchant_mode

    @delivery_merchant_mode.setter
    def delivery_merchant_mode(self, value):
        self._delivery_merchant_mode = value
    @property
    def delivery_merchant_rule(self):
        return self._delivery_merchant_rule

    @delivery_merchant_rule.setter
    def delivery_merchant_rule(self, value):
        if isinstance(value, DeliveryMerchantRule):
            self._delivery_merchant_rule = value
        else:
            self._delivery_merchant_rule = DeliveryMerchantRule.from_alipay_dict(value)
    @property
    def delivery_promo_tags(self):
        return self._delivery_promo_tags

    @delivery_promo_tags.setter
    def delivery_promo_tags(self, value):
        self._delivery_promo_tags = value
    @property
    def delivery_recall_mode(self):
        return self._delivery_recall_mode

    @delivery_recall_mode.setter
    def delivery_recall_mode(self, value):
        self._delivery_recall_mode = value
    @property
    def delivery_search_box_rule(self):
        return self._delivery_search_box_rule

    @delivery_search_box_rule.setter
    def delivery_search_box_rule(self, value):
        if isinstance(value, DeliverySearchBoxRule):
            self._delivery_search_box_rule = value
        else:
            self._delivery_search_box_rule = DeliverySearchBoxRule.from_alipay_dict(value)
    @property
    def delivery_template_rule(self):
        return self._delivery_template_rule

    @delivery_template_rule.setter
    def delivery_template_rule(self, value):
        if isinstance(value, DeliveryTemplateRule):
            self._delivery_template_rule = value
        else:
            self._delivery_template_rule = DeliveryTemplateRule.from_alipay_dict(value)
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id_list:
            if isinstance(self.brand_id_list, list):
                for i in range(0, len(self.brand_id_list)):
                    element = self.brand_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_id_list[i] = element.to_alipay_dict()
            if hasattr(self.brand_id_list, 'to_alipay_dict'):
                params['brand_id_list'] = self.brand_id_list.to_alipay_dict()
            else:
                params['brand_id_list'] = self.brand_id_list
        if self.delivery_available_scope:
            if hasattr(self.delivery_available_scope, 'to_alipay_dict'):
                params['delivery_available_scope'] = self.delivery_available_scope.to_alipay_dict()
            else:
                params['delivery_available_scope'] = self.delivery_available_scope
        if self.delivery_city_code_rule:
            if hasattr(self.delivery_city_code_rule, 'to_alipay_dict'):
                params['delivery_city_code_rule'] = self.delivery_city_code_rule.to_alipay_dict()
            else:
                params['delivery_city_code_rule'] = self.delivery_city_code_rule
        if self.delivery_crowd_rule:
            if hasattr(self.delivery_crowd_rule, 'to_alipay_dict'):
                params['delivery_crowd_rule'] = self.delivery_crowd_rule.to_alipay_dict()
            else:
                params['delivery_crowd_rule'] = self.delivery_crowd_rule
        if self.delivery_merchant_infos:
            if isinstance(self.delivery_merchant_infos, list):
                for i in range(0, len(self.delivery_merchant_infos)):
                    element = self.delivery_merchant_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_merchant_infos[i] = element.to_alipay_dict()
            if hasattr(self.delivery_merchant_infos, 'to_alipay_dict'):
                params['delivery_merchant_infos'] = self.delivery_merchant_infos.to_alipay_dict()
            else:
                params['delivery_merchant_infos'] = self.delivery_merchant_infos
        if self.delivery_merchant_mode:
            if hasattr(self.delivery_merchant_mode, 'to_alipay_dict'):
                params['delivery_merchant_mode'] = self.delivery_merchant_mode.to_alipay_dict()
            else:
                params['delivery_merchant_mode'] = self.delivery_merchant_mode
        if self.delivery_merchant_rule:
            if hasattr(self.delivery_merchant_rule, 'to_alipay_dict'):
                params['delivery_merchant_rule'] = self.delivery_merchant_rule.to_alipay_dict()
            else:
                params['delivery_merchant_rule'] = self.delivery_merchant_rule
        if self.delivery_promo_tags:
            if hasattr(self.delivery_promo_tags, 'to_alipay_dict'):
                params['delivery_promo_tags'] = self.delivery_promo_tags.to_alipay_dict()
            else:
                params['delivery_promo_tags'] = self.delivery_promo_tags
        if self.delivery_recall_mode:
            if hasattr(self.delivery_recall_mode, 'to_alipay_dict'):
                params['delivery_recall_mode'] = self.delivery_recall_mode.to_alipay_dict()
            else:
                params['delivery_recall_mode'] = self.delivery_recall_mode
        if self.delivery_search_box_rule:
            if hasattr(self.delivery_search_box_rule, 'to_alipay_dict'):
                params['delivery_search_box_rule'] = self.delivery_search_box_rule.to_alipay_dict()
            else:
                params['delivery_search_box_rule'] = self.delivery_search_box_rule
        if self.delivery_template_rule:
            if hasattr(self.delivery_template_rule, 'to_alipay_dict'):
                params['delivery_template_rule'] = self.delivery_template_rule.to_alipay_dict()
            else:
                params['delivery_template_rule'] = self.delivery_template_rule
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
        o = DeliveryTargetRule()
        if 'brand_id_list' in d:
            o.brand_id_list = d['brand_id_list']
        if 'delivery_available_scope' in d:
            o.delivery_available_scope = d['delivery_available_scope']
        if 'delivery_city_code_rule' in d:
            o.delivery_city_code_rule = d['delivery_city_code_rule']
        if 'delivery_crowd_rule' in d:
            o.delivery_crowd_rule = d['delivery_crowd_rule']
        if 'delivery_merchant_infos' in d:
            o.delivery_merchant_infos = d['delivery_merchant_infos']
        if 'delivery_merchant_mode' in d:
            o.delivery_merchant_mode = d['delivery_merchant_mode']
        if 'delivery_merchant_rule' in d:
            o.delivery_merchant_rule = d['delivery_merchant_rule']
        if 'delivery_promo_tags' in d:
            o.delivery_promo_tags = d['delivery_promo_tags']
        if 'delivery_recall_mode' in d:
            o.delivery_recall_mode = d['delivery_recall_mode']
        if 'delivery_search_box_rule' in d:
            o.delivery_search_box_rule = d['delivery_search_box_rule']
        if 'delivery_template_rule' in d:
            o.delivery_template_rule = d['delivery_template_rule']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        return o


