#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCarReservationTextRule(object):

    def __init__(self):
        self._rule_text_list = None
        self._title = None

    @property
    def rule_text_list(self):
        return self._rule_text_list

    @rule_text_list.setter
    def rule_text_list(self, value):
        if isinstance(value, list):
            self._rule_text_list = list()
            for i in value:
                self._rule_text_list.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.rule_text_list:
            if isinstance(self.rule_text_list, list):
                for i in range(0, len(self.rule_text_list)):
                    element = self.rule_text_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_text_list[i] = element.to_alipay_dict()
            if hasattr(self.rule_text_list, 'to_alipay_dict'):
                params['rule_text_list'] = self.rule_text_list.to_alipay_dict()
            else:
                params['rule_text_list'] = self.rule_text_list
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarReservationTextRule()
        if 'rule_text_list' in d:
            o.rule_text_list = d['rule_text_list']
        if 'title' in d:
            o.title = d['title']
        return o


