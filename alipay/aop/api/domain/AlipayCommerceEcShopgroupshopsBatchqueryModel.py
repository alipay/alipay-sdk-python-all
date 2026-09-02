#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndustryQueryOption import IndustryQueryOption


class AlipayCommerceEcShopgroupshopsBatchqueryModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._industry_query_option = None
        self._page_no = None
        self._page_size = None
        self._shop_group_id = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def industry_query_option(self):
        return self._industry_query_option

    @industry_query_option.setter
    def industry_query_option(self, value):
        if isinstance(value, IndustryQueryOption):
            self._industry_query_option = value
        else:
            self._industry_query_option = IndustryQueryOption.from_alipay_dict(value)
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def shop_group_id(self):
        return self._shop_group_id

    @shop_group_id.setter
    def shop_group_id(self, value):
        self._shop_group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.industry_query_option:
            if hasattr(self.industry_query_option, 'to_alipay_dict'):
                params['industry_query_option'] = self.industry_query_option.to_alipay_dict()
            else:
                params['industry_query_option'] = self.industry_query_option
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.shop_group_id:
            if hasattr(self.shop_group_id, 'to_alipay_dict'):
                params['shop_group_id'] = self.shop_group_id.to_alipay_dict()
            else:
                params['shop_group_id'] = self.shop_group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcShopgroupshopsBatchqueryModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'industry_query_option' in d:
            o.industry_query_option = d['industry_query_option']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'shop_group_id' in d:
            o.shop_group_id = d['shop_group_id']
        return o


