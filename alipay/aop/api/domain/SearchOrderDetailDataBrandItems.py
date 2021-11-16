#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchOrderBrandDetail import SearchOrderBrandDetail


class SearchOrderDetailDataBrandItems(object):

    def __init__(self):
        self._biz_id = None
        self._box_status = None
        self._brand_box_keywords = None
        self._brand_detail_list = None
        self._brand_template_id = None
        self._channel = None
        self._merchant_type = None
        self._template_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def box_status(self):
        return self._box_status

    @box_status.setter
    def box_status(self, value):
        self._box_status = value
    @property
    def brand_box_keywords(self):
        return self._brand_box_keywords

    @brand_box_keywords.setter
    def brand_box_keywords(self, value):
        self._brand_box_keywords = value
    @property
    def brand_detail_list(self):
        return self._brand_detail_list

    @brand_detail_list.setter
    def brand_detail_list(self, value):
        if isinstance(value, list):
            self._brand_detail_list = list()
            for i in value:
                if isinstance(i, SearchOrderBrandDetail):
                    self._brand_detail_list.append(i)
                else:
                    self._brand_detail_list.append(SearchOrderBrandDetail.from_alipay_dict(i))
    @property
    def brand_template_id(self):
        return self._brand_template_id

    @brand_template_id.setter
    def brand_template_id(self, value):
        self._brand_template_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.box_status:
            if hasattr(self.box_status, 'to_alipay_dict'):
                params['box_status'] = self.box_status.to_alipay_dict()
            else:
                params['box_status'] = self.box_status
        if self.brand_box_keywords:
            if hasattr(self.brand_box_keywords, 'to_alipay_dict'):
                params['brand_box_keywords'] = self.brand_box_keywords.to_alipay_dict()
            else:
                params['brand_box_keywords'] = self.brand_box_keywords
        if self.brand_detail_list:
            if isinstance(self.brand_detail_list, list):
                for i in range(0, len(self.brand_detail_list)):
                    element = self.brand_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.brand_detail_list, 'to_alipay_dict'):
                params['brand_detail_list'] = self.brand_detail_list.to_alipay_dict()
            else:
                params['brand_detail_list'] = self.brand_detail_list
        if self.brand_template_id:
            if hasattr(self.brand_template_id, 'to_alipay_dict'):
                params['brand_template_id'] = self.brand_template_id.to_alipay_dict()
            else:
                params['brand_template_id'] = self.brand_template_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
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
        o = SearchOrderDetailDataBrandItems()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'box_status' in d:
            o.box_status = d['box_status']
        if 'brand_box_keywords' in d:
            o.brand_box_keywords = d['brand_box_keywords']
        if 'brand_detail_list' in d:
            o.brand_detail_list = d['brand_detail_list']
        if 'brand_template_id' in d:
            o.brand_template_id = d['brand_template_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


