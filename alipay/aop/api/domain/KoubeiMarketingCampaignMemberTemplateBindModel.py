#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignMemberTemplateBindModel(object):

    def __init__(self):
        self._add_shop_ids = None
        self._member_template_id = None
        self._remove_shop_ids = None
        self._request_id = None

    @property
    def add_shop_ids(self):
        return self._add_shop_ids

    @add_shop_ids.setter
    def add_shop_ids(self, value):
        if isinstance(value, list):
            self._add_shop_ids = list()
            for i in value:
                self._add_shop_ids.append(i)
    @property
    def member_template_id(self):
        return self._member_template_id

    @member_template_id.setter
    def member_template_id(self, value):
        self._member_template_id = value
    @property
    def remove_shop_ids(self):
        return self._remove_shop_ids

    @remove_shop_ids.setter
    def remove_shop_ids(self, value):
        if isinstance(value, list):
            self._remove_shop_ids = list()
            for i in value:
                self._remove_shop_ids.append(i)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_shop_ids:
            if isinstance(self.add_shop_ids, list):
                for i in range(0, len(self.add_shop_ids)):
                    element = self.add_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.add_shop_ids, 'to_alipay_dict'):
                params['add_shop_ids'] = self.add_shop_ids.to_alipay_dict()
            else:
                params['add_shop_ids'] = self.add_shop_ids
        if self.member_template_id:
            if hasattr(self.member_template_id, 'to_alipay_dict'):
                params['member_template_id'] = self.member_template_id.to_alipay_dict()
            else:
                params['member_template_id'] = self.member_template_id
        if self.remove_shop_ids:
            if isinstance(self.remove_shop_ids, list):
                for i in range(0, len(self.remove_shop_ids)):
                    element = self.remove_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.remove_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.remove_shop_ids, 'to_alipay_dict'):
                params['remove_shop_ids'] = self.remove_shop_ids.to_alipay_dict()
            else:
                params['remove_shop_ids'] = self.remove_shop_ids
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
        o = KoubeiMarketingCampaignMemberTemplateBindModel()
        if 'add_shop_ids' in d:
            o.add_shop_ids = d['add_shop_ids']
        if 'member_template_id' in d:
            o.member_template_id = d['member_template_id']
        if 'remove_shop_ids' in d:
            o.remove_shop_ids = d['remove_shop_ids']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


