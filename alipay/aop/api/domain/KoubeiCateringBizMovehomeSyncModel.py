#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KcpLeadsInfo import KcpLeadsInfo


class KoubeiCateringBizMovehomeSyncModel(object):

    def __init__(self):
        self._leads_info_list = None
        self._partner_id = None

    @property
    def leads_info_list(self):
        return self._leads_info_list

    @leads_info_list.setter
    def leads_info_list(self, value):
        if isinstance(value, list):
            self._leads_info_list = list()
            for i in value:
                if isinstance(i, KcpLeadsInfo):
                    self._leads_info_list.append(i)
                else:
                    self._leads_info_list.append(KcpLeadsInfo.from_alipay_dict(i))
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.leads_info_list:
            if isinstance(self.leads_info_list, list):
                for i in range(0, len(self.leads_info_list)):
                    element = self.leads_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.leads_info_list[i] = element.to_alipay_dict()
            if hasattr(self.leads_info_list, 'to_alipay_dict'):
                params['leads_info_list'] = self.leads_info_list.to_alipay_dict()
            else:
                params['leads_info_list'] = self.leads_info_list
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringBizMovehomeSyncModel()
        if 'leads_info_list' in d:
            o.leads_info_list = d['leads_info_list']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o


