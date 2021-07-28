#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExternalContact import ExternalContact


class AlipayEbppCommunityPropertyCreateModel(object):

    def __init__(self):
        self._contacts = None
        self._isv_short_name = None
        self._logo = None
        self._memo = None
        self._name = None
        self._pid = None
        self._rich_text = None
        self._scale = None
        self._short_company_name = None

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, value):
        if isinstance(value, list):
            self._contacts = list()
            for i in value:
                if isinstance(i, ExternalContact):
                    self._contacts.append(i)
                else:
                    self._contacts.append(ExternalContact.from_alipay_dict(i))
    @property
    def isv_short_name(self):
        return self._isv_short_name

    @isv_short_name.setter
    def isv_short_name(self, value):
        self._isv_short_name = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def rich_text(self):
        return self._rich_text

    @rich_text.setter
    def rich_text(self, value):
        self._rich_text = value
    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = value
    @property
    def short_company_name(self):
        return self._short_company_name

    @short_company_name.setter
    def short_company_name(self, value):
        self._short_company_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.contacts:
            if isinstance(self.contacts, list):
                for i in range(0, len(self.contacts)):
                    element = self.contacts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contacts[i] = element.to_alipay_dict()
            if hasattr(self.contacts, 'to_alipay_dict'):
                params['contacts'] = self.contacts.to_alipay_dict()
            else:
                params['contacts'] = self.contacts
        if self.isv_short_name:
            if hasattr(self.isv_short_name, 'to_alipay_dict'):
                params['isv_short_name'] = self.isv_short_name.to_alipay_dict()
            else:
                params['isv_short_name'] = self.isv_short_name
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.rich_text:
            if hasattr(self.rich_text, 'to_alipay_dict'):
                params['rich_text'] = self.rich_text.to_alipay_dict()
            else:
                params['rich_text'] = self.rich_text
        if self.scale:
            if hasattr(self.scale, 'to_alipay_dict'):
                params['scale'] = self.scale.to_alipay_dict()
            else:
                params['scale'] = self.scale
        if self.short_company_name:
            if hasattr(self.short_company_name, 'to_alipay_dict'):
                params['short_company_name'] = self.short_company_name.to_alipay_dict()
            else:
                params['short_company_name'] = self.short_company_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityPropertyCreateModel()
        if 'contacts' in d:
            o.contacts = d['contacts']
        if 'isv_short_name' in d:
            o.isv_short_name = d['isv_short_name']
        if 'logo' in d:
            o.logo = d['logo']
        if 'memo' in d:
            o.memo = d['memo']
        if 'name' in d:
            o.name = d['name']
        if 'pid' in d:
            o.pid = d['pid']
        if 'rich_text' in d:
            o.rich_text = d['rich_text']
        if 'scale' in d:
            o.scale = d['scale']
        if 'short_company_name' in d:
            o.short_company_name = d['short_company_name']
        return o


