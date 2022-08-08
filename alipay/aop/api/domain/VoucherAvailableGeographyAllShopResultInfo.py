#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherFailShopInfo import VoucherFailShopInfo


class VoucherAvailableGeographyAllShopResultInfo(object):

    def __init__(self):
        self._fail_exclude_shop_infos = None
        self._success_exclude_shop_ids = None

    @property
    def fail_exclude_shop_infos(self):
        return self._fail_exclude_shop_infos

    @fail_exclude_shop_infos.setter
    def fail_exclude_shop_infos(self, value):
        if isinstance(value, list):
            self._fail_exclude_shop_infos = list()
            for i in value:
                if isinstance(i, VoucherFailShopInfo):
                    self._fail_exclude_shop_infos.append(i)
                else:
                    self._fail_exclude_shop_infos.append(VoucherFailShopInfo.from_alipay_dict(i))
    @property
    def success_exclude_shop_ids(self):
        return self._success_exclude_shop_ids

    @success_exclude_shop_ids.setter
    def success_exclude_shop_ids(self, value):
        if isinstance(value, list):
            self._success_exclude_shop_ids = list()
            for i in value:
                self._success_exclude_shop_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.fail_exclude_shop_infos:
            if isinstance(self.fail_exclude_shop_infos, list):
                for i in range(0, len(self.fail_exclude_shop_infos)):
                    element = self.fail_exclude_shop_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fail_exclude_shop_infos[i] = element.to_alipay_dict()
            if hasattr(self.fail_exclude_shop_infos, 'to_alipay_dict'):
                params['fail_exclude_shop_infos'] = self.fail_exclude_shop_infos.to_alipay_dict()
            else:
                params['fail_exclude_shop_infos'] = self.fail_exclude_shop_infos
        if self.success_exclude_shop_ids:
            if isinstance(self.success_exclude_shop_ids, list):
                for i in range(0, len(self.success_exclude_shop_ids)):
                    element = self.success_exclude_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.success_exclude_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.success_exclude_shop_ids, 'to_alipay_dict'):
                params['success_exclude_shop_ids'] = self.success_exclude_shop_ids.to_alipay_dict()
            else:
                params['success_exclude_shop_ids'] = self.success_exclude_shop_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableGeographyAllShopResultInfo()
        if 'fail_exclude_shop_infos' in d:
            o.fail_exclude_shop_infos = d['fail_exclude_shop_infos']
        if 'success_exclude_shop_ids' in d:
            o.success_exclude_shop_ids = d['success_exclude_shop_ids']
        return o


