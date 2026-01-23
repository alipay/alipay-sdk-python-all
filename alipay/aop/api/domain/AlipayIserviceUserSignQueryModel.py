#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceUserSignQueryModel(object):

    def __init__(self):
        self._agreement_gmt_create_end = None
        self._agreement_gmt_create_start = None
        self._current_page = None
        self._id_card = None
        self._page_size = None

    @property
    def agreement_gmt_create_end(self):
        return self._agreement_gmt_create_end

    @agreement_gmt_create_end.setter
    def agreement_gmt_create_end(self, value):
        self._agreement_gmt_create_end = value
    @property
    def agreement_gmt_create_start(self):
        return self._agreement_gmt_create_start

    @agreement_gmt_create_start.setter
    def agreement_gmt_create_start(self, value):
        self._agreement_gmt_create_start = value
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_gmt_create_end:
            if hasattr(self.agreement_gmt_create_end, 'to_alipay_dict'):
                params['agreement_gmt_create_end'] = self.agreement_gmt_create_end.to_alipay_dict()
            else:
                params['agreement_gmt_create_end'] = self.agreement_gmt_create_end
        if self.agreement_gmt_create_start:
            if hasattr(self.agreement_gmt_create_start, 'to_alipay_dict'):
                params['agreement_gmt_create_start'] = self.agreement_gmt_create_start.to_alipay_dict()
            else:
                params['agreement_gmt_create_start'] = self.agreement_gmt_create_start
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
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
        o = AlipayIserviceUserSignQueryModel()
        if 'agreement_gmt_create_end' in d:
            o.agreement_gmt_create_end = d['agreement_gmt_create_end']
        if 'agreement_gmt_create_start' in d:
            o.agreement_gmt_create_start = d['agreement_gmt_create_start']
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


