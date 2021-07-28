#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantContractPageQueryModel(object):

    def __init__(self):
        self._begin_time = None
        self._contract_status_list = None
        self._current_page = None
        self._end_time = None
        self._include_event_detail = None
        self._include_item = None
        self._offer_no = None
        self._page_size = None
        self._sign_principal_id = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def contract_status_list(self):
        return self._contract_status_list

    @contract_status_list.setter
    def contract_status_list(self, value):
        self._contract_status_list = value
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def include_event_detail(self):
        return self._include_event_detail

    @include_event_detail.setter
    def include_event_detail(self, value):
        self._include_event_detail = value
    @property
    def include_item(self):
        return self._include_item

    @include_item.setter
    def include_item(self, value):
        self._include_item = value
    @property
    def offer_no(self):
        return self._offer_no

    @offer_no.setter
    def offer_no(self, value):
        self._offer_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def sign_principal_id(self):
        return self._sign_principal_id

    @sign_principal_id.setter
    def sign_principal_id(self, value):
        self._sign_principal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.contract_status_list:
            if hasattr(self.contract_status_list, 'to_alipay_dict'):
                params['contract_status_list'] = self.contract_status_list.to_alipay_dict()
            else:
                params['contract_status_list'] = self.contract_status_list
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.include_event_detail:
            if hasattr(self.include_event_detail, 'to_alipay_dict'):
                params['include_event_detail'] = self.include_event_detail.to_alipay_dict()
            else:
                params['include_event_detail'] = self.include_event_detail
        if self.include_item:
            if hasattr(self.include_item, 'to_alipay_dict'):
                params['include_item'] = self.include_item.to_alipay_dict()
            else:
                params['include_item'] = self.include_item
        if self.offer_no:
            if hasattr(self.offer_no, 'to_alipay_dict'):
                params['offer_no'] = self.offer_no.to_alipay_dict()
            else:
                params['offer_no'] = self.offer_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.sign_principal_id:
            if hasattr(self.sign_principal_id, 'to_alipay_dict'):
                params['sign_principal_id'] = self.sign_principal_id.to_alipay_dict()
            else:
                params['sign_principal_id'] = self.sign_principal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantContractPageQueryModel()
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'contract_status_list' in d:
            o.contract_status_list = d['contract_status_list']
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'include_event_detail' in d:
            o.include_event_detail = d['include_event_detail']
        if 'include_item' in d:
            o.include_item = d['include_item']
        if 'offer_no' in d:
            o.offer_no = d['offer_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sign_principal_id' in d:
            o.sign_principal_id = d['sign_principal_id']
        return o


