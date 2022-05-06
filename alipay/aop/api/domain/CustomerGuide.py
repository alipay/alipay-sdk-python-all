#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherSendGuide import VoucherSendGuide
from alipay.aop.api.domain.VoucherUseGuide import VoucherUseGuide


class CustomerGuide(object):

    def __init__(self):
        self._mini_app_id = None
        self._mini_app_path = None
        self._real_shop_ids = None
        self._service_codes = None
        self._shop_ids = None
        self._store_ids = None
        self._voucher_send_guide = None
        self._voucher_use_guide = None

    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_path(self):
        return self._mini_app_path

    @mini_app_path.setter
    def mini_app_path(self, value):
        self._mini_app_path = value
    @property
    def real_shop_ids(self):
        return self._real_shop_ids

    @real_shop_ids.setter
    def real_shop_ids(self, value):
        if isinstance(value, list):
            self._real_shop_ids = list()
            for i in value:
                self._real_shop_ids.append(i)
    @property
    def service_codes(self):
        return self._service_codes

    @service_codes.setter
    def service_codes(self, value):
        if isinstance(value, list):
            self._service_codes = list()
            for i in value:
                self._service_codes.append(i)
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)
    @property
    def store_ids(self):
        return self._store_ids

    @store_ids.setter
    def store_ids(self, value):
        if isinstance(value, list):
            self._store_ids = list()
            for i in value:
                self._store_ids.append(i)
    @property
    def voucher_send_guide(self):
        return self._voucher_send_guide

    @voucher_send_guide.setter
    def voucher_send_guide(self, value):
        if isinstance(value, VoucherSendGuide):
            self._voucher_send_guide = value
        else:
            self._voucher_send_guide = VoucherSendGuide.from_alipay_dict(value)
    @property
    def voucher_use_guide(self):
        return self._voucher_use_guide

    @voucher_use_guide.setter
    def voucher_use_guide(self, value):
        if isinstance(value, VoucherUseGuide):
            self._voucher_use_guide = value
        else:
            self._voucher_use_guide = VoucherUseGuide.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_path:
            if hasattr(self.mini_app_path, 'to_alipay_dict'):
                params['mini_app_path'] = self.mini_app_path.to_alipay_dict()
            else:
                params['mini_app_path'] = self.mini_app_path
        if self.real_shop_ids:
            if isinstance(self.real_shop_ids, list):
                for i in range(0, len(self.real_shop_ids)):
                    element = self.real_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.real_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.real_shop_ids, 'to_alipay_dict'):
                params['real_shop_ids'] = self.real_shop_ids.to_alipay_dict()
            else:
                params['real_shop_ids'] = self.real_shop_ids
        if self.service_codes:
            if isinstance(self.service_codes, list):
                for i in range(0, len(self.service_codes)):
                    element = self.service_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_codes[i] = element.to_alipay_dict()
            if hasattr(self.service_codes, 'to_alipay_dict'):
                params['service_codes'] = self.service_codes.to_alipay_dict()
            else:
                params['service_codes'] = self.service_codes
        if self.shop_ids:
            if isinstance(self.shop_ids, list):
                for i in range(0, len(self.shop_ids)):
                    element = self.shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        if self.store_ids:
            if isinstance(self.store_ids, list):
                for i in range(0, len(self.store_ids)):
                    element = self.store_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.store_ids[i] = element.to_alipay_dict()
            if hasattr(self.store_ids, 'to_alipay_dict'):
                params['store_ids'] = self.store_ids.to_alipay_dict()
            else:
                params['store_ids'] = self.store_ids
        if self.voucher_send_guide:
            if hasattr(self.voucher_send_guide, 'to_alipay_dict'):
                params['voucher_send_guide'] = self.voucher_send_guide.to_alipay_dict()
            else:
                params['voucher_send_guide'] = self.voucher_send_guide
        if self.voucher_use_guide:
            if hasattr(self.voucher_use_guide, 'to_alipay_dict'):
                params['voucher_use_guide'] = self.voucher_use_guide.to_alipay_dict()
            else:
                params['voucher_use_guide'] = self.voucher_use_guide
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerGuide()
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_path' in d:
            o.mini_app_path = d['mini_app_path']
        if 'real_shop_ids' in d:
            o.real_shop_ids = d['real_shop_ids']
        if 'service_codes' in d:
            o.service_codes = d['service_codes']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        if 'store_ids' in d:
            o.store_ids = d['store_ids']
        if 'voucher_send_guide' in d:
            o.voucher_send_guide = d['voucher_send_guide']
        if 'voucher_use_guide' in d:
            o.voucher_use_guide = d['voucher_use_guide']
        return o


