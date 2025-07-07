#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TenantListNftDTO import TenantListNftDTO


class AnttechNftCtocOperationOnlineModel(object):

    def __init__(self):
        self._id_no = None
        self._id_type = None
        self._operation = None
        self._tenant_nft_list = None

    @property
    def id_no(self):
        return self._id_no

    @id_no.setter
    def id_no(self, value):
        self._id_no = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value
    @property
    def tenant_nft_list(self):
        return self._tenant_nft_list

    @tenant_nft_list.setter
    def tenant_nft_list(self, value):
        if isinstance(value, list):
            self._tenant_nft_list = list()
            for i in value:
                if isinstance(i, TenantListNftDTO):
                    self._tenant_nft_list.append(i)
                else:
                    self._tenant_nft_list.append(TenantListNftDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.id_no:
            if hasattr(self.id_no, 'to_alipay_dict'):
                params['id_no'] = self.id_no.to_alipay_dict()
            else:
                params['id_no'] = self.id_no
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        if self.tenant_nft_list:
            if isinstance(self.tenant_nft_list, list):
                for i in range(0, len(self.tenant_nft_list)):
                    element = self.tenant_nft_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tenant_nft_list[i] = element.to_alipay_dict()
            if hasattr(self.tenant_nft_list, 'to_alipay_dict'):
                params['tenant_nft_list'] = self.tenant_nft_list.to_alipay_dict()
            else:
                params['tenant_nft_list'] = self.tenant_nft_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftCtocOperationOnlineModel()
        if 'id_no' in d:
            o.id_no = d['id_no']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'operation' in d:
            o.operation = d['operation']
        if 'tenant_nft_list' in d:
            o.tenant_nft_list = d['tenant_nft_list']
        return o


