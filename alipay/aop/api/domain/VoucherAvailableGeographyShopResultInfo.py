#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherAvailableGeographyAllShopResultInfo import VoucherAvailableGeographyAllShopResultInfo
from alipay.aop.api.domain.VoucherFailShopInfo import VoucherFailShopInfo
from alipay.aop.api.domain.VoucherFailShopInfo import VoucherFailShopInfo


class VoucherAvailableGeographyShopResultInfo(object):

    def __init__(self):
        self._available_geography_all_shop_result_info = None
        self._fail_available_real_shop_infos = None
        self._fail_available_shop_infos = None
        self._success_available_real_shop_ids = None
        self._success_available_shop_ids = None

    @property
    def available_geography_all_shop_result_info(self):
        return self._available_geography_all_shop_result_info

    @available_geography_all_shop_result_info.setter
    def available_geography_all_shop_result_info(self, value):
        if isinstance(value, VoucherAvailableGeographyAllShopResultInfo):
            self._available_geography_all_shop_result_info = value
        else:
            self._available_geography_all_shop_result_info = VoucherAvailableGeographyAllShopResultInfo.from_alipay_dict(value)
    @property
    def fail_available_real_shop_infos(self):
        return self._fail_available_real_shop_infos

    @fail_available_real_shop_infos.setter
    def fail_available_real_shop_infos(self, value):
        if isinstance(value, list):
            self._fail_available_real_shop_infos = list()
            for i in value:
                if isinstance(i, VoucherFailShopInfo):
                    self._fail_available_real_shop_infos.append(i)
                else:
                    self._fail_available_real_shop_infos.append(VoucherFailShopInfo.from_alipay_dict(i))
    @property
    def fail_available_shop_infos(self):
        return self._fail_available_shop_infos

    @fail_available_shop_infos.setter
    def fail_available_shop_infos(self, value):
        if isinstance(value, list):
            self._fail_available_shop_infos = list()
            for i in value:
                if isinstance(i, VoucherFailShopInfo):
                    self._fail_available_shop_infos.append(i)
                else:
                    self._fail_available_shop_infos.append(VoucherFailShopInfo.from_alipay_dict(i))
    @property
    def success_available_real_shop_ids(self):
        return self._success_available_real_shop_ids

    @success_available_real_shop_ids.setter
    def success_available_real_shop_ids(self, value):
        if isinstance(value, list):
            self._success_available_real_shop_ids = list()
            for i in value:
                self._success_available_real_shop_ids.append(i)
    @property
    def success_available_shop_ids(self):
        return self._success_available_shop_ids

    @success_available_shop_ids.setter
    def success_available_shop_ids(self, value):
        if isinstance(value, list):
            self._success_available_shop_ids = list()
            for i in value:
                self._success_available_shop_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.available_geography_all_shop_result_info:
            if hasattr(self.available_geography_all_shop_result_info, 'to_alipay_dict'):
                params['available_geography_all_shop_result_info'] = self.available_geography_all_shop_result_info.to_alipay_dict()
            else:
                params['available_geography_all_shop_result_info'] = self.available_geography_all_shop_result_info
        if self.fail_available_real_shop_infos:
            if isinstance(self.fail_available_real_shop_infos, list):
                for i in range(0, len(self.fail_available_real_shop_infos)):
                    element = self.fail_available_real_shop_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fail_available_real_shop_infos[i] = element.to_alipay_dict()
            if hasattr(self.fail_available_real_shop_infos, 'to_alipay_dict'):
                params['fail_available_real_shop_infos'] = self.fail_available_real_shop_infos.to_alipay_dict()
            else:
                params['fail_available_real_shop_infos'] = self.fail_available_real_shop_infos
        if self.fail_available_shop_infos:
            if isinstance(self.fail_available_shop_infos, list):
                for i in range(0, len(self.fail_available_shop_infos)):
                    element = self.fail_available_shop_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fail_available_shop_infos[i] = element.to_alipay_dict()
            if hasattr(self.fail_available_shop_infos, 'to_alipay_dict'):
                params['fail_available_shop_infos'] = self.fail_available_shop_infos.to_alipay_dict()
            else:
                params['fail_available_shop_infos'] = self.fail_available_shop_infos
        if self.success_available_real_shop_ids:
            if isinstance(self.success_available_real_shop_ids, list):
                for i in range(0, len(self.success_available_real_shop_ids)):
                    element = self.success_available_real_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.success_available_real_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.success_available_real_shop_ids, 'to_alipay_dict'):
                params['success_available_real_shop_ids'] = self.success_available_real_shop_ids.to_alipay_dict()
            else:
                params['success_available_real_shop_ids'] = self.success_available_real_shop_ids
        if self.success_available_shop_ids:
            if isinstance(self.success_available_shop_ids, list):
                for i in range(0, len(self.success_available_shop_ids)):
                    element = self.success_available_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.success_available_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.success_available_shop_ids, 'to_alipay_dict'):
                params['success_available_shop_ids'] = self.success_available_shop_ids.to_alipay_dict()
            else:
                params['success_available_shop_ids'] = self.success_available_shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableGeographyShopResultInfo()
        if 'available_geography_all_shop_result_info' in d:
            o.available_geography_all_shop_result_info = d['available_geography_all_shop_result_info']
        if 'fail_available_real_shop_infos' in d:
            o.fail_available_real_shop_infos = d['fail_available_real_shop_infos']
        if 'fail_available_shop_infos' in d:
            o.fail_available_shop_infos = d['fail_available_shop_infos']
        if 'success_available_real_shop_ids' in d:
            o.success_available_real_shop_ids = d['success_available_real_shop_ids']
        if 'success_available_shop_ids' in d:
            o.success_available_shop_ids = d['success_available_shop_ids']
        return o


