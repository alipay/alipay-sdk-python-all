#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MorphoIdentity import MorphoIdentity


class AlipayOpenMiniMorphoTemplatelistBatchqueryModel(object):

    def __init__(self):
        self._identity = None
        self._keyword = None
        self._page_num = None
        self._page_size = None
        self._type = None

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        if isinstance(value, MorphoIdentity):
            self._identity = value
        else:
            self._identity = MorphoIdentity.from_alipay_dict(value)
    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, value):
        self._keyword = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.keyword:
            if hasattr(self.keyword, 'to_alipay_dict'):
                params['keyword'] = self.keyword.to_alipay_dict()
            else:
                params['keyword'] = self.keyword
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniMorphoTemplatelistBatchqueryModel()
        if 'identity' in d:
            o.identity = d['identity']
        if 'keyword' in d:
            o.keyword = d['keyword']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'type' in d:
            o.type = d['type']
        return o


