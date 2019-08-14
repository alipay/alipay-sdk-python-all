#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiSalesLeadsSaleleadsCreateModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_principle_type = None
        self._leads_tags = None
        self._leads_type = None
        self._memo = None
        self._request_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_principle_type(self):
        return self._biz_principle_type

    @biz_principle_type.setter
    def biz_principle_type(self, value):
        self._biz_principle_type = value
    @property
    def leads_tags(self):
        return self._leads_tags

    @leads_tags.setter
    def leads_tags(self, value):
        if isinstance(value, list):
            self._leads_tags = list()
            for i in value:
                self._leads_tags.append(i)
    @property
    def leads_type(self):
        return self._leads_type

    @leads_type.setter
    def leads_type(self, value):
        self._leads_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_principle_type:
            if hasattr(self.biz_principle_type, 'to_alipay_dict'):
                params['biz_principle_type'] = self.biz_principle_type.to_alipay_dict()
            else:
                params['biz_principle_type'] = self.biz_principle_type
        if self.leads_tags:
            if isinstance(self.leads_tags, list):
                for i in range(0, len(self.leads_tags)):
                    element = self.leads_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.leads_tags[i] = element.to_alipay_dict()
            if hasattr(self.leads_tags, 'to_alipay_dict'):
                params['leads_tags'] = self.leads_tags.to_alipay_dict()
            else:
                params['leads_tags'] = self.leads_tags
        if self.leads_type:
            if hasattr(self.leads_type, 'to_alipay_dict'):
                params['leads_type'] = self.leads_type.to_alipay_dict()
            else:
                params['leads_type'] = self.leads_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesLeadsSaleleadsCreateModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_principle_type' in d:
            o.biz_principle_type = d['biz_principle_type']
        if 'leads_tags' in d:
            o.leads_tags = d['leads_tags']
        if 'leads_type' in d:
            o.leads_type = d['leads_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


