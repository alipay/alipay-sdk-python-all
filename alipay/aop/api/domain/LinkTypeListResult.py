#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LinkTypeResult import LinkTypeResult


class LinkTypeListResult(object):

    def __init__(self):
        self._link_type_list = None

    @property
    def link_type_list(self):
        return self._link_type_list

    @link_type_list.setter
    def link_type_list(self, value):
        if isinstance(value, list):
            self._link_type_list = list()
            for i in value:
                if isinstance(i, LinkTypeResult):
                    self._link_type_list.append(i)
                else:
                    self._link_type_list.append(LinkTypeResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.link_type_list:
            if isinstance(self.link_type_list, list):
                for i in range(0, len(self.link_type_list)):
                    element = self.link_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.link_type_list[i] = element.to_alipay_dict()
            if hasattr(self.link_type_list, 'to_alipay_dict'):
                params['link_type_list'] = self.link_type_list.to_alipay_dict()
            else:
                params['link_type_list'] = self.link_type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LinkTypeListResult()
        if 'link_type_list' in d:
            o.link_type_list = d['link_type_list']
        return o


