#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrivilegeBenefit(object):

    def __init__(self):
        self._benefit_context = None
        self._benefit_rule = None
        self._benefit_type = None
        self._desc = None
        self._logo = None
        self._out_benefit_id = None
        self._priority = None
        self._status = None
        self._sub_title = None
        self._title = None
        self._url = None

    @property
    def benefit_context(self):
        return self._benefit_context

    @benefit_context.setter
    def benefit_context(self, value):
        self._benefit_context = value
    @property
    def benefit_rule(self):
        return self._benefit_rule

    @benefit_rule.setter
    def benefit_rule(self, value):
        self._benefit_rule = value
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        if isinstance(value, list):
            self._desc = list()
            for i in value:
                self._desc.append(i)
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def out_benefit_id(self):
        return self._out_benefit_id

    @out_benefit_id.setter
    def out_benefit_id(self, value):
        self._out_benefit_id = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_context:
            if hasattr(self.benefit_context, 'to_alipay_dict'):
                params['benefit_context'] = self.benefit_context.to_alipay_dict()
            else:
                params['benefit_context'] = self.benefit_context
        if self.benefit_rule:
            if hasattr(self.benefit_rule, 'to_alipay_dict'):
                params['benefit_rule'] = self.benefit_rule.to_alipay_dict()
            else:
                params['benefit_rule'] = self.benefit_rule
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.desc:
            if isinstance(self.desc, list):
                for i in range(0, len(self.desc)):
                    element = self.desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.desc[i] = element.to_alipay_dict()
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.out_benefit_id:
            if hasattr(self.out_benefit_id, 'to_alipay_dict'):
                params['out_benefit_id'] = self.out_benefit_id.to_alipay_dict()
            else:
                params['out_benefit_id'] = self.out_benefit_id
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrivilegeBenefit()
        if 'benefit_context' in d:
            o.benefit_context = d['benefit_context']
        if 'benefit_rule' in d:
            o.benefit_rule = d['benefit_rule']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'logo' in d:
            o.logo = d['logo']
        if 'out_benefit_id' in d:
            o.out_benefit_id = d['out_benefit_id']
        if 'priority' in d:
            o.priority = d['priority']
        if 'status' in d:
            o.status = d['status']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'title' in d:
            o.title = d['title']
        if 'url' in d:
            o.url = d['url']
        return o


