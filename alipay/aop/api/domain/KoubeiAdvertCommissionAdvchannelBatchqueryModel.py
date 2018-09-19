#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiAdvertCommissionAdvchannelBatchqueryModel(object):

    def __init__(self):
        self._adv_id = None
        self._page_index = None
        self._page_size = None

    @property
    def adv_id(self):
        return self._adv_id

    @adv_id.setter
    def adv_id(self, value):
        self._adv_id = value
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.adv_id:
            if hasattr(self.adv_id, 'to_alipay_dict'):
                params['adv_id'] = self.adv_id.to_alipay_dict()
            else:
                params['adv_id'] = self.adv_id
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionAdvchannelBatchqueryModel()
        if 'adv_id' in d:
            o.adv_id = d['adv_id']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


