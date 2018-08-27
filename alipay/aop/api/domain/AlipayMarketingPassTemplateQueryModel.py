#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingPassTemplateQueryModel(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._tpl_id = None

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
    def tpl_id(self):
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, value):
        self._tpl_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.tpl_id:
            if hasattr(self.tpl_id, 'to_alipay_dict'):
                params['tpl_id'] = self.tpl_id.to_alipay_dict()
            else:
                params['tpl_id'] = self.tpl_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingPassTemplateQueryModel()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'tpl_id' in d:
            o.tpl_id = d['tpl_id']
        return o


