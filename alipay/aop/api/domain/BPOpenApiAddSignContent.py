#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BPOpenApiAddSignContent(object):

    def __init__(self):
        self._additional_lines = None
        self._assignee = None
        self._deal_actions = None
        self._deal_url = None
        self._detail_url = None
        self._display_name = None

    @property
    def additional_lines(self):
        return self._additional_lines

    @additional_lines.setter
    def additional_lines(self, value):
        if isinstance(value, list):
            self._additional_lines = list()
            for i in value:
                self._additional_lines.append(i)
    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        self._assignee = value
    @property
    def deal_actions(self):
        return self._deal_actions

    @deal_actions.setter
    def deal_actions(self, value):
        self._deal_actions = value
    @property
    def deal_url(self):
        return self._deal_url

    @deal_url.setter
    def deal_url(self, value):
        self._deal_url = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_lines:
            if isinstance(self.additional_lines, list):
                for i in range(0, len(self.additional_lines)):
                    element = self.additional_lines[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.additional_lines[i] = element.to_alipay_dict()
            if hasattr(self.additional_lines, 'to_alipay_dict'):
                params['additional_lines'] = self.additional_lines.to_alipay_dict()
            else:
                params['additional_lines'] = self.additional_lines
        if self.assignee:
            if hasattr(self.assignee, 'to_alipay_dict'):
                params['assignee'] = self.assignee.to_alipay_dict()
            else:
                params['assignee'] = self.assignee
        if self.deal_actions:
            if hasattr(self.deal_actions, 'to_alipay_dict'):
                params['deal_actions'] = self.deal_actions.to_alipay_dict()
            else:
                params['deal_actions'] = self.deal_actions
        if self.deal_url:
            if hasattr(self.deal_url, 'to_alipay_dict'):
                params['deal_url'] = self.deal_url.to_alipay_dict()
            else:
                params['deal_url'] = self.deal_url
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BPOpenApiAddSignContent()
        if 'additional_lines' in d:
            o.additional_lines = d['additional_lines']
        if 'assignee' in d:
            o.assignee = d['assignee']
        if 'deal_actions' in d:
            o.deal_actions = d['deal_actions']
        if 'deal_url' in d:
            o.deal_url = d['deal_url']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'display_name' in d:
            o.display_name = d['display_name']
        return o


