#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticsAccountInfo import LogisticsAccountInfo


class AlipayOpenInstantdeliveryAccountstatusModifyModel(object):

    def __init__(self):
        self._logistics_account_infos = None
        self._out_biz_no = None

    @property
    def logistics_account_infos(self):
        return self._logistics_account_infos

    @logistics_account_infos.setter
    def logistics_account_infos(self, value):
        if isinstance(value, list):
            self._logistics_account_infos = list()
            for i in value:
                if isinstance(i, LogisticsAccountInfo):
                    self._logistics_account_infos.append(i)
                else:
                    self._logistics_account_infos.append(LogisticsAccountInfo.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_account_infos:
            if isinstance(self.logistics_account_infos, list):
                for i in range(0, len(self.logistics_account_infos)):
                    element = self.logistics_account_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_account_infos[i] = element.to_alipay_dict()
            if hasattr(self.logistics_account_infos, 'to_alipay_dict'):
                params['logistics_account_infos'] = self.logistics_account_infos.to_alipay_dict()
            else:
                params['logistics_account_infos'] = self.logistics_account_infos
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenInstantdeliveryAccountstatusModifyModel()
        if 'logistics_account_infos' in d:
            o.logistics_account_infos = d['logistics_account_infos']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


