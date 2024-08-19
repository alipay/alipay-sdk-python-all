#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunObjectstorageCdsRefreshModel(object):

    def __init__(self):
        self._content = None
        self._envid = None
        self._operator = None
        self._operatortype = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, list):
            self._content = list()
            for i in value:
                self._content.append(i)
    @property
    def envid(self):
        return self._envid

    @envid.setter
    def envid(self, value):
        self._envid = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def operatortype(self):
        return self._operatortype

    @operatortype.setter
    def operatortype(self, value):
        self._operatortype = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if isinstance(self.content, list):
                for i in range(0, len(self.content)):
                    element = self.content[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content[i] = element.to_alipay_dict()
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.envid:
            if hasattr(self.envid, 'to_alipay_dict'):
                params['envid'] = self.envid.to_alipay_dict()
            else:
                params['envid'] = self.envid
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.operatortype:
            if hasattr(self.operatortype, 'to_alipay_dict'):
                params['operatortype'] = self.operatortype.to_alipay_dict()
            else:
                params['operatortype'] = self.operatortype
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunObjectstorageCdsRefreshModel()
        if 'content' in d:
            o.content = d['content']
        if 'envid' in d:
            o.envid = d['envid']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operatortype' in d:
            o.operatortype = d['operatortype']
        return o


