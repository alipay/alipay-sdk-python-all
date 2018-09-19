#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCraftsmanDataProviderBatchqueryModel(object):

    def __init__(self):
        self._auth_code = None
        self._craftsman_ids = None
        self._out_craftsman_ids = None
        self._page_no = None
        self._page_size = None
        self._qr_code_shop_id = None
        self._recommend = None
        self._shop_id = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def craftsman_ids(self):
        return self._craftsman_ids

    @craftsman_ids.setter
    def craftsman_ids(self, value):
        if isinstance(value, list):
            self._craftsman_ids = list()
            for i in value:
                self._craftsman_ids.append(i)
    @property
    def out_craftsman_ids(self):
        return self._out_craftsman_ids

    @out_craftsman_ids.setter
    def out_craftsman_ids(self, value):
        if isinstance(value, list):
            self._out_craftsman_ids = list()
            for i in value:
                self._out_craftsman_ids.append(i)
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def qr_code_shop_id(self):
        return self._qr_code_shop_id

    @qr_code_shop_id.setter
    def qr_code_shop_id(self, value):
        self._qr_code_shop_id = value
    @property
    def recommend(self):
        return self._recommend

    @recommend.setter
    def recommend(self, value):
        self._recommend = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.craftsman_ids:
            if isinstance(self.craftsman_ids, list):
                for i in range(0, len(self.craftsman_ids)):
                    element = self.craftsman_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.craftsman_ids[i] = element.to_alipay_dict()
            if hasattr(self.craftsman_ids, 'to_alipay_dict'):
                params['craftsman_ids'] = self.craftsman_ids.to_alipay_dict()
            else:
                params['craftsman_ids'] = self.craftsman_ids
        if self.out_craftsman_ids:
            if isinstance(self.out_craftsman_ids, list):
                for i in range(0, len(self.out_craftsman_ids)):
                    element = self.out_craftsman_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_craftsman_ids[i] = element.to_alipay_dict()
            if hasattr(self.out_craftsman_ids, 'to_alipay_dict'):
                params['out_craftsman_ids'] = self.out_craftsman_ids.to_alipay_dict()
            else:
                params['out_craftsman_ids'] = self.out_craftsman_ids
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.qr_code_shop_id:
            if hasattr(self.qr_code_shop_id, 'to_alipay_dict'):
                params['qr_code_shop_id'] = self.qr_code_shop_id.to_alipay_dict()
            else:
                params['qr_code_shop_id'] = self.qr_code_shop_id
        if self.recommend:
            if hasattr(self.recommend, 'to_alipay_dict'):
                params['recommend'] = self.recommend.to_alipay_dict()
            else:
                params['recommend'] = self.recommend
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCraftsmanDataProviderBatchqueryModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'craftsman_ids' in d:
            o.craftsman_ids = d['craftsman_ids']
        if 'out_craftsman_ids' in d:
            o.out_craftsman_ids = d['out_craftsman_ids']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'qr_code_shop_id' in d:
            o.qr_code_shop_id = d['qr_code_shop_id']
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


