#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.YxContactInfo import YxContactInfo


class AlipayIserviceCcmCrmYxcustomerSyncModel(object):

    def __init__(self):
        self._contact_info_list = None
        self._customer_id = None
        self._ext_info = None
        self._tenant_id = None

    @property
    def contact_info_list(self):
        return self._contact_info_list

    @contact_info_list.setter
    def contact_info_list(self, value):
        if isinstance(value, list):
            self._contact_info_list = list()
            for i in value:
                if isinstance(i, YxContactInfo):
                    self._contact_info_list.append(i)
                else:
                    self._contact_info_list.append(YxContactInfo.from_alipay_dict(i))
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_info_list:
            if isinstance(self.contact_info_list, list):
                for i in range(0, len(self.contact_info_list)):
                    element = self.contact_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_info_list[i] = element.to_alipay_dict()
            if hasattr(self.contact_info_list, 'to_alipay_dict'):
                params['contact_info_list'] = self.contact_info_list.to_alipay_dict()
            else:
                params['contact_info_list'] = self.contact_info_list
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmCrmYxcustomerSyncModel()
        if 'contact_info_list' in d:
            o.contact_info_list = d['contact_info_list']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


