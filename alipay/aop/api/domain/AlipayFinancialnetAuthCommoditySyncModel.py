#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommodityInfoList import CommodityInfoList


class AlipayFinancialnetAuthCommoditySyncModel(object):

    def __init__(self):
        self._commodity_infos = None
        self._out_order_no = None
        self._platform_id = None

    @property
    def commodity_infos(self):
        return self._commodity_infos

    @commodity_infos.setter
    def commodity_infos(self, value):
        if isinstance(value, list):
            self._commodity_infos = list()
            for i in value:
                if isinstance(i, CommodityInfoList):
                    self._commodity_infos.append(i)
                else:
                    self._commodity_infos.append(CommodityInfoList.from_alipay_dict(i))
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_infos:
            if isinstance(self.commodity_infos, list):
                for i in range(0, len(self.commodity_infos)):
                    element = self.commodity_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commodity_infos[i] = element.to_alipay_dict()
            if hasattr(self.commodity_infos, 'to_alipay_dict'):
                params['commodity_infos'] = self.commodity_infos.to_alipay_dict()
            else:
                params['commodity_infos'] = self.commodity_infos
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthCommoditySyncModel()
        if 'commodity_infos' in d:
            o.commodity_infos = d['commodity_infos']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        return o


