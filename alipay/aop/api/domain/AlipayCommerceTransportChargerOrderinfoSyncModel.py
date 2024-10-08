#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SiteChargerOrderDTO import SiteChargerOrderDTO


class AlipayCommerceTransportChargerOrderinfoSyncModel(object):

    def __init__(self):
        self._site_charger_order = None

    @property
    def site_charger_order(self):
        return self._site_charger_order

    @site_charger_order.setter
    def site_charger_order(self, value):
        if isinstance(value, SiteChargerOrderDTO):
            self._site_charger_order = value
        else:
            self._site_charger_order = SiteChargerOrderDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.site_charger_order:
            if hasattr(self.site_charger_order, 'to_alipay_dict'):
                params['site_charger_order'] = self.site_charger_order.to_alipay_dict()
            else:
                params['site_charger_order'] = self.site_charger_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportChargerOrderinfoSyncModel()
        if 'site_charger_order' in d:
            o.site_charger_order = d['site_charger_order']
        return o


