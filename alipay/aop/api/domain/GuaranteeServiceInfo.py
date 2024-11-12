#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GuaranteeService import GuaranteeService
from alipay.aop.api.domain.GuaranteeService import GuaranteeService


class GuaranteeServiceInfo(object):

    def __init__(self):
        self._basic_guarantee = None
        self._more_services = None
        self._rule_detail_page_url = None
        self._rule_text = None

    @property
    def basic_guarantee(self):
        return self._basic_guarantee

    @basic_guarantee.setter
    def basic_guarantee(self, value):
        if isinstance(value, GuaranteeService):
            self._basic_guarantee = value
        else:
            self._basic_guarantee = GuaranteeService.from_alipay_dict(value)
    @property
    def more_services(self):
        return self._more_services

    @more_services.setter
    def more_services(self, value):
        if isinstance(value, list):
            self._more_services = list()
            for i in value:
                if isinstance(i, GuaranteeService):
                    self._more_services.append(i)
                else:
                    self._more_services.append(GuaranteeService.from_alipay_dict(i))
    @property
    def rule_detail_page_url(self):
        return self._rule_detail_page_url

    @rule_detail_page_url.setter
    def rule_detail_page_url(self, value):
        self._rule_detail_page_url = value
    @property
    def rule_text(self):
        return self._rule_text

    @rule_text.setter
    def rule_text(self, value):
        self._rule_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.basic_guarantee:
            if hasattr(self.basic_guarantee, 'to_alipay_dict'):
                params['basic_guarantee'] = self.basic_guarantee.to_alipay_dict()
            else:
                params['basic_guarantee'] = self.basic_guarantee
        if self.more_services:
            if isinstance(self.more_services, list):
                for i in range(0, len(self.more_services)):
                    element = self.more_services[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.more_services[i] = element.to_alipay_dict()
            if hasattr(self.more_services, 'to_alipay_dict'):
                params['more_services'] = self.more_services.to_alipay_dict()
            else:
                params['more_services'] = self.more_services
        if self.rule_detail_page_url:
            if hasattr(self.rule_detail_page_url, 'to_alipay_dict'):
                params['rule_detail_page_url'] = self.rule_detail_page_url.to_alipay_dict()
            else:
                params['rule_detail_page_url'] = self.rule_detail_page_url
        if self.rule_text:
            if hasattr(self.rule_text, 'to_alipay_dict'):
                params['rule_text'] = self.rule_text.to_alipay_dict()
            else:
                params['rule_text'] = self.rule_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GuaranteeServiceInfo()
        if 'basic_guarantee' in d:
            o.basic_guarantee = d['basic_guarantee']
        if 'more_services' in d:
            o.more_services = d['more_services']
        if 'rule_detail_page_url' in d:
            o.rule_detail_page_url = d['rule_detail_page_url']
        if 'rule_text' in d:
            o.rule_text = d['rule_text']
        return o


