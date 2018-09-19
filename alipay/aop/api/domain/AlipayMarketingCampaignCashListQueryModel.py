#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignCashListQueryModel(object):

    def __init__(self):
        self._camp_status = None
        self._page_index = None
        self._page_size = None

    @property
    def camp_status(self):
        return self._camp_status

    @camp_status.setter
    def camp_status(self, value):
        self._camp_status = value
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
        if self.camp_status:
            if hasattr(self.camp_status, 'to_alipay_dict'):
                params['camp_status'] = self.camp_status.to_alipay_dict()
            else:
                params['camp_status'] = self.camp_status
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
        o = AlipayMarketingCampaignCashListQueryModel()
        if 'camp_status' in d:
            o.camp_status = d['camp_status']
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


