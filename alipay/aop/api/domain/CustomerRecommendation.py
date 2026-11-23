#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecommendationRegion import RecommendationRegion


class CustomerRecommendation(object):

    def __init__(self):
        self._company_crn = None
        self._company_name = None
        self._contact_count = None
        self._ecommerce_platforms = None
        self._main_business = None
        self._recommendation_reason = None
        self._region = None
        self._sales_amount_text = None

    @property
    def company_crn(self):
        return self._company_crn

    @company_crn.setter
    def company_crn(self, value):
        self._company_crn = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def contact_count(self):
        return self._contact_count

    @contact_count.setter
    def contact_count(self, value):
        self._contact_count = value
    @property
    def ecommerce_platforms(self):
        return self._ecommerce_platforms

    @ecommerce_platforms.setter
    def ecommerce_platforms(self, value):
        if isinstance(value, list):
            self._ecommerce_platforms = list()
            for i in value:
                self._ecommerce_platforms.append(i)
    @property
    def main_business(self):
        return self._main_business

    @main_business.setter
    def main_business(self, value):
        self._main_business = value
    @property
    def recommendation_reason(self):
        return self._recommendation_reason

    @recommendation_reason.setter
    def recommendation_reason(self, value):
        self._recommendation_reason = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        if isinstance(value, RecommendationRegion):
            self._region = value
        else:
            self._region = RecommendationRegion.from_alipay_dict(value)
    @property
    def sales_amount_text(self):
        return self._sales_amount_text

    @sales_amount_text.setter
    def sales_amount_text(self, value):
        self._sales_amount_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_crn:
            if hasattr(self.company_crn, 'to_alipay_dict'):
                params['company_crn'] = self.company_crn.to_alipay_dict()
            else:
                params['company_crn'] = self.company_crn
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.contact_count:
            if hasattr(self.contact_count, 'to_alipay_dict'):
                params['contact_count'] = self.contact_count.to_alipay_dict()
            else:
                params['contact_count'] = self.contact_count
        if self.ecommerce_platforms:
            if isinstance(self.ecommerce_platforms, list):
                for i in range(0, len(self.ecommerce_platforms)):
                    element = self.ecommerce_platforms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ecommerce_platforms[i] = element.to_alipay_dict()
            if hasattr(self.ecommerce_platforms, 'to_alipay_dict'):
                params['ecommerce_platforms'] = self.ecommerce_platforms.to_alipay_dict()
            else:
                params['ecommerce_platforms'] = self.ecommerce_platforms
        if self.main_business:
            if hasattr(self.main_business, 'to_alipay_dict'):
                params['main_business'] = self.main_business.to_alipay_dict()
            else:
                params['main_business'] = self.main_business
        if self.recommendation_reason:
            if hasattr(self.recommendation_reason, 'to_alipay_dict'):
                params['recommendation_reason'] = self.recommendation_reason.to_alipay_dict()
            else:
                params['recommendation_reason'] = self.recommendation_reason
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.sales_amount_text:
            if hasattr(self.sales_amount_text, 'to_alipay_dict'):
                params['sales_amount_text'] = self.sales_amount_text.to_alipay_dict()
            else:
                params['sales_amount_text'] = self.sales_amount_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerRecommendation()
        if 'company_crn' in d:
            o.company_crn = d['company_crn']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'contact_count' in d:
            o.contact_count = d['contact_count']
        if 'ecommerce_platforms' in d:
            o.ecommerce_platforms = d['ecommerce_platforms']
        if 'main_business' in d:
            o.main_business = d['main_business']
        if 'recommendation_reason' in d:
            o.recommendation_reason = d['recommendation_reason']
        if 'region' in d:
            o.region = d['region']
        if 'sales_amount_text' in d:
            o.sales_amount_text = d['sales_amount_text']
        return o


